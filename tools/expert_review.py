"""Ask outside experts to review one state's SPEDLex entries, by email.

Experts shouldn't have to learn GitHub. This tool turns the open questions in
the data into a plain-text email they can answer by hitting Reply, and reads
their replies back into a form a maintainer can review and paste into
sources/reviews.tsv.

  python tools/expert_review.py request NV
      --sender "Your Name" --greeting "Dr. Lee"     (optional; defaults are
                                                     visible [BRACKETS])
      --limit 40                                    (cap Parts B and C)
      --stale-years 3                               (ask about documents this old)

  python tools/expert_review.py reply outreach/expert-review/rounds/NV-.../key.json reply.txt

`request` writes outreach/expert-review/rounds/<ST>-<date>/email.txt and
key.json (what each item id means). `reply` reads one reply, then writes
<reply>.proposed-reviews.tsv (rows in reviews.tsv format) and
<reply>.followups.md (everything a person has to decide).

This tool never writes sources/reviews.tsv. Only people do (AGENTS.md).
Details: outreach/expert-review/README.md
"""

import argparse
import datetime as dt
import hashlib
import json
import math
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "outreach" / "expert-review"
ROUNDS = OUTDIR / "rounds"
DATA = ROOT / "data" / "spedlex.jsonl"
STATS = ROOT / "data" / "stats.json"
COVERAGE = ROOT / "docs" / "COVERAGE.md"
WIDTH = 78
RULE = "=" * WIDTH
BOX = "[   ]"
# Notes (written by the people who drafted a layer) that signal an open question.
CUES = re.compile(r"verify|may differ|ambiguous|name from the|out of date|outdated", re.I)
EQUIVALENT_TYPES = {"synonym", "legacy"}


# ---------------------------------------------------------------- loading

def load_records():
    return [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]


def resolve_state(arg):
    """Return (code, name) for a two-letter code or a name in docs/COVERAGE.md."""
    rows = {}
    for line in COVERAGE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*US-([A-Z]{2})\s*\|\s*(\w+)", line)
        if m and m.group(3) == "added":
            rows[m.group(2)] = m.group(1)
    key = arg.strip()
    if key.upper() in rows:
        return key.upper(), rows[key.upper()]
    for code, name in rows.items():
        if name.lower() == key.lower().replace("_", " "):
            return code, name
    raise SystemExit(f"{arg!r} is not a state with a layer. Added: {', '.join(sorted(rows))}")


def split_citation(citation):
    """'Doc title (Jun. 2023), pp. 3-4' -> ('Doc title (Jun. 2023)', 'pp. 3-4'); 'NAC 388.1' -> (None, 'NAC 388.1')."""
    if ", " in citation:
        doc, loc = citation.rsplit(", ", 1)
        return doc, loc
    return None, citation


class Docs:
    """Numbers each cited document in the order an item first mentions it."""

    def __init__(self):
        self.order = []  # (label, url)
        self.inline = []  # citations with no document title (e.g. 'NAC 388.093')

    def cite(self, source):
        doc, loc = split_citation(source["citation"])
        if doc is None:
            if source["citation"] not in self.inline:
                self.inline.append(source["citation"])
            return source["citation"]
        entry = (doc, source.get("url", ""))
        if entry not in self.order:
            self.order.append(entry)
        return f"doc {self.order.index(entry) + 1}, {loc}"


def wrap(text, first, rest):
    return textwrap.fill(text, width=WIDTH, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False)


# ---------------------------------------------------------------- items

def build_items(recs, code, name, stale_years, limit, extras, today):
    j = f"US-{code}"
    mine = [r for r in recs if any(s.get("jurisdiction") == j for s in r["sources"])]
    mine = [r for r in mine if r["review"]["status"] != "illustrative"]
    nv_sources = lambda r: [s for s in r["sources"] if s.get("jurisdiction") == j]
    owns = lambda r: r["sources"][0].get("jurisdiction") == j  # this layer defined the concept
    docs = Docs()
    A, B, C, D = [], [], [], []

    skip_pairs = {e["skip_pair"] for e in extras if e["skip_pair"]}
    replaced = {e["replaces"] for e in extras if e["replaces"]}

    # Part A1: documents that may have been replaced.
    seen = {}
    for r in mine:
        for s in nv_sources(r):
            doc, _ = split_citation(s["citation"])
            if doc:
                seen.setdefault((doc, s.get("url", "")), s)
    for (doc, url), s in sorted(seen.items(), key=lambda kv: kv[0][0]):
        m = re.search(r"\((?:[^()]*?)(\d{4})\)", doc)
        if m and int(m.group(1)) <= today.year - stale_years:
            docs.cite(s)
            A.append({"kind": "yn", "part": "A", "concept_id": None, "maps_to_review": False, "label": f"Is {doc} still current?",
                      "text": f"The {name} document we worked from is \"{doc}\" (doc {docs.order.index((doc, url)) + 1} below). "
                              f"Is it still the current version? (N = it has been replaced; please give the new title or date in a comment.)"})

    # Part A2: concepts this layer defined whose notes flag an open question.
    flagged = set()
    for r in mine:
        note = r.get("definition_note", "")
        if owns(r) and note and CUES.search(note) and r["concept_id"] not in replaced:
            alts = [s["text"] for s in r["strings"] if j in s.get("regional", []) and s["string_type"] != "preferred"]
            also = f" (also written {', '.join(chr(34) + a + chr(34) for a in alts)})" if alts else ""
            flagged.add(r["concept_id"])
            A.append({"kind": "yn", "part": "A", "concept_id": r["concept_id"], "maps_to_review": True,
                      "label": f"Is \"{r['preferred_term']}\" right and current?",
                      "text": f"Is \"{r['preferred_term']}\"{also} right and current for {name}? Our note on it says: \"{note}\" "
                              f"(N = wrong or out of date; please correct it in a comment.)"})

    # Part A3: hand-written questions for this state.
    for e in extras:
        if e["part"] == "key":
            A.append({"kind": e["kind"], "part": "A", "concept_id": None, "maps_to_review": False, "label": e["text"][:80], "text": e["text"]})

    # Part B: another name for a known term.
    for r in mine:
        for s in r["strings"]:
            if j in s.get("regional", []) and s["string_type"] in EQUIVALENT_TYPES and f"{r['concept_id']}|{s['text']}" not in skip_pairs:
                src = nv_sources(r)[0]
                B.append({"kind": "yn", "part": "B", "concept_id": r["concept_id"], "string": s["text"], "maps_to_review": False,
                          "label": f"\"{s['text']}\" = \"{r['preferred_term']}\"",
                          "_src": src, "text": f"\"{s['text']}\" = \"{r['preferred_term']}\""})

    # Part C: candidates nobody has confirmed.
    for r in mine:
        if r["review"]["status"] == "candidate" and r["concept_id"] not in flagged and r["concept_id"] not in replaced:
            src = nv_sources(r)[0]
            alts = [s["text"] for s in r["strings"] if j in s.get("regional", []) and s["string_type"] != "preferred"]
            body = f"\"{r['preferred_term']}\""
            if alts:
                body += f", also written {', '.join(chr(34) + a + chr(34) for a in alts)}"
            C.append({"kind": "yn", "part": "C", "concept_id": r["concept_id"], "maps_to_review": True, "label": r["preferred_term"],
                      "_src": src, "text": body, "_desc": r.get("definition_note", "") if owns(r) else ""})

    if limit:
        B, C = B[:limit], C[:limit]
    for it in B + C:  # number documents in the order items mention them
        it["_cite"] = docs.cite(it["_src"])

    for e in extras:
        if e["part"] == "missing":
            D.append({"kind": "text", "part": "D", "concept_id": None, "maps_to_review": False, "label": e["text"][:80], "text": e["text"], "_extra": True})
    return mine, docs, A, B, C, D


# ---------------------------------------------------------------- rendering

def render_items(items, letter, start=1):
    out = []
    for n, it in enumerate(items, start=start):
        it["id"] = f"{letter}{n}"
        if it["kind"] == "yn":
            if letter == "B":
                text = f"{it['text']} ({it['_cite']})"
            elif letter == "C":
                text = f"{it['text']} ({it['_cite']})"
            else:
                text = it["text"]
            block = wrap(text, f"{it['id']}.".ljust(5) + f"{BOX} ", " " * 11)
            if letter == "C" and it["_desc"]:
                block += "\n" + wrap(f"Our description: {it['_desc']}", " " * 11, " " * 11)
            if letter == "A":
                block += "\n" + " " * 11 + "Comment:"
        else:
            block = wrap(it["text"], f"{it['id']}.".ljust(5), " " * 5) + "\n" + " " * 5 + "Answer:"
        out.append(block)
    return out


def fill(text, values):
    for k, v in values.items():
        text = text.replace("{{" + k + "}}", str(v))
    return text


def read_template():
    sections, cur = {}, None
    for line in (OUTDIR / "template.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("@@ "):
            cur = line[3:].strip()
            sections[cur] = []
        elif cur and not line.startswith("#"):
            sections[cur].append(line)
    return {k: "\n".join(v).strip("\n") for k, v in sections.items()}


def read_extras(code, name):
    path = OUTDIR / "extras" / f"{name.lower().replace(' ', '_')}.tsv"
    rows = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            cols = (line.split("\t") + [""] * 5)[:5]
            rows.append(dict(zip(["part", "kind", "replaces", "skip_pair", "text"], cols)))
    return rows


def request(args):
    code, name = resolve_state(args.state)
    recs = load_records()
    stats = json.loads(STATS.read_text(encoding="utf-8"))
    today = dt.date.today()
    tpl = read_template()
    extras = read_extras(code, name)
    mine, docs, A, B, C, D = build_items(recs, code, name, args.stale_years, args.limit, extras, today)

    # Default Part D prompts come from the template, then the state's own.
    generic = [{"kind": "text", "part": "D", "concept_id": None, "maps_to_review": False,
                "label": t[:80], "text": t} for t in fill(tpl["default_d"], {"STATE": name}).splitlines() if t.strip()]
    D = D + generic

    real = [r for r in recs if r["review"]["status"] != "illustrative"]
    n_expert = sum(r["review"]["status"] == "expert_accepted" for r in real)
    n_cand = sum(r["review"]["status"] == "candidate" for r in mine)
    n_val = sum(r["review"]["status"] == "machine_validated" for r in mine)

    # Render numbered items first (this fixes the document numbering).
    ids_a, ids_b, ids_c, ids_d = (render_items(x, l) for x, l in ((A, "A"), (B, "B"), (C, "C"), (D, "D")))
    minutes_a = max(5, int(math.ceil(len(A) * 1.0 / 5.0) * 5))
    minutes = max(minutes_a, int(math.ceil((len(A) * 1.0 + (len(B) + len(C)) * 0.2 + len(D) * 1.5) / 5.0) * 5))
    doc_lines = [f"  [{i + 1}] {label}\n      {url}" if url else f"  [{i + 1}] {label}" for i, (label, url) in enumerate(docs.order)]
    inline = ""
    if docs.inline:
        prefixes = sorted({re.match(r"[^\d]+", c).group(0).strip() for c in docs.inline if re.match(r"[^\d]+", c)})
        names = ", ".join('"' + x + ' ..."' for x in prefixes)
        inline = f"rule sections cited as {names}" if prefixes else "rule sections"
    doc_short = "; ".join([d[0] for d in docs.order] + ([inline] if inline else []))
    form_id = f"{code}-{today:%Y%m%d}"
    sender = args.sender or "[YOUR NAME]"
    greeting = args.greeting or "[FIRST NAME]"
    signature = "\n".join([sender] + ([f"Reply to: {args.reply_to}"] if args.reply_to else ["Reply to: [YOUR EMAIL]"]))
    vals = {"STATE": name, "SENDER": sender, "GREETING": greeting, "MINUTES_A": minutes_a, "MINUTES": minutes,
            "N_CONCEPTS": f"{stats['concepts']:,}", "N_STATES": stats["states"], "N_EXPERT": n_expert, "N_STATE": len(mine),
            "N_VALIDATED": n_val, "N_CAND": n_cand, "N_A": len(A), "N_B": len(B), "N_C": len(C), "N_D": len(D),
            "DOC_LIST": doc_short, "SIGNATURE": signature}

    def section(key, body=None):
        parts = [RULE, fill(tpl[key], vals)] if key != "opening" and key != "close" else [fill(tpl[key], vals)]
        if body:
            parts.append("\n\n".join(body))
        return "\n\n".join(parts)

    pieces = [section("opening"), section("what"), section("why"), section("how"), section("about")]
    for key, blocks in (("part_a", ids_a), ("part_b", ids_b), ("part_c", ids_c), ("part_d", ids_d)):
        if blocks:
            pieces.append(section(key, blocks if key != "part_b" else ["\n".join(blocks)]))
    pieces.append(RULE + "\n\n" + fill(tpl["close"], vals))
    footer = [RULE, f"SPEDLex: {stats_url('repo')}", f"Browse every term: {stats_url('explorer')}", "",
              f"Documents we used for {name}:"] + doc_lines
    if docs.inline:
        footer.append("  Rule sections cited by number (for example " + docs.inline[0] + ") are in the state's administrative code.")
    footer += ["", f"Form ID: {form_id} (SPEDLex v{stats['version']}). Please leave this line in your reply."]
    subject = fill(tpl["subject"], vals)
    email = f"Subject: {subject}\n\n" + "\n\n".join(pieces) + "\n\n" + "\n".join(footer) + "\n"

    rounds = ROUNDS / form_id
    rounds.mkdir(parents=True, exist_ok=True)
    (rounds / "email.txt").write_text(email, encoding="utf-8")
    key = {"form_id": form_id, "state": code, "state_name": name, "spedlex_version": stats["version"], "generated": str(today),
           "items": {it["id"]: {k: v for k, v in it.items() if not k.startswith("_") and k not in ("id", "text")} | {"text": it["text"]}
                     for it in A + B + C + D}}
    (rounds / "key.json").write_text(json.dumps(key, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{name}: {len(A)} key questions, {len(B)} name pairs, {len(C)} candidate terms, {len(D)} open questions "
          f"(~{minutes_a} min for Part A, ~{minutes} min in all)\nwrote {rounds / 'email.txt'}\nwrote {rounds / 'key.json'}")
    if not args.sender or not args.reply_to or not args.greeting:
        print("note: fill in the [BRACKETED] sender, greeting and reply-to before sending (or pass --sender/--greeting/--reply-to).")
    if len(B) + len(C) > 60:
        print(f"note: {len(B) + len(C)} lines in Parts B and C is long for an email; consider --limit.")


def stats_url(which):
    toml = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(rf'^{"Homepage" if which == "repo" else "Explorer"}\s*=\s*"([^"]+)"', toml, re.M)
    return m.group(1) if m else ""


# ---------------------------------------------------------------- replies

HEADER = re.compile(r"^[>\s|]*([A-D]\d{1,3})\.\s")
STOP = re.compile(r"^[>\s|]*(=====|-----|PART [A-D]\b)")
ANSWER = re.compile(r"^[>\s|]*[A-D]\d{1,3}\.\s*\[\s*([^\]]*?)\s*\]")


def norm_answer(raw):
    """-> (yes|no|unsure|blank|other, leftover text)"""
    raw = raw.strip()
    if not raw:
        return "blank", ""
    m = re.match(r"(yes|y|no|n|\?|unsure|not sure|u)\b[\s.,:;\-–—]*(.*)$", raw, re.I | re.S) or re.match(r"(\?)(.*)$", raw)
    if not m:
        return "other", raw
    head = m.group(1).lower()
    return ("yes" if head in ("y", "yes") else "no" if head in ("n", "no") else "unsure"), m.group(2).strip()


def strip_quote(line):
    return re.sub(r"^[>\s|]+", "", line).strip()


def parse_reply(key, text):
    lines = text.splitlines()
    # item id -> (answer, comment lines, free-text lines)
    got, cur, mode = {}, None, None
    for line in lines:
        h = HEADER.match(line)
        if h and h.group(1) in key["items"]:
            cur, mode = h.group(1), None
            a = ANSWER.match(line)
            got[cur] = {"raw": a.group(1) if a else None, "comment": [], "answer": []}
            continue
        if STOP.match(line):
            cur, mode = None, None
            continue
        if not cur:
            continue
        body = strip_quote(line)
        m = re.match(r"comment\s*:\s*(.*)$", body, re.I)
        if m:
            mode = "comment"
            if m.group(1):
                got[cur]["comment"].append(m.group(1))
            continue
        m = re.match(r"answer\s*:\s*(.*)$", body, re.I)
        if m:
            mode = "answer"
            if m.group(1):
                got[cur]["answer"].append(m.group(1))
            continue
        if not body:
            mode = None
        elif mode in ("comment", "answer"):
            got[cur][mode].append(body)
    about = {}
    for line in lines:
        body = strip_quote(line)
        for field, pat in (("name", r"name\s*:\s*(.*)"), ("role", r"role\b[^:]*:\s*(.*)"), ("setting", r"setting\b[^:]*:\s*(.*)"),
                           ("affiliation", r"affiliation\b[^:]*:\s*(.*)")):
            m = re.match(pat, body, re.I)
            if m and field not in about and m.group(1).strip():
                about[field] = m.group(1).strip()
        m = re.match(r"credit\b[^\[]*\[\s*([^\]]*?)\s*\]", body, re.I)
        if m and "credit" not in about:
            about["credit"] = credit_choice(m.group(1))
    return got, about


def credit_choice(raw):
    """A = name, role and affiliation; B = name and role; C = anonymous. Anything unclear is anonymous."""
    c = raw.strip().upper()[:1]
    return c if c in ("A", "B", "C") else "C"


def reply(args):
    key = json.loads(Path(args.key).read_text(encoding="utf-8"))
    path = Path(args.reply)
    got, about = parse_reply(key, path.read_text(encoding="utf-8", errors="replace"))
    today = dt.date.today()
    st = key["state"]
    if args.reviewer:
        reviewer = args.reviewer
    elif about.get("credit") in ("A", "B") and about.get("name"):
        reviewer = about["name"] + (f" ({about['role']})" if about.get("role") else "")
    else:
        reviewer = "anonymous-" + st + "-" + hashlib.sha1(path.stem.encode()).hexdigest()[:4]
    rows, follow, counts = [], [], {}
    for iid, it in key["items"].items():
        g = got.get(iid)
        if not g:
            continue
        comment = " ".join(g["comment"]).strip()
        if it["kind"] == "text":
            free = " ".join(g["answer"]).strip()
            if free:
                follow.append((iid, it, "answer", free, comment))
            continue
        verdict, extra = norm_answer(g["raw"] or "")
        counts[verdict] = counts.get(verdict, 0) + 1
        comment = " ".join(x for x in (extra, comment) if x)
        if verdict == "blank":
            if comment:
                follow.append((iid, it, "no answer, but commented", "", comment))
            continue
        if it["maps_to_review"] and it["concept_id"] and verdict == "yes":
            rows.append((it["concept_id"], "accept", reviewer, str(today), (comment or f"confirmed by email, form {key['form_id']}").replace("\t", " ")))
            if comment:
                follow.append((iid, it, "yes, with comment", "", comment))
        elif it["maps_to_review"] and it["concept_id"] and verdict == "no" and it["part"] == "C" and comment:
            rows.append((it["concept_id"], "reject", reviewer, str(today), comment.replace("\t", " ")))
        elif it["part"] == "B" and verdict == "yes" and not comment:
            continue  # a confirmed name pair needs no action
        else:
            follow.append((iid, it, verdict, "", comment + ("  [reject needs a reason]" if verdict == "no" and it["part"] == "C" and not comment else "")))
    tsv = path.with_suffix(".proposed-reviews.tsv")
    tsv.write_text("concept_id\tdecision\treviewer\tdate\tnote\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
    md = [f"# Follow-ups from one {key['state_name']} reply (form {key['form_id']})", "",
          f"Reviewer: {reviewer}. Role: {about.get('role', 'not given')}. Setting: {about.get('setting', 'not given')}. "
          f"Credit choice: {about.get('credit', 'not answered (treated as anonymous)')}.", "",
          "Proposed review rows are in the .proposed-reviews.tsv beside this file. A maintainer reads them, then appends "
          "the good ones to `sources/reviews.tsv`. Nothing here has been applied.", ""]
    for iid, it, verdict, free, comment in follow:
        md.append(f"- **{iid}** {it['text'] if len(it['text']) < 200 else it['text'][:197] + '...'}  \n  verdict: {verdict}"
                  + (f"  \n  answer: {free}" if free else "") + (f"  \n  comment: {comment}" if comment else "")
                  + (f"  \n  concept: {it['concept_id']}" if it.get("concept_id") else ""))
    if about.get("credit") in ("A", "B") and about.get("name"):
        who = ", ".join([about["name"]] + [about[k] for k in ("role", "affiliation") if about.get(k) and (k == "role" or about["credit"] == "A")])
        md += ["", "## CONTRIBUTORS.md line (they opted in)", "",
               f"| {key['state_name']} | {who} | {today} |"]
    fu = path.with_suffix(".followups.md")
    fu.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"answers read: {counts or 'none'}\nproposed review rows: {len(rows)} -> {tsv}\nfollow-ups: {len(follow)} -> {fu}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    rq = sub.add_parser("request", help="write the email for one state")
    rq.add_argument("state", help="two-letter code or name, e.g. NV")
    rq.add_argument("--sender")
    rq.add_argument("--greeting")
    rq.add_argument("--reply-to", dest="reply_to")
    rq.add_argument("--limit", type=int, default=0, help="cap Part B and Part C at this many lines each")
    rq.add_argument("--stale-years", type=int, default=3, help="ask whether documents at least this old are still current")
    rq.set_defaults(fn=request)
    rp = sub.add_parser("reply", help="read one reply")
    rp.add_argument("key", help="key.json from the round")
    rp.add_argument("reply", help="the reply, saved as plain text")
    rp.add_argument("--reviewer", help="override the reviewer name written to the proposed rows")
    rp.set_defaults(fn=reply)
    args = ap.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
