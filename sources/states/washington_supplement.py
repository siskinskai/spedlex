"""
Washington layer, consistency additions.

A second reading of the Washington layer's safeguards notice for terms the
first pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PSN  OSPI Notice of Special Education Procedural Safeguards, cited by page
"""

from .washington import src, A, S, V, L, AB, P, WA, WAJ

STRINGS = []

CONCEPTS = [
    ("wa_wac", "Washington Administrative Code", "legal_procedural", [("WAC", A, WA)], src("PSN", "p. 6"), WAJ),
    ("wa_rcw", "Revised Code of Washington", "legal_procedural", [("RCW", A, WA)], src("PSN", "p. 16"), WAJ),
    ("parent_initiated_eval", "Parent-initiated evaluation", "evaluation_eligibility",
     [("Parent-Initiated Evaluations", P, None)], src("PSN", "p. 12"), {"broader": "iee"}),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-WA"
LAYER_NAME = "Washington (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
