"""
Georgia layer, consistency additions.

A second reading of Ga. Comp. R. & Regs. 160-4-7, rules .06 (IEP) and .21
(definitions), for terms the first pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  RULES  Ga. Comp. R. & Regs. 160-4-7-.06 and 160-4-7-.21, cited by paragraph
"""

from .georgia import src, A, S, V, L, AB, P, GA

GAJ = {"jurisdiction": "US-GA"}

STRINGS = []

CONCEPTS = [
    ("ga_bcw", "Babies Can't Wait", "early_intervention", [("BCW", A, GA)], src(".06", "(10)"),
     {**GAJ, "note": "Georgia's Part C early intervention program; also named in 160-4-7-.21."}),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-GA"
LAYER_NAME = "Georgia (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
