"""Evidence for one source check: find a record's terms at its cited page.

A source check asks whether the cited document, at the cited page or
paragraph, contains the term and uses it for the concept the record says.
This tool does the looking so a person can do the deciding. It prints a short
report to the screen and writes nothing: AGENTS.md forbids committing source
text, so extracted text is never saved to a file.

  python tools/review_evidence.py SPED:000207
  python tools/review_evidence.py SPED:000207 --citation "p. 36"
  python tools/review_evidence.py provenance/verification/queue-2026-11-23.csv 7
  python tools/review_evidence.py <...> --json        (machine-readable, still screen only)

With a worklist CSV, the second argument is the row's `rank` value. With a
concept ID, the first state citation that has a document is used unless
--citation picks another (any part of the citation text will do).

It needs `pdftotext` (poppler) for PDF copies. Documents with no copy in
.sources-cache/ are reported as "NO LOCAL COPY: read online", with the URL.
Standard library only.
"""

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "spedlex.jsonl"
DOCS = ROOT / "sources" / "documents.tsv"
CACHE = ROOT / ".sources-cache"

NEAR = 3            # pages either side of the cited page to search next
HEADER_LINES = 3    # lines at the top and bottom of a page that may hold its printed number
PRINTED_SCAN = 14   # how many PDF pages past N to look for printed page N
MAX_MATCHES = 3
MAX_LINE = 200

_NUM = r"(\d+)"


# ---------------------------------------------------------------- citations

def parse_citation(text):
    """Split a citation into page and section parts.

    Returns {"printed": (a, b) | None, "pdf": (a, b) | None, "section": str | None}.
    "p. 19" and "pp. 115-118" are printed pages; "PDF p. 35" is a page index in
    the file. A section ("§ 3010.7", "Section I(2)", "511 IAC 7-32-93.5") is
    kept as text for searching.
    """
    text = " ".join((text or "").split())
    out = {"printed": None, "pdf": None, "section": None}
    m = re.search(r"\bPDF\s+pp?\.\s*" + _NUM + r"(?:\s*[-–—]\s*" + _NUM + r")?", text, re.I)
    if m:
        a = int(m.group(1))
        out["pdf"] = (a, int(m.group(2)) if m.group(2) else a)
        text = text[:m.start()] + text[m.end():]
    m = re.search(r"\bpp?\.\s*" + _NUM + r"(?:\s*[-–—]\s*" + _NUM + r")?", text, re.I)
    if m:
        a = int(m.group(1))
        out["printed"] = (a, int(m.group(2)) if m.group(2) else a)
        text = text[:m.start()] + text[m.end():]
    m = re.search(r"(?:§+|\bSections?\b)\s*([^,;]+)", text)
    if m:
        out["section"] = m.group(1).strip(" .")
    elif not (out["printed"] or out["pdf"]):
        # "511 IAC 7-32-93.5", "COMAR 13A.05.01.03B(27)": the last token holding a digit
        toks = [t for t in text.replace(",", " ").split()
                if re.search(r"\d", t) and re.search(r"[-.()]", t)
                and not re.fullmatch(r"(?:19|20)\d\d", t.strip("().;:"))]
        out["section"] = toks[-1] if toks else None
    return out


def section_token(section):
    """The part of a section label worth searching for ("3010.7", "7-32-93.5"), or None."""
    if not section:
        return None
    m = re.search(r"\d[\w.\-]*", section)
    return m.group(0).rstrip(".-") if m else None


# ----------------------------------------------------------------- patterns

def form_pattern(text, case_sensitive=False):
    """A regex for a form: whitespace may be a line break, hyphens may break a line."""
    words = []
    for w in text.split():
        parts = [re.escape(p) for p in re.split(r"-", w)]
        words.append(r"-?\s*".join(parts) if len(parts) > 1 else parts[0])
    body = r"\s+".join(words)
    # not glued to other letters or digits, so "IAP" does not match inside "MAP" or "IAPA"
    return re.compile(r"(?<![A-Za-z0-9])" + body + r"(?![A-Za-z0-9])", 0 if case_sensitive else re.I)


def record_forms(rec):
    """[(text, case_sensitive)] for every string of the record, preferred term first."""
    seen, forms = set(), []
    for s in sorted(rec["strings"], key=lambda s: s["string_type"] != "preferred"):
        if s["text"] not in seen:
            seen.add(s["text"])
            forms.append((s["text"], s.get("match") == "phrase_cs"))
    return forms


# -------------------------------------------------------------------- pages

def load_pages(path):
    """A list of page texts (PDF page 1 is index 0). Raises RuntimeError if it can't be read."""
    path = Path(path)
    if path.suffix.lower() == ".pdf":
        if not shutil.which("pdftotext"):
            raise RuntimeError("pdftotext is not installed (poppler). Install it, or read the PDF yourself.")
        r = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, check=False)
        if r.returncode != 0:
            raise RuntimeError("pdftotext could not read this file: " + r.stderr.decode("utf-8", "replace")[:200])
        pages = r.stdout.decode("utf-8", "replace").split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        if not any(p.strip() for p in pages):
            raise RuntimeError("no text in this PDF (scanned?). Read it by eye.")
        return pages
    return [path.read_text(encoding="utf-8", errors="replace")]  # saved web page or text: one "page"


def find_printed_page(pages, n):
    """The PDF page (1-based) whose header or footer shows printed page number n, or None."""
    pat = re.compile(r"^\W*(?:page\s+)?" + str(n) + r"(?:\s+of\s+\d+)?\W*$|(?:\bpage\s+|\s{3,}|\|\s*)" +
                     str(n) + r"\W*$", re.I)
    lo = max(0, n - 2)
    for i in range(lo, min(len(pages), n + PRINTED_SCAN)):
        lines = [ln.strip() for ln in pages[i].splitlines() if ln.strip()]
        for ln in lines[:HEADER_LINES] + lines[-HEADER_LINES:]:
            if pat.search(ln):
                return i + 1
    return None


def search_page(text, patterns):
    """[(form, line_number)] for each form found in text."""
    hits = []
    for form, pat in patterns:
        for m in pat.finditer(text):
            hits.append((form, text.count("\n", 0, m.start()), m.start()))
    return hits


def context(text, pos, form_len):
    """The matched line with one line either side, trimmed, as a list of strings."""
    lines = text.splitlines()
    n = text.count("\n", 0, pos)
    out = []
    for k in range(max(0, n - 1), min(len(lines), n + 2)):
        s = " ".join(lines[k].split())
        if s:
            out.append(s[:MAX_LINE] + ("…" if len(s) > MAX_LINE else ""))
    return out


# ------------------------------------------------------------------ records

def load_records():
    return [json.loads(x) for x in DATA.read_text(encoding="utf-8").splitlines() if x.strip()]


def load_documents():
    if not DOCS.exists():
        return {}
    with DOCS.open(encoding="utf-8", newline="") as f:
        return {r["doc_id"]: r for r in csv.DictReader(f, delimiter="\t")}


def choose_source(rec, citation=None):
    srcs = rec["sources"]
    if citation:
        hit = [s for s in srcs if citation == s["citation"]] or \
              [s for s in srcs if citation.lower() in s["citation"].lower()]
        if not hit:
            raise SystemExit(f"{rec['concept_id']} has no citation matching {citation!r}. Its citations:\n  " +
                             "\n  ".join(s["citation"] for s in srcs))
        return hit[0]
    for s in srcs:
        if s["source_type"] != "federal_regulation" and s.get("doc_id"):
            return s
    return srcs[0]


def local_copy(doc):
    name = doc.get("local_name") if doc else ""
    if not name:
        return None
    p = CACHE / doc["jurisdiction"][3:].lower() / name
    return p if p.exists() else None


# ------------------------------------------------------------------- report

def gather(rec, source, doc):
    """Run the check. Returns a dict that the printers use; touches no files."""
    cit = parse_citation(source["citation"])
    rep = {"concept_id": rec["concept_id"], "term": rec["preferred_term"], "citation": source["citation"],
           "url": source.get("url") or (doc or {}).get("url", ""), "doc_id": source.get("doc_id", ""),
           "forms": [f for f, _ in record_forms(rec)], "evidence": None, "where": None, "pages": [],
           "matches": [], "notes": []}
    path = local_copy(doc)
    if not path:
        rep["evidence"] = "online"
        rep["notes"].append("NO LOCAL COPY: read online")
        return rep
    rep["evidence"] = "local copy"
    rep["file"] = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    try:
        pages = load_pages(path)
    except RuntimeError as e:
        rep["notes"].append(str(e))
        return rep
    patterns = [(f, form_pattern(f, cs)) for f, cs in record_forms(rec)]

    def found_on(idx):  # idx: list of 0-based page indexes
        res = []
        for i in idx:
            for form, ln, pos in search_page(pages[i], patterns):
                res.append({"pdf_page": i + 1, "form": form, "context": context(pages[i], pos, len(form))})
        return res

    cited = None  # PDF page range the citation points at (1-based, inclusive)
    if cit["pdf"]:
        cited = cit["pdf"]
        rep["where"] = f"PDF p. {cited[0]}" + (f"-{cited[1]}" if cited[1] != cited[0] else "")
    elif cit["printed"]:
        a, b = cit["printed"]
        pa, pb = find_printed_page(pages, a), find_printed_page(pages, b)
        if pa:
            cited = (pa, pb or pa + (b - a))
            rep["where"] = f"printed p. {a}" + (f"-{b}" if b != a else "") + f" = PDF p. {cited[0]}" + \
                           (f"-{cited[1]}" if cited[1] != cited[0] else "")
        else:
            cited = (a, b)
            rep["where"] = f"printed p. {a}: page number not found in headers or footers, so PDF p. {a} was assumed"
            rep["notes"].append("printed-to-PDF page mapping unconfirmed")
    if len(pages) == 1 and path.suffix.lower() != ".pdf":
        cited = None
        rep["notes"].append("not a PDF: searched the whole file")

    if cited:
        lo, hi = max(1, cited[0]), min(len(pages), cited[1])
        rep["pages"] = list(range(lo, hi + 1))
        rep["matches"] = found_on(range(lo - 1, hi))
        rep["scope"] = "cited page"
        if not rep["matches"]:
            near = [i for i in range(max(0, lo - 1 - NEAR), min(len(pages), hi + NEAR)) if not lo - 1 <= i < hi]
            rep["matches"] = found_on(near)
            rep["scope"] = f"nearby pages (±{NEAR})"
            if not rep["matches"]:
                rep["matches"] = found_on(range(len(pages)))
                rep["scope"] = "whole document"
    else:
        tok = section_token(cit["section"])
        scope_idx = None
        if tok:
            anchor = re.compile(r"(?<![\w.])" + re.escape(tok) + r"(?![\w])")
            scope_idx = [i for i, p in enumerate(pages) if anchor.search(p)]
            rep["where"] = f"section {cit['section']}: " + (
                "on PDF p. " + ", ".join(str(i + 1) for i in scope_idx[:6]) if scope_idx
                else "label not found in the document")
        if scope_idx:
            rep["matches"] = found_on(scope_idx)
            rep["scope"] = "pages showing the section label"
        if not rep["matches"]:
            rep["matches"] = found_on(range(len(pages)))
            rep["scope"] = "whole document"
    rep["pages_in_file"] = len(pages)
    if not rep["matches"]:
        rep["notes"].append("couldn't find any listed form anywhere in the document")
    return rep


def print_report(rep):
    print(f"{rep['concept_id']}  {rep['term']}")
    print(f"Citation: {rep['citation']}")
    print(f"Evidence: {rep['evidence']}" + (f" ({rep['file']})" if rep.get("file") else ""))
    if rep["evidence"] == "online":
        print(f"URL: {rep['url']}")
    print("Forms to look for: " + " | ".join(rep["forms"]))
    if rep.get("where"):
        print("Cited: " + rep["where"])
    ms = rep["matches"]
    if ms:
        forms = sorted({m["form"] for m in ms}, key=lambda f: rep["forms"].index(f))
        pages = sorted({m["pdf_page"] for m in ms})
        print(f"Found ({rep['scope']}): {', '.join(forms)}  on PDF p. {', '.join(map(str, pages[:8]))}"
              + (" …" if len(pages) > 8 else ""))
        for m in ms[:MAX_MATCHES]:
            print(f"  [{m['form']}] PDF p. {m['pdf_page']}:")
            for ln in m["context"]:
                print("    " + ln)
        if len(ms) > MAX_MATCHES:
            print(f"  (+{len(ms) - MAX_MATCHES} more matches)")
    for n in rep["notes"]:
        print("Note: " + n)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("target", help="a concept ID (SPED:000207) or a worklist CSV")
    ap.add_argument("row", nargs="?", help="with a CSV: the row's rank")
    ap.add_argument("--citation", help="pick this citation (or part of it) of the record")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    citation = args.citation
    if args.target.lower().endswith(".csv"):
        if not args.row:
            ap.error("with a CSV, give the row's rank")
        with open(args.target, encoding="utf-8-sig", newline="") as f:
            rows = [r for r in csv.DictReader(f) if r.get("rank") == str(args.row)]
        if not rows:
            sys.exit(f"no row with rank {args.row} in {args.target}")
        cid, citation = rows[0]["concept_id"], rows[0]["citation"]
    else:
        cid = args.target
    by_id = {r["concept_id"]: r for r in load_records()}
    if cid not in by_id:
        sys.exit(f"unknown concept {cid!r}")
    rec = by_id[cid]
    source = choose_source(rec, citation)
    rep = gather(rec, source, load_documents().get(source.get("doc_id", "")))
    if args.json:
        print(json.dumps(rep, indent=1, ensure_ascii=False))
    else:
        print_report(rep)


if __name__ == "__main__":
    main()
