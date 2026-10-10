"""Reference matcher: find safelisted spans in text and shield them from a
scrubber.

    from spedlex import Safelist
    sl = Safelist.from_default(jurisdictions={"US-TX"}, household_names={"Georgia"})
    masked, restore = sl.protect(note)
    redacted = restore(my_scrubber(masked))

Rules applied (docs/METHODOLOGY.md explains why):
  * phrase_ci strings match whole phrases, ignoring case; phrase_cs and
    token_cs strings match case-sensitively. "Whole" means the match is not
    preceded or followed by a letter or digit.
  * In a never_bare concept, a single-word string is skipped unless it is an
    all-caps acronym: "Kaufman" alone is never protected, though
    "Kaufman Assessment Battery for Children" is.
  * A two-letter all-caps string listed in pii_risk.possible_initials ("LS",
    "OT") is skipped unless the caller confirms it in confirmed_acronyms,
    because it could be a student's initials ("LS will...").
  * Any string containing a household name is dropped, so a child named
    Georgia or Braille is still redacted.
  * A match that is a month name or abbreviation ("APR", "May", "Sept") is
    skipped when a number sits next to it ("APR 14, 2015", "14-APR-15",
    "APR 2015"), so the matcher never shelters part of a date of birth.
  * Longest match wins; matches never overlap.
  * Illustrative placeholders are excluded unless asked for.
"""

import json
import re
from dataclasses import dataclass
from pathlib import Path

_PKG_DATA = Path(__file__).parent / "_data" / "spedlex.jsonl"
_REPO_DATA = Path(__file__).resolve().parents[1] / "data" / "spedlex.jsonl"
_WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")  # "Tourette's" is one word
_PLACEHOLDER_BASE = 0xF0000  # Supplementary Private Use Area-A: no scrubber pattern matches it
_MONTHS = frozenset(
    "january february march april may june july august september october november december "
    "jan feb mar apr jun jul aug sep sept oct nov dec".split())
_NUM_BEFORE = re.compile(r"\d(?:st|nd|rd|th)?[\s.,/-]*$", re.IGNORECASE)  # "14 APR", "14th-APR"
_NUM_AFTER = re.compile(r"^\.?[\s,/-]*\d")  # "APR 14", "APR. 14", "APR-2015", "APR/14"
DEFAULT_STATUSES = frozenset({"candidate", "machine_validated", "expert_accepted"})


def load(path=None):
    """Read SPEDLex records from a JSONL file (default: the bundled data)."""
    if path is None:
        path = _PKG_DATA if _PKG_DATA.exists() else _REPO_DATA
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


@dataclass(frozen=True)
class Match:
    start: int
    end: int
    text: str
    concept_id: str
    preferred_term: str


class Safelist:
    def __init__(self, records, jurisdictions=None, household_names=(), statuses=DEFAULT_STATUSES,
                 confirmed_acronyms=()):
        """
        records          output of load()
        jurisdictions    e.g. {"US-TX"}: keep federal terms plus these states'.
                         None keeps every state.
        household_names  names of the people in the documents; any string
                         containing one is dropped.
        statuses         review statuses to include. Add "illustrative" to
                         include placeholders.
        confirmed_acronyms  two-letter acronyms the user has confirmed are
                         acronyms, not initials, in this document (e.g.
                         {"LS"}). Any other possible_initials string is not
                         protected, so the scrubber redacts it.
        """
        keep_j = None if jurisdictions is None else {"US", *jurisdictions}
        household = {n.lower() for n in household_names}
        confirmed = frozenset(confirmed_acronyms)
        self._concepts = {}
        entries = {}  # (text, case_sensitive) -> concept_id
        for r in records:
            if r["review"]["status"] not in statuses:
                continue
            if keep_j is not None and r["jurisdiction"] not in keep_j:
                continue
            never_bare = r["pii_risk"]["protect_rule"] == "never_bare"
            initials = {p["text"] for p in r["pii_risk"].get("possible_initials", [])} - confirmed
            for s in r["strings"]:
                text = s["text"]
                if keep_j is not None and s.get("regional") and not set(s["regional"]) & keep_j:
                    continue
                words = _WORD.findall(text)
                cs = s["match"] in ("phrase_cs", "token_cs")
                if never_bare and len(words) == 1 and not (cs and text.isupper()):
                    continue
                if text in initials:
                    continue
                if household & {re.sub(r"['’]s$", "", w).lower() for w in words}:
                    continue
                entries.setdefault((text, cs), r["concept_id"])
            self._concepts[r["concept_id"]] = r["preferred_term"]
        self._lookup = {(t if cs else t.lower(), cs): cid for (t, cs), cid in entries.items()}
        self._patterns = [p for p in (self._compile([t for t, cs in entries if cs], 0),
                                      self._compile([t for t, cs in entries if not cs], re.IGNORECASE)) if p]

    @classmethod
    def from_default(cls, **kwargs):
        return cls(load(), **kwargs)

    @staticmethod
    def _compile(texts, flags):
        if not texts:
            return None
        alts = "|".join(re.escape(t) for t in sorted(set(texts), key=len, reverse=True))
        return re.compile(rf"(?<![A-Za-z0-9])(?:{alts})(?![A-Za-z0-9])", flags)

    def find(self, text):
        """Non-overlapping safelisted spans in text, longest first, returned in order."""
        cands = []
        for p in self._patterns:
            cs = not (p.flags & re.IGNORECASE)
            for m in p.finditer(text):
                key = (m.group(), True) if cs else (m.group().lower(), False)
                cid = self._lookup.get(key)
                if cid and self._in_date(text, m):
                    continue
                if cid:
                    cands.append(Match(m.start(), m.end(), m.group(), cid, self._concepts[cid]))
        cands.sort(key=lambda m: (-(m.end - m.start), m.start))
        taken, out = [], []
        for m in cands:
            if all(m.end <= a or m.start >= b for a, b in taken):
                taken.append((m.start, m.end))
                out.append(m)
        return sorted(out, key=lambda m: m.start)

    @staticmethod
    def _in_date(text, m):
        """True if the match is a month name with a number right next to it."""
        if m.group().rstrip(".").lower() not in _MONTHS:
            return False
        return bool(_NUM_BEFORE.search(text[max(0, m.start() - 12):m.start()])
                    or _NUM_AFTER.search(text[m.end():m.end() + 12]))

    def protect(self, text):
        """Replace each safelisted span with a one-character placeholder.

        Returns (masked_text, restore). Run your scrubber on masked_text, then
        call restore() on its output to put the protected spans back.
        """
        matches = self.find(text)
        if len(matches) > 0xFFFD:
            raise ValueError("too many protected spans in one text")
        parts, pos = [], 0
        for i, m in enumerate(matches):
            parts += [text[pos:m.start], chr(_PLACEHOLDER_BASE + i)]
            pos = m.end
        parts.append(text[pos:])
        spans = [m.text for m in matches]

        def restore(scrubbed):
            return "".join(spans[ord(c) - _PLACEHOLDER_BASE]
                           if _PLACEHOLDER_BASE <= ord(c) < _PLACEHOLDER_BASE + len(spans) else c
                           for c in scrubbed)

        return "".join(parts), restore

    def __len__(self):
        return len(self._lookup)
