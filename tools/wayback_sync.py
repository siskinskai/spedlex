#!/usr/bin/env python3
"""Find or create Wayback Machine snapshots for sources/documents.tsv.

For every row that has a URL and an empty wayback_url, this script:
  1. asks the Wayback availability API for the snapshot closest to `retrieved`;
  2. downloads that snapshot in raw form (".../web/<timestamp>id_/<url>") and
     compares its SHA-256 with the manifest's `sha256`;
  3. if there is no snapshot, or it differs, asks Save Page Now for a fresh
     one and checks that;
  4. writes the snapshot URL into `wayback_url`. If the snapshot's hash differs
     from the version we read, it still records the URL and adds a note, because
     the state has probably changed the document since. If the site refuses
     archiving, it writes `blocked`.

It is slow on purpose (the anonymous service is rate-limited), saves the
manifest after every row, and can be stopped with Ctrl-C and run again: rows
that already have a wayback_url are skipped.

Usage:
  python3 tools/wayback_sync.py --dry-run          # list what would be done
  python3 tools/wayback_sync.py --lookup-only      # look for existing snapshots; never request new ones
  python3 tools/wayback_sync.py                    # full run
  python3 tools/wayback_sync.py --state md         # one jurisdiction
  python3 tools/wayback_sync.py --pause 20         # seconds between requests (default 12)

Standard library only, Python 3.9+. Needs network access to archive.org and the
source sites' snapshots (not the sites themselves).
"""
import argparse
import csv
import hashlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources" / "documents.tsv"
UA = "SPEDLex-wayback-sync/1.0 (+https://github.com/siskinskai/spedlex; citation audit trail)"
NOTE_TAG = "Wayback"


def read_manifest(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        header = next(reader)
        rows = [dict(zip(header, r)) for r in reader if r]
    return header, rows


def write_manifest(path, header, rows):
    tmp = path.with_suffix(".tsv.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None)
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(h, "") for h in header])
    tmp.replace(path)


class RateLimited(Exception):
    pass


def http(url, timeout=90, read=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.geturl(), (resp.read() if read else b"")
    except urllib.error.HTTPError as e:
        if e.code in (429, 503):
            raise RateLimited(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}")
        return e.code, url, b""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, url, b""


def clean(url):
    return url.split("#")[0]


def closest_snapshot(url, retrieved):
    """Return (timestamp, snapshot_url) or None."""
    import json
    ts = retrieved.replace("-", "") if re.match(r"^\d{4}-\d{2}-\d{2}$", retrieved) else ""
    q = "https://archive.org/wayback/available?url=" + urllib.parse.quote(clean(url), safe="")
    if ts:
        q += "&timestamp=" + ts
    status, _, body = http(q, timeout=60)
    if status != 200:
        return None
    try:
        snap = json.loads(body.decode("utf-8"))["archived_snapshots"].get("closest")
    except (ValueError, KeyError):
        return None
    if not snap or not snap.get("available"):
        return None
    return snap["timestamp"], f"https://web.archive.org/web/{snap['timestamp']}/{clean(url)}"


def raw_hash(timestamp, url):
    status, _, body = http(f"https://web.archive.org/web/{timestamp}id_/{clean(url)}", timeout=180)
    if status != 200 or not body:
        return None
    return hashlib.sha256(body).hexdigest()


def save_page_now(url):
    """Ask Save Page Now for a fresh snapshot; return its timestamp or None."""
    status, final, _ = http("https://web.archive.org/save/" + clean(url), timeout=240, read=False)
    m = re.search(r"/web/(\d{14})/", final or "")
    if status in (200, 301, 302) and m:
        return m.group(1)
    return None


def add_note(row, text):
    notes = row.get("notes", "")
    if text not in notes:
        row["notes"] = (notes + " " + text).strip()


def process(row, args):
    url, want = row["url"], row["sha256"]
    # Pages and copies whose bytes the live URL cannot reproduce can't be hash-compared.
    comparable = not any(m in row["notes"] for m in (
        "[not fetchable]", "cannot reproduce this file", "may not serve the same bytes", "portal home page"))
    snap = closest_snapshot(url, row["retrieved"])
    best = None  # (timestamp, matches)
    if snap:
        ts = snap[0]
        time.sleep(args.pause)
        h = raw_hash(ts, url) if comparable else None
        best = (ts, h == want if h else None)
        if best[1]:
            return ts, "match"
    if not args.lookup_only:
        time.sleep(args.pause)
        ts = save_page_now(url)
        if ts:
            time.sleep(args.pause)
            h = raw_hash(ts, url) if comparable else None
            cand = (ts, h == want if h else None)
            if cand[1] or best is None:
                best = cand
        elif best is None:
            return None, "blocked"
    if best is None:
        return None, "none"
    ts, ok = best
    if ok is None:
        return ts, "unverified"
    return ts, ("match" if ok else "differs")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--state", help="two-letter code, e.g. md, or 'us'")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--lookup-only", action="store_true", help="never request new snapshots")
    ap.add_argument("--pause", type=float, default=12.0, help="seconds between requests")
    args = ap.parse_args()

    header, rows = read_manifest(MANIFEST)
    todo = [r for r in rows if r["url"] and not r["wayback_url"]]
    if args.state:
        want = "US" if args.state.lower() == "us" else "US-" + args.state.upper()
        todo = [r for r in todo if r["jurisdiction"] == want]
    print(f"{len(todo)} row(s) to do; {sum(1 for r in rows if r['wayback_url'])} already have a wayback_url.")
    if args.dry_run:
        for r in todo:
            print("  ", r["doc_id"], r["url"][:100])
        return 0

    tally = {}
    try:
        for i, r in enumerate(todo, 1):
            try:
                ts, status = process(r, args)
            except RateLimited as e:
                print(f"Rate limited ({e}). Stopping; wait a few minutes and run again.")
                break
            tally[status] = tally.get(status, 0) + 1
            if status == "blocked":
                r["wayback_url"] = "blocked"
                add_note(r, f"{NOTE_TAG}: archiving refused or failed; the hash is the only proof of the version used.")
            elif status == "none":
                print(f"[{i}/{len(todo)}] {r['doc_id']}: no snapshot (lookup only); left blank")
                continue
            else:
                r["wayback_url"] = f"https://web.archive.org/web/{ts}/{clean(r['url'])}"
                if status == "differs":
                    add_note(r, f"{NOTE_TAG}: snapshot {ts} differs from the version read (hash mismatch); the source may have changed since {r['retrieved']}.")
                elif status == "unverified":
                    add_note(r, f"{NOTE_TAG}: snapshot {ts} not hash-checked (page or file cannot be compared).")
            write_manifest(MANIFEST, header, rows)
            print(f"[{i}/{len(todo)}] {r['doc_id']}: {status}")
            time.sleep(args.pause)
    except KeyboardInterrupt:
        print("Interrupted; progress so far is saved.")
    print("Summary:", tally or "nothing done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
