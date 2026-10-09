"""
Alabama layer, audit additions.

Terms the independent audit of the Alabama layer (provenance/al/al-layer-audit-
2026-10-08.md) found in the same documents but missing from the first pass.
Sources reviewed 2026-10-08 (the Alabama layer's documents and citation format):
  RULE   Ala. Admin. Code ch. 290-8-9 (Supp. No. 13-3; ALSDE copy, 94 pp.)

RULE records are 'machine_validated'.
"""

from .alabama import src, A, S, V, L, AB, P, AL, ALJ, R

STRINGS = []

CONCEPTS = [
    ("child_count", "Child Count", "legal_procedural", [], R(".12(8)"),
     {"note": "The LEA's count of students served, taken as of a State capture date; Alabama's rule says when gifted students are included."}),
]

JURISDICTION = "US-AL"
LAYER_NAME = "Alabama (audit additions)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.38.0"  # tools/add_state.py sets this
