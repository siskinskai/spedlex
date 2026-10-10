"""
Ohio layer, consistency additions.

A second reading of the Ohio layer's own two documents (both in
.sources-cache/oh/ and sources/documents.tsv), made on 2026-10-10 to bring the
layer up to what the newer layers record: the state agency's acronym and older
name, the rule and statute names, other state agencies and programs the rule
names, preschool settings, and general terms defined in the rule. See
provenance/consistency-audit-2026-10-10.md.

Sources reviewed 2026-10-10 (the Ohio layer's documents):
  RULE  Operating Standards for the Education of Children with Disabilities
        (DEW booklet, June 2025, 185 pp.), cited by rule and paragraph and by
        the booklet's PDF page
  PR    A Guide to Parent Rights in Special Education (April 2025, 36 pp.),
        cited by PDF page

RULE records are 'machine_validated'; PR records are 'candidate'. Left out on
purpose: "Kindergarten age eligible", "Full-day class session" and
"Half-day class session" (3301-51-11, scheduling terms), "Math Markup
Language 3" (3301-51-01(B)(37), a file-format standard), and the funding
definitions.
"""

from .ohio import src, A, S, V, L, AB, P, OH, OHJ, PR

RP = lambda loc, page: src("RULE", f"{loc} (Operating Standards booklet, PDF p. {page})")

STRINGS = [
    ("oh_dew", [("DEW", A, OH)], PR(18)),
    ("oh_dew", [("Ohio Department of Education", L, OH)], RP("3301-51-01(B)(56)", 24)),
    ("oh_jon_peterson", [("Jon Peterson Special Needs Program", V, OH)], PR(36)),
]

CONCEPTS = [
    ("oh_operating_standards", "Operating Standards for the Education of Children with Disabilities", "legal_procedural",
     [("Ohio Operating Standards", S, OH)], PR(3), {**OHJ, "note": "Ohio Adm.Code 3301-51-01 to 3301-51-11 and 3301-51-21."}),
    ("oh_oac", "Ohio Administrative Code", "legal_procedural", [], PR(7), OHJ),
    ("oh_orc", "Ohio Revised Code", "legal_procedural", [], RP("3301-51-01", 29), OHJ),
    ("oh_odjfs", "Ohio Department of Job and Family Services", "legal_procedural", [("ODJFS", A, OH)],
     RP("3301-51-11", 172), OHJ),
    ("oh_sutq", "Step Up to Quality", "legal_procedural", [("SUTQ", A, OH)], RP("3301-51-11", 172),
     {**OHJ, "note": "Ohio's star rating system for early childhood programs."}),
    ("oh_nonchartered", "Non-chartered nonpublic school", "placement_setting", [], RP("3301-51-01(B)(41)", 17), OHJ),
    ("oh_ps_sped_class", "Public school preschool special education class", "placement_setting", [], RP("3301-51-11", 170), OHJ),
    ("oh_ps_gened_class", "Public school preschool general education class", "placement_setting", [], RP("3301-51-11", 171), OHJ),
    ("oh_ps_integrated", "Public school preschool integrated class", "placement_setting", [], RP("3301-51-11", 171), OHJ),
    ("oh_np_preschool", "Non-public school preschool program", "placement_setting", [], RP("3301-51-11", 172), OHJ),
    ("reg_ec_setting", "Regular early childhood setting", "placement_setting", [], RP("3301-51-11", 171), {}),
    ("reeval_team", "Re-evaluation team", "evaluation_eligibility", [], RP("3301-51-01(B)(24)", 15), {"broader": "iep_team"}),
    ("reader_services", "Reader services", "related_service", [], RP("3301-51-01(B)(56)", 24), {"broader": "related"}),
    ("mckinney_vento", "McKinney-Vento Homeless Assistance Act", "legal_procedural", [], RP("3301-51-01(B)(29)", 16),
     {"flags": ["eponym"], "note": "Named for Stewart B. McKinney and Bruce Vento. The surnames alone are never recorded."}),
    ("rehab_act", "Rehabilitation Act of 1973", "legal_procedural", [], RP("3301-51-01(B)(56)", 24),
     {"note": "Section 504 of the Act has its own record (s504)."}),
    ("subavg_gif", "Significantly sub average general intellectual functioning", "evaluation_eligibility", [],
     RP("3301-51-01(B)(10)", 9), {"broader": "id"}),
    ("adaptive_deficits", "Deficits in adaptive behavior", "evaluation_eligibility", [], RP("3301-51-01(B)(10)", 9),
     {"broader": "adaptive"}),
]

JURISDICTION = "US-OH"
LAYER_NAME = "Ohio (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.50.0"  # tools/add_state.py sets this
