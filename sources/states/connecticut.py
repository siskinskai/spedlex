"""
Connecticut layer for SPEDLex.

Sources reviewed 2026-10-06 (all published by the Connecticut State
Department of Education, CSDE):
  REG    Regulations of Connecticut State Agencies, Children Requiring Special
         Education, Sections 10-76a-1 through 10-76l-1 (CSDE's PDF copy of the
         regulations, revised 2015-11-21, 44 pp.), cited by section and
         subdivision
  GUIDE  A Parent's Guide to Special Education in Connecticut (PDF file,
         2021, 60 pp.), cited by PDF page because the printed page numbers
         are four lower
  PSN    Procedural Safeguards Notice Required Under IDEA Part B (PDF file,
         revised March 31, 2021, 45 pp.), cited by PDF page

All three were read as text extracted from the files on the CSDE "Special
Education Legal and Due Process" web page. REG sections 10-76a-1, 10-76a-2,
10-76d-1, 10-76d-2, 10-76d-6, 10-76d-7, 10-76d-10, 10-76d-14 to 10-76d-17,
10-76h-1 and 10-76h-6 were read in full; the other sections were read by
heading. GUIDE pp. 5-11, 24, 27, 32, 35 and 50-51 were read in full and
the rest searched; PSN pp. 1-4 and 17 were read and the rest searched. REG
records are 'machine_validated'; the others are 'candidate'.

Left out on purpose: the Bureau of Special Education and its acronym BSE
(the list already has a Pennsylvania-only concept with that exact name; see
the contributor report); the six named RESCs on GUIDE p. 27; the
Department of Public Health (a common agency name); and every mailing
address, phone number and staff name in the sources.
"""

REG_URL = ("https://portal.ct.gov/-/media/sde/special-education/"
           "regulations-of-connecticut-state-agencies-department-of-education-children-requiring-special-educati.pdf")
GUIDE_URL = "https://portal.ct.gov/-/media/sde/special-education/parents_guide_se.pdf"
PSN_URL = "https://portal.ct.gov/-/media/sde/special-education/prosaf.pdf"


def src(doc, loc=""):
    """REG loc is a section and subdivision, e.g. '10-76a-1(14)'; GUIDE and PSN loc is a PDF page number."""
    if doc == "REG":
        return {"source_type": "state_regulation", "citation": f"Conn. Agencies Regs. § {loc}", "doc_id": "ct-rcsa1076-2015", "url": REG_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"CSDE A Parent's Guide to Special Education in Connecticut (2021), PDF p. {loc}",
                "doc_id": "ct-parentsguide-2021", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"CSDE Procedural Safeguards Notice (rev. Mar. 2021), PDF p. {loc}", "doc_id": "ct-psn-2021", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
CT = ["US-CT"]
CTJ = {"jurisdiction": "US-CT"}
R = lambda loc: src("REG", loc)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # Conn. Agencies Regs. § 10-76a-1, general definitions
    ("iep_team", [("Planning and placement team", S, CT), ("PPT", A, CT)], R("10-76a-1(14)")),
    ("esy", [], R("10-76a-1(7)")),
    ("iee", [], R("10-76a-1(8)")),
    ("iep", [], R("10-76a-1(10)")),
    ("lre", [], R("10-76a-1(12)")),
    ("gifted", [], R("10-76a-2(2)")),
    ("referral", [], R("10-76d-7")),
    ("home_instr", [("homebound and hospitalized instruction", S, CT)], R("10-76d-15")),
    # Parent's Guide p. 11: eligibility categories
    ("autism", [], G(11)), ("deafblind", [], G(11)), ("dd", [], G(11)), ("ed", [], G(11)),
    ("hi", [], G(11)), ("id", [], G(11)), ("md", [], G(11)), ("oi", [], G(11)),
    ("ohi", [], G(11)), ("adhd", [("OHI/ADD/ADHD", S, CT)], G(11)),
    ("sld", [], G(11)), ("dyslexia", [("Specific Learning Disability/Dyslexia", S, CT)], G(11)),
    ("sli", [], G(11)), ("tbi", [], G(11)),
    ("vi", [("Vision Impairment", S, CT)], G(11)),
    # Parent's Guide, other pages
    ("pbis", [], G(8)), ("pwn", [], G(8)), ("mdr", [], G(8)),
    ("srbi", [("Scientific Research-Based Intervention", V, CT), ("SRBI", A, CT)], G(9)),
    ("approved_priv", [("approved private special education program", S, CT)], G(27)),
    ("surrogate", [], G(35)),
    ("safeguards_notice", [], src("PSN", 2)),
]

CONCEPTS = [
    # agencies and offices
    ("ct_csde", "Connecticut State Department of Education", "legal_procedural", [("CSDE", A, CT)], src("PSN", 17),
     {**CTJ, "broader": "sea"}),
    ("ct_due_process_unit", "Due process unit", "legal_procedural", [], R("10-76h-1(f)"),
     {**CTJ, "broader": "ct_csde",
      "note": "The Bureau of Special Education unit that manages mediation, advisory opinions and hearings."}),
    ("ct_resc", "Regional Educational Service Center", "legal_procedural", [("RESC", A, CT)], G(9),
     {**CTJ, "broader": "esa"}),
    ("ct_serc", "State Education Resource Center", "legal_procedural", [("SERC", A, CT)], G(50), CTJ),
    ("ct_cpac", "Connecticut Parent Advocacy Center", "legal_procedural", [("CPAC", A, CT)], G(50),
     {**CTJ, "broader": "pti"}),
    ("ct_oec", "Office of Early Childhood", "early_intervention", [("OEC", A, CT)], G(51), CTJ),
    ("ct_b23", "Birth to Three System", "early_intervention", [("Connecticut Birth to Three System", S, CT)], G(7),
     {**CTJ, "broader": "ct_oec", "note": "Connecticut's Part C early intervention system."}),
    ("ct_ads", "Department of Aging and Disability Services", "transition", [("ADS", A, CT)], G(51), CTJ),
    ("ct_besb", "Bureau of Education and Services for the Blind", "transition", [("BESB", A, CT)], G(32),
     {**CTJ, "broader": "ct_ads"}),
    ("ct_brs", "Bureau of Rehabilitation Services", "transition", [("BRS", A, CT)], G(32),
     {**CTJ, "broader": "ct_ads"}),
    ("ct_dds", "Department of Developmental Services", "transition", [("DDS", A, CT)], G(32),
     {**CTJ, "note": "Its acronym DDS is shared with agencies in the District of Columbia and New Jersey."}),
    ("ct_dmhas", "Department of Mental Health and Addiction Services", "legal_procedural", [("DMHAS", A, CT)], G(32),
     CTJ),
    ("ct_dcf", "Department of Children and Families", "legal_procedural", [("DCF", A, CT)], G(35), CTJ),
    # boards and programs (Conn. Agencies Regs. § 10-76a-1)
    ("ct_boe", "Board of education", "legal_procedural", [], R("10-76a-1(1)"),
     {**CTJ, "broader": "lea", "note": "Any public body responsible for educating children, including local and regional boards."}),
    ("ct_unified", "Unified school district", "legal_procedural", [], R("10-76a-1(1)"),
     {**CTJ, "broader": "ct_boe"}),
    ("ct_tech_hs", "Technical high school system", "legal_procedural", [], R("10-76a-1(1)"),
     {**CTJ, "broader": "ct_boe"}),
    ("ct_private_sped", "Private special education program", "placement_setting", [], R("10-76a-1(15)"), CTJ),
    # eligibility
    ("ct_child_req_sped", "Child requiring special education", "evaluation_eligibility", [], R("10-76a-1(3)"),
     {**CTJ, "note": "Covers both a child with a disability and a gifted or talented child."}),
    ("ct_ela", "Extraordinary learning ability", "evaluation_eligibility", [], R("10-76a-2(1)"),
     {**CTJ, "broader": "gifted"}),
    ("ct_otca", "Outstanding talent in the creative arts", "evaluation_eligibility", [], R("10-76a-2(3)"),
     {**CTJ, "broader": "gifted"}),
    ("ct_trial_placement", "Trial placement for diagnostic purposes", "evaluation_eligibility", [], R("10-76d-14"),
     {**CTJ, "note": "A structured program of up to forty school days used to finish an inconclusive evaluation."}),
    ("ct_medically_complex", "Medically complex", "health_condition", [], R("10-76d-15"), CTJ),
    # assessment and standards
    ("ct_ctaa", "Connecticut Alternate Assessment", "iep_component", [("CTAA", A, CT)], G(6),
     {**CTJ, "broader": "alt_assess"}),
    ("ct_ctas", "Connecticut Alternate Science", "iep_component", [("CTAS", A, CT)], G(6),
     {**CTJ, "broader": "alt_assess"}),
    ("ct_ccs", "Connecticut Core Standards", "academic_skill", [("CCS", A, CT)], G(6), CTJ),
    ("aba", "Applied behavior analysis", "iep_component", [("ABA", A, None)], G(6), {}),
    # dispute resolution
    ("ct_advisory_opinion", "Advisory opinion", "legal_procedural", [], R("10-76h-6"),
     {**CTJ, "broader": "dp_hearing", "note": "An optional process the Department may offer the parties after a hearing request and before the hearing convenes."}),
]

JURISDICTION = "US-CT"
LAYER_NAME = "Connecticut"
RETRIEVED = "2026-10-06"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.28.0"
