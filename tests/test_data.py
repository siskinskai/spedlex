"""Invariants of the published data. CI runs these on every pull request."""

import importlib
import json

import pytest

from spedlex import build, load
from sources.states import LAYERS

ROOT = build.ROOT
RECORDS = load(ROOT / "data" / "spedlex.jsonl")


def test_committed_outputs_match_a_fresh_build():
    assert build.main(["--check"]) == 0, "run `python -m spedlex.build` and commit the result"


def test_every_record_is_schema_valid():
    assert build.validate(RECORDS) == []


def test_no_string_is_claimed_by_two_concepts():
    _, conflicts = build.duplicate_strings(RECORDS)
    assert conflicts == []


def test_registry_ids_are_unique_and_match_the_data():
    rows = [line.split("\t") for line in (ROOT / "data" / "concept_ids.tsv").read_text().splitlines()[1:]]
    ids = [r[1] for r in rows]
    keys = [r[0] for r in rows]
    assert len(ids) == len(set(ids)), "a concept ID is assigned twice"
    assert len(keys) == len(set(keys)), "a key is registered twice"
    active = {r[1] for r in rows if r[3] == "active"}
    retired = {r[1] for r in rows if r[3] == "retired"}
    data_ids = {r["concept_id"] for r in RECORDS}
    assert data_ids == active
    assert not data_ids & retired


def test_broader_links_point_to_real_concepts():
    ids = {r["concept_id"] for r in RECORDS}
    for r in RECORDS:
        for b in r.get("broader", []):
            assert b in ids, f"{r['concept_id']} has broader {b} which does not exist"


@pytest.mark.parametrize("name", LAYERS)
def test_state_layer_is_well_formed(name):
    mod = importlib.import_module(f"sources.states.{name}")
    for attr in ("STRINGS", "CONCEPTS", "JURISDICTION", "LAYER_NAME", "RETRIEVED", "ASSISTED_BY", "VERSION_ADDED"):
        assert hasattr(mod, attr), f"{name} is missing {attr}"
    assert mod.JURISDICTION.startswith("US-") and len(mod.JURISDICTION) == 5 and mod.JURISDICTION != "US-XX"
    assert "<" not in mod.LAYER_NAME, f"{name}: fill in LAYER_NAME from the template"
    assert mod.__doc__ and "Sources reviewed" in mod.__doc__, f"{name} must list its sources in the docstring"
    for key, strings, source in mod.STRINGS:
        assert source.get("url", "").startswith("http"), f"{name}: {key} source has no URL"
    for key, pref, cat, strings, source, opts in mod.CONCEPTS:
        assert source.get("url", "").startswith("http"), f"{name}: {key} source has no URL"


def test_every_state_source_carries_its_jurisdiction():
    for r in RECORDS:
        for s in r["sources"]:
            if s["source_type"] in ("state_regulation", "state_guidance", "procedural_safeguards_notice", "secondary_guidance"):
                assert s.get("jurisdiction", "US").startswith("US-"), (r["concept_id"], s["citation"])


def test_high_risk_concepts_are_never_bare():
    for r in RECORDS:
        if r["pii_risk"]["level"] == "high":
            assert r["pii_risk"]["protect_rule"] == "never_bare"


def test_stats_match_records():
    st = json.loads((ROOT / "data" / "stats.json").read_text())
    real = [r for r in RECORDS if r["review"]["status"] != "illustrative"]
    assert st["concepts"] == len(real)


def test_every_source_records_whether_a_model_assisted():
    for r in RECORDS:
        for s in r["sources"]:
            assert s.get("assisted_by"), (r["concept_id"], s["citation"])
