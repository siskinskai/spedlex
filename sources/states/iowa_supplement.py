"""
Iowa layer, cross-document strings.

Strings for concepts that the Iowa layer defines from one document but that
another of its documents spells differently. A layer's STRINGS can only
point at concepts defined by earlier layers, so these live here.
Sources reviewed 2026-10-08 (the Iowa layer's documents and citation format):
  GUIDE  Special Education Terms and Acronyms, Ages 3-21 (Iowa DE; undated,
         PDF created Feb. 2021), cited by page

"EI" usually means early intervention elsewhere; here it is the terms
sheet's acronym for an eligible individual, so it is tagged US-IA.
Records are 'candidate'.
"""

from .iowa import src, A, S, V, L, AB, P, IA, IAJ, G

STRINGS = [
    ("ia_eligible_individual", [("EI", A, IA)], G(3)),
]

CONCEPTS = []

JURISDICTION = "US-IA"
LAYER_NAME = "Iowa (cross-document strings)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.41.0"
