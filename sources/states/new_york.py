"""
New York layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN   NYSED Procedural Safeguards Notice, July 2017 (still the current edition)
  R1    8 NYCRR §200.1, definitions
  R6    8 NYCRR §200.6, continuum of services
  GRAD  NYSED, Information Related to Graduation Requirements and Exiting
        Credentials for Students with Disabilities
  SEIT  NYSED, Special Education Itinerant Teacher (SEIT) Services and Related
        Services for Preschool Students with Disabilities
  TAG   NYSED, Testing Accommodations for Students with Disabilities
        (Feb. 2018, updated Sept. 2025)

NYSED's own §200.1 page could not be fetched (robots.txt), so the Justia
copy of the regulation was used. PSN, GRAD, SEIT and TAG references come
from text extraction and are 'candidate'; 8 NYCRR records are
'machine_validated'. BOCES, the individualized education services program
(IESP), and the CSE 'parent member' are routine in New York IEPs but were
not attested by these sources.
"""

PSN_URL = "https://www.nysed.gov/sites/default/files/special-education/nysed-procedural-safeguards-notice-july-2017.pdf"
R1_URL = "https://regulations.justia.com/states/new-york/title-8/chapter-ii/subchapter-p/part-200/section-200-1/"
R6_URL = "https://regulations.justia.com/states/new-york/title-8/chapter-ii/subchapter-p/part-200/section-200-6/"
GRAD_URL = "https://www.nysed.gov/special-education/information-related-graduation-requirements-and-exiting-credentials-students"
SEIT_URL = "https://nysed.gov/special-education/special-education-itinerant-teacher-seit-services-and-related-services-preschool"
TAG_URL = "https://www.nysed.gov/sites/default/files/programs/special-education/testing-accommodations-guide.pdf"


def src(doc, loc=""):
    stype, title, url = {
        "PSN": ("procedural_safeguards_notice", "NYSED Procedural Safeguards Notice (July 2017)", PSN_URL),
        "R1": ("state_regulation", "8 NYCRR §200.1", R1_URL),
        "R6": ("state_regulation", "8 NYCRR §200.6", R6_URL),
        "GRAD": ("state_guidance", "NYSED Graduation Requirements and Exiting Credentials for Students with Disabilities", GRAD_URL),
        "SEIT": ("state_guidance", "NYSED SEIT Services and Related Services for Preschool Students with Disabilities", SEIT_URL),
        "TAG": ("state_guidance", "NYSED Testing Accommodations for Students with Disabilities (updated Sept. 2025)", TAG_URL),
    }[doc]
    if doc in ("R1", "R6"):
        return {"source_type": stype, "citation": f"{title}{loc}", "url": url}
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
NY = ["US-NY"]
NYJ = {"jurisdiction": "US-NY"}
REG = {"status": "machine_validated"}

STRINGS = [
    # 8 NYCRR §200.1 definitions and classifications
    ("iep_team", [("Committee on Special Education", S, NY), ("CSE", A, NY)], src("R1", "(k)")),
    ("cwd", [], src("R1", "(zz)")),
    ("autism", [], src("R1", "(zz)(1)")),
    ("deafness", [], src("R1", "(zz)(2)")),
    ("deafblind", [], src("R1", "(zz)(3)")),
    ("ed", [("emotional disability", S, NY)], src("R1", "(zz)(4)")),
    ("hi", [], src("R1", "(zz)(5)")),
    ("sld", [], src("R1", "(zz)(6)")),  # NY's label "learning disability" is already a national synonym
    ("id", [], src("R1", "(zz)(7)")),
    ("md", [], src("R1", "(zz)(8)")),
    ("oi", [], src("R1", "(zz)(9)")),
    ("ohi", [("other health-impairment", V, NY)], src("R1", "(zz)(10)")),
    ("sli", [], src("R1", "(zz)(11)")),
    ("tbi", [], src("R1", "(zz)(12)")),
    ("vi", [], src("R1", "(zz)(13)")),
    ("pe", [], src("R1", "(b)")),
    ("annual_review", [], src("R1", "(c)")),
    ("at_device", [], src("R1", "(e)")),
    ("at_service", [], src("R1", "(f)")),
    ("cop", [], src("R1", "(h)")),
    ("fba", [], src("R1", "(r)")),
    ("bip", [], src("R1", "(mmm)")),
    ("home_instr", [("home and hospital instruction", S, NY)], src("R1", "(w)")),
    ("dp_hearing", [("impartial hearing officer", S, None), ("IHO", A, NY), ("impartial hearing", AB, NY)], src("R1", "(x)")),
    ("iee", [], src("R1", "(z)")),
    ("evaluation", [("individual evaluation", S, NY)], src("R1", "(aa)")),
    ("lre", [], src("R1", "(cc)")),
    ("ot", [], src("R1", "(gg)")),
    ("para", [("supplementary school personnel", S, NY)], src("R1", "(hh)")),
    ("parent_training", [], src("R1", "(kk)")),
    ("pt", [], src("R1", "(ll)")),
    ("pwn", [("Notice of Recommendation", S, NY)], src("PSN", "pp. 1-2")),
    ("gen_teacher", [], src("R1", "(pp)")),
    ("related", [], src("R1", "(qq)")),
    ("resource_room", [("resource room program", S, None), ("resource room programs", P, None)], src("R1", "(rr)")),
    ("nursing", [], src("R1", "(ss)")),
    ("special_class", [("special class programs", P, NY)], src("R1", "(uu)")),
    ("sdi", [], src("R1", "(vv)")),
    ("special_ed", [], src("R1", "(ww)")),
    ("sped_teacher", [], src("R1", "(xx)")),
    ("regression", [], src("R1", "(aaa)")),
    ("saas", [], src("R1", "(bbb)")),
    ("surrogate", [], src("R1", "(ccc)")),
    ("esy", [("twelve-month special service and/or program", S, NY), ("twelve-month services", S, NY), ("12-month services", S, NY)], src("R1", "(eee)")),
    ("transition", [], src("R1", "(fff)")),
    ("travel_training", [], src("R1", "(ggg)")),
    ("homeless", [], src("R1", "(hhh)")),
    ("lep", [("limited English proficient student", V, None), ("English language learner", S, None), ("ELL", A, None), ("ELLs", P, None)], src("R1", "(iii)")),
    ("universal_design", [], src("R1", "(jjj)")),
    ("ward", [], src("R1", "(kkk)")),
    ("interpreting", [], src("R1", "(nnn)")),
    ("continuum", [], src("R6")),
    # Procedural safeguards notice
    ("stay_put", [], src("PSN", "p. 20")),
    ("state_complaint", [], src("PSN", "pp. 13-15")),
    ("resolution", [], src("PSN", "pp. 20-22")),
    ("mediation", [], src("PSN", "pp. 18-19")),
    ("mdr", [], src("PSN", "pp. 32-33")),
    ("iaes", [], src("PSN", "pp. 30-34")),
    ("exp_hearing", [], src("PSN", "p. 35")),
    ("basis_know", [], src("PSN", "pp. 35-36")),
    ("sro", [("Office of State Review", S, NY), ("SRO", A, NY)], src("PSN", "pp. 25-26")),
    # Testing accommodations guide
    ("alt_assess", [], src("TAG")),
    ("test_accom", [("testing accommodations", S, None)], src("TAG")),
    ("ext_time", [], src("TAG", "scheduling/timing")),
    ("tts", [("text-to-speech software", S, None)], src("TAG", "method of presentation")),
    ("stt", [("speech-to-text software", S, None)], src("TAG", "method of response")),
    ("word_pred", [("word-prediction software", S, None)], src("TAG", "method of response")),
    ("large_print", [("large type", S, None)], src("TAG", "method of presentation")),
    ("oral_admin", [("tests read", S, NY), ("tests read aloud", S, None)], src("TAG", "method of presentation")),
    ("calc_aids", [], src("TAG", "other accommodations")),
    ("spell_check", [("spell-checking device", S, None)], src("TAG", "method of response")),
    ("s504", [("Section 504 Accommodation Plan", S, None)], src("TAG")),
]

CONCEPTS = [
    # --- Agencies, committees, hearings ---
    ("nysed", "New York State Education Department", "legal_procedural", [("NYSED", A, NY), ("SED", A, NY)], src("PSN", "p. 1"), {**NYJ, "broader": "sea"}),
    ("nysed_ose", "Office of Special Education", "legal_procedural", [], src("PSN", "p. 1"), {**NYJ, "broader": "nysed"}),
    ("cpse", "Committee on Preschool Special Education", "personnel_role", [("CPSE", A, NY)], src("R1", "(j)"),
     {**NYJ, **REG, "note": "New York's preschool counterpart to the CSE, under Education Law §4410."}),
    ("cdrc", "Community Dispute Resolution Center", "legal_procedural", [("CDRC", A, NY)], src("PSN", "p. 19"),
     {**NYJ, "broader": "mediation", "note": "New York mediations are run through these centers."}),
    ("sro_form_a", "Notice of Intention to Seek Review", "legal_procedural", [("Form A", AB, NY)], src("PSN", "p. 26"), {**NYJ, "broader": "sro"}),
    ("sro_form_b", "Notice of Request for Review", "legal_procedural", [("Form B", AB, NY)], src("PSN", "p. 26"), {**NYJ, "broader": "sro"}),
    ("gal", "Guardian ad litem", "legal_procedural", [], src("R1", "(s)"), REG),

    # --- Continuum (8 NYCRR §200.6) ---
    ("consult_teacher", "Consultant teacher services", "placement_setting", [("consultant teacher", AB, NY), ("CT services", S, NY)], src("R1", "(m)"),
     {**REG, "broader": "continuum", "note": "'CT services' is practitioner usage."}),
    ("ict", "Integrated co-teaching services", "placement_setting", [("integrated co-teaching", AB, NY), ("ICT", A, NY)], src("R6"),
     {**NYJ, **REG, "broader": "coteach", "note": "'ICT' is practitioner usage, not from the regulation."}),
    ("sc_15_1", "15:1 special class", "placement_setting", [("15:1", A, NY)], src("R6"), {**NYJ, **REG, "broader": "special_class"}),
    ("sc_12_1", "12:1 special class", "placement_setting", [("12:1", A, NY)], src("R6"), {**NYJ, **REG, "broader": "special_class"}),
    ("sc_12_1_1", "12:1+1 special class", "placement_setting", [("12:1+1", A, NY)], src("R6"), {**NYJ, **REG, "broader": "special_class"}),
    ("sc_8_1_1", "8:1+1 special class", "placement_setting", [("8:1+1", A, NY)], src("R6"), {**NYJ, **REG, "broader": "special_class"}),
    ("sc_6_1_1", "6:1+1 special class", "placement_setting", [("6:1+1", A, NY)], src("R6"), {**NYJ, **REG, "broader": "special_class",
     "note": "Ratios read as students : teacher + paraprofessional. They are protected only as exact strings so they never shelter a date or score."}),
    ("approved_priv", "Approved private school", "placement_setting", [("approved private schools", P, None)], src("R1", "(d)"), REG),
    ("change_prog", "Change in program", "iep_component", [], src("R1", "(g)"), {**NYJ, **REG}),
    ("tss", "Transitional support services", "related_service", [], src("R1", "(ddd)"), {**NYJ, **REG}),
    ("dss", "Declassification support services", "related_service", [("declassification", AB, NY), ("declassified", AB, NY)], src("R1", "(ooo)"),
     {**NYJ, **REG, "note": "Services for a student moving out of special education."}),

    # --- Preschool ---
    ("preschool_swd", "Preschool student with a disability", "early_intervention", [("preschool students with disabilities", P, NY)], src("R1", "(mm)"), {**REG, "broader": "cwd"}),
    ("seit", "Special education itinerant teacher services", "early_intervention", [("SEIT", A, NY), ("special education itinerant services", S, NY),
                                                                                     ("special education itinerant teacher", S, NY)], src("SEIT"), NYJ),
    ("approved_presch", "Approved preschool program", "early_intervention", [("Section 4410", AB, NY), ("4410 program", S, NY)], src("SEIT"),
     {**NYJ, "note": "'4410 program' is practitioner shorthand for programs approved under Education Law §4410."}),
    ("fullday_presch", "Full-day preschool program", "early_intervention", [("half-day preschool program", S, NY)], src("R1", "(p), (u)"), {**NYJ, **REG}),

    # --- Evaluation and discipline ---
    ("ind_psych", "Individual psychological evaluation", "evaluation_eligibility", [("psychological evaluation", AB, None)], src("R1", "(bb)"), REG),
    ("social_hist", "Social history", "evaluation_eligibility", [], src("R1", "(tt)"), REG),
    ("approved_eval", "Approved evaluator", "evaluation_eligibility", [], src("R1", "(ppp)"), {**NYJ, **REG}),
    ("aversive", "Aversive intervention", "discipline", [("aversive interventions", P, None)], src("R1", "(lll)"), REG),

    # --- Assessment, diplomas, credentials ---
    ("nysaa", "New York State Alternate Assessment", "iep_component", [("NYSAA", A, NY)], src("GRAD"), {**NYJ, "broader": "alt_assess"}),
    ("regents_exam", "Regents examinations", "iep_component", [("Regents exams", S, NY), ("Regents exam", P, NY)], src("GRAD"), NYJ),
    ("regents_dip", "Regents diploma", "transition", [("Regents diploma with advanced designation", S, NY)], src("GRAD"), NYJ),
    ("local_dip", "Local diploma", "transition", [], src("GRAD"), NYJ),
    ("safety_net", "Safety net", "transition", [("Low Pass Safety Net", S, NY), ("Compensatory Safety Net", S, NY), ("Low Pass Safety Net with Appeal", S, NY)], src("GRAD"),
     {**NYJ, "note": "Lower passing options on Regents exams for students with disabilities."}),
    ("supt_det", "Superintendent determination", "transition", [], src("GRAD"), {**NYJ, "broader": "local_dip"}),
    ("cdos", "Career Development and Occupational Studies Commencement Credential", "transition", [("CDOS Commencement Credential", AB, NY), ("CDOS", A, NY)], src("GRAD"), NYJ),
    ("sacc", "Skills and Achievement Commencement Credential", "transition", [], src("GRAD"),
     {**NYJ, "note": "For students who take the New York State Alternate Assessment; compare California's certificate of completion."}),
    ("cbt", "Computer-based testing", "iep_component", [("CBT", A, None)], src("TAG"), {}),

    # --- Testing accommodations (TAG) ---
    ("separate_loc", "Separate location", "accommodation_modification", [("separate setting", S, None), ("separate location/setting", V, NY)], src("TAG", "location/setting"), {"broader": "test_accom"}),
    ("small_group", "Small group administration", "accommodation_modification", [("small group", AB, None)], src("TAG", "location/setting"), {"broader": "test_accom"}),
    ("indiv_admin", "Individual administration", "accommodation_modification", [("individual test administration", S, None)], src("TAG", "location/setting"), {"broader": "test_accom"}),
    ("revised_fmt", "Revised test format", "accommodation_modification", [], src("TAG", "method of presentation"), {"broader": "test_accom"}),
    ("graphic_org", "Graphic organizer", "accommodation_modification", [("graphic organizers", P, None)], src("TAG", "method of presentation"), {"broader": "test_accom"}),
    ("scribe_use", "Use of a scribe", "accommodation_modification", [], src("TAG", "method of response"), {"broader": "test_accom"}),
    ("word_proc", "Use of a word processor", "accommodation_modification", [], src("TAG", "method of response"), {"broader": "test_accom"}),
    ("ans_any", "Answers recorded in any manner", "accommodation_modification", [("record answers in any manner", V, NY)], src("TAG", "method of response"), {**NYJ, "broader": "test_accom"}),
    ("formula_sheet", "Mathematical formula sheet", "accommodation_modification", [("formula sheet", AB, None)], src("TAG", "other accommodations"), {"broader": "test_accom"}),
    ("biling_gloss", "Bilingual glossary", "accommodation_modification", [("bilingual glossaries", P, None)], src("TAG", "other accommodations"), {"broader": "test_accom"}),
]

JURISDICTION = "US-NY"
LAYER_NAME = "New York"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.7.0"
