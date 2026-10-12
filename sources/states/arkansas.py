"""
Arkansas layer for SPEDLex.

Sources reviewed 2026-10-08 (all published by the Arkansas Department of
Education (ADE), Division of Elementary and Secondary Education (DESE),
Special Education Unit):
  RULE   6 CAR pt. 130, Subpart 2, Definitions (§§ 130-201 to 130-276), the
         Code of Arkansas Rules copy saved from the DESE website (33 pp.,
         printed Mar. 11, 2026), cited by section, e.g. "6 CAR § 130-257"
  PSN    Arkansas Department of Education Procedural Safeguards Notice,
         Special Education Unit ("Part B Procedural Safeguards Notice",
         47 pp.; no date printed, PDF created Sept. 2006), cited by PDF page
         (printed page number + 3)
  GUIDE  Special Education Process Guide (DESE Special Education Unit,
         Mar. 14, 2023, 126 pp.), cited by PDF page (printed page number + 4)

All three were read in full as text extracted with pdftotext. Only the
Definitions subpart of 6 CAR pt. 130 was provided; the other subparts and the
Special Education Eligibility Criteria and Program Guidelines were not read.
The PSN is the 2006 U.S. Department of Education model notice with an
Arkansas header; it predates the 2008 revocation-of-consent rule. RULE
records are 'machine_validated'; the others are 'candidate'.

Left out on purpose: every person named in the documents (the process guide
task force on GUIDE p. 2), the districts and cooperatives they work for,
addresses, phone numbers and web addresses; two-letter placement codes (RG,
RR, SC, HM and the like, several of which are postal codes or common words);
test products named as examples (GUIDE p. 88); "PBS", which has common other
meanings; "Administrative case management" (6 CAR § 130-202), whose
preferred term already belongs to a New Hampshire concept with a different
meaning; and Easter Seals Outreach and ArKids, which the guide only names in
passing.
"""

RULE_URL = "https://dese.ade.arkansas.gov/Files/ADE_Spec._Ed._-_Definitions_6CARpt.130-Subpart2_Legal.pdf"
PSN_URL = "https://arksped.ade.arkansas.gov/documents/grantsanddata/Procedural_Safeguards_Notice.pdf"
GUIDE_URL = "https://arksped.ade.arkansas.gov/documents/paperwork-reduction/sped-process-guide.pdf"


def src(doc, loc=""):
    """RULE loc is a section number, e.g. '257'; PSN and GUIDE loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"6 CAR § 130-{loc}", "doc_id": "ar-6car130-2026", "url": RULE_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"DESE Special Education Process Guide (Mar. 14, 2023), PDF p. {loc}",
                "doc_id": "ar-processguide-2023", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"ADE Part B Procedural Safeguards Notice (Special Education Unit; PDF created Sept. 2006), PDF p. {loc}",
            "doc_id": "ar-psn-2006", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
AR = ["US-AR"]
ARJ = {"jurisdiction": "US-AR"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # 6 CAR pt. 130, Subpart 2 definitions
    ("adverse", [], R("201")), ("at_device", [], R("204")), ("at_service", [], R("205")),
    ("charter_school", [], R("207")), ("cwd", [], R("208")), ("ed", [], R("208")), ("ohi", [], R("208")),
    ("consent", [], R("212")), ("school_day", [], R("215")), ("rti", [], R("214")),
    ("discrepancy", [], R("217")),
    ("ceis", [("early intervening services", S, None)], R("218")),
    ("ed_records", [], R("220")), ("esa", [], R("222")), ("evaluation", [], R("226")), ("esy", [], R("227")),
    ("fape", [], R("228")), ("homeless", [], R("229")), ("iee", [], R("231")),
    ("indirect_svc", [], R("232")), ("consult_teacher", [("consulting teacher", REL, AR)], R("232")),
    ("interpreting", [], R("234")), ("itinerant", [], R("235")), ("iep", [], R("236")), ("iep_team", [], R("237")),
    ("idea", [], R("238")), ("lep", [], R("241")), ("lea", [], R("242")), ("mediation", [], R("243")),
    ("native_language", [], R("245")), ("braille", [], R("245")), ("foster", [], R("246")), ("surrogate", [], R("246")),
    ("para", [], R("247")), ("part_agency", [], R("248")), ("pii", [], R("249")), ("public_agency", [], R("250")),
    ("pe", [], R("252")), ("pbis", [], R("253")), ("nh_qual_examiner", [], R("254")),
    ("related", [], R("256")), ("implant", [], R("256")), ("transport", [], R("256")),
    ("resource_room", [("resource services", S, AR)], R("257")),
    ("rti", [], R("258")), ("nursing", [], R("261")), ("screening", [], R("262")), ("services_plan", [], R("264")),
    ("special_class", [("special class services", REL, AR)], R("265")),
    ("special_school", [("special day school, private", REL, AR)], R("266")),
    ("special_school", [("special day school, public", REL, AR)], R("267")),
    ("special_ed", [], R("268")), ("sdi", [], R("269")), ("sea", [], R("270")), ("saas", [], R("271")),
    ("transition", [], R("272")), ("travel_training", [], R("273")), ("voc_ed", [], R("274")),
    ("universal_design", [], R("275")), ("ward", [], R("276")),
    # Procedural Safeguards Notice (2006 federal model)
    ("safeguards_notice", [("Part B Procedural Safeguards Notice", S, None)], PS(4)),
    ("pwn", [], PS(4)), ("native_language", [], PS(5)), ("consent", [], PS(6)), ("ward", [], PS(7)),
    ("equitable", [], PS(9)), ("iee", [], PS(9)), ("ed_records", [], PS(12)), ("pii", [], PS(12)),
    ("part_agency", [], PS(12)), ("ferpa", [], PS(12)), ("child_find", [], PS(13)), ("state_complaint", [], PS(18)),
    ("pti", [], PS(18)), ("dp_complaint", [], PS(22)), ("mediation", [], PS(25)), ("stay_put", [], PS(26)),
    ("resolution", [], PS(27)), ("dp_hearing", [], PS(30)), ("state_panel", [], PS(33)),
    ("code_conduct", [], PS(38)), ("iaes", [], PS(38)), ("fba", [], PS(39)), ("mdr", [], PS(39)),
    ("bip", [], PS(40)), ("special_circ", [], PS(40)), ("controlled", [], PS(40)), ("illegal_drug", [], PS(41)),
    ("sbi", [], PS(41)), ("weapon", [], PS(41)), ("cop", [], PS(41)), ("exp_hearing", [], PS(43)),
    ("basis_know", [], PS(44)), ("ppps", [], PS(9)), ("unilateral_pl", [], PS(46)),
    # Special Education Process Guide
    ("dyslexia", [], G(7)), ("mtss", [], G(7)),
    ("safeguards_notice", [("Your Rights Under IDEA", S, AR)], G(9)),
    ("referral", [], G(12)), ("ferpa", [], G(8)),
    ("reed", [("Existing Data Review", S, AR), ("EDR", A, AR)], G(21)),
    ("lpac", [("LPAC", A, AR)], G(22)),
    ("rti", [], G(36)), ("psw", [], G(37)),
    ("annual_review", [], G(52)),
    ("amendment", [], G(53)), ("reeval", [], G(53)),
    ("sped_admin", [("Special Education Supervisor", S, AR), ("Special Education Director", S, AR)], G(58)),
    ("fba", [], G(58)), ("bip", [], G(58)), ("pbis", [], G(58)), ("braille", [], G(58)), ("s504", [], G(58)),
    ("saas", [], G(59)), ("esy", [], G(60)), ("plaafp", [], G(61)), ("lep", [], G(61)),
    ("coteach", [("co-taught services", S, AR)], G(66)), ("lre", [], G(66)),
    ("special_school", [("Special Day School", S, AR)], G(70)),
    ("residential", [("Residential School", REL, AR)], G(70)),
    ("hospital_instr", [("Hospital Program", REL, AR)], G(70)),
    ("home_instr", [], G(70)),
    ("alt_assess", [], G(72)), ("sig_cog", [], G(72)),
    ("pwn", [("Notice of Action", S, AR)], G(78)), ("age_majority", [], G(80)),
    ("head_start", [], G(86)), ("ifsp", [], G(88)),
    ("nc_recp", [], G(92)), ("ecse", [], G(95)),
    ("trans_assess", [], G(96)),
    ("sop", [], G(103)), ("postsecondary", [], G(103)),
]

CONCEPTS = [
    # state agencies, offices and organizations
    ("ar_ade", "Arkansas Department of Education", "legal_procedural", [], PS(1),
     {**ARJ, "broader": "sea", "note": "The state educational agency; the rule calls it the Department of Education."}),
    ("ar_dese", "Arkansas Division of Elementary and Secondary Education", "legal_procedural", [("DESE", A, AR)], G(2),
     {**ARJ, "broader": "ar_ade", "note": "The division of the state education department that houses special education."}),
    ("ar_seu", "Special Education Unit of the Division of Elementary and Secondary Education", "legal_procedural",
     [("Special Education Unit", S, AR)], R("217"),
     {**ARJ, "broader": "ar_dese", "note": "The state office that issues Arkansas's special education rules and forms."}),
    ("ar_psych_board", "Arkansas Psychology Board", "legal_procedural", [], R("254"),
     {**ARJ, "note": "Licenses psychologists and psychological examiners who may serve as qualified examiners."}),
    ("ar_counsel_board", "Arkansas Board of Examiners in Counseling", "legal_procedural", [], R("254"),
     {**ARJ, "note": "Licenses counselors who may give individual intelligence tests."}),
    ("ar_slp_board", "Board of Examiners in Speech-Language Pathology and Audiology", "legal_procedural", [], R("254"),
     {**ARJ, "note": "The Arkansas licensing board for speech-language pathologists."}),
    ("ar_esvi", "Educational Services for the Visually Impaired", "related_service", [("ESVI", A, AR)], G(58),
     {**ARJ, "note": "A state source of support the guide names for students with visual impairments."}),
    ("ar_ideas", "ArkansasIDEAS", "legal_procedural", [], G(58),
     {**ARJ, "note": "An online professional learning portal the guide points to for behavior training."}),
    ("ar_ats", "Arkansas Transition Services", "transition", [], G(103),
     {**ARJ, "note": "A state project that supports secondary transition; ATS in the guide."}),
    ("ar_ida_office", "IDEA Data and Research Office", "legal_procedural", [], G(75),
     {**ARJ, "note": "Receives the annual special education parent survey."}),
    ("ar_abc", "Arkansas Better Chance", "placement_setting", [("ABC", A, AR)], G(86),
     {**ARJ, "note": "Arkansas's state-funded preschool program."}),
    # placements and service models (rule)
    ("ar_combo_rs", "Combination resource services/special class services", "placement_setting", [], R("210"),
     {**ARJ, "broader": "resource_room", "note": "A resource setting in which up to three students receive special class services."}),
    ("ar_combo_sr", "Combination special class services/resource services", "placement_setting", [], R("211"),
     {**ARJ, "broader": "special_class", "note": "A special class setting in which up to five students receive resource services."}),
    ("ar_integrated", "Integrated classroom", "placement_setting", [], R("233"),
     {**ARJ, "broader": "regular_class",
      "note": "A general education classroom taught all day by a teacher dually licensed in general and special education."}),
    ("ar_day_treatment", "School-based day treatment services", "placement_setting",
     [("School-based Day Treatment", AB, AR)], R("259"),
     {**ARJ, "note": "A school-campus program combining education and mental health services for students with emotional disturbance."}),
    ("ar_instr_day", "Instructional day", "legal_procedural", [], R("240"),
     {**ARJ, "note": "Time spent in instruction, used to measure resource and special class services."}),
    # personnel (rule)
    ("ar_edu_examiner", "Educational examiner", "personnel_role", [], R("254"),
     {**ARJ, "broader": "nh_qual_examiner", "note": "A state-licensed examiner who may give intellectual, academic and behavior rating measures."}),
    ("ar_school_psych_spec", "School psychology specialist", "personnel_role", [], R("254"),
     {**ARJ, "broader": "school_psych"}),
    ("ar_psych_examiner", "Psychological examiner", "personnel_role", [], R("254"),
     {**ARJ, "note": "Licensed by the Arkansas Psychology Board to give tests of mental abilities."}),
    ("ar_student_evaluator", "Student evaluator", "personnel_role", [], R("254"),
     {**ARJ, "note": "An intern or practicum student who gives tests under supervision."}),
    # national concepts first attested by Arkansas's documents
    ("edu_interpreter", "Educational interpreter", "personnel_role", [], R("221"),
     {"broader": "interpreting"}),
    ("dbps", "Data-based problem solving", "evaluation_eligibility", [], R("214"),
     {"note": "A four-step process: problem identification, analysis, intervention and evaluation."}),
    ("core_acad", "Core academic subjects", "academic_skill", [], R("213"), {}),
    ("sbr", "Scientifically based research", "legal_procedural", [], R("260"), {}),
    ("record_access", "Record of access", "legal_procedural", [], PS(14),
     {"note": "A log of who has seen a child's education records, when and why."}),
    ("child_outcomes", "Early Childhood Outcomes", "early_intervention",
     [("Early Childhood Outcomes Process", S, AR), ("COS", A, AR)], G(85),
     {"note": "The three child outcome ratings reported for preschool children with IEPs."}),
    ("act_aspire", "ACT Aspire", "instrument", [], G(71),
     {"note": "A commercial assessment the guide names as Arkansas's general statewide test for grades 3-10."}),
    ("nsttac", "National Secondary Transition Technical Assistance Center", "transition", [("NSTTAC", A, None)], G(103), {}),
    ("i13_checklist", "Indicator 13 Checklist", "transition", [], G(103),
     {"note": "A checklist for whether an IEP's transition components meet federal requirements."}),
    # forms, procedures and IEP parts (guide)
    ("ar_notice_conf", "Notice of Conference", "legal_procedural", [], G(15),
     {**ARJ, "note": "The state form that invites parents to special education meetings."}),
    ("ar_referral_conf", "Referral conference", "evaluation_eligibility", [], G(12),
     {**ARJ, "broader": "referral", "note": "A meeting held within 21 calendar days of a referral to decide whether to evaluate."}),
    ("ar_epc", "Evaluation/Programming Conference", "evaluation_eligibility", [], G(11),
     {**ARJ, "broader": "eligibility", "note": "The conference, and its decision form, at which eligibility and programming are decided."}),
    ("ar_sld_form", "Specific Learning Disability Eligibility Determination form", "evaluation_eligibility", [], G(33),
     {**ARJ, "broader": "sld"}),
    ("ar_temp_iep", "Temporary IEP", "iep_component", [], G(52),
     {**ARJ, "broader": "iep", "note": "An IEP for a diagnostic placement of up to 60 calendar days while an evaluation is completed."}),
    ("ar_sched_services", "Schedule of Services", "iep_component", [], G(66),
     {**ARJ, "note": "The IEP section that lists the type, amount and setting of special education services."}),
    ("ar_seecp", "Special Education Early Childhood Program", "placement_setting", [], G(92),
     {**ARJ, "broader": "ecse", "note": "A preschool setting that separates children with disabilities from nondisabled children."}),
    ("ar_ecse_k", "Early Childhood Special Education to Kindergarten Transition Process", "early_intervention", [], G(95),
     ARJ),
    ("ar_pao", "Public Agency Official", "personnel_role", [], G(14),
     {**ARJ, "note": "The principal or designee who receives a special education referral."}),
    # standards, assessments, manuals and pathways (guide)
    ("ar_aas", "Arkansas Academic Standards", "academic_skill", [], G(61), ARJ),
    ("ar_elp_std", "Arkansas English Language Proficiency standards", "academic_skill", [], G(61), ARJ),
    ("ar_cdels", "Arkansas Child Development and Early Learning Standards", "academic_skill", [("AR CDELS", A, AR)], G(86),
     ARJ),
    ("ar_rti", "RTI Arkansas", "evaluation_eligibility", [], G(7),
     {**ARJ, "broader": "mtss", "note": "The state's multi-tiered intervention initiative."}),
    ("ar_dys_guide", "Dyslexia Resource Guide", "evaluation_eligibility", [], G(7),
     {**ARJ, "note": "State guidance on dyslexia screening and intervention."}),
    ("ar_sld_tam", "Arkansas Technical Assistance Manual: Identification of Children with Specific Learning Disabilities",
     "evaluation_eligibility", [], G(36), {**ARJ, "broader": "sld"}),
    ("ar_aa_manual", "Arkansas Alternate Assessment Participation Manual", "iep_component", [], G(72),
     {**ARJ, "broader": "alt_assess", "note": "Sets the criteria IEP teams use to decide alternate assessment participation."}),
    ("ar_alt_pathway", "Alternate Pathway to Graduation", "transition", [], G(73),
     {**ARJ, "note": "A graduation pathway for students with the most significant cognitive disabilities who take the alternate assessment."}),
]

JURISDICTION = "US-AR"
LAYER_NAME = "Arkansas"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.37.0"
