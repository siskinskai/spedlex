"""sources/documents.tsv, the manifest of source documents, and its links to the records."""

import copy
import json

from spedlex import build

ROOT = build.ROOT
RECORDS = [json.loads(line) for line in (ROOT / "data" / "spedlex.jsonl").read_text(encoding="utf-8").splitlines()]


def test_manifest_is_well_formed_and_consistent_with_the_records():
    assert build.manifest_errors(RECORDS) == []


def test_a_mistyped_doc_id_fails_the_check():
    records = copy.deepcopy(RECORDS)
    for r in records:
        for s in r["sources"]:
            if s.get("doc_id") == "wv-psn-2024":
                s["doc_id"] = "wv-psn-2042"
    errors = build.manifest_errors(records)
    assert any("wv-psn-2042" in e and "not in sources/documents.tsv" in e for e in errors)
    assert any("wv-psn-2024" in e and "no record cites it" in e for e in errors)


def test_a_doc_id_from_the_wrong_state_fails_the_check():
    records = copy.deepcopy(RECORDS)
    for r in records:
        for s in r["sources"]:
            if s.get("doc_id") == "wv-psn-2024":
                s["doc_id"] = "wy-psn-2025"
                break
        else:
            continue
        break
    assert any("belongs to US-WY" in e for e in build.manifest_errors(records))


def test_every_cited_source_with_a_saved_document_has_a_doc_id():
    """State layers that saved their documents must cite them by doc_id."""
    rows, _ = build.load_manifest()
    states = {row["jurisdiction"] for row in rows.values() if row["jurisdiction"] != "US"}
    missing = {}
    for r in RECORDS:
        for s in r["sources"]:
            if s.get("jurisdiction") in states and s["source_type"] != "federal_regulation" and not s.get("doc_id"):
                missing.setdefault((s["jurisdiction"], s["citation"].split(",")[0][:60]), 0)
                missing[(s["jurisdiction"], s["citation"].split(",")[0][:60])] += 1
    # Web pages that were not saved (alternate-assessment pages and the like) legitimately have none.
    unexpected = {k: n for k, n in missing.items() if "page" not in k[1].lower() and "assess" not in k[1].lower()}
    assert not unexpected, f"sources without a doc_id: {unexpected}"
