"""
Arizona layer, audit additions.

Terms the independent audit of the Arizona layer (provenance/az/az-layer-audit-
2026-10-08.md) found in the same documents but missing from the first pass.
Sources reviewed 2026-10-08 (the Arizona layer's documents and citation format):
  RULE   Ariz. Admin. Code R7-2-404, Special Education Voucher Program
         Policies and Procedures, from the same Secretary of State text of
         7 A.A.C. 2 (Supp. 25-4, PDF pp. 40-41), cited by subsection, e.g.
         "R7-2-404(A)". The first pass read only R7-2-401.

RULE records are 'machine_validated'. Left out on purpose: "SPA" (State
Placing Agency), a common word in capitals; the Arizona State Hospital
("ASH"), for the same reason; the residential voucher categories (NSE, CSE,
RSE); and the Division of Developmental Disabilities (GLOSS p. 48), whose
exact name New Jersey's layer already uses for its own agency.
"""

from .arizona import src, RULE_URL, A, S, V, L, AB, P, AZ, AZJ


def R4(loc):
    return {"source_type": "state_regulation", "citation": f"Ariz. Admin. Code R7-2-404{loc}", "doc_id": "az-aac7-2025", "url": RULE_URL}


STRINGS = []

CONCEPTS = [
    ("az_asdb", "Arizona Schools for the Deaf and the Blind", "placement_setting", [("ASDB", A, AZ)], R4("(A)"),
     {**AZJ, "broader": "state_sp_sch"}),
    ("az_inst_voucher", "Institutional voucher", "legal_procedural",
     [("special education institutional voucher", S, AZ)], R4("(A)"),
     {**AZJ, "note": "State funding for students in special education programs at ASDB or the Arizona State Hospital."}),
    ("az_hsd", "Home school district", "legal_procedural", [("HSD", A, AZ)], R4("(A)(1)(b)"),
     {**AZJ, "broader": "lea", "note": "The district that stays responsible for a student placed in an institution or residential facility under a voucher."}),
    ("az_spa", "State Placing Agency", "legal_procedural", [], R4("(B)(2)(a)(i)"),
     {**AZJ, "note": "One of the state agencies that can place a student in a private residential facility under a residential voucher."}),
]

JURISDICTION = "US-AZ"
LAYER_NAME = "Arizona (audit additions)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.38.0"
