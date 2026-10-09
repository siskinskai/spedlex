"""
Maryland layer, audit additions.

Terms the independent audit of the Maryland layer (provenance/md/md-layer-audit-
2026-10-08.md) found in the same documents but missing from the first pass.
Sources reviewed 2026-10-08 (the Maryland layer's documents and citation format):
  RULE   COMAR 13A.05.01 (text saved in .sources-cache/md/MD-COMAR-13A.05.01.txt),
         cited by regulation and subsection

RULE records are 'machine_validated'. Left out on purpose: "nonpublic
school" (.03B(47)), which in Maryland means any private school, unlike the
California concept that uses the same words; and the other orientation and
mobility credentials in .08A(6)(d) (NOMC, ACVREP, NBPCB).
"""

from .maryland import src, A, S, V, L, AB, P, MD, MDJ, R

STRINGS = []

CONCEPTS = [
    ("coms", "Certified Orientation and Mobility Specialist", "personnel_role", [("COMS", A, None)], R(".08A(6)(d)"),
     {"note": "An orientation and mobility credential from the Academy for Certification of Vision Rehabilitation and Education Professionals."}),
    ("statewide_assess", "Statewide assessment", "iep_component", [], R(".03B(76)"),
     {"note": "The testing procedures a state adopts to measure student or school performance."}),
]

JURISDICTION = "US-MD"
LAYER_NAME = "Maryland (audit additions)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.38.0"
