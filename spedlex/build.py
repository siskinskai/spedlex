"""Build SPEDLex from its source modules.

    python -m spedlex.build             rebuild data/ (fails on unregistered concepts)
    python -m spedlex.build --register  also give new concepts permanent IDs
    python -m spedlex.build --check     rebuild in memory; fail if data/ is stale
    python -m spedlex.build --adapter none --out /tmp/x   test another scrubber

Inputs
  sources/federal.py         34 CFR Part 300 core and illustrative placeholders
  sources/states/*.py        one module per state layer, applied in LAYERS order
  sources/reviews.tsv        human review decisions
  sources/disfavored.tsv     strings flagged as no longer acceptable in new writing
  sources/documents.tsv      manifest of source documents (URL, hash, snapshot); records cite rows by doc_id
  data/concept_ids.tsv       permanent key -> concept_id registry
  schema/sped_concept.schema.json

Outputs (data/)
  spedlex.jsonl              one concept record per line
  spedlex.csv                one row per surface string, for spreadsheets
  collision_report.csv       every string a scrubber or name list would hit
  stats.json                 counts used by the README and the site
  ../docs/SOURCES.md         every document cited, grouped by jurisdiction
"""

import argparse
import csv
import importlib
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from jsonschema import Draft202012Validator

from . import __version__
from .adapters import DEFAULT, get_adapter
from .risk import assess_risk

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sources import federal  # noqa: E402
from sources.states import LAYERS  # noqa: E402

A = "acronym"
REGISTRY = ROOT / "data" / "concept_ids.tsv"
MANIFEST = ROOT / "sources" / "documents.tsv"
ILLUSTRATIVE_BASE = 900000


# --------------------------------------------------------------------------
# Concept-ID registry. IDs are permanent: once a key has an ID it keeps it,
# and an ID is never handed to a different key, even after retirement.
# --------------------------------------------------------------------------

class Registry:
    def __init__(self, path=REGISTRY):
        self.path = path
        self.rows = {}  # key -> [concept_id, preferred_term, status]
        if path.exists():
            for line in path.read_text().splitlines()[1:]:
                key, cid, term, status = line.split("\t")
                self.rows[key] = [cid, term, status]
        self.new = []

    def get(self, key, term, illustrative, register):
        if key in self.rows:
            row = self.rows[key]
            if row[2] == "retired":
                raise SystemExit(f"key {key!r} ({row[0]}) is retired; choose a new key")
            row[1] = term
            return row[0]
        if not register:
            raise SystemExit(f"concept {key!r} ({term}) has no ID yet; run with --register")
        nums = [int(r[0].split(":")[1]) for r in self.rows.values()]
        pool = [n for n in nums if (n > ILLUSTRATIVE_BASE) == illustrative]
        floor = ILLUSTRATIVE_BASE if illustrative else 0
        cid = f"SPED:{max(pool, default=floor) + 1:06d}"
        self.rows[key] = [cid, term, "active"]
        self.new.append((key, cid))
        return cid

    def text(self):
        out = ["key\tconcept_id\tpreferred_term\tstatus"]
        for key, (cid, term, status) in sorted(self.rows.items(), key=lambda kv: kv[1][0]):
            out.append(f"{key}\t{cid}\t{term}\t{status}")
        return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Record construction
# --------------------------------------------------------------------------

def make_string(text, stype, regional=None):
    s = {"text": text, "string_type": stype, "match": "phrase_cs" if stype == A else "phrase_ci"}
    if regional:
        s["regional"] = list(regional)
    return s


def norm(s):
    return s["text"] if s["match"] == "phrase_cs" else s["text"].lower()


def federal_records(reg, register, adapter):
    records, keys, flags = [], {}, {}
    for key, pref, *_ in federal.SEED:
        keys[key] = reg.get(key, pref, False, register)
    for key, pref, cat, cit, extras, opts in federal.SEED:
        regional = opts.get("regional", {})
        strings = [make_string(pref, "preferred")] + [make_string(t, st, regional.get(t)) for t, st in extras]
        flags[key] = opts.get("flags", [])
        rec = {
            "concept_id": keys[key],
            "preferred_term": pref,
            "category": cat,
            "strings": strings,
            "sources": [{
                "source_type": "federal_regulation",
                "citation": f"34 CFR {cit}",
                "url": federal.LII.format(cit.split("(")[0]),
                "retrieved": federal.RETRIEVED,
                "jurisdiction": "US",
                "assisted_by": federal.ASSISTED_BY,
            }],
            "cross_maps": [{"system": s, **({"label": lbl} if lbl else {}), "relation": r}
                           for s, lbl, r in opts.get("xmap", [])] or [{"system": "MeSH", "relation": "pending"}],
            "pii_risk": assess_risk(strings, flags[key], adapter),
            "review": {"status": "machine_validated", "reviewers": 0},
            "extraction": {"method": "regulatory_definition" if "(" in cit or cit in ("300.17", "300.22") else "regulatory_heading"},
            "jurisdiction": "US",
            "version_added": federal.VERSION_ADDED,
        }
        if opts.get("broader"):
            rec["broader"] = [keys[opts["broader"]]]
        if opts.get("note"):
            rec["definition_note"] = opts["note"]
        records.append(rec)
    return records, keys, flags


def apply_layer(mod, records, keys, flags, reg, register, adapter):
    """Attach a state's strings to existing concepts and add its new concepts."""
    by_id = {r["concept_id"]: r for r in records}
    retrieved = getattr(mod, "RETRIEVED", federal.RETRIEVED)

    def add_source(rec, source):
        source = {**source, "retrieved": retrieved, "jurisdiction": mod.JURISDICTION, "assisted_by": mod.ASSISTED_BY}
        if source["citation"] not in {s["citation"] for s in rec["sources"]}:
            rec["sources"].append(source)

    for key, strings, source in mod.STRINGS:
        if key not in keys:
            raise SystemExit(f"{mod.__name__}: STRINGS refers to unknown concept key {key!r}")
        rec = by_id[keys[key]]
        add_source(rec, source)
        have = {norm(s): s for s in rec["strings"]}
        for text, stype, regional in strings:
            s = make_string(text, stype, regional)
            if norm(s) in have:
                if regional:
                    old = have[norm(s)]
                    old["regional"] = sorted(set(old.get("regional", [])) | set(regional))
                continue
            rec["strings"].append(s)
            have[norm(s)] = s
        rec["pii_risk"] = assess_risk(rec["strings"], flags.get(key, []), adapter)

    for key, pref, *_ in mod.CONCEPTS:
        if key in keys:
            raise SystemExit(f"{mod.__name__}: concept key {key!r} is already defined by an earlier layer")
        keys[key] = reg.get(key, pref, False, register)
    for key, pref, cat, strings, source, opts in mod.CONCEPTS:
        strs = [make_string(pref, "preferred")] + [make_string(t, st, rg) for t, st, rg in strings]
        is_reg = source["source_type"] == "state_regulation"
        rec = {
            "concept_id": keys[key],
            "preferred_term": pref,
            "category": cat,
            "strings": strs,
            "sources": [{**source, "retrieved": retrieved, "jurisdiction": mod.JURISDICTION, "assisted_by": mod.ASSISTED_BY}],
            "cross_maps": [{"system": "ERIC", "relation": "pending"}],
            "pii_risk": assess_risk(strs, opts.get("flags", []), adapter),
            "review": {"status": opts.get("status", "machine_validated" if is_reg else "candidate"), "reviewers": 0,
                       **({} if is_reg else {"notes": "Page reference from text extraction; confirm against the PDF."})},
            "extraction": {"method": "regulatory_heading" if is_reg else "manual"},
            "jurisdiction": opts.get("jurisdiction", "US"),
            "version_added": mod.VERSION_ADDED,
        }
        if opts.get("broader"):
            # Resolved in build() after every layer is applied, so a layer can
            # point at a parent concept that a later layer defines.
            b = opts["broader"]
            rec["_broader"] = [b] if isinstance(b, str) else list(b)
        if opts.get("note"):
            rec["definition_note"] = opts["note"]
        records.append(rec)
        by_id[rec["concept_id"]] = rec
        flags[key] = opts.get("flags", [])


def illustrative_records(reg, register, adapter):
    out = []
    for entry in federal.ILLUSTRATIVE:
        if entry is None:  # retired placeholder; its ID stays reserved in the registry
            continue
        key, pref, cat, extras, method, flags, stype = entry
        strings = [make_string(pref, "preferred")] + [make_string(t, st) for t, st in extras]
        out.append({
            "concept_id": reg.get(key, pref, True, register),
            "preferred_term": pref,
            "category": cat,
            "strings": strings,
            "sources": [{"source_type": stype, "citation": "ILLUSTRATIVE: placeholder for a later harvest",
                         "retrieved": federal.RETRIEVED, "assisted_by": federal.ASSISTED_BY}],
            "cross_maps": [{"system": "ERIC", "relation": "pending"}],
            "pii_risk": assess_risk(strings, flags, adapter),
            "review": {"status": "illustrative", "reviewers": 0,
                       "notes": "Shows the shape of later-phase records; not attested by a regulation or state source yet."},
            "extraction": {"method": method},
            "jurisdiction": "US",
            "version_added": federal.VERSION_ADDED,
        })
    return out


def apply_reviews(records, path=ROOT / "sources" / "reviews.tsv"):
    """Apply human review decisions from sources/reviews.tsv.

    Columns: concept_id, decision (accept | reject), reviewer, date, note.
    A reviewer's latest row for a concept counts. Any reject makes the
    concept expert_rejected (kept in the data so it isn't re-added, but
    excluded by the matcher); otherwise one accept makes it expert_accepted.
    """
    if not path.exists():
        return
    by_id = {r["concept_id"]: r for r in records}
    latest = {}
    for n, line in enumerate(path.read_text().splitlines()[1:], start=2):
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) != 5:
            raise SystemExit(f"reviews.tsv line {n}: expected 5 tab-separated columns, got {len(cols)}")
        cid, decision, reviewer, date, note = cols
        if cid not in by_id:
            raise SystemExit(f"reviews.tsv line {n}: unknown concept {cid}")
        if decision not in ("accept", "reject"):
            raise SystemExit(f"reviews.tsv line {n}: decision must be accept or reject")
        if decision == "reject" and not note.strip():
            raise SystemExit(f"reviews.tsv line {n}: a reject needs a note saying why")
        if by_id[cid]["review"]["status"] == "illustrative":
            raise SystemExit(f"reviews.tsv line {n}: {cid} is an illustrative placeholder")
        latest[(cid, reviewer)] = (decision, date, note)
    per = defaultdict(list)
    for (cid, reviewer), (decision, date, note) in latest.items():
        per[cid].append((decision, reviewer, date, note))
    for cid, decisions in per.items():
        rev = by_id[cid]["review"]
        accepts = [d for d in decisions if d[0] == "accept"]
        rejects = [d for d in decisions if d[0] == "reject"]
        rev["reviewers"] = len(decisions)
        rev["status"] = "expert_rejected" if rejects else "expert_accepted"
        notes = "; ".join(f"{d[1]} ({d[2]}): {d[3]}" for d in (rejects or accepts) if d[3])
        if notes:
            rev["notes"] = notes
        else:
            rev.pop("notes", None)


DISFAVORED_COLUMNS = ["key", "string", "usage_note", "basis", "assisted_by"]


def apply_disfavored(records, keys, path=ROOT / "sources" / "disfavored.tsv"):
    """Flag strings from sources/disfavored.tsv as disfavored.

    Columns: key, string, usage_note, basis, assisted_by. The string must
    already exist on the concept (it stays matched: older documents use it)
    and may not be the concept's preferred term; to retire a preferred term,
    change the concept's preferred term instead.
    """
    if not path.exists():
        return
    by_id = {r["concept_id"]: r for r in records}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t") != DISFAVORED_COLUMNS:
        raise SystemExit(f"disfavored.tsv: header must be exactly: {chr(9).join(DISFAVORED_COLUMNS)}")
    for n, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) != len(DISFAVORED_COLUMNS):
            raise SystemExit(f"disfavored.tsv line {n}: expected {len(DISFAVORED_COLUMNS)} columns, got {len(cols)}")
        key, text, note, basis, assisted = (c.strip() for c in cols)
        if key not in keys:
            raise SystemExit(f"disfavored.tsv line {n}: unknown concept key {key!r}")
        if not (note and basis and assisted):
            raise SystemExit(f"disfavored.tsv line {n}: usage_note, basis and assisted_by are all required")
        rec = by_id[keys[key]]
        hits = [s for s in rec["strings"] if s["text"] == text]
        if not hits:
            raise SystemExit(f"disfavored.tsv line {n}: {text!r} is not a string of {key!r}")
        if hits[0]["string_type"] == "preferred":
            raise SystemExit(f"disfavored.tsv line {n}: {text!r} is {key!r}'s preferred term; change the preferred term instead")
        hits[0].update({"disfavored": True, "usage_note": note, "usage_basis": basis})


def build(adapter, register=False):
    reg = Registry()
    records, keys, flags = federal_records(reg, register, adapter)
    for name in LAYERS:
        mod = importlib.import_module(f"sources.states.{name}")
        apply_layer(mod, records, keys, flags, reg, register, adapter)
    for r in records:
        pending = r.pop("_broader", None)
        if pending:
            unknown = [k for k in pending if k not in keys]
            if unknown:
                raise SystemExit(f"{r['preferred_term']}: 'broader' refers to unknown concept key(s) {unknown}")
            r["broader"] = [keys[k] for k in pending]
            if "definition_note" in r:  # keep the field order the files have always used
                r["definition_note"] = r.pop("definition_note")
    apply_disfavored(records, keys)
    records += illustrative_records(reg, register, adapter)
    apply_reviews(records)
    seen = {r["concept_id"] for r in records}
    missing = [f"{k} ({cid})" for k, (cid, _, st) in reg.rows.items() if st == "active" and cid not in seen]
    if missing:
        raise SystemExit("registered concepts missing from sources (mark them 'retired' in "
                         f"data/concept_ids.tsv if the removal is intended): {missing}")
    return records, reg


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def validate(records):
    schema = json.loads((ROOT / "schema" / "sped_concept.schema.json").read_text())
    v = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
    return [f"{r['concept_id']} {r['preferred_term']}: {e.message}" for r in records for e in v.iter_errors(r)]


def duplicate_strings(records):
    """A string may belong to two concepts only when each use is tagged to a
    different state (a regional ambiguity, reported); otherwise it's an error."""
    uses = defaultdict(list)
    for r in records:
        for s in r["strings"]:
            uses[norm(s)].append(tuple(s.get("regional") or ()))
    ambiguous, conflicts = [], []
    for text, regions in sorted(uses.items()):
        if len(regions) < 2:
            continue
        if all(regions) and len(set(regions)) == len(regions):
            ambiguous.append(f"{text} ({', '.join('/'.join(x) for x in regions)})")
        else:
            conflicts.append(text)
    return ambiguous, conflicts


MANIFEST_COLUMNS = ["doc_id", "jurisdiction", "title", "publisher", "edition_date", "url", "retrieved", "sha256",
                    "bytes", "pages", "wayback_url", "rights", "local_name", "notes"]
RIGHTS = {"federal_public_domain", "state_law_text", "state_guidance", "third_party"}
DOC_ID = re.compile(r"^[a-z]{2}-[a-z0-9-]+-\d{4}$")


def load_manifest(path=MANIFEST):
    """sources/documents.tsv -> ({doc_id: row}, [problems])."""
    problems, rows = [], {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t") != MANIFEST_COLUMNS:
        return {}, [f"{path.name}: header must be exactly: {chr(9).join(MANIFEST_COLUMNS)}"]
    for n, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != len(MANIFEST_COLUMNS):
            problems.append(f"{path.name} line {n}: {len(cells)} columns, expected {len(MANIFEST_COLUMNS)}")
            continue
        row = dict(zip(MANIFEST_COLUMNS, cells))
        where = f"{path.name} {row['doc_id'] or 'line ' + str(n)}"
        if not DOC_ID.match(row["doc_id"]):
            problems.append(f"{where}: doc_id must look like wv-policy2419-2023")
        elif row["doc_id"] in rows:
            problems.append(f"{where}: duplicate doc_id")
        if not re.match(r"^(US|US-[A-Z]{2})$", row["jurisdiction"]):
            problems.append(f"{where}: jurisdiction must be US or US-XX")
        elif row["doc_id"][:2] != (row["jurisdiction"][3:].lower() or "us"):
            problems.append(f"{where}: doc_id prefix does not match jurisdiction {row['jurisdiction']}")
        if not re.match(r"^[0-9a-f]{64}$", row["sha256"]):
            problems.append(f"{where}: sha256 must be 64 hex digits")
        if not row["bytes"].isdigit():
            problems.append(f"{where}: bytes must be a whole number")
        if row["pages"] and not row["pages"].isdigit():
            problems.append(f"{where}: pages must be a whole number or empty")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", row["retrieved"]):
            problems.append(f"{where}: retrieved must be a date like 2026-10-09")
        if row["rights"] not in RIGHTS:
            problems.append(f"{where}: rights must be one of {sorted(RIGHTS)}")
        if not row["local_name"] or "/" in row["local_name"]:
            problems.append(f"{where}: local_name must be a bare file name")
        rows.setdefault(row["doc_id"], row)
    return rows, problems


def manifest_errors(records, path=MANIFEST):
    """Every doc_id on a source must be in the manifest, with the same jurisdiction;
    every manifest row must be cited by a record or declared in a module's UNCITED_DOCS."""
    rows, problems = load_manifest(path)
    cited = set()
    for r in records:
        for s in r["sources"]:
            did = s.get("doc_id")
            if not did:
                continue
            cited.add(did)
            if did not in rows:
                problems.append(f"{r['concept_id']} {r['preferred_term']}: doc_id {did!r} is not in sources/documents.tsv")
            elif rows[did]["jurisdiction"] != s.get("jurisdiction"):
                problems.append(f"{r['concept_id']} {r['preferred_term']}: doc_id {did!r} belongs to "
                                f"{rows[did]['jurisdiction']}, not {s.get('jurisdiction')}")
    declared = {}
    for name in LAYERS:
        mod = importlib.import_module(f"sources.states.{name}")
        for did in getattr(mod, "UNCITED_DOCS", {}):
            declared[did] = name
    for did, name in sorted(declared.items()):
        if did not in rows:
            problems.append(f"{name}.UNCITED_DOCS: {did!r} is not in sources/documents.tsv")
        elif did in cited:
            problems.append(f"{name}.UNCITED_DOCS: {did!r} is cited by a record; remove it from UNCITED_DOCS")
    unused = sorted(set(rows) - cited - set(declared))
    problems += [f"sources/documents.tsv {d}: no record cites it; cite it by doc_id or list it in a module's UNCITED_DOCS"
                 for d in unused]
    return problems


# --------------------------------------------------------------------------
# Outputs
# --------------------------------------------------------------------------

def render(records, reg, adapter):
    files = {}
    files["data/spedlex.jsonl"] = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records)

    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    key_of = {cid: key for key, (cid, _, _) in reg.rows.items()}
    w.writerow(["concept_id", "key", "preferred_term", "category", "string", "string_type", "match", "regional",
                "jurisdictions_attesting", "first_citation", "pii_level", "protect_rule", "review_status",
                "disfavored", "usage_note"])
    for r in records:
        juris = sorted({s.get("jurisdiction", "") for s in r["sources"]} - {""})
        for s in r["strings"]:
            w.writerow([r["concept_id"], key_of[r["concept_id"]], r["preferred_term"], r["category"], s["text"], s["string_type"], s["match"],
                        " ".join(s.get("regional", [])), " ".join(juris), r["sources"][0]["citation"],
                        r["pii_risk"]["level"], r["pii_risk"]["protect_rule"], r["review"]["status"],
                        "yes" if s.get("disfavored") else "", s.get("usage_note", "")])
    files["data/spedlex.csv"] = buf.getvalue()

    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["concept_id", "preferred_term", "review_status", "pii_level", "check", "hit"])
    for r in records:
        for h in r["pii_risk"]["scrubber_collisions"]:
            w.writerow([r["concept_id"], r["preferred_term"], r["review"]["status"], r["pii_risk"]["level"], f"scrubber:{adapter.NAME}", h])
        for h in r["pii_risk"]["name_list_hits"]:
            w.writerow([r["concept_id"], r["preferred_term"], r["review"]["status"], r["pii_risk"]["level"], "name_list", h])
        for h in r["pii_risk"].get("place_list_hits", []):
            w.writerow([r["concept_id"], r["preferred_term"], r["review"]["status"], r["pii_risk"]["level"], "place_list", h])
    files["data/collision_report.csv"] = buf.getvalue()

    files["data/concept_ids.tsv"] = reg.text()
    files["data/stats.json"] = json.dumps(stats(records, adapter), indent=2) + "\n"
    files["docs/SOURCES.md"] = sources_md(records)
    files["README.md"] = readme_with_stats(json.loads(files["data/stats.json"]))
    return files


def readme_with_stats(st):
    """Refresh the generated block between the stats markers in README.md."""
    readme = (ROOT / "README.md").read_text()
    start, end = "<!-- stats:start -->", "<!-- stats:end -->"
    if start not in readme:
        return readme
    reviewed = st["by_review_status"]
    risk = st["by_risk"]
    block = "\n".join([
        start,
        f"## What's in it (v{st['version']})",
        "",
        "| | |",
        "|---|---|",
        f"| Concepts | {st['concepts']:,}: {st['federal_concepts']} from 34 CFR Part 300, "
        f"{st['concepts'] - st['federal_concepts']} added by state layers |",
        f"| Surface strings | {st['strings']:,} (phrases, acronyms, plurals, legacy and regional forms): "
        f"{st['regional_strings']:,} tagged to the states that use them, {st['legacy_strings']} older forms, "
        f"{st['disfavored_strings']} flagged as disfavored |",
        f"| States | {st['states']}: {', '.join(st['state_codes'])} |",
        f"| Documents cited | {st['documents_cited']}, listed in [docs/SOURCES.md](docs/SOURCES.md) |",
        f"| Review status | {reviewed.get('machine_validated', 0)} checked against regulation text, "
        f"{reviewed.get('candidate', 0)} candidates awaiting a human check, "
        f"{reviewed.get('expert_accepted', 0)} expert-accepted |",
        f"| Privacy risk | {risk.get('none', 0)} none, {risk.get('low', 0)} low, {risk.get('high', 0)} high |",
        "",
        f"{st['illustrative_placeholders']} more records are **illustrative placeholders** for later work",
        "(test instruments, score terms). They're marked and excluded by default.",
        "",
        "_This section is generated by `python -m spedlex.build`._",
        end,
    ])
    return readme[:readme.index(start)] + block + readme[readme.index(end) + len(end):]


def stats(records, adapter):
    real = [r for r in records if r["review"]["status"] != "illustrative"]
    juris = sorted({s["jurisdiction"] for r in real for s in r["sources"] if s.get("jurisdiction", "US") != "US"})
    return {
        "version": __version__,
        "concepts": len(real),
        "illustrative_placeholders": len(records) - len(real),
        "federal_concepts": sum(1 for r in real if r["version_added"] == federal.VERSION_ADDED),
        "strings": sum(len(r["strings"]) for r in real),
        "disfavored_strings": sum(1 for r in real for s in r["strings"] if s.get("disfavored")),
        "legacy_strings": sum(1 for r in real for s in r["strings"] if s["string_type"] == "legacy"),
        "regional_strings": sum(1 for r in real for s in r["strings"] if s.get("regional")),
        "states": len(juris),
        "state_codes": [j[3:] for j in juris],
        "documents_cited": len({"34 CFR Part 300" if s["source_type"] == "federal_regulation" else (s.get("url") or s["citation"])
                                for r in real for s in r["sources"]}),
        "by_category": dict(sorted(Counter(r["category"] for r in real).items())),
        "by_risk": dict(sorted(Counter(r["pii_risk"]["level"] for r in real).items())),
        "by_review_status": dict(sorted(Counter(r["review"]["status"] for r in real).items())),
        "sources_by_assisting_model": dict(sorted(Counter(s.get("assisted_by", "unrecorded") for r in real for s in r["sources"]).items())),
        "collision_adapter": adapter.NAME,
        "concepts_with_scrubber_collisions": sum(1 for r in real if r["pii_risk"]["scrubber_collisions"]),
    }


def sources_md(records):
    groups = defaultdict(dict)
    for r in records:
        if r["review"]["status"] == "illustrative":
            continue
        for s in r["sources"]:
            url = s.get("url", "")
            doc = s["citation"].split(",")[0].strip()
            if s["source_type"] == "federal_regulation":
                doc = "34 CFR Part 300"
                url = "https://www.ecfr.gov/current/title-34/subtitle-B/chapter-III/part-300"
            doc = re.sub(r"(\([0-9A-Za-z]+\))+$", "", doc).strip()
            entry = groups[s.get("jurisdiction", "US")].setdefault(url or doc, [[], s["source_type"], 0])
            if doc not in entry[0]:
                entry[0].append(doc)
            entry[2] += 1
    names = {"US": "Federal"}
    for name in LAYERS:
        mod = importlib.import_module(f"sources.states.{name}")
        names.setdefault(mod.JURISDICTION, mod.LAYER_NAME.split(" (")[0])
    lines = ["# Sources", "",
             "Generated by `python -m spedlex.build`; do not edit by hand. Every document",
             "cited by at least one record, with the number of records that cite it. The",
             "state modules in `sources/states/` say which documents could not be read and why.", ""]
    for j in sorted(groups, key=lambda j: (j != "US", names.get(j, j))):
        lines += [f"## {names.get(j, j)} ({j})", "", "| Document | Type | Records |", "|---|---|---|"]
        for url, (docs, stype, n) in sorted(groups[j].items(), key=lambda kv: kv[1][0][0]):
            doc = "; ".join(sorted(docs)[:3]) + ("; ..." if len(docs) > 3 else "")
            label = f"[{doc}]({url})" if url.startswith("http") else doc
            lines.append(f"| {label} | {stype.replace('_', ' ')} | {n} |")
        lines.append("")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--register", action="store_true", help="assign permanent IDs to new concepts")
    ap.add_argument("--check", action="store_true", help="fail if committed outputs differ from a fresh build")
    ap.add_argument("--adapter", default=DEFAULT, help="scrubber collision adapter (default: %(default)s)")
    ap.add_argument("--out", type=Path, help="write outputs under this directory instead of the repo")
    args = ap.parse_args(argv)

    adapter = get_adapter(args.adapter)
    records, reg = build(adapter, register=args.register and not args.check)
    errors = validate(records)
    errors += manifest_errors(records)
    ambiguous, conflicts = duplicate_strings(records)
    for e in errors:
        print("INVALID", e)
    if conflicts:
        print("DUPLICATE strings across concepts:", conflicts)
    if ambiguous:
        print("Ambiguous across states (allowed):", "; ".join(ambiguous))
    files = render(records, reg, adapter)
    st = json.loads(files["data/stats.json"])
    print(f"{st['concepts']} concepts, {st['strings']} strings, {st['states']} states, "
          f"{st['illustrative_placeholders']} illustrative placeholders; risk {st['by_risk']}; "
          f"{st['concepts_with_scrubber_collisions']} concepts hit by the {adapter.NAME} adapter")
    for key, cid in reg.new:
        print(f"registered {cid} for {key}")
    if errors or conflicts:
        return 1

    base = args.out or ROOT
    if args.check:
        stale = [p for p, text in files.items() if not (base / p).exists() or (base / p).read_text() != text]
        if stale:
            print("STALE: these files differ from a fresh build; run `python -m spedlex.build` and commit:", stale)
            return 1
        print("check passed: committed outputs match a fresh build")
        return 0
    for p, text in files.items():
        (base / p).parent.mkdir(parents=True, exist_ok=True)
        (base / p).write_text(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
