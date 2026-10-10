"""
Michigan layer, consistency additions.

A second reading of the Michigan layer's own documents (in .sources-cache/mi/
and sources/documents.tsv), made on 2026-10-10 to bring the layer up to what
the newer layers record for agencies and their acronyms. See
provenance/consistency-audit-2026-10-10.md.

Sources reviewed 2026-10-10 (the Michigan layer's documents):
  PSN   MDE Procedural Safeguards Notice (updated 10/16/18), cited by PDF page
  PROG  MDE, IEP Development: Special Education Programs and Services (May 2022)

Records are 'candidate'. The rules (MARSE) were searched again and add
nothing new: their Michigan Register and Public Act citations are not terms.
"""

from .michigan import src, A, S, V, L, AB, P, MI, MIJ, N, G

STRINGS = [
    ("mi_moahr", [("State Office of Administrative Hearings and Rules", L, MI), ("SOAHR", A, MI)], N(3)),
]

CONCEPTS = [
    ("mi_ose", "Michigan Department of Education Office of Special Education", "legal_procedural", [("OSE", A, MI)], N(3),
     {**MIJ, "broader": "mi_mde", "note": "The full name is on PSN pp. 1 and 3 and the PROG cover; the PSN acronym list (p. 3) gives OSE."}),
    ("mi_sems", "Special Education Mediation Services", "legal_procedural", [], N(24), MIJ),
]

JURISDICTION = "US-MI"
LAYER_NAME = "Michigan (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.50.0"
