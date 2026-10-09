"""
New Jersey layer for SPEDLex.

Sources reviewed 2026-10-06 (all published by the New Jersey Department of
Education, NJDOE):
  CODE   N.J.A.C. 6A:14, Special Education (NJDOE's current-code PDF,
         179 pp.), cited by section and paragraph
  PRISE  NJDOE Office of Special Education, Parental Rights in Special
         Education (PTM 1506.13, revised June 2026, 69 pp.); this is New
         Jersey's procedural safeguards statement and its main parent guide
  PAGE   NJDOE Special Education web page "Parental Rights and Engagement"

CODE and PRISE were read as text extracted from the official PDFs. PRISE
citations use PDF page numbers ("PDF p."), because the printed numbers in
the extracted text are not reliable. PAGE is a web page, read as page text.
CODE subchapters 1, 3 and 4 were read in full; subchapters 2 and 5-10 were
read by heading and searched for New Jersey terms. PRISE was read in full
for pages 1-6 and 41-47 and searched elsewhere. CODE records are
'machine_validated'; the others are 'candidate'.

Left out on purpose: the State Board members and NJDOE officials named on
PRISE pp. 1-2 (person names, listed with their counties), and the Boggs
Center (named for a person).
"""

CODE_URL = "https://www.nj.gov/education/code/current/title6a/chap14.pdf"
PRISE_URL = "https://www.nj.gov/education/specialed/parents/ParentalRightsinSpecialEducation_June26.pdf"
PAGE_URL = "https://www.nj.gov/education/specialed/parents/"


def src(doc, loc=""):
    """CODE loc is a section and paragraph, e.g. '3.5(c)5'; PRISE loc is a PDF page number."""
    if doc == "CODE":
        return {"source_type": "state_regulation", "citation": f"N.J.A.C. 6A:14-{loc}", "doc_id": "nj-njac6a14-2026", "url": CODE_URL}
    if doc == "PAGE":
        return {"source_type": "state_guidance", "citation": "NJDOE Parental Rights and Engagement page", "url": PAGE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"NJDOE Parental Rights in Special Education (rev. June 2026), PDF p. {loc}", "doc_id": "nj-prise-2026", "url": PRISE_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
NJ = ["US-NJ"]
NJJ = {"jurisdiction": "US-NJ"}
C = lambda loc: src("CODE", loc)
PR = lambda page: src("PRISE", page)

STRINGS = [
    # N.J.A.C. 6A:14-3.5(c): eligibility categories
    ("hi", [("auditory impairment", S, NJ), ("auditorily handicapped", L, NJ)], C("3.5(c)1")),
    ("deafness", [], C("3.5(c)1")),
    ("autism", [], C("3.5(c)2")),
    ("id", [], C("3.5(c)3")),
    ("sli", [("communication impairment", S, NJ)], C("3.5(c)4")),
    ("ed", [("emotional regulation impairment", S, NJ)], C("3.5(c)5")),
    ("md", [], C("3.5(c)6")),
    ("deafblind", [("deaf/blindness", V, NJ)], C("3.5(c)7")),
    ("oi", [], C("3.5(c)8")),
    ("ohi", [], C("3.5(c)9")), ("adhd", [], C("3.5(c)9")), ("tourette", [], C("3.5(c)9")),
    ("epilepsy", [], C("3.5(c)9")), ("sickle", [], C("3.5(c)9")),
    ("preschool_swd", [("preschool child with a disability", S, NJ)], C("3.5(c)10")),
    ("dd", [], C("3.5(c)10")),
    ("sld", [], C("3.5(c)12")),
    ("perceptual", [], C("3.5(c)12")), ("mbd", [], C("3.5(c)12")), ("aphasia", [], C("3.5(c)12")),
    ("discrepancy", [], C("3.5(c)12")),
    ("basic_reading", [], C("3.5(c)12")), ("reading_comp", [], C("3.5(c)12")), ("oral_expr", [], C("3.5(c)12")),
    ("listen_comp", [], C("3.5(c)12")), ("written_expr", [], C("3.5(c)12")), ("fluency", [], C("3.5(c)12")),
    ("tbi", [], C("3.5(c)13")),
    ("vi", [], C("3.5(c)14")),
    ("exclusionary", [], C("3.5(b)")),
    ("lep", [("multilingual learner", S, None)], C("3.5(b)")),
    ("eligibility", [], C("3.5(a)")),
    ("eval_report", [], C("3.5(a)")),
    # definitions, N.J.A.C. 6A:14-1.3
    ("adaptive", [], C("1.3")), ("age_majority", [], C("1.3")), ("alt_assess", [], C("1.3")),
    ("approved_priv", [("approved private school for students with disabilities", S, NJ)], C("1.3")),
    ("at_device", [], C("1.3")), ("at_service", [], C("1.3")), ("consent", [], C("1.3")),
    ("dyslexia", [], C("1.3")), ("esy", [], C("1.3")), ("iep", [], C("1.3")), ("iep_team", [], C("1.3")),
    ("native_language", [], C("1.3")), ("ward", [], C("1.3")),
    ("foster", [("resource family parent", S, NJ)], C("1.3")),
    ("transition", [], C("1.3")),
    # programs, N.J.A.C. 6A:14-4
    ("saas", [], C("4.3(a)")), ("consult", [], C("4.3(a)")),
    ("para", [("teacher aide", S, None)], C("4.3(a)")),
    ("continuum", [], C("4.3(b)")),
    ("regression", [], C("4.3(c)")),
    ("resource_room", [], C("4.6(e)")),
    ("special_class", [("special class program", S, None)], C("4.7(a)")),
    ("dedicated_aide", [("personal aide", S, None)], C("4.7(e)")),
    ("home_instr", [], C("4.8(a)")),
    ("std_diploma", [("State-endorsed diploma", S, NJ)], C("4.11(a)")),
    ("sop", [], C("4.11(b)")),
    # Parental Rights in Special Education
    ("safeguards_notice", [("Parental Rights in Special Education", S, NJ)], PR(3)),
    ("safeguards_notice", [("PRISE", A, NJ)], src("PAGE")),
    ("dp_hearing", [], PR(22)),
    ("fba", [], PR(42)), ("lre", [], PR(42)), ("stay_put", [], PR(42)),
    ("pti", [], src("PAGE")),
]

CONCEPTS = [
    # agencies and offices
    ("nj_doe", "New Jersey Department of Education", "legal_procedural", [], C("1.3"), {**NJJ, "broader": "sea"}),
    ("nj_osepdr", "Office of Special Education Policy and Dispute Resolution", "legal_procedural", [], C("1.3"),
     {**NJJ, "broader": "nj_doe"}),
    ("nj_county_office", "County office of education", "legal_procedural", [], C("4.9(a)"),
     {**NJJ, "broader": "nj_doe", "note": "Approves group-size exceptions and receives home-instruction notices."}),
    ("nj_dboe", "District board of education", "legal_procedural", [], C("1.3"),
     {**NJJ, "broader": "lea", "note": "The agency responsible for a student's evaluation, IEP and FAPE."}),
    ("nj_csssd", "County special services school district", "placement_setting", [], C("4.3(b)5"),
     {**NJJ, "broader": "continuum"}),
    ("nj_esc", "Educational services commission", "legal_procedural", [], C("4.3(b)5"), {**NJJ, "broader": "esa"}),
    ("nj_jointure", "Jointure commission", "legal_procedural", [], C("4.3(b)5"), {**NJJ, "broader": "esa"}),
    ("nj_cbvi", "New Jersey Commission for the Blind and Visually Impaired", "legal_procedural", [], C("3.5(c)14"), NJJ),
    ("nj_oal", "Office of Administrative Law", "legal_procedural", [("OAL", A, NJ)], PR(22),
     {**NJJ, "broader": "dp_hearing", "note": "Where administrative law judges hear New Jersey due process cases."}),
    ("nj_span", "Statewide Parent Advocacy Network", "legal_procedural", [("SPAN", A, NJ)], PR(3),
     {**NJJ, "broader": "pti", "flags": ["common_english_word"]}),
    ("nj_drnj", "Disability Rights New Jersey", "legal_procedural", [("DRNJ", A, NJ)], PR(3), NJJ),
    ("nj_dvrs", "Division of Vocational Rehabilitation Services", "transition", [("DVRS", A, NJ)], PR(44), NJJ),
    ("nj_ddd", "Division of Developmental Disabilities", "transition", [("DDD", A, NJ)], PR(44), NJJ),
    ("nj_csoc", "Children's System of Care", "legal_procedural", [("CSOC", A, NJ)], PR(45), NJJ),
    ("nj_ddhh", "Division of the Deaf and Hard of Hearing", "legal_procedural", [("DDHH", A, NJ)], PR(46), NJJ),
    ("nj_dds", "Division of Disability Services", "legal_procedural", [("DDS", A, NJ)], PR(46),
     {**NJJ, "note": "Its acronym DDS is shared with the District of Columbia's Department on Disability Services."}),
    ("nj_sepag", "Special Education Parent Advisory Group", "legal_procedural", [("SEPAG", A, NJ)], src("PAGE"), NJJ),
    # personnel and evaluation
    ("nj_ldtc", "Learning disabilities teacher-consultant", "personnel_role", [], C("3.1(b)"),
     {**NJJ, "broader": "mdt", "note": "Required member of a New Jersey child study team."}),
    ("nj_sls", "Speech-language specialist", "personnel_role", [], C("1.3"),
     {"broader": "slp", "note": "General concept: New Hampshire also uses the title. The key keeps its original nj_ prefix."}),
    ("referral", "Referral", "evaluation_eligibility", [], C("1.3"),
     {"flags": ["common_english_word"], "note": "The written request for an initial evaluation."}),
    # eligibility
    ("nj_social_maladj", "Social maladjustment", "disability_category", [], C("3.5(c)11"),
     {**NJJ, "note": "Defined in New Jersey's eligibility rule, distinct from emotional regulation impairment."}),
    ("nj_eligible_sls", "Eligible for speech-language services", "disability_category", [], C("3.6(a)"),
     {**NJJ, "broader": "sli"}),
    # programs
    ("nj_icr", "In-class resource program", "placement_setting", [], C("4.6(i)"), {**NJJ, "broader": "resource_room"}),
    ("nj_pullout", "Pull-out replacement resource program", "placement_setting", [], C("4.6(d)"),
     {**NJJ, "broader": "resource_room"}),
    ("nj_supp_instr", "Supplementary instruction", "placement_setting", [], C("4.6(a)"), {**NJJ, "broader": "saas"}),
    ("nj_njsls", "New Jersey Student Learning Standards", "academic_skill", [], C("4.7(a)"), NJJ),
    # dispute resolution
    ("nj_emergent", "Emergent relief", "legal_procedural", [], PR(25),
     {**NJJ, "broader": "dp_hearing", "note": "A temporary ALJ decision while a due process request is pending."}),
    # transition
    ("cbi", "Community-Based Instruction", "transition", [("CBI", A, None)], PR(43), {}),
    ("nj_sle", "Structured learning experience", "transition", [("SLE", A, NJ)], PR(43), NJJ),
]

JURISDICTION = "US-NJ"
LAYER_NAME = "New Jersey"
RETRIEVED = "2026-10-06"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.26.0"
