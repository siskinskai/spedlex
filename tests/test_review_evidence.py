"""tools/review_evidence.py: citation parsing, form patterns and page finding.

None of these tests needs .sources-cache/ or pdftotext.
"""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import review_evidence as ev  # noqa: E402


@pytest.mark.parametrize("text, printed, pdf, section", [
    ("p. 19", (19, 19), None, None),
    ("TEA Notice of Procedural Safeguards (Jan. 2025), p. 19", (19, 19), None, None),
    ("PDF p. 35", None, (35, 35), None),
    ("Iowa Procedural Safeguards Manual (Aug. 2023), PDF p. 15", None, (15, 15), None),
    ("pp. 115-118", (115, 118), None, None),
    ("ISBE Parent Guide (May 2025), pp. 115–118", (115, 118), None, None),
    ("PDF pp. 3-4", None, (3, 4), None),
    ("Section I(2), p. 2", (2, 2), None, "I(2)"),
    ("05-071 Chapter 101, MUSER (eff. July 2024), Section I(2), p. 2", (2, 2), None, "I(2)"),
    ("5-A DCMR § 3010.7", None, None, "3010.7"),
    ("511 IAC 7-32-93.5", None, None, "7-32-93.5"),
    ("NYSED Testing Accommodations Guide (Sept. 2025)", None, None, None),
])
def test_parse_citation(text, printed, pdf, section):
    got = ev.parse_citation(text)
    assert got["printed"] == printed
    assert got["pdf"] == pdf
    assert got["section"] == section


def test_pdf_page_is_not_read_as_printed_page():
    got = ev.parse_citation("PDF p. 35")
    assert got["printed"] is None and got["pdf"] == (35, 35)


@pytest.mark.parametrize("section, token", [
    ("3010.7", "3010.7"), ("I(2)", "2"), ("7-32-93.5", "7-32-93.5"), ("", None), (None, None),
])
def test_section_token(section, token):
    assert ev.section_token(section) == token


def test_pattern_allows_line_breaks_and_case():
    pat = ev.form_pattern("Expedited due process hearing")
    assert pat.search("an EXPEDITED due\n   process  hearing must")


def test_pattern_allows_hyphen_line_break():
    pat = ev.form_pattern("Child-find")
    assert pat.search("the Child-\nfind duty")
    assert pat.search("the child-find duty")


def test_pattern_does_not_match_inside_words():
    pat = ev.form_pattern("IAP", case_sensitive=True)
    assert pat.search("the IAP was written")
    assert not pat.search("the iap was written")
    assert not pat.search("MAPIAPS")
    assert not ev.form_pattern("504").search("1504")


def test_find_printed_page_with_offset():
    # printed page 2 sits on PDF page 9; the other pages carry other numbers
    pages = [f"text {i}\n   x{i}\n" for i in range(20)]
    pages[8] = "text\n\nPage 2\n"
    assert ev.find_printed_page(pages, 2) == 9


def test_find_printed_page_none_when_absent():
    pages = ["no numbers here\nat all"] * 10
    assert ev.find_printed_page(pages, 4) is None


def test_find_printed_page_ignores_numbers_in_body():
    pages = ["The 36 states\nfinish line\nend of text"] * 5
    assert ev.find_printed_page(pages, 36) is None


def test_record_forms_puts_preferred_first_and_marks_case():
    rec = {"strings": [{"text": "IAP", "string_type": "acronym", "match": "phrase_cs"},
                       {"text": "Individual accommodation plan", "string_type": "preferred", "match": "phrase_ci"}]}
    assert ev.record_forms(rec) == [("Individual accommodation plan", False), ("IAP", True)]


def test_choose_source_by_citation_text():
    rec = {"concept_id": "X", "sources": [
        {"source_type": "federal_regulation", "citation": "34 CFR 300.17"},
        {"source_type": "state_regulation", "citation": "5-A DCMR § 3001.1", "doc_id": "d1"},
        {"source_type": "state_regulation", "citation": "511 IAC 7-32-40", "doc_id": "d2"}]}
    assert ev.choose_source(rec)["doc_id"] == "d1"
    assert ev.choose_source(rec, "511 iac")["doc_id"] == "d2"
    with pytest.raises(SystemExit):
        ev.choose_source(rec, "no such citation")


def test_no_local_copy_is_reported_online(tmp_path, monkeypatch):
    monkeypatch.setattr(ev, "CACHE", tmp_path)
    rec = {"concept_id": "X", "preferred_term": "Term", "strings": [
        {"text": "Term", "string_type": "preferred", "match": "phrase_ci"}]}
    src = {"citation": "p. 3", "doc_id": "d1", "url": "https://example.org/a.pdf", "source_type": "state_guidance"}
    doc = {"jurisdiction": "US-ZZ", "local_name": "missing.pdf", "url": "https://example.org/a.pdf"}
    rep = ev.gather(rec, src, doc)
    assert rep["evidence"] == "online"
    assert "NO LOCAL COPY: read online" in rep["notes"]
    assert rep["matches"] == []


def test_text_file_search_and_wrong_page_note(tmp_path, monkeypatch):
    monkeypatch.setattr(ev, "CACHE", tmp_path)
    (tmp_path / "zz").mkdir()
    (tmp_path / "zz" / "doc.txt").write_text("Intro\nthe Term appears here\n", encoding="utf-8")
    rec = {"concept_id": "X", "preferred_term": "Term", "strings": [
        {"text": "Term", "string_type": "preferred", "match": "phrase_ci"}]}
    src = {"citation": "p. 3", "doc_id": "d1", "source_type": "state_guidance"}
    doc = {"jurisdiction": "US-ZZ", "local_name": "doc.txt", "url": ""}
    rep = ev.gather(rec, src, doc)
    assert rep["evidence"] == "local copy"
    assert rep["matches"] and rep["matches"][0]["form"] == "Term"


def test_report_never_writes_files(tmp_path, monkeypatch):
    # the tool saves nothing: running a report leaves the working directory untouched
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(ev, "CACHE", tmp_path / "none")
    rec = {"concept_id": "X", "preferred_term": "T", "strings": [
        {"text": "T", "string_type": "preferred", "match": "phrase_ci"}]}
    ev.print_report(ev.gather(rec, {"citation": "p. 1", "doc_id": "d", "source_type": "s"},
                              {"jurisdiction": "US-ZZ", "local_name": "x.pdf", "url": ""}))
    assert list(tmp_path.iterdir()) == []
