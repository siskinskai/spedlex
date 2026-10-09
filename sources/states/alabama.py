"""
Alabama layer for SPEDLex.

Sources reviewed 2026-10-08 (all published by the Alabama State Department of
Education, ALSDE):
  RULE   Ala. Admin. Code ch. 290-8-9, Special Education Services (Supp. No.
         13-3, effective Nov. 4, 2013; ALSDE copy, 94 pp.), cited by rule and
         paragraph, e.g. "Ala. Admin. Code r. 290-8-9-.03(4)"
  PSN    Alabama's Procedural Safeguards (Special Education Rights), English
         v1.0 (ALSDE approved January 2025, 29 pp.), cited by PDF page
  MAZE   Mastering the Maze, The Special Education Process, Process 1:
         Referral Through IEP Implementation (August 2019 edition, 190 pp.),
         cited by PDF page (printed page number + 3)

All three were read as text extracted with pdftotext. RULE and PSN were read
in full. MAZE was read in full except pp. 26-38, a reprint of an older
federal-model rights notice, which was skimmed. The contributor saved two
copies of RULE; their text is identical apart from line breaks in the table
of contents. ALSDE still calls the 2013 chapter current; later amendments,
if any, were not checked. RULE records are 'machine_validated'; the others
are 'candidate'.

Left out on purpose: every person named in the documents (State Board
members, superintendents, rule authors); the county board credited on MAZE
pp. 139-141; addresses, phone numbers and email addresses; test products
named in the MAZE questions (screeners, achievement and creativity tests);
general education initiatives in the MAZE acronym list (reading, math and
science initiatives); "SES", which ALSDE uses for its Special Education
Services section but which usually means socioeconomic status; and "DB",
"EL" and "PBS", two- and three-letter acronyms with common other meanings.
"""

RULE_URL = "https://www.alabamaachieves.org/wp-content/uploads/2021/04/SE-AAC-290-8-9-11-4-2013.pdf"
PSN_URL = "https://www.alabamaachieves.org/wp-content/uploads/2025/02/SPECED_PP_20250212_Alabamas-Procedural-Safeguards-Special-Education-Rights-English_v1.0.pdf"
MAZE_URL = "https://www.alabamaachieves.org/wp-content/uploads/2021/04/2019-Mastering-the-Maze-Process-1.pdf"


def src(doc, loc=""):
    """RULE loc is a rule and paragraph, e.g. '.03(4)'; PSN and MAZE loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"Ala. Admin. Code r. 290-8-9-{loc}", "doc_id": "al-aac290-2013", "url": RULE_URL}
    if doc == "MAZE":
        return {"source_type": "state_guidance",
                "citation": f"ALSDE Mastering the Maze, Process 1: Referral Through IEP Implementation (Aug. 2019), PDF p. {loc}",
                "doc_id": "al-maze1-2019", "url": MAZE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"ALSDE Alabama's Procedural Safeguards (Special Education Rights) (Jan. 2025), PDF p. {loc}",
            "doc_id": "al-psn-2025", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
AL = ["US-AL"]
ALJ = {"jurisdiction": "US-AL"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("MAZE", page)

STRINGS = [
    # 290-8-9-.00 definitions
    ("consent", [], R(".00(1)")), ("school_day", [], R(".00(3)")), ("adverse", [], R(".00(4)")),
    ("evaluation", [], R(".00(6)")), ("fape", [], R(".00(7)")), ("homeless", [], R(".00(8)")),
    ("idea", [], R(".00(9)")), ("iep", [], R(".00(10)")), ("ifsp", [], R(".00(11)")), ("lea", [], R(".00(12)")),
    ("esa", [], R(".00(12)")), ("native_language", [], R(".00(13)")), ("foster", [], R(".00(14)")),
    ("part_agency", [], R(".00(15)")), ("pii", [], R(".00(16)")), ("public_agency", [], R(".00(17)")),
    ("related", [], R(".00(18)")), ("implant", [], R(".00(18)(b)")),
    ("audiology", [], R(".00(18)(c)")), ("counseling", [], R(".00(18)(c)")), ("early_id", [], R(".00(18)(c)")),
    ("interpreting", [], R(".00(18)(c)")), ("cart", [], R(".00(18)(c)")), ("medical", [], R(".00(18)(c)")),
    ("ot", [], R(".00(18)(c)")), ("om", [], R(".00(18)(c)")), ("parent_training", [], R(".00(18)(c)")),
    ("pt", [], R(".00(18)(c)")), ("psych", [], R(".00(18)(c)")), ("recreation", [], R(".00(18)(c)")),
    ("rehab", [], R(".00(18)(c)")), ("nursing", [], R(".00(18)(c)")), ("social_work", [], R(".00(18)(c)")),
    ("slp", [], R(".00(18)(c)")), ("transport", [], R(".00(18)(c)")),
    ("services_plan", [], R(".00(20)")), ("special_ed", [], R(".00(21)")), ("pe", [], R(".00(21)(b)")),
    ("sdi", [], R(".00(21)(b)")), ("travel_training", [], R(".00(21)(b)")), ("voc_ed", [], R(".00(21)(b)")),
    ("sea", [], R(".00(22)")), ("saas", [], R(".00(23)")), ("transition", [], R(".00(24)")), ("ward", [], R(".00(25)")),
    # .01 child identification
    ("child_find", [], R(".01(1)")), ("part_c_transition", [], R(".01(1)")), ("data_doc", [], R(".01(2)")),
    ("sst", [], R(".01(4)")), ("screening", [], R(".01(5)")), ("referral", [], R(".01(6)")),
    # .02 evaluations
    ("iee", [], R(".02(4)")), ("reeval", [], R(".02(6)")), ("sop", [], R(".02(6)")), ("std_diploma", [], R(".02(6)")),
    ("ged", [], R(".02(6)")), ("alt_assess", [], R(".02(8)")),
    # .03 disability definitions and criteria
    ("autism", [], R(".03(1)")), ("deafblind", [], R(".03(2)")), ("dd", [], R(".03(3)")),
    ("ed", [("emotional disability", S, AL)], R(".03(4)")),
    ("hi", [], R(".03(5)")), ("id", [], R(".03(6)")), ("adaptive", [], R(".03(6)")),
    ("md", [], R(".03(7)")), ("oi", [], R(".03(8)")), ("ohi", [], R(".03(9)")),
    ("adhd", [], R(".03(9)")), ("epilepsy", [], R(".03(9)")), ("sickle", [], R(".03(9)")), ("tourette", [], R(".03(9)")),
    ("sld", [], R(".03(10)")), ("perceptual", [], R(".03(10)")), ("mbd", [], R(".03(10)")),
    ("dyslexia", [], R(".03(10)")), ("aphasia", [], R(".03(10)")), ("discrepancy", [], R(".03(10)")),
    ("rti", [], R(".03(10)")), ("psw", [], R(".03(10)")), ("oral_expr", [], R(".03(10)")),
    ("listen_comp", [], R(".03(10)")), ("written_expr", [], R(".03(10)")), ("basic_reading", [], R(".03(10)")),
    ("fluency", [], R(".03(10)")), ("reading_comp", [], R(".03(10)")), ("math_calc", [], R(".03(10)")),
    ("math_ps", [], R(".03(10)")), ("observation", [], R(".03(10)")), ("exclusionary", [], R(".03(10)")),
    ("sli", [], R(".03(11)")),
    ("artic", [("articulation/phonological disorder", S, AL)], R(".03(11)")),
    ("voice", [], R(".03(11)")), ("fluency_dis", [], R(".03(11)")), ("lang_dis", [], R(".03(11)")),
    ("tbi", [], R(".03(12)")), ("vi", [], R(".03(13)")), ("lma", [], R(".03(13)")), ("fva", [], R(".03(13)")),
    # .04 eligibility and consent
    ("eligibility", [("Eligibility Committee", S, AL)], R(".04(1)")),
    ("eval_report", [("eligibility report", S, AL)], R(".04(2)")),
    ("revoke", [], R(".04(4)")),
    # .05 IEP
    ("iep_team", [], R(".05(3)")), ("gen_teacher", [], R(".05(3)")), ("sped_teacher", [], R(".05(3)")),
    ("lea_rep", [], R(".05(3)")), ("eval_interp", [], R(".05(3)")), ("postsecondary", [], R(".05(3)")),
    ("prefs", [], R(".05(3)")), ("part_c_transition", [("early intervention", S, None)], R(".05(3)")), ("plaafp", [], R(".05(6)")), ("annual_goals", [], R(".05(6)")),
    ("sto", [], R(".05(6)")), ("program_mods", [], R(".05(6)")), ("prr", [], R(".05(6)")),
    ("removal_expl", [], R(".05(6)")), ("test_accom", [], R(".05(6)")), ("fld", [], R(".05(6)")),
    ("progress", [], R(".05(6)")), ("trans_assess", [], R(".05(6)")), ("course_study", [], R(".05(6)")),
    ("pbis", [], R(".05(6)")), ("braille", [], R(".05(6)")), ("comm_mode", [], R(".05(6)")),
    ("age_majority", [], R(".05(6)")), ("sig_cog", [], R(".05(6)")),
    ("esy", [], R(".05(9)")), ("regression", [], R(".05(9)")), ("critical_skill", [], R(".05(9)")),
    ("comparable", [], R(".05(10)")), ("amendment", [], R(".05(11)")), ("medicaid_sbs", [], R(".05(14)")),
    # .06 LRE
    ("lre", [], R(".06")), ("nonacademic_settings", [], R(".06(2)")), ("continuum", [], R(".06(3)")),
    ("regular_class", [], R(".06(3)")), ("special_class", [], R(".06(3)")), ("special_school", [], R(".06(3)")),
    ("home_instr", [], R(".06(3)")), ("hospital_instr", [], R(".06(3)")),
    # .07 other services
    ("voc_ed", [("career/technical education", V, AL)], R(".07(1)")),
    ("nonacademic", [], R(".07(3)")), ("at_device", [], R(".07(6)")), ("at_service", [], R(".07(6)")),
    ("transport", [("special transportation", S, AL)], R(".07(8)")),
    # .08 procedural safeguards
    ("surrogate", [], R(".08(1)")), ("uhy", [], R(".08(1)")), ("ed_records", [], R(".08(2)")),
    ("pwn", [], R(".08(4)")),
    ("safeguards_notice", [("Special Education Rights", S, AL)], R(".08(6)")),
    ("state_complaint", [("special education complaint", S, AL)], R(".08(9)")),
    ("mediation", [], R(".08(9)")), ("dp_hearing", [], R(".08(9)")),
    ("dp_complaint", [("due process hearing request", S, None)], R(".08(9)")),
    ("resolution", [], R(".08(9)")), ("stay_put", [], R(".08(9)")), ("state_panel", [], R(".08(9)")),
    ("pti", [], R(".08(9)")),
    # .09 discipline
    ("code_conduct", [], R(".09(1)")), ("iaes", [], R(".09(1)")), ("fba", [], R(".09(1)")),
    ("cop", [], R(".09(2)")), ("mdr", [], R(".09(2)")), ("bip", [], R(".09(2)")), ("special_circ", [], R(".09(2)")),
    ("controlled", [], R(".09(2)")), ("illegal_drug", [], R(".09(2)")), ("sbi", [], R(".09(2)")),
    ("weapon", [], R(".09(2)")), ("exp_hearing", [], R(".09(3)")), ("basis_know", [], R(".09(5)")),
    # .10 administration
    ("ppps", [], R(".10(8)")), ("equitable", [], R(".10(8)")),
    ("cert_completion", [("graduation certificate", S, AL)], R(".10(9)")),
    ("disprop", [], R(".10(13)")),
    # .12 gifted
    ("gifted", [("intellectually gifted", S, AL)], R(".12(1)")),
    # Procedural Safeguards Notice
    ("safeguards_notice", [("Alabama's Procedural Safeguards", S, AL)], PS(1)),
    ("pwn", [], PS(4)), ("consent", [], PS(5)), ("revoke", [], PS(5)), ("ward", [], PS(6)),
    ("equitable", [], PS(7)), ("age_majority", [], PS(7)), ("iee", [], PS(7)), ("state_complaint", [], PS(8)),
    ("pti", [], PS(9)), ("mediation", [], PS(11)), ("dp_complaint", [], PS(12)), ("resolution", [], PS(14)),
    ("dp_hearing", [], PS(15)),
    ("state_panel", [("Special Education Advisory Panel", S, AL), ("SEAP", A, AL)], PS(17)),
    ("stay_put", [], PS(18)), ("ed_records", [], PS(20)), ("pii", [], PS(20)), ("part_agency", [], PS(20)),
    ("child_find", [], PS(21)), ("ppps", [], PS(7)), ("code_conduct", [], PS(24)), ("iaes", [], PS(24)),
    ("mdr", [], PS(25)), ("fba", [], PS(25)), ("bip", [], PS(25)), ("special_circ", [], PS(25)),
    ("controlled", [], PS(25)), ("illegal_drug", [], PS(25)), ("sbi", [], PS(25)), ("weapon", [], PS(25)),
    ("cop", [], PS(26)), ("exp_hearing", [], PS(26)), ("basis_know", [], PS(27)),
    # Mastering the Maze: acronym list
    ("autism", [("AUT", A, AL)], G(7)), ("aba", [], G(7)), ("ada", [], G(7)), ("adhd", [], G(7)),
    ("dp_hearing", [("DPH", A, AL)], G(7)),
    ("ifsp", [("Individual Family Service Plan", V, AL)], G(8)), ("lep", [], G(8)),
    ("sst", [("Problem Solving Team", S, AL), ("PST", A, AL)], G(8)),
    # Mastering the Maze: forms and process
    ("iep_team", [], G(10)), ("part_c_transition", [], G(11)),
    ("sst", [("Problem-Solving Team", V, AL)], G(25)),
    ("pwn", [("Notice of Proposal or Refusal to Take Action", S, AL)], G(44)),
    ("plaafp", [], G(90)), ("strengths", [], G(74)), ("parent_concerns", [], G(74)),
    ("trans_assess", [], G(81)), ("comm_exp", [], G(88)), ("fve", [], G(89)),
    ("fed_place_code", [], G(98)), ("progress", [("Annual Goal Progress Report", S, AL)], G(104)),
    ("sop", [("SAAFP", A, AL)], G(106)), ("fba", [], G(112)), ("mdr", [], G(116)),
    ("revoke", [("Notice of Revocation of Consent for Continued Provision of Special Education and Related Services", S, AL)], G(122)),
    ("amendment", [], G(126)), ("annual_review", [], G(75)),
    ("pe", [], G(78)), ("part_c_transition", [("Transition Planning Meeting", S, AL)], G(188)),
]

CONCEPTS = [
    # state agencies, offices and organizations
    ("al_alsde", "Alabama State Department of Education", "legal_procedural", [("ALSDE", A, AL)], G(7),
     {**ALJ, "broader": "sea"}),
    ("al_sboe", "Alabama State Board of Education", "legal_procedural", [], PS(2), ALJ),
    ("al_adrs", "Alabama Department of Rehabilitation Services", "transition", [("ADRS", A, AL)], G(7), ALJ),
    ("al_aeis", "Alabama's Early Intervention System", "early_intervention", [("AEIS", A, AL)], G(7),
     {**ALJ, "note": "Alabama's Part C early intervention system, called Part C/Early Intervention (EI) in the rule."}),
    ("al_crs", "Children's Rehabilitation Services", "legal_procedural", [], G(153),
     {**ALJ, "note": "A state agency the guide names as a source of help with glasses and hearing aids."}),
    ("al_medicaid", "Alabama State Medicaid Agency", "legal_procedural", [], G(120), ALJ),
    ("al_adap", "Alabama Disabilities Advocacy Program", "legal_procedural", [("ADAP", A, AL)], PS(12),
     {**ALJ, "note": "Listed in the safeguards notice as a free or low-cost legal resource."}),
    ("al_apec", "Alabama Parent Education Center", "legal_procedural", [("APEC", A, AL)], PS(12),
     {**ALJ, "note": "Listed in the safeguards notice as a resource for parents."}),
    ("al_ric", "Regional Inservice Center", "legal_procedural", [("RIC", A, AL)], G(8), ALJ),
    ("al_sets", "Special Education Tracking System", "iep_component", [("SETS", A, AL)], G(8),
     {**ALJ, "note": "The statewide online system in which Alabama's special education forms are completed."}),
    # forms and procedures
    ("al_invite", "Notice and Invitation to a Meeting/Consent for Agency Participation", "legal_procedural", [], G(40),
     {**ALJ, "note": "The state form used to invite parents to every IEP Team meeting."}),
    ("al_nci", "Notice and Consent for Initial Evaluation", "legal_procedural", [], G(47),
     {**ALJ, "broader": "consent", "note": "Receipt of the signed form starts the 60-day initial evaluation timeline."}),
    ("al_reeval_notice", "Notice of IEP Team's Decision Regarding Reevaluation", "legal_procedural", [], G(42),
     {**ALJ, "broader": "reeval"}),
    ("al_elig_notice", "Notice and Eligibility Decision Regarding Special Education Services", "evaluation_eligibility", [], G(64),
     {**ALJ, "broader": "eval_report", "note": "Alabama's eligibility report form."}),
    ("al_consent_svc", "Notice and Consent for the Provision of Special Education Services", "legal_procedural", [], G(72),
     {**ALJ, "broader": "consent"}),
    ("al_sif", "Special Instructional Factors", "iep_component", [], G(77),
     {**ALJ, "note": "The IEP section where the team considers behavior, English proficiency, Braille, communication, AT and similar factors."}),
    ("al_acc_checklist", "IEP Accommodations Checklist", "accommodation_modification", [], G(95),
     {**ALJ, "broader": "test_accom", "note": "Lists the accommodations allowed on state assessments."}),
    ("al_persons_resp", "Persons Responsible for IEP Implementation", "iep_component", [], G(102),
     {**ALJ, "note": "A form each person who carries out the IEP signs."}),
    ("al_ecec", "Environmental, Cultural, and/or Economic Concerns", "evaluation_eligibility", [("ECEC", A, AL)], G(4),
     {**ALJ, "broader": "exclusionary", "note": "A referral checklist used to rule out environmental, cultural and economic factors."}),
    ("al_ffi", "Family Focus Interview", "evaluation_eligibility", [("FFI", A, AL)], G(56),
     {**ALJ, "note": "A parent interview required for preschool developmental delay eligibility."}),
    ("al_neo", "Natural Environment Observation", "evaluation_eligibility", [("NEO", A, AL)], G(56),
     {**ALJ, "note": "An observation of a preschool child in a natural setting, required for developmental delay eligibility."}),
    ("al_elpp", "Early Learning Progress Profile", "evaluation_eligibility", [("ELPP", A, AL)], G(56),
     {**ALJ, "note": "Alabama's preschool outcome measure, documented within 45 days of starting services."}),
    ("al_predicted", "Predicted achievement model", "evaluation_eligibility", [], R(".03(10)"),
     {**ALJ, "broader": "discrepancy", "note": "Alabama's method for calculating a severe discrepancy for specific learning disability."}),
    # standards and assessments
    ("al_aaa", "Alabama Alternate Assessment", "iep_component", [("AAA", A, AL)], G(7), {**ALJ, "broader": "alt_assess"}),
    ("al_aaa_pdd", "Alabama Alternate Assessment Program Participation Decision Documentation", "iep_component", [], G(78),
     {**ALJ, "broader": "al_aaa", "note": "The form an IEP Team uses to decide that a student takes the alternate assessment."}),
    ("al_ext_std", "Alabama Extended Standards", "academic_skill", [], R(".05(6)"),
     {**ALJ, "note": "Standards the rule names for students with significant cognitive disabilities assessed with the alternate assessment."}),
    ("al_aas", "Alabama Alternate Achievement Standards", "academic_skill", [], G(91),
     {**ALJ, "note": "The standards the 2019 guide names for academic goals of students with significant cognitive disabilities."}),
    ("al_dev_std", "Alabama Developmental Standards for Preschool Children", "academic_skill", [], G(75), ALJ),
    ("al_trans_std", "Alabama Transition Standards", "transition", [], G(83), ALJ),
    ("al_cos", "Alabama Course of Study", "academic_skill", [], G(75), ALJ),
    ("al_ccrs", "College and Career Ready Standards", "academic_skill", [("CCRS", A, AL)], G(7),
     {**ALJ, "note": "Alabama's general education content standards."}),
    # diplomas and pathways
    ("al_ahsd", "Alabama High School Diploma", "transition", [("AHSD", A, AL)], G(45), {**ALJ, "broader": "std_diploma"}),
    ("al_gen_path", "General Education Pathway", "transition", [], G(81), {**ALJ, "broader": "al_ahsd"}),
    ("al_ess_path", "Essentials Pathway", "transition", [], G(81), {**ALJ, "broader": "al_ahsd"}),
    ("al_aas_path", "Alternate Achievement Standards Pathway", "transition", [], G(81), {**ALJ, "broader": "al_ahsd"}),
    ("al_aod", "Alabama Occupational Diploma", "transition", [("AOD", A, AL)], R(".10(9)"),
     {**ALJ, "note": "A diploma option named in the 2013 rule."}),
    ("al_ahsge", "Alabama High School Graduation Exam", "transition", [("AHSGE", A, AL)], R(".10(9)"),
     {**ALJ, "note": "The exit exam the 2013 rule ties to the diploma."}),
    ("al_post_survey", "Alabama Post-School Outcomes Survey", "transition", [], G(108), ALJ),
    # gifted
    ("al_grst", "Gifted Referrals Screening Team", "evaluation_eligibility", [("GRST", A, AL)], R(".12(2)"),
     {**ALJ, "broader": "gifted"}),
    ("al_edt", "Eligibility Determination Team", "evaluation_eligibility", [("EDT", A, AL)], R(".12(5)"),
     {**ALJ, "broader": "gifted", "note": "The team that decides eligibility for gifted services."}),
    ("al_matrix", "Matrix of Multiple Criteria", "evaluation_eligibility", [], R(".12(5)"), {**ALJ, "broader": "gifted"}),
    ("al_gep", "Gifted Education Plan", "iep_component", [("GEP", A, AL)], R(".12(7)"), {**ALJ, "broader": "gifted"}),
    # national concepts first attested by Alabama's documents
    ("psychometrist", "Psychometrist", "personnel_role", [("school psychometrist", S, None)], R(".02(3)"),
     {"note": "A specialist qualified to give intellectual and achievement tests."}),
    ("indiv_intel", "Individual intellectual evaluation", "evaluation_eligibility", [], R(".02(3)"), {}),
    ("ceis", "Coordinated early intervening services", "legal_procedural", [("CEIS", A, None)], G(7), {}),
    ("cceis", "Comprehensive coordinated early intervening services", "legal_procedural", [("CCEIS", A, None)], G(7),
     {"broader": "ceis"}),
    ("osep", "Office of Special Education Programs", "legal_procedural", [("OSEP", A, None)], G(8), {}),
    ("bcba", "Board-Certified Behavior Analyst", "personnel_role", [("BCBA", A, None)], G(7), {}),
    ("sbmh", "School based mental health", "related_service", [("SBMH", A, None)], G(8), {}),
    ("vr_services", "Vocational rehabilitation services", "transition", [("VRS", A, AL)], G(9), {}),
    ("bus_susp", "Bus suspension", "discipline", [], R(".09(7)"), {}),
    ("iss", "In-school suspension", "discipline", [], R(".09(8)"), {}),
    ("carnegie", "Carnegie unit", "transition", [("Carnegie Units", P, None)], R(".10(9)"),
     {"flags": ["eponym"], "note": "A high school course credit."}),
    ("head_start", "Head Start", "placement_setting", [], G(22), {}),
    ("sb_iep", "Standards-based IEP", "iep_component", [], G(167), {"broader": "iep"}),
]

JURISDICTION = "US-AL"
LAYER_NAME = "Alabama"
# Documents listed in sources/documents.tsv that no record cites, and why.
UNCITED_DOCS = {"al-aac290copy-2013": "Second saved copy of the rule; the cited copy is al-aac290-2013."}

RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.36.0"
