"""The terminology helpers (spedlex.lexicon) and the disfavored flag."""

import asyncio
import json

import pytest

from spedlex import Lexicon, Safelist, build, load
from spedlex.__main__ import main as cli

RECORDS = load(build.ROOT / "data" / "spedlex.jsonl")
NATIONAL = Lexicon(RECORDS)
NY = Lexicon(RECORDS, jurisdiction="NY")
TX = Lexicon(RECORDS, jurisdiction="US-TX")


def kinds(lex, text):
    return [(i.kind, i.text) for i in lex.check(text)]


# --- disfavored flag -------------------------------------------------------

def disfavored_strings():
    return [(r, s) for r in RECORDS for s in r["strings"] if s.get("disfavored")]


def test_every_disfavored_row_is_applied():
    rows = [line.split("\t") for line in (build.ROOT / "sources" / "disfavored.tsv").read_text().splitlines()[1:] if line.strip()]
    assert len(rows) == len(disfavored_strings())


def test_disfavored_strings_carry_a_note_and_basis_and_are_never_preferred():
    for r, s in disfavored_strings():
        assert s["usage_note"] and s["usage_basis"], r["concept_id"]
        assert s["string_type"] != "preferred", r["concept_id"]


def test_disfavored_strings_are_still_protected_from_redaction():
    """Older documents use them; a scrubber must not destroy them."""
    sl = Safelist(RECORDS)
    for r, s in disfavored_strings():
        assert [m.text for m in sl.find(f"Records say {s['text']} here.")] == [s["text"]]


def test_apply_disfavored_rejects_unknown_strings(tmp_path):
    p = tmp_path / "d.tsv"
    p.write_text("\t".join(build.DISFAVORED_COLUMNS) + "\nid\tnot a real string\tA note long enough.\tbasis\tnone\n")
    records, _ = build.build(build.get_adapter(build.DEFAULT))
    keys = {line.split("\t")[0]: line.split("\t")[1]
            for line in (build.ROOT / "data" / "concept_ids.tsv").read_text().splitlines()[1:]}
    with pytest.raises(SystemExit):
        build.apply_disfavored(records, keys, p)


# --- lookup and state terms -----------------------------------------------

def test_lookup_gives_each_states_name():
    [hit] = NY.lookup("ARD committee")
    assert hit["preferred_term"] == "IEP Team"
    assert hit["use_for_reader"] == "Committee on Special Education"
    assert "ARD committee" in hit["forms_by_jurisdiction"]["US-TX"]


def test_lookup_is_case_aware_for_acronyms():
    assert NATIONAL.lookup("PLAAFP")
    assert NATIONAL.lookup("plaafp") == []          # acronyms match exact case
    assert NATIONAL.lookup("prior WRITTEN notice")  # phrases ignore case


def test_unknown_term():
    assert NATIONAL.lookup("not a special education term") == []


def test_best_term_falls_back_to_the_national_term():
    cid = NATIONAL.lookup("PLAAFP")[0]["concept_id"]
    assert TX.best_term(cid) == NATIONAL.concept(cid)["preferred_term"]


def test_best_term_never_returns_a_related_form():
    """A 'related' string (a level, person, document, or narrower or broader term) is not the
    same thing as the concept, so it is never the term to write for a reader."""
    for r in RECORDS:
        related = {s["text"] for s in r["strings"] if s["string_type"] == "related"}
        same = {s["text"] for s in r["strings"] if s["string_type"] != "related"}
        for s in r["strings"]:
            if s["string_type"] != "related":
                continue
            for j in s.get("regional", []):
                got = Lexicon(RECORDS, jurisdiction=j).best_term(r["concept_id"])
                assert got in same or got == r["preferred_term"], (r["concept_id"], j, got)
                assert got not in related - same


def test_best_term_prefers_a_current_name_over_a_legacy_one():
    for r in RECORDS:
        for s in r["strings"]:
            if s["string_type"] != "legacy":
                continue
            for j in s.get("regional", []):
                got = Lexicon(RECORDS, jurisdiction=j).best_term(r["concept_id"])
                current = [t for t in r["strings"] if j in (t.get("regional") or []) and not t.get("disfavored")
                           and t["string_type"] not in ("acronym", "abbreviation", "plural", "related", "legacy")]
                if current:
                    assert got == current[0]["text"]


# --- annotate --------------------------------------------------------------

def test_annotate_finds_terms_with_citations():
    ann = TX.annotate("The ARD committee reviewed the PLAAFP.")
    assert [a.text for a in ann] == ["ARD committee", "PLAAFP"]
    assert all(a.citation and a.review_status for a in ann)


def test_annotate_skips_month_names_in_dates():
    assert all(a.text != "APR" for a in NATIONAL.annotate("Born APR 14, 2015."))


def test_ambiguous_acronym_is_settled_by_the_readers_state():
    [national] = NATIONAL.annotate("Ask CDE.")
    assert national.concept_id is None and len(national.candidates) >= 2
    [co] = Lexicon(RECORDS, jurisdiction="CO").annotate("Ask CDE.")
    assert co.preferred_term == "Colorado Department of Education"


# --- check -----------------------------------------------------------------

def test_check_flags_disfavored_terms_with_a_suggestion():
    [issue] = NATIONAL.check("Older records say mental retardation.")
    assert issue.kind == "disfavored" and issue.suggestion == "Intellectual disability"


def test_check_flags_other_states_terms():
    assert ("other_state", "ARD committee") in kinds(NY, "The ARD committee met.")
    assert ("other_state", "CSE") in kinds(TX, "The CSE met.")
    assert kinds(TX, "The ARD committee met.") == []


def test_check_leaves_ordinary_lowercase_phrases_alone():
    assert kinds(NY, "We held a team meeting.") == []


def test_check_without_a_state_reports_only_state_independent_issues():
    found = {k for k, _ in kinds(NATIONAL, "The ARD committee met. Ask CDE.")}
    assert found == {"ambiguous"}


def test_glossary_is_cited_and_says_it_is_not_a_definition():
    g = TX.glossary("The CSE reviewed the PLAAFP.")
    assert "not legal definitions" in g and "34 CFR 300.320(a)(1)" in g and "ARD committee" in g
    assert TX.glossary("Nothing here.") == ""


def test_jurisdiction_codes_are_validated():
    with pytest.raises(ValueError):
        Lexicon(RECORDS, jurisdiction="Texas")


# --- command line and MCP --------------------------------------------------

def test_cli_lookup_json(capsys):
    assert cli(["lookup", "PPT", "--state", "CT", "--json"]) == 0
    assert json.loads(capsys.readouterr().out)[0]["preferred_term"] == "IEP Team"


def test_mcp_tools():
    mcp = pytest.importorskip("mcp")  # noqa: F841  optional dependency, Python 3.10+
    from spedlex import mcp_server
    names = {t.name for t in asyncio.run(mcp_server.server.list_tools())}
    assert names == {"lookup_term", "terms_in_text", "check_text", "glossary_for_text"}
    assert mcp_server.check_text("The ARD committee met.", "NY")[0]["kind"] == "other_state"
