"""
Indiana layer for SPEDLex.

Sources reviewed 2026-10-07 (all published by the Indiana Department of
Education, IDOE):
  RULE  Special Education Rules, Title 511 Article 7 (511 IAC 7-32 to 7-49),
        IDOE's English compilation dated May 2024 (PDF file, 167 pp.), cited
        by rule section, e.g. "511 IAC 7-41-2"
  PSN   IDOE Notice of Procedural Safeguards (August 2025, PDF file, 25 pp.),
        cited by PDF page
  NAV   Navigating the Course: Finding Your Way through Indiana's Special
        Education Rules (IDOE Dispute Resolution Team, August 2025, PDF file,
        63 pp.), IDOE's parent guide, cited by PDF page

All three were downloaded from IDOE's Special Education page and read as
text extracted from the PDFs. NAV was searched for Indiana terms, and its
acronym index (p. 7) was read in full; that index is printed in two
columns, so each acronym was matched to its expansion by hand. RULE 511 IAC 7-32
(definitions) and 7-41 (eligibility categories) were read in full; the
other rules were read by section heading and searched. PSN pp. 1-3, 19 and
25 were read in full and the rest searched; it follows the federal model
notice. RULE records are 'machine_validated'; the others are 'candidate'.

Left out on purpose: the Joseph Maley Foundation (named for a person) and
every address and phone number on PSN p. 25; the degree labels in 511 IAC
7-41-3 (mild, moderate and severe intellectual disability), which are
eligibility criteria rather than separate terms; and "Office of Special
Education", which the list already holds as a New York concept.
"""

RULE_URL = "https://www.in.gov/doe/files/Special-Education-Rules-Title-511-Article-7-May-2024.pdf"
PSN_URL = "https://www.in.gov/doe/files/Notice-of-Procedural-Safeguards-English-August-2025.pdf"
NAV_URL = "https://www.in.gov/doe/files/Navigating-the-Course-August-2025.pdf"


def src(doc, loc=""):
    """RULE loc is a rule section, e.g. '7-41-2'; PSN and NAV loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"511 IAC {loc}", "doc_id": "in-511iac7-2024", "url": RULE_URL}
    if doc == "NAV":
        return {"source_type": "state_guidance",
                "citation": f"IDOE Navigating the Course (Aug. 2025), PDF p. {loc}", "doc_id": "in-navigating-2025", "url": NAV_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"IDOE Notice of Procedural Safeguards (Aug. 2025), PDF p. {loc}", "doc_id": "in-nops-2025", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
IN = ["US-IN"]
INJ = {"jurisdiction": "US-IN"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
NV = lambda page: src("NAV", page)

STRINGS = [
    # 511 IAC 7-41: eligibility categories
    ("autism", [], R("7-41-1")),
    ("vi", [("blind or low vision", S, IN)], R("7-41-2")),
    ("id", [], R("7-41-3")),
    ("hi", [], R("7-41-4")), ("deafness", [], R("7-41-4")),
    ("deafblind", [("dual sensory impaired", S, IN)], R("7-41-5")),
    ("dd", [], R("7-41-6")),
    ("ed", [("emotional disability", S, IN)], R("7-41-7")),
    ("sli", [("language or speech impairment", S, IN)], R("7-41-8")),
    ("md", [], R("7-41-9")),
    ("ohi", [], R("7-41-10")),
    ("oi", [], R("7-41-11")),
    ("sld", [], R("7-41-12")),
    ("tbi", [], R("7-41-13")),
    # 511 IAC 7-32: definitions
    ("adaptive", [], R("7-32-3")), ("adverse", [], R("7-32-5")),
    ("at_device", [], R("7-32-7")), ("at_service", [], R("7-32-8")),
    ("bip", [], R("7-32-10")), ("sto", [], R("7-32-11")),
    ("iep_team", [("case conference committee", S, IN), ("CCC", A, IN)], R("7-32-12")),
    ("cop", [], R("7-32-14")),
    ("consent", [], R("7-32-17")),
    ("consult", [("consultation", S, IN)], R("7-32-18")),
    ("controlled", [], R("7-32-20")),
    ("dp_hearing", [], R("7-32-27")),
    ("evaluation", [("educational evaluation", S, IN)], R("7-32-30")),
    ("ed_records", [], R("7-32-31")),
    ("surrogate", [("educational surrogate parent", S, IN)], R("7-32-32")),
    ("exp_hearing", [], R("7-32-37")),
    ("esy", [], R("7-32-39")), ("fape", [], R("7-32-40")), ("fba", [], R("7-32-41")),
    ("func_perf", [], R("7-32-42")),
    ("homeless", [], R("7-32-46")), ("illegal_drug", [], R("7-32-47")),
    ("ifsp", [], R("7-32-49")), ("itd", [], R("7-32-50")),
    ("lep", [], R("7-32-59")), ("lea", [], R("7-32-60")),
    ("mdr", [], R("7-32-61")), ("mediation", [], R("7-32-62")), ("medical", [], R("7-32-63")),
    ("mdt", [], R("7-32-65")),
    ("native_language", [], R("7-32-66")), ("om", [], R("7-32-68")),
    ("ppps", [("parentally-placed nonpublic school students with disabilities", S, IN)], R("7-32-71")),
    ("home_instr", [], R("7-32-45")), ("iaes", [], R("7-32-53")),
    ("travel_training", [], R("7-32-101")), ("cert_completion", [], R("7-43-4")),
    ("pti", [], R("7-32-72")), ("pe", [], R("7-32-74")), ("progress", [], R("7-32-76")),
    ("public_agency", [], R("7-32-77")),
    ("resolution", [], R("7-32-80")), ("sbi", [], R("7-32-83")),
    ("services_plan", [("service plan", S, None)], R("7-32-84")),
    ("special_ed", [], R("7-32-86")), ("sdi", [], R("7-32-88")),
    ("sig_cog", [], R("7-32-93.5")), ("sop", [], R("7-32-94")),
    ("saas", [], R("7-32-95")),
    ("part_c_transition", [("transition planning", REL, IN)], R("7-32-99")),
    ("transition", [], R("7-32-100")),
    ("universal_design", [], R("7-32-102")),
    ("voc_ed", [], R("7-32-104")), ("ward", [], R("7-32-105")), ("weapon", [], R("7-32-106")),
    # other rules
    ("alt_assess", [], R("7-36-10")),
    ("ecse", [], R("7-43-2")),
    ("age_majority", [], R("7-43-5")),
    ("alt_diploma", [("alternate diploma", S, IN)], R("7-43-4")),
    ("dc_educ_rep", [], R("7-43-6")),
    ("dp_hearing", [("independent hearing officer", S, IN)], R("7-45-8")),
    ("excess_costs", [], R("7-47-1")),
    # Notice of Procedural Safeguards
    ("safeguards_notice", [], PS(1)),
    ("sea", [], PS(2)),
    # Navigating the Course, acronym index (p. 7) and text
    ("vi", [("BLV", A, IN)], NV(7)),
    ("mdt", [("M-Team", AB, IN)], NV(7)),
    ("safeguards_notice", [("NOPS", A, IN)], NV(7)),
    ("id", [("cognitive disability", L, IN)], NV(7)),
    ("lea_rep", [("public agency representative", S, IN)], NV(7)),
]

CONCEPTS = [
    # agencies and offices
    ("in_doe", "Indiana Department of Education", "legal_procedural", [("IDOE", A, IN)], PS(1),
     {**INJ, "broader": "sea"}),
    ("in_dse", "Division of special education", "legal_procedural", [], R("7-33-1"),
     {**INJ, "broader": "in_doe", "note": "The part of the Department named by the rule as the state educational agency for special education."}),
    ("in_oalp", "Office of Administrative Law Proceedings", "legal_procedural", [("OALP", A, IN)], PS(19),
     {**INJ, "broader": "dp_hearing", "note": "Receives due process hearing requests for the secretary of education."}),
    ("in_insource", "IN*SOURCE", "legal_procedural", [], PS(25), {**INJ, "broader": "pti"}),
    ("in_idr", "Indiana Disability Rights", "legal_procedural", [], PS(25), INJ),
    ("in_isbvi", "Indiana School for the Blind and Visually Impaired", "placement_setting", [], R("7-32-77"),
     {**INJ, "broader": "state_sp_sch"}),
    ("in_isd", "Indiana School for the Deaf", "placement_setting", [], R("7-32-77"), {**INJ, "broader": "state_sp_sch"}),
    # districts and legal terms
    ("in_school_corp", "School corporation", "legal_procedural", [], R("7-32-77"),
     {**INJ, "broader": "lea", "note": "Indiana's legal term for a public school district."}),
    ("in_scols", "School corporation of legal settlement", "legal_procedural", [("SCOLS", A, IN)], NV(7),
     {**INJ, "broader": "in_school_corp", "note": "The school corporation responsible for a student under Indiana's legal settlement rules."}),
    ("in_legal_settlement", "Legal settlement", "legal_procedural", [], R("7-32-56"),
     {**INJ, "note": "Which school corporation must let a student attend without tuition or pay for the student's schooling."}),
    ("in_sepd", "Special education planning district", "legal_procedural", [], R("7-32-87"),
     {**INJ, "broader": "lea", "note": "One school corporation, or several under a written agreement, responsible for special education in an area."}),
    ("in_article7", "Article 7", "legal_procedural", [], PS(1),
     {**INJ, "note": "Indiana's special education rules, 511 IAC 7-32 through 7-50."}),
    ("in_student_legal_age", "Student of legal age", "transition", [], R("7-32-91"),
     {**INJ, "broader": "age_majority", "note": "A student 18 or older who has no court-appointed guardian."}),
    # IEP and services
    ("in_transition_iep", "Transition IEP", "iep_component", [], R("7-32-48"),
     {"broader": "iep", "note": "The IEP for a student who will turn 14 or enter grade 9 while it is in effect."}),
    ("in_teacher_record", "Teacher of record", "personnel_role", [("TOR", A, IN)], NV(7),
     {**INJ, "broader": "sped_teacher", "note": "The one special education teacher each student with a disability is assigned to."}),
    ("in_teacher_service", "Teacher of service", "personnel_role", [("TOS", A, IN)], NV(7), INJ),
    ("in_consult_collab", "Consultation and collaboration", "related_service", [], R("7-32-19"),
     {**INJ, "broader": "equitable", "note": "Services for eligible students placed by their parents in nonpublic schools."}),
    ("job_coach", "Job coach", "personnel_role", [], R("7-32-55"),
     {"broader": "transition", "note": "Supports a student in supported employment, on the job."}),
    ("systematic_obs", "Systematic observation", "evaluation_eligibility", [], R("7-32-96"),
     {"broader": "observation"}),
    # early childhood and assessment
    ("in_first_steps", "First Steps", "early_intervention", [], NV(30),
     {**INJ, "flags": ["common_english_word"], "note": "Indiana's early intervention (Part C) program."}),
    ("in_istar", "Indiana Standards Tool for Alternative Reporting", "instrument", [("ISTAR", A, IN)], NV(7), INJ),
    # choice scholarships
    ("in_choice_scholarship", "Choice scholarship", "legal_procedural", [], R("7-49-2"), INJ),
    ("in_csep", "Choice special education plan", "iep_component", [("CSEP", A, IN)], R("7-49-2"),
     {**INJ, "broader": "services_plan", "note": "The plan a choice school writes for a choice scholarship student with a disability."}),
]

JURISDICTION = "US-IN"
LAYER_NAME = "Indiana"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.32.0"
