"""Terminology helpers for AI and writing tools.

The Safelist (match.py) answers one question for a de-identification tool:
"is this span a special-education term?" The same records answer more, and
this module exposes them for tools that read or write special-education text
(chat assistants, summarizers, letter drafters, translation and plain-language
tools):

    from spedlex import Lexicon
    lex = Lexicon.from_default(jurisdiction="US-TX")   # the reader's state

    lex.lookup("CSE")          # what a term names, and what Texas calls it
    lex.annotate(text)         # every term in a text, with its concept and citation
    lex.check(text)            # disfavored, older, other-state and ambiguous terms
    lex.glossary(text)         # a short cited glossary to put in a model's prompt

The same functions are on the command line (python -m spedlex) and,
optionally, as an MCP server (spedlex/mcp_server.py). Everything runs locally on the bundled data; no text leaves the machine.

What the data can and cannot support (docs/USING-WITH-AI.md has more):
  * It records which names official documents use for a concept, where, and
    with a citation. It is not a dictionary of legal meanings, and
    `definition_note` is a short note in the project's own words.
  * A `regional` tag lists the states whose documents were read and use the
    form. Other states may use it too, and uncovered states are unknown, so
    other-state findings are hints, not errors.
  * Records are mostly unreviewed (`candidate`, `machine_validated`). Every
    result carries the review status so a tool can decide what to trust.

Matching follows the Safelist's rules (whole phrases, case-sensitive
acronyms, never_bare, month names next to numbers are skipped), but this
module indexes every state's strings, so it can recognise a term from
another state.
"""

import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional

from .match import _NUM_AFTER, _NUM_BEFORE, _MONTHS, _WORD, DEFAULT_STATUSES, load

ISSUE_KINDS = ("disfavored", "legacy", "other_state", "ambiguous")


def _jur(code):
    """'TX', 'tx', 'US-TX' -> 'US-TX'; 'US' and None pass through."""
    if code is None:
        return None
    code = code.strip().upper()
    if code == "US" or code.startswith("US-"):
        return code
    if re.fullmatch(r"[A-Z]{2}", code):
        return f"US-{code}"
    raise ValueError(f"not a jurisdiction: {code!r} (use a postal code like 'TX' or 'US-TX')")


@dataclass
class Annotation:
    """One special-education term found in a text."""
    start: int
    end: int
    text: str
    concept_id: Optional[str]          # None when the term is ambiguous (see candidates)
    preferred_term: Optional[str]      # the concept's national name
    category: Optional[str]
    string_type: Optional[str]         # preferred, synonym, acronym, legacy, ...
    regional: List[str] = field(default_factory=list)   # states whose documents use this form
    disfavored: bool = False
    usage_note: Optional[str] = None
    state_terms: List[str] = field(default_factory=list)  # what the reader's state calls the concept
    definition_note: Optional[str] = None
    citation: Optional[str] = None
    review_status: Optional[str] = None
    candidates: List[Dict[str, str]] = field(default_factory=list)  # when ambiguous

    def to_dict(self):
        return asdict(self)


@dataclass
class Issue:
    """Something a writer or a model may want to change."""
    kind: str                # disfavored | legacy | other_state | ambiguous
    start: int
    end: int
    text: str
    concept_id: Optional[str]
    message: str
    suggestion: Optional[str] = None

    def to_dict(self):
        return asdict(self)


class Lexicon:
    def __init__(self, records, jurisdiction=None, statuses=DEFAULT_STATUSES):
        """
        records       output of load()
        jurisdiction  the reader's state, e.g. "US-TX" or "TX". None means
                      national: no state-specific suggestions, and terms
                      that mean different things in different states are
                      reported as ambiguous.
        statuses      review statuses to include (default: candidate,
                      machine_validated, expert_accepted).
        """
        self.jurisdiction = _jur(jurisdiction)
        self._records = {}
        self._senses = defaultdict(list)  # (key text, case_sensitive) -> [(record, string)]
        covered = set()
        for r in records:
            if r["review"]["status"] not in statuses:
                continue
            self._records[r["concept_id"]] = r
            covered.update(s.get("jurisdiction") for s in r["sources"])
            never_bare = r["pii_risk"]["protect_rule"] == "never_bare"
            for s in r["strings"]:
                cs = s["match"] in ("phrase_cs", "token_cs")
                if never_bare and len(_WORD.findall(s["text"])) == 1 and not (cs and s["text"].isupper()):
                    continue
                key = (s["text"] if cs else s["text"].lower(), cs)
                self._senses[key].append((r, s))
        self.covered = frozenset(j for j in covered if j and j != "US")
        cs_texts = sorted({k for k, cs in self._senses if cs}, key=len, reverse=True)
        ci_texts = sorted({k for k, cs in self._senses if not cs}, key=len, reverse=True)
        self._patterns = [(p, cs) for p, cs in ((self._compile(cs_texts, 0), True),
                                                (self._compile(ci_texts, re.IGNORECASE), False)) if p]

    @classmethod
    def from_default(cls, **kwargs):
        return cls(load(), **kwargs)

    @staticmethod
    def _compile(texts, flags):
        if not texts:
            return None
        alts = "|".join(re.escape(t) for t in texts)
        return re.compile(rf"(?<![A-Za-z0-9])(?:{alts})(?![A-Za-z0-9])", flags)

    # ------------------------------------------------------------------
    # Concepts
    # ------------------------------------------------------------------

    def concept(self, concept_id):
        """The full record for a concept ID, or None."""
        return self._records.get(concept_id)

    def forms_by_jurisdiction(self, concept_id):
        """{'US': [national forms], 'US-TX': [Texas forms], ...}. A form with
        no regional tag belongs to the concept's own jurisdiction. Disfavored
        forms are left out."""
        r = self._records[concept_id]
        out = defaultdict(list)
        for s in r["strings"]:
            if s.get("disfavored"):
                continue
            for j in s.get("regional") or [r["jurisdiction"]]:
                out[j].append(s["text"])
        return dict(sorted(out.items(), key=lambda kv: (kv[0] != "US", kv[0])))

    def state_terms(self, concept_id, jurisdiction=None):
        """The forms the given state's documents use for a concept (not
        disfavored ones). Empty when the state has no form of its own on
        record; then the national preferred term is the best choice."""
        j = _jur(jurisdiction) or self.jurisdiction
        if not j or j == "US":
            return []
        r = self._records[concept_id]
        return [s["text"] for s in r["strings"] if j in (s.get("regional") or []) and not s.get("disfavored")]

    def best_term(self, concept_id, jurisdiction=None):
        """The single form to write for this reader: the state's own first
        phrase for the concept if it has one, else the national preferred term.
        A phrase that names the same thing comes first, and an older (legacy)
        form only if nothing current exists. Acronyms, abbreviations, plurals
        and 'related' forms (a narrower or broader term, a person, a document,
        a level) are never chosen, because they are not the same thing."""
        j = _jur(jurisdiction) or self.jurisdiction
        r = self._records[concept_id]
        if not j or j == "US":
            return r["preferred_term"]
        mine = [s for s in r["strings"] if j in (s.get("regional") or []) and not s.get("disfavored")]
        for skip in (("acronym", "abbreviation", "plural", "related", "legacy"),
                     ("acronym", "abbreviation", "plural", "related")):
            for s in mine:
                if s["string_type"] not in skip:
                    return s["text"]
        return r["preferred_term"]

    def lookup(self, term):
        """Every concept a surface form names, as plain dicts, best match
        for the reader's state first."""
        senses = self._senses.get((term, True)) or self._senses.get((term.lower(), False)) or []
        senses = self._rank(senses)
        return [self._describe(r, s) for r, s in senses]

    def _describe(self, r, s):
        cid = r["concept_id"]
        out = {
            "concept_id": cid,
            "preferred_term": r["preferred_term"],
            "category": r["category"],
            "jurisdiction": r["jurisdiction"],
            "matched_form": s["text"],
            "string_type": s["string_type"],
            "regional": s.get("regional", []),
            "disfavored": bool(s.get("disfavored")),
            "usage_note": s.get("usage_note"),
            "use_for_reader": self.best_term(cid) if self.jurisdiction else r["preferred_term"],
            "forms_by_jurisdiction": self.forms_by_jurisdiction(cid),
            "broader": [self._records[b]["preferred_term"] for b in r.get("broader", []) if b in self._records],
            "definition_note": r.get("definition_note"),
            "citations": [x["citation"] for x in r["sources"][:5]],
            "review_status": r["review"]["status"],
        }
        return out

    def _rank(self, senses):
        """Order senses by fit to the reader's state: tagged to it, then
        national, then other states."""
        j = self.jurisdiction

        def score(rs):
            r, s = rs
            reg = s.get("regional") or []
            if j and j in reg:
                return 0
            if not reg and r["jurisdiction"] in ("US", j):
                return 1
            return 2
        return sorted(senses, key=score)

    def _resolve(self, senses):
        """One sense if the reader's state settles it, else None."""
        if len(senses) == 1:
            return senses[0]
        j = self.jurisdiction
        if not j:
            return None
        fits = [(r, s) for r, s in senses if j in (s.get("regional") or [])]
        if len(fits) == 1:
            return fits[0]
        fits = [(r, s) for r, s in senses if not s.get("regional") and r["jurisdiction"] in ("US", j)]
        return fits[0] if len(fits) == 1 else None

    # ------------------------------------------------------------------
    # Text
    # ------------------------------------------------------------------

    @staticmethod
    def _in_date(text, m):
        if m.group().rstrip(".").lower() not in _MONTHS:
            return False
        return bool(_NUM_BEFORE.search(text[max(0, m.start() - 12):m.start()])
                    or _NUM_AFTER.search(text[m.end():m.end() + 12]))

    def _spans(self, text):
        cands = []
        for p, cs in self._patterns:
            for m in p.finditer(text):
                senses = self._senses.get((m.group(), True) if cs else (m.group().lower(), False))
                if senses and not self._in_date(text, m):
                    cands.append((m.start(), m.end(), m.group(), senses))
        cands.sort(key=lambda c: (-(c[1] - c[0]), c[0]))
        taken, out = [], []
        for c in cands:
            if all(c[1] <= a or c[0] >= b for a, b in taken):
                taken.append((c[0], c[1]))
                out.append(c)
        return sorted(out, key=lambda c: c[0])

    def annotate(self, text):
        """Every special-education term in text, longest match first, in order."""
        out = []
        for start, end, found, senses in self._spans(text):
            pick = self._resolve(senses)
            if pick is None:
                out.append(Annotation(start, end, found, None, None, None, None, candidates=[
                    {"concept_id": r["concept_id"], "preferred_term": r["preferred_term"],
                     "regional": ", ".join(s.get("regional") or [r["jurisdiction"]])}
                    for r, s in self._rank(senses)]))
                continue
            r, s = pick
            out.append(Annotation(
                start, end, found, r["concept_id"], r["preferred_term"], r["category"], s["string_type"],
                regional=list(s.get("regional", [])), disfavored=bool(s.get("disfavored")),
                usage_note=s.get("usage_note"), state_terms=self.state_terms(r["concept_id"]),
                definition_note=r.get("definition_note"), citation=r["sources"][0]["citation"],
                review_status=r["review"]["status"]))
        return out

    def check(self, text):
        """Terms a writer may want to change for this reader.

        disfavored   a form flagged as no longer acceptable (see usage_note)
        legacy       an older form; the current one is suggested
        other_state  a form recorded only in other states' documents, or a
                     concept that exists only in another state (only when
                     the reader's state is covered by the data)
        ambiguous    a form that names different concepts in different
                     states, with no reader's state to settle it
        """
        issues = []
        j = self.jurisdiction
        for a in self.annotate(text):
            if a.concept_id is None:
                options = "; ".join(f"{c['preferred_term']} ({c['regional']})" for c in a.candidates)
                issues.append(Issue("ambiguous", a.start, a.end, a.text, None,
                                    f"'{a.text}' names different things in different states: {options}. "
                                    "Spell it out, or set the reader's state."))
                continue
            best = self.best_term(a.concept_id) if j else a.preferred_term
            if a.disfavored:
                issues.append(Issue("disfavored", a.start, a.end, a.text, a.concept_id,
                                    a.usage_note or f"'{a.text}' is no longer an acceptable term.", best))
                continue
            if a.string_type == "legacy":
                issues.append(Issue("legacy", a.start, a.end, a.text, a.concept_id,
                                    f"'{a.text}' is an older name for {a.preferred_term}; current documents use '{best}'."
                                    + (f" {a.usage_note}" if a.usage_note else ""), best))
                continue
            if not j or j not in self.covered:
                continue
            rec = self._records[a.concept_id]
            if rec["jurisdiction"] not in ("US", j):
                issues.append(Issue("other_state", a.start, a.end, a.text, a.concept_id,
                                    f"'{a.text}' is specific to {rec['jurisdiction']}; it has no recorded counterpart "
                                    f"in {j}'s documents.", None))
            elif a.regional and j not in a.regional:
                # A short all-lowercase phrase ("team meeting") is too likely
                # to be ordinary English to call it another state's term.
                if best.lower() == a.text.lower() or (a.text.islower() and len(_WORD.findall(a.text)) < 3):
                    continue
                issues.append(Issue("other_state", a.start, a.end, a.text, a.concept_id,
                                    f"'{a.text}' is the term in {', '.join(a.regional)}; {j}'s documents say "
                                    f"'{best}' for {a.preferred_term}.", best))
        return issues

    def glossary(self, text, max_terms=40):
        """A compact, cited glossary of the terms in text, as Markdown, to
        include in a model's prompt. One entry per concept."""
        seen, lines = set(), []
        for a in self.annotate(text):
            if a.concept_id is None:
                opts = "; ".join(f"{c['preferred_term']} ({c['regional']})" for c in a.candidates)
                key = ("?", a.text)
                if key not in seen:
                    seen.add(key)
                    lines.append(f"- **{a.text}**: ambiguous across states: {opts}.")
                continue
            if a.concept_id in seen:
                continue
            seen.add(a.concept_id)
            bits = [f"- **{a.text}**: {a.preferred_term}" if a.text.lower() != a.preferred_term.lower()
                    else f"- **{a.text}**"]
            bits[0] += f" ({a.category.replace('_', ' ')}; {a.concept_id})."
            if self.jurisdiction and self.jurisdiction != "US":
                st = a.state_terms
                if st:
                    bits.append(f"In {self.jurisdiction}: {', '.join(dict.fromkeys(st))}.")
            if a.disfavored:
                bits.append(f"Disfavored term: {a.usage_note}")
            elif a.string_type == "legacy":
                bits.append("Older name.")
            if a.definition_note:
                bits.append(f"Note: {a.definition_note}")
            bits.append(f"Source: {a.citation}. Review status: {a.review_status}.")
            lines.append(" ".join(bits))
            if len(seen) >= max_terms:
                break
        if not lines:
            return ""
        from . import __version__
        where = f", reader's jurisdiction {self.jurisdiction}" if self.jurisdiction else ""
        head = (f"Special-education terms in this text (from SPEDLex v{__version__}{where}). "
                "These record how official documents name each concept; they are not legal definitions.")
        return head + "\n" + "\n".join(lines)
