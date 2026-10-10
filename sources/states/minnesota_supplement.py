"""
Minnesota layer, consistency additions.

A second reading of Minn. R. ch. 3525 for terms the first pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the source is cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  DEF  Minn. R. ch. 3525 (full chapter as posted by the Revisor), cited by part
"""

from .minnesota import src, A, S, V, L, AB, P

MN = ["US-MN"]
MNJ = {"jurisdiction": "US-MN"}

STRINGS = []

CONCEPTS = [
    ("mn_tses", "Total special education system", "legal_procedural", [("TSES", A, MN)], src("DEF", "3525.1100, subp. 1"), MNJ),
    ("mn_pelsb", "Professional Educator Licensing and Standards Board", "legal_procedural", [], src("DEF", "3525.0210, subp. 44"), MNJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-MN"
LAYER_NAME = "Minnesota (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
