#!/usr/bin/env python3
"""Download the source documents listed in sources/documents.tsv and verify them.

SPEDLex cites source documents; it never stores them in git. This script gets
your own local copies into .sources-cache/<xx>/ (ignored by git) and checks each
one against the SHA-256 hash recorded in the manifest.

  python tools/fetch_sources.py              # fetch and verify everything
  python tools/fetch_sources.py --state md   # one jurisdiction ('us' for federal)
  python tools/fetch_sources.py --check      # verify local copies only; no network

Per row:
  ok            the local copy exists and its hash matches
  ok (wayback)  the original URL failed; the Wayback Machine copy matched
  CHANGED       the live document no longer matches the hash we read. It is saved
                as <local_name>.new and nothing is overwritten
  MISSING       no copy could be obtained (or, with --check, the file is absent)
  skipped       the row is marked as not fetchable (a saved web page or a copy
                made by hand); it can only be checked against a local copy

The exit status is non-zero if any row is CHANGED or MISSING.
Standard library only, Python 3.9+.
"""
import argparse
import csv
import hashlib
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "SPEDLex-fetch-sources/1.0 (+https://github.com/siskinskai/spedlex; citation audit trail)"
# A row whose notes contain one of these cannot be re-downloaded byte for byte.
NOT_FETCHABLE = ("[not fetchable]", "fetch_sources.py cannot reproduce")


def read_manifest(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        header = next(reader)
        return [dict(zip(header, r)) for r in reader if r]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_dir_for(row):
    j = row["jurisdiction"]
    return "us" if j == "US" else j.split("-", 1)[1].lower()


def download(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return None


def wayback_raw(wayback_url):
    """https://web.archive.org/web/<ts>/<url> -> the raw-file form with id_."""
    m = re.match(r"^(https?://web\.archive\.org/web/)(\d{14})/(.+)$", wayback_url or "")
    return f"{m.group(1)}{m.group(2)}id_/{m.group(3)}" if m else None


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def handle(row, cache, check_only):
    name = row["local_name"]
    if "/" in name or name.startswith("."):
        return "MISSING", "unsafe local_name"
    target = cache / cache_dir_for(row) / name
    want = row["sha256"]
    if target.is_file():
        if sha256_file(target) == want:
            return "ok", ""
        if check_only:
            return "CHANGED", "local file does not match the recorded hash"
    elif check_only:
        if any(m in row.get("notes", "") for m in NOT_FETCHABLE):
            return "skipped", "not fetchable; add your own copy to check it"
        return "MISSING", "not in the cache"
    if any(m in row.get("notes", "") for m in NOT_FETCHABLE):
        return "skipped", "not fetchable; add your own copy to check it"

    data = download(row["url"]) if row["url"] else None
    if data is not None:
        if hashlib.sha256(data).hexdigest() == want:
            save(target, data)
            return "ok", ""
        save(target.with_name(name + ".new"), data)
        return "CHANGED", f"live document differs from the recorded hash; saved as {name}.new"
    raw = wayback_raw(row.get("wayback_url", ""))
    if raw:
        data = download(raw, timeout=180)
        if data is not None and hashlib.sha256(data).hexdigest() == want:
            save(target, data)
            return "ok (wayback)", ""
        if data is not None:
            return "MISSING", "the Wayback copy does not match the recorded hash"
    return "MISSING", "download failed" + ("" if row["url"] else " (no URL recorded)")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Fetch and verify the source documents in sources/documents.tsv.")
    ap.add_argument("--state", help="one jurisdiction: a two-letter code such as md, or 'us'")
    ap.add_argument("--check", action="store_true", help="verify local copies only; no network")
    ap.add_argument("--manifest", default=str(ROOT / "sources" / "documents.tsv"), help=argparse.SUPPRESS)
    ap.add_argument("--cache", default=str(ROOT / ".sources-cache"), help=argparse.SUPPRESS)
    args = ap.parse_args(argv)

    rows = read_manifest(Path(args.manifest))
    if args.state:
        rows = [r for r in rows if cache_dir_for(r) == args.state.lower()]
        if not rows:
            print(f"No rows for {args.state!r}.")
            return 1
    counts = {}
    for row in rows:
        status, why = handle(row, Path(args.cache), args.check)
        counts[status] = counts.get(status, 0) + 1
        print(f"{status:13} {row['doc_id']}" + (f"  ({why})" if why else ""))
    print("Summary: " + ", ".join(f"{n} {s}" for s, n in sorted(counts.items())))
    return 1 if counts.get("CHANGED") or counts.get("MISSING") else 0


if __name__ == "__main__":
    sys.exit(main())
