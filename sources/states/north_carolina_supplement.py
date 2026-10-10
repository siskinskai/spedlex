"""
North Carolina layer, consistency additions.

A second reading of the North Carolina layer's own two documents (both in
.sources-cache/nc/ and sources/documents.tsv), made on 2026-10-10 to bring
the layer up to what the newer layers record: the state agency's acronym,
the State Board, other state agencies and programs the policies name, the
standards and courses of study in the class-size chart, and federal laws the
policies cite. See provenance/consistency-audit-2026-10-10.md.

Sources reviewed 2026-10-10 (the North Carolina layer's documents):
  POL  Policies Governing Services for Children with Disabilities (rev. March
       2021, 132 pp.), cited by policy section and PDF page
  PSN  NCDPI Notice of Procedural Safeguards (July 2026)

POL records are 'machine_validated'. Left out on purpose: "Teacher
Assistants (TA)" (NC 1508-3; a two-letter acronym), the Department of Health
and Human Services and the Department of Correction (generic names other
states also use; the policies do not prefix them with the state), and the
board members named on PDF p. 2.
"""

from .north_carolina import src, A, S, V, L, AB, P, NC, NCJ

RP = lambda loc, page: src("POL", f"{loc} (PDF p. {page})")
FRONT = lambda page: {**src("POL", ""), "citation": f"NC Policies Governing Services for Children with Disabilities, front matter (PDF p. {page})"}

STRINGS = [
    ("nc_dpi", [("NCDPI", A, NC), ("NC Department of Public Instruction", AB, NC)], FRONT(2)),
    ("mckinney_vento", [], RP("1500-2.18", 15)),
    ("rehab_act", [], RP("1500-2.31", 20)),
]

CONCEPTS = [
    ("nc_sbe", "North Carolina State Board of Education", "legal_procedural", [], FRONT(2), {**NCJ, "broader": "sea"}),
    ("nc_djjdp", "Department of Juvenile Justice and Delinquency Prevention", "legal_procedural", [],
     RP("1500-2.24", 16), {**NCJ, "note": "Named among the state agencies that are public agencies."}),
    ("nc_lea_self_assessment", "LEA Self-Assessment", "legal_procedural", [], RP("1505-1.2", 103), NCJ),
    ("nc_dev_day", "Developmental Day Centers", "placement_setting", [], RP("1506-1.7", 123), NCJ),
    ("nc_irt", "Individual Residential Treatment", "placement_setting", [("IRT", A, NC)], RP("1506-1.5", 121), NCJ),
    ("nc_extended_content", "Extended Content Standards", "academic_skill", [], RP("1508-3.1", 131),
     {**NCJ, "note": "North Carolina's alternate academic achievement standards."}),
    ("nc_futureready_core", "FutureReady Core Course of Study", "academic_skill", [], RP("1508-3.1", 131), NCJ),
    ("gepa", "General Education Provisions Act", "legal_procedural", [("GEPA", A, None)], RP("1505-1.5", 105), {}),
]

JURISDICTION = "US-NC"
LAYER_NAME = "North Carolina (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.50.0"
