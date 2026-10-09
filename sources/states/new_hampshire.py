"""
New Hampshire layer for SPEDLex.

Sources reviewed 2026-10-06 (all published by the New Hampshire Department
of Education):
  RULE  NH Special Education Reference Manual (Bureau of Special Education
        Support, PDF file, 257 pp., stated "accurate as of October 20, 2023").
        The manual reprints the New Hampshire Rules for the Education of
        Children with Disabilities (N.H. Code Admin. R. Ed 1100) with the
        matching RSA and 34 CFR text inserted after each rule. It is the
        Department's compiled copy, not the official text published by the
        Office of Legislative Services. Citations name the rule (Ed 11xx.xx)
        and the manual page; printed and PDF page numbers are the same.
  PSN   Special Education Procedural Safeguards Handbook (PDF file, 62 pp., updated
        December 20, 2024), cited by PDF page
  PAGE  Bureau of Special Education Support web page, read as page text

All three were read as text extracted from the files the Department
publishes. RULE: the Ed 1102 definitions, Ed 1103.01, Ed 1107.04 (Table
1100.1), Ed 1111.02-1111.04 (Tables 1100.2 and 1100.3), Ed 1113.12-1113.13
and Ed 1122.02 were read in full; the other parts were read by heading and
searched for New Hampshire terms. PSN pp. 1-4 and 33-35 were read in full
and the rest searched. RULE records are 'machine_validated'; the others
are 'candidate'.

Left out on purpose: the acronym "SAU", which the sources use without ever
spelling it out; "NHED", which the PSN uses for the Department without
defining it; the "Disabilities Right Center", whose name is printed in a
form that may not be the organization's own; and the mailing addresses and
phone numbers on PSN p. 4.
"""

RULE_URL = "https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/nh-standards-2023-print-revised-2-16-24.pdf"
PSN_URL = "https://www.education.nh.gov/sites/g/files/ehbemt326/files/inline-documents/sonh/procedural-safeguards-december-2024.corrected_1.15.24pdf_0.pdf"
PAGE_URL = "https://www.education.nh.gov/who-we-are/division-of-learner-support/bureau-special-education-support"


def src(doc, loc="", page=""):
    """RULE loc is a rule section, e.g. '1102.01(r)', with its manual page; PSN loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation",
                "citation": f"N.H. Code Admin. R. Ed {loc} (NH Special Education Reference Manual, Oct. 2023, p. {page})",
                "doc_id": "nh-refmanual-2023", "url": RULE_URL}
    if doc == "PAGE":
        return {"source_type": "state_guidance", "citation": "NHED Bureau of Special Education Support page",
                "url": PAGE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"NH Special Education Procedural Safeguards Handbook (Dec. 2024), PDF p. {loc}", "doc_id": "nh-psn-2024", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
NH = ["US-NH"]
NHJ = {"jurisdiction": "US-NH"}
R = lambda loc, page: src("RULE", loc, page)
PS = lambda page: src("PSN", page)

STRINGS = [
    # Ed 1102 definitions
    ("dd", [], R("1102.01(s)", 19)),
    ("rti", [], R("1102.04(t)", 48)),
    ("para", [], R("1102.04(g)", 44)),
    ("home_instr", [], R("1102.03(e)", 32)),
    ("state_panel", [("State advisory committee", S, NH)], R("1102.05(i)", 53)),
    ("surrogate", [], R("1102.05(m)", 55)),
    # Ed 1107.04, Table 1100.1: disabilities and qualified examiners
    ("autism", [], R("1107.04", 75)), ("deafblind", [], R("1107.04", 75)), ("deafness", [], R("1107.04", 75)),
    ("ed", [], R("1107.04", 76)), ("hi", [], R("1107.04", 76)), ("id", [], R("1107.04", 76)),
    ("oi", [], R("1107.04", 76)),
    ("ohi", [("other health impaired", V, None)], R("1107.04", 77)),
    ("sld", [], R("1107.04", 77)), ("sli", [], R("1107.04", 77)), ("tbi", [], R("1107.04", 77)),
    ("vi", [], R("1107.04", 78)),
    ("nj_sls", [], R("1107.04", 75)),
    # Ed 1111.03, Tables 1100.2 and 1100.3: educational environments
    ("ecse", [("early childhood special education program", S, None)], R("1111.03", 92)),
    ("resource_room", [], R("1111.03", 93)),
    ("special_class", [("self-contained special education class", S, None)], R("1111.03", 93)),
    ("residential", [], R("1111.03", 93)),
    # Ed 1122.02: alternative dispute resolution
    ("adr", [], R("1122.02", 173)), ("mediation", [], R("1122.02", 173)),
    # Procedural Safeguards Handbook and Bureau page
    ("safeguards_notice", [("Special Education Procedural Safeguards Handbook", S, NH)], PS(1)),
    ("iep_facil", [], PS(34)),
    ("state_panel", [("State Advisory Committee on the Education of Students/Children with Disabilities", S, NH),
                     ("SAC", A, NH)], src("PAGE")),
    ("surrogate", [("ESP", A, NH)], src("PAGE")),
]

CONCEPTS = [
    # agencies and offices
    ("nh_doe", "New Hampshire Department of Education", "legal_procedural", [], R("1102.02(b)", 24),
     {**NHJ, "broader": "sea"}),
    ("nh_bsess", "Bureau of Special Education Support", "legal_procedural", [], src("PAGE"),
     {**NHJ, "broader": "nh_doe"}),
    ("nh_olh", "Office of Legislation and Hearings", "legal_procedural", [], PS(34),
     {**NHJ, "broader": "nh_doe", "note": "The Department office named for neutral conference requests."}),
    ("nh_dcyf", "Division for Children, Youth and Families", "legal_procedural", [("DCYF", A, NH)],
     R("1102.02(g)", 25),
     {**NHJ, "note": "Its acronym DCYF is shared with Washington's Department of Children, Youth, and Families."}),
    ("nh_ose_advocate", "Office of the Special Education Advocate", "legal_procedural", [], PS(4), NHJ),
    ("nh_pic", "Parent Information Center", "legal_procedural", [("PIC", A, NH)], PS(4),
     {**NHJ, "broader": "pti"}),
    ("nhseis", "New Hampshire Special Education Information System", "legal_procedural", [("NHSEIS", A, NH)],
     R("1102.04(d)", 43), NHJ),
    # districts and schools
    ("nh_sau", "School administrative unit", "legal_procedural", [], R("1102.01(v)", 23),
     {**NHJ, "broader": "lea"}),
    ("nh_collab", "Collaborative program", "legal_procedural", [], R("1102.01(v)", 23),
     {**NHJ, "note": "A cooperative agreement between school districts or school administrative units under RSA 186-C:8."}),
    ("nh_sending", "Sending district", "legal_procedural", [], R("1102.05(c)", 49), {**NHJ, "broader": "lea"}),
    ("nh_receiving", "Receiving district", "legal_procedural", [], R("1102.04(r)", 48), {**NHJ, "broader": "lea"}),
    ("nh_chartered", "Chartered public school", "legal_procedural", [], R("1102.01(p)", 19),
     {**NHJ, "broader": "charter_school", "note": "New Hampshire's term for a charter school under RSA 194-B."}),
    ("nh_public_academy", "Public academy", "legal_procedural", [], R("1102.04(n)", 47), NHJ),
    ("nh_private_provider", "Private provider of special education", "placement_setting", [],
     R("1102.04(k)", 47), {**NHJ, "broader": "approved_priv"}),
    ("home_education", "Home education", "legal_procedural", [("homeschooling", S, None)],
     R("1102.03(c)", 28), {}),
    # eligibility and evaluation
    ("nh_abi", "Acquired brain injury", "disability_category", [("ABI", A, NH)], R("1102.01(r)", 19),
     {**NHJ, "note": "Brain injury after birth from infection, disease or lack of oxygen; listed beside traumatic brain injury."}),
    ("nh_func_blind", "Functionally blind", "disability_category", [], R("1102.02(v)", 27),
     {**NHJ, "broader": "vi"}),
    ("nh_qual_examiner", "Qualified examiner", "evaluation_eligibility", [], R("1102.04(q)", 48), {}),
    ("nh_saif", "Specialist in the assessment of intellectual functioning", "personnel_role", [("SAIF", A, NH)],
     R("1102.05(h)", 53), NHJ),
    ("school_psych", "School psychologist", "personnel_role", [], R("1107.04", 75), {}),
    ("nh_assoc_school_psych", "Associate school psychologist", "personnel_role", [], R("1107.04", 75),
     {**NHJ, "broader": "school_psych"}),
    # early childhood
    ("nh_fcess", "Family centered early supports and services", "early_intervention", [], R("1102.02(p)", 26),
     {**NHJ, "note": "New Hampshire's Part C program for children from birth through age 2."}),
    # procedures
    ("nh_admin_case_mgmt", "Administrative case management", "legal_procedural", [], R("1102.01(d)", 10),
     {**NHJ, "note": "Non-instructional tasks such as scheduling IEP meetings and coordinating evaluations."}),
    ("nh_neutral_conf", "Neutral conference", "legal_procedural", [], R("1102.04(e)", 43),
     {**NHJ, "broader": "adr"}),
    ("nh_committed_juvenile", "Committed juvenile student", "legal_procedural", [], R("1102.01(w)", 23), NHJ),
]

JURISDICTION = "US-NH"
LAYER_NAME = "New Hampshire"
RETRIEVED = "2026-10-06"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.27.0"
