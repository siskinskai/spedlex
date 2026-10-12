"""
<State> layer for SPEDLex.

Copy this file to sources/states/<state>.py, fill it in, add the module
name to the end of LAYERS in sources/states/__init__.py, then run
    python tools/add_state.py <state>
CONTRIBUTING.md walks through each step.

Sources reviewed YYYY-MM-DD:
  PSN  <Agency>, <title of the procedural safeguards notice> (<date>)
  GUIDE  <Agency>, <parent guide or IEP manual> (<date>)
  RULE  <state administrative code citation>, definitions/eligibility

Say here which documents could not be read and why (dead link, scanned
PDF, robots.txt), and which copy you used instead.
Documents are not stored in the repository: add one row per document to
sources/documents.tsv (local copies go in .sources-cache/<xx>/), and put its
doc_id on every source below. A saved document that no record cites goes in
UNCITED_DOCS, with the reason.
Records from the regulation text are 'machine_validated'; records from
PDFs read by text extraction are 'candidate'.
"""

PSN_URL = "https://example.gov/procedural-safeguards.pdf"
RULE_URL = "https://www.law.cornell.edu/regulations/<state>/<section>"


def src(doc, loc=""):
    """Build a source dict. loc is a page or paragraph, e.g. 'p. 4' or '(2)(a)'."""
    tail = f", {loc}" if loc else ""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"<Code> <section>{tail}", "doc_id": "xx-rule-2026", "url": RULE_URL}
    return {"source_type": "procedural_safeguards_notice", "citation": f"<Agency> Procedural Safeguards Notice (<year>){tail}", "doc_id": "xx-psn-2026", "url": PSN_URL}


# string types
A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
XX = ["US-XX"]                    # regional tag for strings only used in this state
XXJ = {"jurisdiction": "US-XX"}   # opts for concepts that only exist in this state

# STRINGS: the state uses a concept that already exists (find its key in
# the `key` column of data/spedlex.csv). Each entry: (key, [(string, type, regional)], source).
# An empty list just records that this state's document attests the concept.
STRINGS = [
    ("iep", [], src("PSN", "p. 1")),
    ("ed", [("emotional disability", S, XX)], src("RULE", "(3)")),
]

# CONCEPTS: terms with no existing concept. Each entry:
# (new_key, preferred_term, category, [(string, type, regional)], source, opts)
# opts may hold: jurisdiction (for concepts created by state law or
# programs), broader (parent key, or a list of keys; the parent may come
# from any layer), note, flags (manual pii reasons such as
# "eponym" or "place_name"). State and territory names and postal codes
# are flagged automatically; add "place_name" by hand only for other places
# (cities, counties). Leave status out; the build assigns it.
# Prefix keys for state-only concepts with the lowercase state code.
CONCEPTS = [
    ("xx_doe", "<State> Department of Education", "legal_procedural", [("XDE", A, XX)], src("PSN", "p. 2"),
     {**XXJ, "broader": "sea"}),
]

JURISDICTION = "US-XX"
LAYER_NAME = "<State>"
RETRIEVED = "YYYY-MM-DD"
ASSISTED_BY = "none"  # or the model's API identifier, e.g. "claude-opus-5-5", "gpt-5", "gemini-2.5-pro"
VERSION_ADDED = "0.0.0"  # tools/add_state.py sets this
