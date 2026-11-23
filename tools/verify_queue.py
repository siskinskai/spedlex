"""Source checks: confirm a record's citation without a special-education expert.

A source check is the step a careful legal or research reviewer can do alone:
open the cited document at the cited page or paragraph and confirm the term
is there, used the way the record says. A record with a confirmed citation
moves from `candidate` (or `machine_validated`) to `source_verified`. Expert
review (tools/expert_review.py, sources/reviews.tsv) is a separate, higher
step and still overrides it.

  python tools/verify_queue.py queue                  write a ranked worklist CSV
      --limit 150                                     (default 150; 0 = all)
      --include-validated                             (also queue machine_validated records)
      --state TX                                      (only records citing this state)
      --out provenance/verification/queue-<date>.csv  (default)

  python tools/verify_queue.py apply <filled.csv> --verifier "Your Name"
      [--date 2026-11-23] [--append]

`queue` ranks records by how many jurisdictions cite them, so the first rows
are the terms most tools will meet. Open the CSV in Excel, Numbers or Google
Sheets, fill in `result` (verified or problem) and `note` for the rows you
checked, and leave the rest blank.

`apply` reads the filled CSV, checks every row against the data, and writes
<filled>.proposed-verifications.tsv. With --append it also appends the rows to
sources/verifications.tsv; then run `python -m spedlex.build`.

Only people check sources. An AI agent may draft the queue, but it must never
fill in `result`, and it runs `apply --append` only when the person asks it to
in the same conversation (AGENTS.md).
"""

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "spedlex.jsonl"
DOCS = ROOT / "sources" / "documents.tsv"
VERIFICATIONS = ROOT / "sources" / "verifications.tsv"
COLUMNS = ["concept_id", "result", "citation", "verifier", "date", "note"]
QUEUE_COLUMNS = ["rank", "concept_id", "preferred_term", "status", "category", "jurisdictions_citing",
                 "forms_to_look_for", "citation", "doc_id", "url", "local_copy", "result", "note"]


def load_records():
    return [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_documents():
    if not DOCS.exists():
        return {}
    with DOCS.open(encoding="utf-8", newline="") as f:
        return {row["doc_id"]: row for row in csv.DictReader(f, delimiter="\t")}


def pick_source(rec, state=None):
    """The citation to check: a state document when there is one, else the first source."""
    sources = rec["sources"]
    if state:
        sources = [s for s in sources if s.get("jurisdiction") == state] or sources
    for s in sources:
        if s["source_type"] != "federal_regulation" and s.get("doc_id"):
            return s
    return sources[0]


def jurisdictions(rec):
    return sorted({s.get("jurisdiction", "US") for s in rec["sources"]})


def cmd_queue(args):
    statuses = {"candidate"} | ({"machine_validated"} if args.include_validated else set())
    state = None
    if args.state:
        state = args.state.upper()
        state = state if state.startswith("US-") else "US-" + state
    docs = load_documents()
    recs = [r for r in load_records() if r["review"]["status"] in statuses]
    if state:
        recs = [r for r in recs if state in jurisdictions(r)]
    recs.sort(key=lambda r: (-len(jurisdictions(r)), r["concept_id"]))
    if args.limit:
        recs = recs[:args.limit]
    out = Path(args.out or ROOT / "provenance" / "verification" / f"queue-{dt.date.today().isoformat()}.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(QUEUE_COLUMNS)
        for i, r in enumerate(recs, start=1):
            s = pick_source(r, state)
            doc = docs.get(s.get("doc_id", ""), {})
            local = ""
            if doc.get("local_name"):
                local = f".sources-cache/{doc['jurisdiction'][3:].lower()}/{doc['local_name']}"
            forms = [r["preferred_term"]] + [x["text"] for x in r["strings"] if x["text"] != r["preferred_term"]][:4]
            w.writerow([i, r["concept_id"], r["preferred_term"], r["review"]["status"], r["category"],
                        len(jurisdictions(r)), " | ".join(forms), s["citation"], s.get("doc_id", ""),
                        s.get("url", "") or doc.get("url", ""), local, "", ""])
    print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}: {len(recs)} records")


def cmd_apply(args):
    by_id = {r["concept_id"]: r for r in load_records()}
    date = args.date or dt.date.today().isoformat()
    rows, errors = [], []
    with open(args.csv, encoding="utf-8-sig", newline="") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            result = (row.get("result") or "").strip().lower()
            if not result:
                continue
            cid = (row.get("concept_id") or "").strip()
            citation = (row.get("citation") or "").strip()
            note = " ".join((row.get("note") or "").split())
            if cid not in by_id:
                errors.append(f"row {n}: unknown concept {cid!r}")
            elif result not in ("verified", "problem"):
                errors.append(f"row {n}: result must be verified or problem, not {result!r}")
            elif result == "problem" and not note:
                errors.append(f"row {n}: a problem needs a note saying what is wrong")
            elif citation not in {s["citation"] for s in by_id[cid]["sources"]}:
                errors.append(f"row {n}: {citation!r} is not one of {cid}'s citations")
            else:
                rows.append([cid, result, citation, args.verifier, date, note])
    if errors:
        sys.exit("Nothing written. Fix these rows first:\n  " + "\n  ".join(errors))
    proposed = Path(str(args.csv) + ".proposed-verifications.tsv")
    proposed.write_text("\t".join(COLUMNS) + "\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    print(f"wrote {proposed}: {len(rows)} rows "
          f"({sum(r[1] == 'verified' for r in rows)} verified, {sum(r[1] == 'problem' for r in rows)} problems)")
    if args.append and rows:
        if not VERIFICATIONS.exists():
            VERIFICATIONS.write_text("\t".join(COLUMNS) + "\n", encoding="utf-8")
        with VERIFICATIONS.open("a", encoding="utf-8") as f:
            f.writelines("\t".join(r) + "\n" for r in rows)
        print(f"appended to sources/verifications.tsv; now run: python -m spedlex.build")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("queue", help="write a ranked worklist CSV")
    q.add_argument("--limit", type=int, default=150)
    q.add_argument("--include-validated", action="store_true")
    q.add_argument("--state")
    q.add_argument("--out")
    a = sub.add_parser("apply", help="turn a filled worklist into verifications.tsv rows")
    a.add_argument("csv")
    a.add_argument("--verifier", required=True)
    a.add_argument("--date")
    a.add_argument("--append", action="store_true")
    args = ap.parse_args(argv)
    {"queue": cmd_queue, "apply": cmd_apply}[args.cmd](args)


if __name__ == "__main__":
    main()
