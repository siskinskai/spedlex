"""
Virginia layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN   VDOE, Your Family's Special Education Rights: Virginia Procedural
        Safeguards Notice. Read from the Regulatory Town Hall copy (revision
        dated September 2013); VDOE now posts a September 2024 edition whose
        PDF could not be read here.
  FG    VDOE, Virginia Family's Guide to Special Education, May 2023
  VAC   8VAC20-81-10, definitions in the Regulations Governing Special
        Education Programs for Children with Disabilities in Virginia
  VAAP  VDOE, Virginia Alternate Assessment Program FAQ for parents
  GRAD  Fairfax County Public Schools, Special Education Graduation
        Requirements / Diploma Credit Accommodations (Nov. 2023): a local
        summary of state rules, used because VDOE's Applied Studies Diploma
        and SPLAVC fact sheets returned access errors
  SPL   VDOE SPLAVC fact sheet (Aug. 2024), title and scope only, via the
        Formed Families Forward resource listing

PSN, FG, VAAP, GRAD and SPL references come from text extraction and are
'candidate'. VAC records come from the regulation's list of defined terms
and are 'machine_validated'.
"""

PSN_URL = "https://www.townhall.virginia.gov/L/GetFile.cfm?File=C:\\TownHall\\docroot\\GuidanceDocs\\201\\GDoc_DOE_866_v4.pdf"
FG_URL = "https://www.doe.virginia.gov/programs-services/special-education/information-for-families/virginia-family-s-guide-to-special-education"
VAC_URL = "https://law.lis.virginia.gov/admincode/title8/agency20/chapter81/section10/"
VAAP_URL = "https://www.doe.virginia.gov/home/showpublisheddocument/3232/637982610954100000"
GRAD_URL = "https://www.fcps.edu/sites/default/files/media/forms/SpecialEducationGraduationRequirementsEnglish.pdf"
SPL_URL = "https://formedfamiliesforward.org/family_resource/locally-awarded-verified-credit-accommodation-vdoe-fact-sheet/"
FAM_URL = "https://www.doe.virginia.gov/programs-services/special-education/information-for-families"


def src(doc, loc=""):
    stype, title, url = {
        "PSN": ("procedural_safeguards_notice", "VDOE Virginia Procedural Safeguards Notice (Town Hall copy, rev. Sept. 2013)", PSN_URL),
        "FG": ("state_guidance", "VDOE Virginia Family's Guide to Special Education (May 2023)", FG_URL),
        "VAC": ("state_regulation", "8VAC20-81-10", VAC_URL),
        "VAAP": ("state_guidance", "VDOE VAAP FAQ for Parents", VAAP_URL),
        "GRAD": ("secondary_guidance", "Fairfax County Public Schools, Special Education Graduation Requirements (Nov. 2023)", GRAD_URL),
        "SPL": ("state_guidance", "VDOE SPLAVC fact sheet (Aug. 2024)", SPL_URL),
        "FAM": ("state_guidance", "VDOE Special Education for Families page", FAM_URL),
    }[doc]
    if doc == "VAC":
        cit = f"{title}, '{loc}'" if loc else title
    else:
        cit = f"{title}, {loc}" if loc else title
    return {"source_type": stype, "citation": cit, "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
VA = ["US-VA"]
VAJ = {"jurisdiction": "US-VA"}
REG = {"status": "machine_validated"}

STRINGS = [
    # Definitions in 8VAC20-81-10
    ("autism", [], src("VAC", "Autism")),
    ("deafblind", [], src("VAC", "Deaf-blindness")),
    ("deafness", [], src("VAC", "Deafness")),
    ("hi", [], src("VAC", "Hearing impairment")),
    ("ed", [("emotional disability", S, VA)], src("VAC", "Emotional disability")),
    ("id", [("mental retardation", L, VA)], src("VAC", "Mental retardation")),
    ("md", [], src("VAC", "Multiple disabilities")),
    ("oi", [], src("VAC", "Orthopedic impairment")),
    ("ohi", [], src("VAC", "Other health impairment")),
    ("sld", [], src("VAC", "Specific learning disability")),
    ("sli", [], src("VAC", "Speech or language impairment")),
    ("tbi", [], src("VAC", "Traumatic brain injury")),
    ("vi", [], src("VAC", "Visual impairment including blindness")),
    ("dd", [], src("VAC", "Developmental delay")),
    ("iep_team", [], src("VAC", "Individualized education program team")),
    ("lea", [("school division", S, VA), ("school divisions", P, VA)], src("FG", "throughout")),
    ("eligibility", [("eligibility group", S, VA), ("eligibility determination meeting", S, None)], src("FG", "p. 17")),
    ("sst", [("teacher assistance team", S, None), ("instructional support team", S, None), ("school-based team", S, VA), ("child study team", S, None), ("child study", AB, VA)], src("FG", "p. 12")),
    ("reeval", [("triennial reevaluation", S, None)], src("FG", "p. 32")),
    ("reed", [("existing data review", S, VA)], src("FG", "p. 14")),
    ("screening", [], src("VAC", "Screening")),
    ("mdr", [], src("VAC", "Manifestation determination review")),
    ("cop", [], src("VAC", "Change in placement")),
    ("fba", [], src("VAC", "Functional behavioral assessment")),
    ("bip", [], src("VAC", "Behavioral intervention plan")),
    ("iaes", [], src("FG", "p. 36")),
    ("home_instr", [], src("VAC", "Home instruction")),
    ("regular_class", [("general education classes", S, None)], src("FG", "p. 30")),
    ("special_class", [("special education classes", S, None)], src("FG", "p. 30")),
    ("special_school", [("special education schools", S, None)], src("FG", "p. 30")),
    ("resource_room", [], src("FG", "p. 30")),
    ("itinerant", [], src("FG", "p. 30")),
    ("residential", [("private residential placement", S, None)], src("FG", "p. 28")),
    ("esy", [], src("VAC", "Extended school year services")),
    ("at_device", [], src("VAC", "Assistive technology device")),
    ("sdi", [], src("VAC", "Specially designed instruction")),
    ("transition", [("secondary transition services", S, None)], src("FG", "p. 24")),
    ("postsecondary", [("post-secondary goals", V, None)], src("FG", "p. 24")),
    ("sop", [], src("FG", "p. 24")),
    ("comm_exp", [], src("FG", "p. 24")),
    ("sig_cog", [("students with significant cognitive disabilities", S, None)], src("VAAP")),
    ("iep_facil", [], src("FG", "p. 44")),
    ("dp_hearing", [("special education hearing officer", S, VA), ("impartial special education hearing officer", S, VA)], src("VAC", "Special education hearing officer")),
    ("consent", [("informed parental consent", S, None)], src("VAC", "Informed parental consent")),
    ("surrogate", [("temporary surrogate", S, None)], src("FG", "p. 10")),
    ("uhy", [], src("FG", "p. 10")),
    ("age_majority", [("educational rights transfer", S, None), ("rights at age of majority", S, None)], src("FG", "pp. 10, 29")),
    ("foster", [], src("FG", "p. 10")),
    ("s504", [], src("VAC", "Section 504")),
    ("voc_ed", [], src("VAC", "Career and technical education")),
    ("mdt", [], src("VAC", "Multidisciplinary team")),
    ("pe", [], src("VAC", "Physical education")),
    ("itd", [("infant and toddler with a disability", V, None)], src("VAC", "Infant and toddler with a disability")),
    ("part_c_transition", [("transition from Part C services", S, None)], src("VAC", "Transition from Part C services")),
    ("eoc", [("end of course test", V, None)], src("FG", "p. 27")),
    ("std_diploma", [], src("FG", "p. 27")),
    ("state_panel", [("State Special Education Advisory Committee", S, VA), ("SSEAC", A, VA)], src("PSN", "p. 28")),
    ("ifsp", [], src("VAC", "Individualized family service plan")),
    ("nimas", [], src("VAC", "National Instructional Materials Accessibility Standard")),
]

CONCEPTS = [
    # --- Agencies, offices, regulation ---
    ("vdoe", "Virginia Department of Education", "legal_procedural", [("VDOE", A, VA)], src("PSN", "cover"), {**VAJ, "broader": "sea"}),
    ("va_regs", "Regulations Governing Special Education Programs for Children with Disabilities in Virginia", "legal_procedural",
     [("Virginia Regulations", AB, VA), ("8VAC20-81", A, VA), ("Virginia Administrative Code", S, VA)], src("FG", "p. 7"), VAJ),
    ("va_odr", "Office of Dispute Resolution and Administrative Services", "legal_procedural", [], src("PSN", "p. i"), {**VAJ, "broader": "vdoe"}),
    ("ombud", "Parent Ombudsman for Special Education", "legal_procedural", [("Parent Ombudsman", AB, VA)], src("FG", "p. 43"), {**VAJ, "broader": "vdoe"}),
    ("peatc", "Parent Educational Advocacy Training Center", "legal_procedural", [("PEATC", A, VA)], src("PSN", "p. 1"), {**VAJ, "broader": "pti"}),
    ("seac", "Local special education advisory committee", "legal_procedural", [("SEAC", A, None), ("special education advisory committee", AB, None)], src("FAM", "Guide for Local Special Education Advisory Committees (2020)"),
     {"note": "Virginia requires one in each school division; the term is used nationally."}),
    ("csa", "Children's Services Act", "legal_procedural", [("CSA", A, VA)], src("VAC", "Children's Services Act"), {**VAJ, **REG}),
    ("cpmt", "Community policy and management team", "personnel_role", [("CPMT", A, VA)], src("VAC", "Community policy and management team"), {**VAJ, **REG, "broader": "csa"}),
    ("fapt", "Family assessment and planning team", "personnel_role", [("family assessment or planning team", V, VA), ("FAPT", A, VA)], src("VAC", "Family assessment or planning team"),
     {**VAJ, **REG, "broader": "csa", "note": "'FAPT' is practitioner usage, not from the regulation."}),
    ("vsdb", "Virginia School for the Deaf and the Blind", "placement_setting", [("Virginia School for the Deaf and the Blind at Staunton", S, VA), ("VSDB", A, VA)],
     src("VAC", "Virginia School for the Deaf and the Blind at Staunton"), {**VAJ, **REG, "flags": ["place_name"],
     "note": "'Staunton' is a city and a surname, so it is protected only inside the full name."}),
    ("state_ops", "State-operated programs", "placement_setting", [("state facilities", S, VA)], src("VAC", "State-operated programs"), {**REG}),

    # --- Placement and services ---
    ("level1", "Level I services", "placement_setting", [("Level I", AB, VA)], src("VAC", "Level I services"),
     {**VAJ, **REG, "note": "Virginia caseload term for services delivered less than half the school day Threshold paraphrased from prior knowledge; confirm in the regulation text."}),
    ("level2", "Level II services", "placement_setting", [("Level II", AB, VA)], src("VAC", "Level II services"),
     {**VAJ, **REG, "note": "Virginia caseload term for services delivered half the school day or more Threshold paraphrased from prior knowledge; confirm in the regulation text."}),
    ("coteach", "Co-teaching", "placement_setting", [("coteaching", V, None), ("co-taught class", S, None)], src("VAC", "Coteaching"), REG),
    ("isd", "Integrated service delivery", "placement_setting", [], src("FG", "p. 30"), {}),
    ("home_based", "Home-based instruction", "placement_setting", [], src("VAC", "Home-based instruction"),
     {**VAJ, **REG, "broader": "continuum", "note": "Virginia separates home-based instruction (an IEP placement), homebound instruction (for a medical confinement), and home instruction or home tutoring (parent-chosen alternatives to school)."}),
    ("home_tutor", "Home tutoring", "placement_setting", [], src("VAC", "Home tutoring"), {**VAJ, **REG}),
    ("long_term_pl", "Long-term placement", "placement_setting", [], src("VAC", "Long-term placement"), {**VAJ, **REG}),
    ("init_place", "Initial placement", "placement_setting", [], src("VAC", "Initial placement"), REG),
    ("change_ident", "Change in identification", "evaluation_eligibility", [], src("VAC", "Change in identification"), REG),
    ("comparable", "Comparable services", "iep_component", [], src("FG", "p. 22"), {"note": "Federal term for services to transfer students (34 CFR 300.323(e))."}),
    ("nimac", "National Instructional Materials Access Center", "accommodation_modification", [("NIMAC", A, None)], src("VAC", "National Instructional Materials Access Center"), {**REG, "broader": "nimas"}),
    ("implant", "Surgically implanted medical device", "accommodation_modification", [("cochlear implant", S, None), ("cochlear implants", P, None)], src("FG", "pp. 19-20, 28"),
     {"note": "Federal term (34 CFR 300.34(b), 300.113)."}),

    # --- People ---
    ("sped_admin", "Special education administrator", "personnel_role", [("director of special education", S, None)], src("FG", "p. 12"), {}),
    ("para", "Paraprofessional", "personnel_role", [("paraeducator", S, None), ("paraprofessionals", P, None)], src("VAC", "Paraprofessional"),
     {**REG, "note": "'Paraeducator' is practitioner usage."}),
    ("hqt", "Highly qualified special education teacher", "personnel_role", [("highly qualified", AB, None)], src("VAC", "Highly qualified special education teacher"),
     {**REG, "note": "No Child Left Behind term still defined in the Virginia regulation."}),
    ("service_coord", "Service coordinator", "early_intervention", [], src("FG", "p. 21"), {"broader": "ifsp"}),

    # --- Discipline and rights ---
    ("st_removal", "Short-term removal", "discipline", [("short-term removals", P, None)], src("FG", "p. 34"), {}),
    ("lt_removal", "Long-term removal", "discipline", [("long-term removals", P, None)], src("FG", "p. 35"), {}),
    ("dis_harass", "Disability harassment", "legal_procedural", [], src("FG", "p. 27"), {}),
    ("audio_rec", "Audio recording of meetings", "legal_procedural", [("audio recording devices at meetings", S, VA), ("video recording of meetings", S, VA)], src("FG", "pp. 39-40"),
     {"note": "Some states, including Virginia and California, give parents a right to audio record IEP meetings."}),
    ("emancipated", "Emancipated minor", "legal_procedural", [], src("FG", "p. 10"), {}),

    # --- Assessment ---
    ("sol", "Standards of Learning", "iep_component", [("SOL", A, VA), ("SOL test", S, VA), ("SOLs", P, VA), ("Virginia Standards of Learning", S, VA)], src("FG", "p. 25"), VAJ),
    ("vaap", "Virginia Alternate Assessment Program", "iep_component", [("VAAP", A, VA)], src("FG", "p. 25"), {**VAJ, "broader": "alt_assess"}),
    ("vesol", "Virginia Essentialized Standards of Learning", "academic_skill", [("VESOL", A, VA), ("Essentialized Standards of Learning", S, VA)], src("FG", "p. 25"),
     {**VAJ, "broader": "sol", "note": "Reduced-complexity standards behind VAAP; compare Texas essence statements."}),
    ("trans_assess", "Age-appropriate transition assessments", "transition", [("transition assessments", AB, None)], src("FG", "p. 24"), {"note": "Federal term (34 CFR 300.320(b)(1))."}),
    ("interagency", "Interagency responsibilities and linkages", "transition", [("interagency linkages", AB, None)], src("FG", "p. 24"), {}),

    # --- Diplomas and credits ---
    ("adv_studies", "Advanced Studies Diploma", "transition", [], src("FG", "p. 27"), VAJ),
    ("applied_studies", "Applied Studies Diploma", "transition", [], src("FG", "p. 27"),
     {**VAJ, "note": "Earned by completing IEP requirements; compare Nevada's adjusted diploma."}),
    ("mod_std", "Modified Standard Diploma", "transition", [("Modified Diploma", AB, VA)], src("PSN", "p. 7"),
     {**VAJ, "note": "Discontinued Virginia diploma that still appears in older records."}),
    ("cert_completion", "Certificate of Program Completion", "transition", [], src("FG", "p. 27"),
     {"note": "A non-diploma credential for completing a program. General concept: Maryland issues one by the same name."}),
    ("ged", "General Educational Development certificate", "transition", [("GED", A, None)], src("FG", "p. 27"), {}),
    ("std_credit", "Standard credit", "transition", [("standard credits", P, VA)], src("GRAD"), VAJ),
    ("ver_credit", "Verified credit", "transition", [("verified credits", P, VA)], src("FG", "p. 27"), VAJ),
    ("lavc", "Locally awarded verified credit", "transition", [("LAVC", A, VA), ("locally awarded verified credits", P, VA)], src("FG", "p. 27"), {**VAJ, "broader": "ver_credit"}),
    ("splavc", "Special Permission Locally Awarded Verified Credit", "accommodation_modification", [("SPLAVC", A, VA), ("SPLAVC-A", A, VA)], src("SPL"),
     {**VAJ, "broader": "lavc"}),
    ("credit_accom", "Credit accommodations", "accommodation_modification", [("diploma credit accommodations", S, VA)], src("GRAD"), VAJ),
    ("subst_tests", "Substitute tests", "iep_component", [("substitute test", P, VA)], src("FG", "p. 27"), VAJ),
    ("exp_retake", "Expedited retake", "iep_component", [("expanded expedited retake", S, VA)], src("GRAD"), VAJ),
]

JURISDICTION = "US-VA"
LAYER_NAME = "Virginia"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.5.0"
