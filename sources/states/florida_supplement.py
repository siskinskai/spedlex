"""
Florida layer, consistency additions.

A second reading of the Florida layer's own documents for terms the first
pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PSN  Part B Procedural Safeguards Notice: Florida (Aug. 2021), cited by page
  R11  Fla. Admin. Code R. 6A-6.03411(1) (definitions), cited by paragraph
"""

from .florida import src, A, S, V, L, AB, P, FL, FLJ

CONCEPTS = [
    ("fl_beess", "Bureau of Exceptional Education and Student Services", "legal_procedural", [], src("R11", "(ll)"),
     {**FLJ, "broader": "fldoe"}),
    ("fl_extraordinary_exemption", "Extraordinary exemption", "iep_component", [], src("PSN", "p. 14"),
     {**FLJ, "note": "An exemption from participation in a state assessment."}),
    ("fl_statutes", "Florida Statutes", "legal_procedural", [], src("PSN", "p. 14"), FLJ),
    ("prot_advocacy", "Protection and advocacy agency", "legal_procedural", [("protection and advocacy agencies", P, None)],
     src("PSN", "p. 10"), {}),
]

STRINGS = []

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-FL"
LAYER_NAME = "Florida (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
