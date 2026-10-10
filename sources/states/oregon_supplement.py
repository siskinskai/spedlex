"""
Oregon layer, consistency additions.

A second reading of the Oregon layer's safeguards notice for terms the first
pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PSN  ODE Procedural Safeguards Notice K-21, cited by page
"""

from .oregon import src, A, S, V, L, AB, P, OR, ORJ

STRINGS = []

CONCEPTS = [
    ("or_oya", "Oregon Youth Authority", "legal_procedural", [], src("PSN", "p. 9"), ORJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-OR"
LAYER_NAME = "Oregon (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
