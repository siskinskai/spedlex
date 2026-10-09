"""
Delaware layer, cross-document strings.

Strings for concepts that the Delaware layer defines from one document but
that another of its documents spells differently, and Delaware attestations
of concepts first defined by the Iowa layer. A layer's STRINGS can only point
at concepts defined by earlier layers, so these live here, and this module
comes after iowa in LAYERS.
Sources reviewed 2026-10-08 (the Delaware layer's documents and citation format):
  RULE922, RULE925  14 DE Admin. Code 922 and 925, cited by section
  PSN    DDOE, Delaware Procedural Safeguards (July 2026), cited by PDF page
  GUIDE  PIC of Delaware, Parents Are the Key (2d ed. 2013), cited by PDF page

Records are 'candidate'.
"""

from .delaware import src, A, S, V, L, AB, P, DE, DEJ, PS, G, R2, R5

STRINGS = [
    ("de_doe", [("DDOE", A, DE)], PS(6)),
    ("de_doe", [], G(3)),
    # Added after the 2026-10-08 audit: concepts the Iowa layer defines
    ("speech_path", [], R5("6.6.6")),
    ("phys_therapist", [], R2("3.0 (Physical Therapy)")),
    ("occ_therapist", [], R2("3.0 (Occupational Therapy)")),
]

CONCEPTS = []

JURISDICTION = "US-DE"
LAYER_NAME = "Delaware (cross-document strings)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.40.0"  # tools/add_state.py sets this
