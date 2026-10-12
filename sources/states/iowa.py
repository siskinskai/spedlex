"""
Iowa layer for SPEDLex.

Sources reviewed 2026-10-08 (listed in sources/documents.tsv; local copies in .sources-cache/ia/):
  RULE   Iowa Administrative Code 281, Chapter 41, Special Education (IAC
         printed 12/10/25, 108 pp.; amendments effective through 1/14/26),
         from the Iowa Legislature's website, cited by rule or subrule,
         e.g. "281 IAC 41.50(2)"
  PSN    Iowa Department of Education, Procedural Safeguards Manual: Rights
         of Parents of Students with Disabilities Ages 3-21 (Aug. 2023,
         50 pp.), cited by PDF page (printed page number + 6)
  GUIDE  Special Education Terms and Acronyms, Ages 3-21 (7 pp.), hosted by
         the Iowa Department of Education. No publisher or date is printed;
         the PDF was created Feb. 18, 2021. Cited by page.

All three were read in full as text extracted with pdftotext. No main parent
guide or IEP manual was provided; the terms-and-acronyms sheet stands in for
it. Iowa's IEP guidance, eligibility standards and alternate assessment
pages were not read. RULE records are 'machine_validated'; the others are
'candidate'.

Left out on purpose: the nine individual Area Education Agencies (local
agencies named for regions, one for a person), the individual Centers for
Independent Living (named for places), every address, phone number, web
address and person; two-letter acronyms the guide uses with other common
meanings (EC, EL, DS, HS) and DE, which is Delaware's postal code; general
health and welfare programs the guide defines in passing (CDC, WIC, HIPAA);
the special education weighting plan and its levels of service (funding
formula, 41.907(9)); and "child requiring special education" (41.8), whose
string already belongs untagged to a Connecticut concept.
"""

RULE_URL = "https://www.legis.iowa.gov/docs/iac/chapter/281.41.pdf"
PSN_URL = "https://educate.iowa.gov/media/2041/download"
GUIDE_URL = "https://educate.iowa.gov/media/7065/download"


def src(doc, loc=""):
    """RULE loc is a rule or subrule, e.g. '41.50(2)'; PSN loc is a PDF page; GUIDE loc is a page."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"281 IAC {loc}", "doc_id": "ia-iac281-2025", "url": RULE_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"Special Education Terms and Acronyms, Ages 3-21 (Iowa DE; undated, PDF created Feb. 2021), p. {loc}",
                "doc_id": "ia-terms-2021", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"Iowa DE Procedural Safeguards Manual: Rights of Parents of Students with Disabilities Ages 3-21 (Aug. 2023), PDF p. {loc}",
            "doc_id": "ia-psn-2023", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
IA = ["US-IA"]
IAJ = {"jurisdiction": "US-IA"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # 281 IAC ch. 41, Division II definitions
    ("idea", [], R("41.3")), ("esa", [], R("41.4")),
    ("at_device", [], R("41.5")), ("at_service", [], R("41.6")), ("charter_school", [], R("41.7")),
    ("cwd", [], R("41.8")), ("consent", [], R("41.9")), ("core_acad", [], R("41.10")),
    ("school_day", [], R("41.11")), ("evaluation", [], R("41.15")), ("excess_costs", [], R("41.16")),
    ("fape", [], R("41.17")), ("homeless", [], R("41.19")), ("iep", [], R("41.22")), ("iep_team", [], R("41.23")),
    ("ifsp", [], R("41.24")), ("itd", [], R("41.25")), ("lep", [], R("41.27")), ("lea", [], R("41.28")),
    ("native_language", [], R("41.29")), ("surrogate", [], R("41.30(1)")), ("pti", [], R("41.31")),
    ("pii", [], R("41.32")), ("public_agency", [], R("41.33")), ("related", [], R("41.34(1)")),
    ("implant", [], R("41.34(2)")), ("audiology", [], R("41.34(3)")), ("counseling", [], R("41.34(3)")),
    ("early_id", [], R("41.34(3)")), ("interpreting", [], R("41.34(3)")), ("cart", [], R("41.34(3)")),
    ("medical", [], R("41.34(3)")), ("ot", [], R("41.34(3)")), ("om", [], R("41.34(3)")),
    ("parent_training", [], R("41.34(3)")), ("pt", [], R("41.34(3)")), ("psych", [], R("41.34(3)")),
    ("recreation", [], R("41.34(3)")), ("rehab", [], R("41.34(3)")), ("nursing", [], R("41.34(3)")),
    ("social_work", [], R("41.34(3)")), ("slp", [], R("41.34(3)")), ("transport", [], R("41.34(3)")),
    ("services_plan", [], R("41.37")), ("special_ed", [], R("41.39(1)")),
    ("pe", [("special physical education", S, IA)], R("41.39(3)")),
    ("sdi", [], R("41.39(3)")), ("travel_training", [], R("41.39(3)")), ("voc_ed", [], R("41.39(3)")),
    ("sea", [], R("41.41")), ("saas", [], R("41.42")), ("transition", [], R("41.43(1)")),
    ("comm_exp", [], R("41.43(1)")), ("post_school", [], R("41.43(1)")), ("daily_living", [], R("41.43(1)")),
    ("fve", [], R("41.43(1)")), ("universal_design", [], R("41.44")), ("ward", [], R("41.45")),
    ("foster", [], R("41.45")),
    # 41.50, the eligibility definitions
    ("autism", [], R("41.50(1)")),
    ("ed", [("behavior disorder", S, IA)], R("41.50(2)")),
    ("deafblind", [], R("41.50(3)")), ("deafness", [], R("41.50(4)")), ("hi", [], R("41.50(5)")),
    ("id", [], R("41.50(6)")), ("md", [], R("41.50(7)")), ("oi", [], R("41.50(8)")), ("ohi", [], R("41.50(9)")),
    ("adhd", [], R("41.50(9)")), ("epilepsy", [], R("41.50(9)")), ("sickle", [], R("41.50(9)")),
    ("tourette", [], R("41.50(9)")), ("sld", [], R("41.50(10)")), ("perceptual", [], R("41.50(10)")),
    ("mbd", [], R("41.50(10)")), ("dyslexia", [], R("41.50(10)")), ("aphasia", [], R("41.50(10)")),
    ("sli", [], R("41.50(11)")), ("tbi", [], R("41.50(12)")), ("vi", [], R("41.50(13)")),
    # 41.51, other definitions
    ("sped_admin", [], R("41.51(4)")),
    ("sped_admin", [("AEA director of special education", S, IA)], R("41.306(4)")),
    ("ecse", [], R("41.51(6)")), ("gen_curr", [], R("41.51(7)")), ("gen_ed_env", [], R("41.51(8)")),
    ("gen_ed_int", [], R("41.51(9)")),
    ("tbi", [("head injury", S, IA)], R("41.51(10)")),
    ("resident_dist", [("school district of the child's residence", S, IA),
                       ("district of residence of the child", S, IA)], R("41.51(12)")),
    # Divisions III to VI
    ("std_diploma", [], R("41.102(1)")),
    ("ged", [("general equivalency diploma", S, None)], R("41.102(1)")),
    ("cert_completion", [("certificate of completion", S, IA)], R("41.102(1)")),
    ("residential", [], R("41.104")), ("esy", [], R("41.106(2)")), ("nonacademic", [], R("41.107")),
    ("feog", [], R("41.109")), ("child_find", [], R("41.111(1)")), ("lre", [], R("41.114")),
    ("continuum", [], R("41.115")), ("regular_class", [], R("41.115(2)")), ("special_class", [], R("41.115(2)")),
    ("special_school", [], R("41.115(2)")), ("home_instr", [], R("41.115(2)")), ("hospital_instr", [], R("41.115(2)")),
    ("resource_room", [], R("41.115(2)")), ("itinerant", [], R("41.115(2)")),
    ("nonacademic_settings", [], R("41.117")), ("part_c_transition", [], R("41.124")),
    ("ppps", [], R("41.130")), ("child_count", [], R("41.133(2)")), ("equitable", [], R("41.137")),
    ("unilateral_pl", [], R("41.148")), ("state_complaint", [], R("41.151")), ("comp_services", [], R("41.151(2)")),
    ("adr", [], R("41.152(2)")), ("para", [], R("41.156(2)")), ("sped_teacher", [], R("41.156(3)")),
    ("alt_assess", [], R("41.160(3)")), ("sig_cog", [], R("41.160(3)")), ("state_panel", [], R("41.167")),
    ("nimas", [], R("41.172(1)")), ("disprop", [], R("41.173")), ("state_ops", [], R("41.176(2)")),
    ("nimac", [], R("41.210(4)")), ("print_disability", [], R("41.210(4)")), ("ceis", [], R("41.226")),
    ("revoke", [], R("41.300(2)")), ("reeval", [], R("41.303")), ("screening", [], R("41.302")),
    ("reed", [], R("41.305(1)")), ("sop", [], R("41.305(5)")), ("eligibility", [], R("41.306")),
    ("eval_report", [], R("41.306(1)")), ("rti", [], R("41.307(1)")), ("discrepancy", [], R("41.307(1)")),
    ("school_psych", [], R("41.308(2)")),
    ("oral_expr", [], R("41.309(1)")), ("listen_comp", [], R("41.309(1)")), ("written_expr", [], R("41.309(1)")),
    ("basic_reading", [], R("41.309(1)")), ("fluency", [], R("41.309(1)")), ("reading_comp", [], R("41.309(1)")),
    ("math_calc", [], R("41.309(1)")), ("math_ps", [], R("41.309(1)")), ("psw", [], R("41.309(1)")),
    ("exclusionary", [], R("41.309(1)")), ("data_doc", [], R("41.309(2)")), ("observation", [], R("41.310")),
    ("nc_sps", [], R("41.313")),
    ("plaafp", [], R("41.320(1)")), ("annual_goals", [], R("41.320(1)")), ("sto", [], R("41.320(1)")),
    ("progress", [], R("41.320(1)")), ("program_mods", [], R("41.320(1)")), ("prr", [], R("41.320(1)")),
    ("removal_expl", [], R("41.320(1)")), ("test_accom", [], R("41.320(1)")), ("fld", [], R("41.320(1)")),
    ("postsecondary", [], R("41.320(2)")), ("trans_assess", [], R("41.320(2)")), ("course_study", [], R("41.320(2)")),
    ("age_majority", [], R("41.320(3)")), ("gen_teacher", [], R("41.321(1)")), ("lea_rep", [], R("41.321(1)")),
    ("eval_interp", [], R("41.321(1)")), ("prefs", [], R("41.321(2)")), ("draft_iep", [], R("41.322(7)")),
    ("comparable", [], R("41.323(5)")), ("strengths", [], R("41.324(1)")), ("parent_concerns", [], R("41.324(1)")),
    ("pbis", [], R("41.324(1)")), ("braille", [], R("41.324(1)")), ("comm_mode", [], R("41.324(1)")),
    ("amendment", [], R("41.324(1)")), ("annual_review", [], R("41.324(2)")), ("interim_iep", [], R("41.324(5)")),
    ("tvi", [], R("41.324(6)")),
    ("edu_interpreter", [], R("41.402(3)")), ("school_social_worker", [], R("41.402(3)")),
    ("sped_admin", [("special education coordinator", S, IA)], R("41.402(3)")),
    ("para", [("para-educator", V, None)], R("41.403(2)")),
    ("tvi", [("teacher of the visually impaired", S, None)], R("41.403(2)")),
    # Division VII procedural safeguards
    ("iee", [], R("41.502")), ("pwn", [], R("41.503")), ("safeguards_notice", [], R("41.504")),
    ("mediation", [("preappeal conference", L, IA)], R("41.506(5)")),
    ("cprc", [], R("41.506(2)")),
    ("dp_complaint", [("request for due process hearing", S, IA)], R("41.507(3)")),
    ("resolution", [], R("41.510")), ("dp_hearing", [], R("41.511")), ("stay_put", [], R("41.518")),
    ("uhy", [], R("41.519(6)")), ("case_by_case", [], R("41.530(1)")), ("iaes", [], R("41.530(2)")),
    ("mdr", [], R("41.530(5)")), ("fba", [], R("41.530(6)")), ("bip", [], R("41.530(6)")),
    ("special_circ", [], R("41.530(7)")), ("code_conduct", [], R("41.530(1)")), ("controlled", [], R("41.530(9)")),
    ("illegal_drug", [], R("41.530(9)")), ("sbi", [], R("41.530(9)")), ("weapon", [], R("41.530(9)")),
    ("exp_hearing", [], R("41.532(3)")), ("basis_know", [], R("41.534(2)")), ("cop", [], R("41.536")),
    ("iss", [], R("41.536(3)")), ("ed_records", [], R("41.611")), ("part_agency", [], R("41.611")),
    ("record_access", [], R("41.614")), ("ferpa", [], R("41.611")), ("cceis", [], R("41.646(3)")),
    ("mediation", [("special education mediation conference", S, IA)], R("41.1002(1)")),
    # Added after the 2026-10-08 audit (existing concepts the rule uses)
    ("adverse", [], R("41.50(1)")), ("adaptive", [], R("41.50(6)")), ("func_perf", [], R("41.303(1)")),
    ("srbi", [], R("41.307(1)")), ("vr_services", [], R("41.34(3)")), ("service_coord", [], R("41.321(6)")),
    ("postsec_ed", [], R("41.43(1)")),
    # Procedural Safeguards Manual
    ("safeguards_notice", [("Procedural Safeguards Manual", S, IA)], PS(7)),
    ("pti", [], PS(8)), ("ferpa", [], PS(10)), ("consent", [], PS(14)), ("ward", [], PS(14)),
    ("revoke", [], PS(15)), ("s504", [], PS(15)), ("equitable", [], PS(16)), ("iee", [], PS(18)),
    ("dp_hearing", [], PS(18)), ("pwn", [], PS(19)), ("mediation", [], PS(20)), ("dp_complaint", [], PS(21)),
    ("cprc", [], PS(21)), ("resolution", [], PS(23)),
    ("state_panel", [("Iowa Special Education Advisory Panel", S, IA)], PS(25)),
    ("state_complaint", [], PS(26)), ("adr", [], PS(26)), ("cop", [], PS(28)), ("iss", [], PS(28)),
    ("mdr", [], PS(28)), ("special_circ", [], PS(29)), ("iaes", [], PS(29)), ("exp_hearing", [], PS(31)),
    ("surrogate", [], PS(33)), ("uhy", [], PS(33)), ("age_majority", [], PS(34)), ("unilateral_pl", [], PS(35)),
    # Special Education Terms and Acronyms
    ("nimas", [("accessible educational materials", S, None), ("AIM", A, IA), ("AEM", A, IA)], G(1)),
    ("age_majority", [], G(1)), ("ada", [], G(1)), ("at_device", [], G(1)), ("adhd", [], G(1)),
    ("autism", [], G(2)),
    ("ed", [("BD", A, IA)], G(2)),
    ("bip", [], G(2)), ("child_find", [], G(2)),
    ("child_outcomes", [("Child Outcome Summary Process", S, IA), ("COS", A, IA)], G(2)),
    ("hi", [], G(2)), ("dd", [], G(3)),
    ("suspected", [("Disability Suspect", S, IA)], G(3)),
    ("child_outcomes", [("ECO", A, IA)], G(3)), ("ecse", [], G(3)),
    ("eval_report", [("Educational Evaluation Report", S, IA), ("EER", A, IA)], G(3)),
    ("ed", [("emotional disorder", S, IA), ("emotional disability", S, IA)], G(4)),
    ("lep", [], G(4)),
    ("esy", [("ESYS", A, IA)], G(4)),
    ("fape", [], G(4)), ("fba", [], G(4)), ("head_start", [], G(4)), ("iee", [], G(4)),
    ("iep", [], G(5)), ("idea", [], G(5)), ("evaluation", [], G(5)), ("id", [], G(5)), ("sld", [], G(5)),
    ("lre", [], G(5)), ("lea", [], G(6)), ("ot", [], G(6)), ("osep", [], G(6)), ("ohi", [], G(6)), ("pt", [], G(6)),
    ("pbis", [], G(6)),
    ("postsecondary", [("postsecondary expectations", S, IA), ("PSE", A, IA)], G(6)),
    ("sop", [("Postsecondary Summary", S, IA), ("PSS", A, IA),
             ("Student Accommodation Request", REL, IA), ("SAR", A, IA)], G(6)),
    ("plaafp", [], G(6)), ("pwn", [], G(6)), ("safeguards_notice", [], G(7)), ("reeval", [], G(7)),
    ("transition", [], G(7)),
    ("special_ed", [("Sp.Ed.", AB, None)], G(7)),
    ("age_majority", [("transfer of rights", S, None)], G(7)),
    ("tbi", [], G(7)), ("vi", [], G(7)),
]

CONCEPTS = [
    # state agencies, offices and organizations
    ("ia_doe", "Iowa Department of Education", "legal_procedural", [("IDE", A, IA), ("IDOE", A, IA)], G(5),
     {**IAJ, "broader": "sea", "note": "The state educational agency; the rule calls it the department."}),
    ("ia_dlr", "Division of Learning and Results", "legal_procedural", [], PS(8),
     {**IAJ, "broader": "ia_doe", "note": "The division of the Iowa Department of Education that houses special education."}),
    ("ia_blss", "Bureau of Learner Strategies and Supports", "legal_procedural", [], PS(8),
     {**IAJ, "broader": "ia_dlr", "note": "The state bureau parents contact about special education."}),
    ("ia_aea", "Area education agency", "legal_procedural",
     [("AEA", A, IA), ("area education agencies", P, IA), ("AEAs", P, IA)], R("41.4, 41.2(1)"),
     {**IAJ, "broader": "esa", "note": "One of Iowa's regional agencies that evaluate children and provide special education support services."}),
    ("ia_boee", "Board of Educational Examiners", "legal_procedural", [], R("41.401"),
     {**IAJ, "note": "Licenses and endorses Iowa special education personnel."}),
    ("ia_iac", "Iowa Administrative Code", "legal_procedural", [("IAC", A, IA)], G(5), IAJ),
    ("ia_rules", "Iowa Administrative Rules of Special Education", "legal_procedural", [], PS(7),
     {**IAJ, "broader": "ia_iac", "note": "Chapter 41 of the education rules in the Iowa Administrative Code."}),
    ("ia_ask", "ASK Resource Center", "legal_procedural", [], PS(8),
     {**IAJ, "broader": "pti", "note": "Iowa's federally funded parent training and information center."}),
    ("ia_dri", "Disability Rights Iowa", "legal_procedural", [("DRI", A, IA)], PS(8),
     {**IAJ, "note": "Iowa's federally funded protection and advocacy organization for people with disabilities."}),
    ("ia_fep", "Family & Educator Partnership", "legal_procedural",
     [("FEP", A, IA)], PS(7),
     {**IAJ, "note": "An Area Education Agency program that builds partnerships between families and educators."}),
    ("ia_i3", "Iowa IDEA Information", "legal_procedural", [("i3", A, IA)], G(5),
     {**IAJ, "note": "An online platform for Iowa's early intervention and special education procedures and guidance."}),
    ("ia_ivrs", "Iowa Vocational Rehabilitation Services", "transition", [("IVRS", A, IA)], G(5),
     {**IAJ, "broader": "vr_services"}),
    ("ia_tap", "Transition Alliance Program", "transition", [("TAP", A, IA)], G(7),
     {**IAJ, "note": "A partnership between a school district and Iowa Vocational Rehabilitation Services for students in transition."}),
    ("ia_dhs", "Department of Human Services", "legal_procedural",
     [("DHS", A, IA)], G(2),
     {**IAJ, "note": "Iowa's agency for public assistance programs, as named on the 2021 terms sheet; it later merged into the Iowa Department of Health and Human Services."}),
    ("ia_hhs", "Iowa Department of Health and Human Services", "legal_procedural", [], R("41.329(1)"),
     {**IAJ, "note": "The state agency the rule names as running the early hearing detection and intervention program."}),
    ("ia_idph", "Iowa Department of Public Health", "legal_procedural", [("IDPH", A, IA)], G(5), IAJ),
    ("ia_chsc", "Child Health Specialty Clinics", "health_condition", [("CHSC", A, IA)], G(2),
     {**IAJ, "note": "A public health agency serving Iowa children and youth with special health care needs."}),
    ("ia_dcch", "Division of Child and Community Health", "health_condition", [("DCCH", A, IA)], G(3),
     {**IAJ, "note": "A University of Iowa medical college division focused on child health."}),
    ("ia_isd", "Iowa School for the Deaf", "placement_setting", [], R("41.329"), IAJ),
    # state programs
    ("ia_early_access", "Iowa Early ACCESS", "early_intervention", [("Early ACCESS", A, IA), ("EA", A, IA)], G(3),
     {**IAJ, "note": "Iowa's Part C early intervention system for infants and toddlers, birth to age 3. The documents call it Early ACCESS; the preferred term adds Iowa to keep it apart from Colorado's Early Access, and the program name is recorded as an acronym-type string only so that it matches case-sensitively."}),
    ("ia_eci", "Early Childhood Iowa", "early_intervention", [("ECI", A, IA)], G(3),
     {**IAJ, "note": "State-supported programs for children ages 0-5 and their families."}),
    ("ia_swvpp", "Statewide Voluntary Preschool Program", "early_intervention",
     [("Statewide Voluntary Preschool Programs", P, IA), ("SWVPP", A, IA)], G(7),
     {**IAJ, "note": "Iowa's preschool program for four-year-olds, with or without disabilities."}),
    ("ia_fsmp", "Family support mentoring program", "early_intervention", [], R("41.329"),
     {**IAJ, "note": "Pairs families of deaf or hard-of-hearing children with parent or deaf adult mentors."}),
    # eligibility and identification (rule)
    ("ia_eligible_individual", "Eligible individual", "evaluation_eligibility",
     [("eligible individuals", P, IA)], R("41.8, 41.50"),
     {**IAJ, "broader": "cwd", "note": "Iowa's term for a child found eligible for special education."}),
    ("ia_dioe", "Disability in obtaining an education", "evaluation_eligibility", [], R("41.8"),
     {**IAJ, "note": "Iowa's term for a condition that causes a child to need special education."}),
    ("ia_spm", "Systematic progress monitoring", "evaluation_eligibility", [], R("41.51(15)"),
     {**IAJ, "note": "Collecting and displaying a student's performance over time to make educational decisions."}),
    ("ia_trial_placement", "Trial placement", "placement_setting", [], R("41.116(7)"),
     {**IAJ, "note": "Up to 45 school days in general education, written into the IEP, before leaving a special education service."}),
    ("ia_classroom_clearance", "Classroom clearance", "discipline", [("clearing classrooms", S, IA)], R("41.320(7)"),
     {**IAJ, "note": "Removing all other students from a classroom to calm one student; an IEP may not provide for it."}),
    ("ia_accredited_np", "Accredited nonpublic school", "placement_setting",
     [("accredited nonpublic schools", P, IA)], R("41.413"),
     {**IAJ, "note": "A private school accredited by the state; Iowa law requires special education for its students."}),
    # service model (rule)
    ("ia_instr_svc", "Special education instructional services", "placement_setting", [], R("41.408(1)"),
     {**IAJ, "note": "Specially designed instruction from special education teachers, usually provided by the school district."}),
    ("ia_delivery_system", "Delivery system for instructional services", "placement_setting", [], R("41.408(1)"),
     {**IAJ, "note": "A district's written, board-adopted plan for organizing special education instruction."}),
    ("ia_support_svc", "Special education support services", "related_service",
     [("support services", S, IA)], R("41.409"),
     {**IAJ, "flags": ["common_english_word"],
      "note": "Consultant, strategist, therapy, psychology, social work, nursing and speech services, usually from the AEA."}),
    ("multicat", "Multicategorical", "placement_setting", [], R("41.51(11)"),
     {"note": "Special education serving students with different types of disabilities together."}),
    # personnel (rule)
    ("ia_asst_director", "Assistant director of special education", "personnel_role", [], R("41.402(3)"),
     {**IAJ, "broader": "sped_admin"}),
    ("ia_sped_consultant", "Special education consultant", "personnel_role", [], R("41.409"),
     {**IAJ, "note": "An AEA instructional specialist who supports teachers serving eligible individuals."}),
    ("ia_ed_strategist", "Educational strategist", "personnel_role", [], R("41.402(3)"),
     {**IAJ, "note": "Helps general education teachers develop strategies for students who can be served in the regular classroom."}),
    ("ia_media_specialist", "Special education media specialist", "personnel_role", [], R("41.402(3)"), IAJ),
    ("ia_sped_nurse", "Special education nurse", "personnel_role", [], R("41.402(3)"),
     {**IAJ, "note": "A registered nurse who assesses eligible individuals' health needs and relates them to education."}),
    ("ia_wec", "Work experience coordinator", "personnel_role", [], R("41.402(3)"),
     {**IAJ, "note": "Plans secondary work experience programs for students needing specially designed vocational preparation."}),
    ("ia_psych_asst", "Psychology assistant", "personnel_role", [], R("41.403(2)"),
     {**IAJ, "broader": "para", "note": "A paraprofessional who works under a school psychologist."}),
    ("ia_vision_asst", "Vision assistant", "personnel_role", [], R("41.403(2)"),
     {**IAJ, "broader": "para", "note": "A paraprofessional who prepares materials for students who are blind or visually impaired."}),
    # national concepts first attested by Iowa's documents
    ("audiologist", "Audiologist", "personnel_role", [], R("41.402(3)"), {"broader": "audiology"}),
    ("occ_therapist", "Occupational therapist", "personnel_role", [], R("41.402(3)"), {"broader": "ot"}),
    ("phys_therapist", "Physical therapist", "personnel_role", [], R("41.402(3)"), {"broader": "pt"}),
    ("speech_path", "Speech-language pathologist", "personnel_role",
     [("speech language pathologist", V, None), ("SLP", A, None)], G(7), {"broader": "slp"}),
    ("audiometrist", "Audiometrist", "personnel_role", [], R("41.403(2)"),
     {"note": "Gives hearing screenings under an audiologist."}),
    ("ot_assistant", "Occupational therapy assistant", "personnel_role", [], R("41.403(2)"), {"broader": "occ_therapist"}),
    ("pt_assistant", "Physical therapist assistant", "personnel_role", [], R("41.403(2)"), {"broader": "phys_therapist"}),
    ("slp_assistant", "Speech-language pathology assistant", "personnel_role", [], R("41.403(2)"), {"broader": "speech_path"}),
    ("ehdi", "Early hearing detection and intervention program", "early_intervention", [], R("41.329(1)"),
     {"note": "A public health program that identifies hearing loss in newborns and infants."}),
    ("cil", "Center for independent living", "transition",
     [("Centers for Independent Living", P, None), ("CIL", A, None), ("CILs", P, None)], PS(9),
     {"note": "A community organization providing independent living supports to people with disabilities."}),
    ("aac", "Augmentative and alternative communication", "accommodation_modification", [("AAC", A, None)], G(1),
     {"broader": "at_device", "note": "Ways of communicating other than speech, such as sign, pictures or speech-generating devices."}),
    ("cyshcn", "Children and youth with special health care needs", "health_condition", [("CYSHCN", A, None)], G(2), {}),
    ("ihp", "Individual health plan", "iep_component", [("IHP", A, None)], G(5),
     {"note": "A plan for meeting a student's health needs at school."}),
    ("dyscalculia", "Dyscalculia", "health_condition", [], G(5), {"broader": "sld"}),
    # dispute resolution model forms (safeguards manual)
    ("ia_med_form", "Model Form: Request for Mediation", "legal_procedural", [], PS(45), {**IAJ, "broader": "mediation"}),
    ("ia_dp_form", "Model Form: Due Process Complaint (Request for Due Process Hearing)", "legal_procedural", [], PS(47),
     {**IAJ, "broader": "dp_complaint"}),
    ("ia_sc_form", "Model Form: IDEA State Complaint", "legal_procedural", [], PS(49), {**IAJ, "broader": "state_complaint"}),
]

JURISDICTION = "US-IA"
LAYER_NAME = "Iowa"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.41.0"
