"""PII-risk grading for safelist strings.

A safelist can do harm in one way: by sheltering a real identifier from
redaction. Every concept therefore gets a risk grade that limits how its
strings may be used. See docs/METHODOLOGY.md, "Grading privacy risk".
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES_DIR = ROOT / "reference" / "names"
_WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")  # "Tourette's" is one word


def _load(name):
    path = NAMES_DIR / name
    return frozenset(line.strip() for line in path.read_text().splitlines() if line.strip())


FIRST_NAMES = _load("ssa_first_names.txt")
SURNAMES = _load("census2000_surnames_10k.txt")

PLACES_DIR = ROOT / "reference" / "places"


def _tsv(name):
    rows = []
    for line in (PLACES_DIR / name).read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            rows.append(line.split("\t"))
    return rows


_JURISDICTIONS = _tsv("us_jurisdictions.tsv")
PLACE_NAMES = frozenset(name for name, code in _JURISDICTIONS)
POSTAL_CODES = frozenset(code for name, code in _JURISDICTIONS)
NOT_PLACES = frozenset(row[0] for row in _tsv("not_places.tsv"))
_PLACE_NAME_RE = re.compile(
    r"(?<![A-Za-z])(" + "|".join(re.escape(n) for n in sorted(PLACE_NAMES, key=len, reverse=True)) + r")(?![A-Za-z])",
    re.IGNORECASE)
_DOTTED = re.compile(r"(?<![A-Za-z])((?:[A-Z]\.){2,})")  # "D.C." -> "DC"


def words(text):
    return _WORD.findall(text)


def name_hits(text):
    """Tokens of text that appear in the reference first-name or surname lists."""
    hits = []
    for tok in words(text):
        t = re.sub(r"['’]s$", "", tok).lower()
        if len(t) < 2:
            continue
        if t in FIRST_NAMES:
            hits.append(("first", tok))
        if t in SURNAMES:
            hits.append(("surname", tok))
    return hits


def place_hits(text):
    """Place names in text: full state or territory names anywhere, and
    capitalized postal codes inside strings of two or more words."""
    hits = [m.group(1) for m in _PLACE_NAME_RE.finditer(text)]
    if text not in NOT_PLACES:
        undotted = _DOTTED.sub(lambda m: m.group(1).replace(".", "") + " ", text)
        toks = words(undotted)
        if len(toks) > 1:
            hits += [t for t in toks if t in POSTAL_CODES]
    return hits


def assess_risk(strings, manual_flags, adapter):
    """Grade a concept from its strings.

    high  a single-word string is itself a name (unless it is an all-caps
          acronym matched case-sensitively), the concept carries a manual
          eponym or place_name flag, a string contains a U.S. state or
          territory name or postal code (reference/places), or the
          scrubber's name dictionary fires on one of its strings.
          Rule: never_bare.
    low   any other name-list hit, scrubber hit, number, or manual flag.
          Rule: phrase_only.
    none  nothing found. Rule: phrase_or_token.
    """
    reasons = list(manual_flags)
    hits, names, places = [], [], []
    bare_name = False
    for s in strings:
        for h in adapter.collisions(s["text"]):
            hits.append(f"{h} <- '{s['text']}'")
            if h.startswith(adapter.NAME_DICT_PREFIX):
                if "common_first_name" not in reasons:
                    reasons.append("common_first_name")
            elif "collides_with_scrubber_pattern" not in reasons:
                reasons.append("collides_with_scrubber_pattern")
        nh = name_hits(s["text"])
        single = len(words(s["text"])) == 1
        # An all-caps acronym matched case-sensitively ("LEA") cannot shelter
        # the name "Lea", so the case rule is itself the guard.
        caps_acronym = s["match"] == "phrase_cs" and s["text"].isupper()
        for kind, tok in nh:
            names.append(f"{kind}:{tok} <- '{s['text']}'")
            reason = "common_first_name" if kind == "first" else "surname"
            if single and not caps_acronym:
                bare_name = True
            if single and reason not in reasons:
                reasons.append(reason)
        for tok in place_hits(s["text"]):
            places.append(f"place:{tok} <- '{s['text']}'")
            if "place_name" not in reasons:
                reasons.append("place_name")
        if any(c.isdigit() for c in s["text"]) and "contains_number" not in reasons:
            reasons.append("contains_number")
    if (bare_name or {"eponym", "place_name"} & set(reasons)
            or any(h.startswith(adapter.NAME_DICT_PREFIX) for h in hits)):
        level = "high"
    elif reasons or names:
        level = "low"
    else:
        level = "none"
    rule = {"high": "never_bare", "low": "phrase_only", "none": "phrase_or_token"}[level]
    return {"level": level, "reasons": reasons, "protect_rule": rule,
            "scrubber_collisions": hits, "name_list_hits": names, "place_list_hits": places}
