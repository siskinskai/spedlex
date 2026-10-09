"""
Federal core: 34 CFR Part 300 (IDEA Part B regulations).

Each SEED entry is
    (key, preferred_term, category, citation, [(string, string_type), ...], opts)
where citation looks like "300.34(c)(1)" and the section number builds the
URL. opts may hold: broader (key), note, flags (manual pii reasons),
regional ({string: [jurisdictions]}), xmap ([(system, label, relation)]).

ILLUSTRATIVE entries are placeholders that show the shape of records the
corpus and instrument harvests will produce. They carry status
"illustrative" and are excluded from the matcher by default. A retired
placeholder is replaced by None so its ID is never reused.

Source text was read from the Cornell LII copy of 34 CFR Part 300.
"""

RETRIEVED = "2026-10-03"
VERSION_ADDED = "0.1.0"
ASSISTED_BY = "claude-opus-5-5"
LII = "https://www.law.cornell.edu/cfr/text/34/{}"

A, S, P, V, L, AB = "acronym", "synonym", "plural", "spelling_variant", "legacy", "abbreviation"

SEED = [
    # --- Core legal / procedural (Subpart A definitions, B, E) ---
    ("fape", "Free appropriate public education", "legal_procedural", "300.17", [("FAPE", A)], {}),
    ("iep", "Individualized education program", "legal_procedural", "300.22",
     [("IEP", A), ("IEPs", P), ("individualized education plan", S), ("individual education program", V)], {}),
    ("iep_team", "IEP Team", "legal_procedural", "300.23",
     [("individualized education program team", S), ("IEP committee", S), ("ARD committee", S)],
     {"note": "'ARD committee' (admission, review, and dismissal) is the Texas name; tagged regional.", "regional": {"ARD committee": ["US-TX"]}}),
    ("cwd", "Child with a disability", "legal_procedural", "300.8(a)", [("children with disabilities", P), ("student with a disability", S)], {}),
    ("consent", "Parental consent", "legal_procedural", "300.300", [("informed consent", S)], {}),
    ("evaluation", "Evaluation", "evaluation_eligibility", "300.15", [("initial evaluation", S), ("comprehensive evaluation", S)], {}),
    ("reeval", "Reevaluation", "evaluation_eligibility", "300.303", [("re-evaluation", V), ("triennial evaluation", S), ("triennial", AB)], {}),
    ("excess_costs", "Excess costs", "legal_procedural", "300.16", [], {}),
    ("lep", "Limited English proficient", "legal_procedural", "300.27", [("LEP", A), ("limited English proficiency", S), ("English learner", S)], {}),
    ("lea", "Local educational agency", "legal_procedural", "300.28", [("LEA", A), ("local education agency", V)], {}),
    ("sea", "State educational agency", "legal_procedural", "300.41", [("SEA", A), ("state education agency", V)], {}),
    ("esa", "Educational service agency", "legal_procedural", "300.12", [("ESA", A)], {}),
    ("native_language", "Native language", "legal_procedural", "300.29", [], {}),
    ("pti", "Parent training and information center", "legal_procedural", "300.31", [("PTI", A), ("parent center", S)], {}),
    ("pii", "Personally identifiable information", "legal_procedural", "300.32", [("PII", A), ("personally identifiable", S)], {}),
    ("public_agency", "Public agency", "legal_procedural", "300.33", [], {}),
    ("services_plan", "Services plan", "legal_procedural", "300.37", [("individual services plan", S), ("ISP", A)], {}),
    ("universal_design", "Universal design", "legal_procedural", "300.44", [("universal design for learning", S), ("UDL", A)], {}),
    ("ward", "Ward of the State", "legal_procedural", "300.45", [], {}),
    ("homeless", "Homeless children", "legal_procedural", "300.19", [], {}),
    ("school_day", "School day", "legal_procedural", "300.11(c)", [("school days", P), ("business day", S)], {}),
    ("child_find", "Child find", "legal_procedural", "300.111", [], {}),
    ("feog", "Full educational opportunity goal", "legal_procedural", "300.109", [("FEOG", A)], {}),
    ("esy", "Extended school year services", "legal_procedural", "300.106", [("extended school year", S), ("ESY", A)], {}),
    ("lre", "Least restrictive environment", "legal_procedural", "300.114", [("LRE", A)],
     {"xmap": [("MeSH", "Mainstreaming (Education)", "related")]}),
    ("continuum", "Continuum of alternative placements", "placement_setting", "300.115", [("continuum of placements", S)], {}),
    ("nonacademic", "Nonacademic services", "legal_procedural", "300.107", [("extracurricular services", S)], {}),
    ("nonacademic_settings", "Nonacademic settings", "placement_setting", "300.117", [], {}),
    ("pwn", "Prior written notice", "legal_procedural", "300.503", [("PWN", A), ("prior notice", S)], {}),
    ("safeguards_notice", "Procedural safeguards notice", "legal_procedural", "300.504", [("procedural safeguards", S), ("notice of procedural safeguards", S)], {}),
    ("iee", "Independent educational evaluation", "evaluation_eligibility", "300.502", [("IEE", A), ("independent evaluation", S)], {}),
    ("mediation", "Mediation", "legal_procedural", "300.506", [], {}),
    ("dp_complaint", "Due process complaint", "legal_procedural", "300.507", [("due process complaint notice", S), ("due process", AB)], {}),
    ("resolution", "Resolution meeting", "legal_procedural", "300.510", [("resolution process", S), ("resolution session", S)], {}),
    ("dp_hearing", "Impartial due process hearing", "legal_procedural", "300.511", [("due process hearing", S), ("hearing officer", S)], {}),
    ("state_complaint", "State complaint", "legal_procedural", "300.153", [("state complaint procedures", S)], {}),
    ("stay_put", "Child's status during proceedings", "legal_procedural", "300.518", [("stay-put", S), ("stay put", V), ("pendency", S)],
     {"note": "'Stay-put' is practitioner usage; the regulation's heading is the preferred term."}),
    ("surrogate", "Surrogate parent", "legal_procedural", "300.519", [("surrogate parents", P)], {}),
    ("age_majority", "Transfer of rights at age of majority", "transition", "300.520", [("age of majority", S), ("transfer of parental rights", S)], {}),
    ("ppps", "Parentally-placed private school children with disabilities", "legal_procedural", "300.130", [("parentally placed private school children", V)], {}),
    ("equitable", "Equitable services", "legal_procedural", "300.137", [], {}),
    ("disprop", "Significant disproportionality", "legal_procedural", "300.173", [("overidentification and disproportionality", S), ("disproportionality", AB)], {}),
    ("nimas", "National Instructional Materials Accessibility Standard", "accommodation_modification", "300.172", [("NIMAS", A), ("accessible instructional materials", S)], {}),
    ("at_device", "Assistive technology device", "accommodation_modification", "300.5", [("assistive technology", S), ("AT", A)],
     {"flags": ["common_english_word"], "note": "'AT' is safe only as an all-caps, case-sensitive match."}),
    ("at_service", "Assistive technology service", "accommodation_modification", "300.6", [("assistive technology services", P)], {"broader": "at_device"}),
    ("special_ed", "Special education", "legal_procedural", "300.39", [("SPED", A), ("special ed", AB), ("exceptional student education", S)],
     {"xmap": [("MeSH", "Education, Special", "exact")]}),
    ("sdi", "Specially designed instruction", "legal_procedural", "300.39(b)(3)", [("SDI", A)], {"broader": "special_ed"}),
    ("travel_training", "Travel training", "functional_skill", "300.39(b)(4)", [], {"broader": "special_ed"}),
    ("voc_ed", "Vocational education", "transition", "300.39(b)(5)", [("career and technical education", S), ("CTE", A)], {"broader": "special_ed"}),
    ("pe", "Physical education", "related_service", "300.39(b)(2)", [("adapted physical education", S), ("APE", A), ("specially designed physical education", S)],
     {"broader": "special_ed", "note": "'Adapted physical education' is practitioner usage for specially designed PE (300.108)."}),

    # --- Disability categories, 300.8(b)-(c) ---
    ("autism", "Autism", "disability_category", "300.8(c)(1)", [("autism spectrum disorder", S), ("ASD", A)], {}),
    ("deafblind", "Deaf-blindness", "disability_category", "300.8(c)(2)", [("deafblindness", V), ("deaf-blind", S)], {}),
    ("deafness", "Deafness", "disability_category", "300.8(c)(3)", [("deaf", S)], {}),
    ("ed", "Emotional disturbance", "disability_category", "300.8(c)(4)", [("ED", A), ("emotional disability", S), ("serious emotional disturbance", L), ("EBD", A)],
     {"flags": ["common_first_name"], "note": "'ED' must stay case-sensitive; 'Ed' is a first name."}),
    ("hi", "Hearing impairment", "disability_category", "300.8(c)(5)", [("HI", A), ("hard of hearing", S), ("DHH", A)], {}),
    ("id", "Intellectual disability", "disability_category", "300.8(c)(6)", [("ID", A), ("mental retardation", L)],
     {"note": "'Mental retardation' is the pre-2010 statutory term; kept as legacy so older records are not stripped."}),
    ("md", "Multiple disabilities", "disability_category", "300.8(c)(7)", [("MD", A)], {}),
    ("oi", "Orthopedic impairment", "disability_category", "300.8(c)(8)", [("OI", A)], {}),
    ("ohi", "Other health impairment", "disability_category", "300.8(c)(9)", [("OHI", A)], {}),
    ("sld", "Specific learning disability", "disability_category", "300.8(c)(10)", [("SLD", A), ("learning disability", S), ("LD", A)], {}),
    ("sli", "Speech or language impairment", "disability_category", "300.8(c)(11)", [("speech-language impairment", V), ("SLI", A)], {}),
    ("tbi", "Traumatic brain injury", "disability_category", "300.8(c)(12)", [("TBI", A)], {}),
    ("vi", "Visual impairment including blindness", "disability_category", "300.8(c)(13)", [("visual impairment", S), ("VI", A)], {}),
    ("dd", "Developmental delay", "disability_category", "300.8(b)", [("DD", A)], {}),

    # --- Conditions named inside 300.8 (mostly already in SNOMED/MeSH) ---
    ("adhd", "Attention deficit hyperactivity disorder", "health_condition", "300.8(c)(9)(i)",
     [("ADHD", A), ("attention deficit disorder", S), ("ADD", A)], {"broader": "ohi", "xmap": [("SNOMEDCT", None, "pending")]}),
    ("tourette", "Tourette syndrome", "health_condition", "300.8(c)(9)(i)", [("Tourette's syndrome", V), ("Tourette's", AB)],
     {"broader": "ohi", "flags": ["eponym", "surname"], "xmap": [("SNOMEDCT", None, "pending")]}),
    ("epilepsy", "Epilepsy", "health_condition", "300.8(c)(9)(i)", [("seizure disorder", S)], {"broader": "ohi", "xmap": [("SNOMEDCT", None, "pending")]}),
    ("sickle", "Sickle cell anemia", "health_condition", "300.8(c)(9)(i)", [], {"broader": "ohi", "xmap": [("SNOMEDCT", None, "pending")]}),
    ("dyslexia", "Dyslexia", "health_condition", "300.8(c)(10)(i)", [], {"broader": "sld", "xmap": [("MeSH", "Dyslexia", "exact")]}),
    ("aphasia", "Developmental aphasia", "health_condition", "300.8(c)(10)(i)", [], {"broader": "sld", "xmap": [("SNOMEDCT", None, "pending")]}),
    ("perceptual", "Perceptual disabilities", "health_condition", "300.8(c)(10)(i)", [("perceptual disability", S)], {"broader": "sld"}),
    ("mbd", "Minimal brain dysfunction", "health_condition", "300.8(c)(10)(i)", [], {"broader": "sld"}),
    ("adaptive", "Adaptive behavior", "functional_skill", "300.8(c)(6)", [("adaptive functioning", S), ("adaptive skills", S)], {}),
    ("adverse", "Adversely affects educational performance", "evaluation_eligibility", "300.8(c)(1)(i)", [("educational performance", AB)], {}),

    # --- Related services, 300.34 ---
    ("related", "Related services", "related_service", "300.34(a)", [("related service", P)], {}),
    ("audiology", "Audiology", "related_service", "300.34(c)(1)", [("audiological services", S)], {"broader": "related"}),
    ("counseling", "Counseling services", "related_service", "300.34(c)(2)", [("school counseling", S)], {"broader": "related"}),
    ("early_id", "Early identification and assessment of disabilities in children", "related_service", "300.34(c)(3)", [], {"broader": "related"}),
    ("interpreting", "Interpreting services", "related_service", "300.34(c)(4)", [("oral transliteration", S), ("cued language transliteration", S), ("sign language interpreting", S)], {"broader": "related"}),
    ("cart", "Communication access realtime translation", "accommodation_modification", "300.34(c)(4)(i)", [("CART", A)], {"broader": "interpreting"}),
    ("medical", "Medical services", "related_service", "300.34(c)(5)", [], {"broader": "related"}),
    ("ot", "Occupational therapy", "related_service", "300.34(c)(6)", [("OT", A)], {"broader": "related"}),
    ("om", "Orientation and mobility services", "related_service", "300.34(c)(7)", [("orientation and mobility", S), ("O&M", A), ("long cane", S)], {"broader": "related"}),
    ("parent_training", "Parent counseling and training", "related_service", "300.34(c)(8)", [], {"broader": "related"}),
    ("pt", "Physical therapy", "related_service", "300.34(c)(9)", [("PT", A)], {"broader": "related"}),
    ("psych", "Psychological services", "related_service", "300.34(c)(10)", [("school psychological services", S)], {"broader": "related"}),
    ("recreation", "Recreation", "related_service", "300.34(c)(11)", [("therapeutic recreation", S), ("leisure education", S)], {"broader": "related"}),
    ("rehab", "Rehabilitation counseling services", "related_service", "300.34(c)(12)", [("rehabilitation counseling", S)], {"broader": "related"}),
    ("nursing", "School health services and school nurse services", "related_service", "300.34(c)(13)", [("school health services", S), ("school nurse services", S)], {"broader": "related"}),
    ("social_work", "Social work services in schools", "related_service", "300.34(c)(14)", [("school social work", S), ("social or developmental history", S)], {"broader": "related"}),
    ("slp", "Speech-language pathology services", "related_service", "300.34(c)(15)", [("speech-language therapy", S), ("speech therapy", S), ("language therapy", S)], {"broader": "related"}),
    ("transport", "Transportation", "related_service", "300.34(c)(16)", [("specialized transportation", S)], {"broader": "related"}),

    # --- Placements, 300.104 / 300.115 ---
    ("regular_class", "Regular class", "placement_setting", "300.115(b)(1)", [("regular classes", P), ("general education classroom", S), ("general education setting", S)], {"broader": "continuum"}),
    ("special_class", "Special class", "placement_setting", "300.115(b)(1)", [("special classes", P), ("self-contained classroom", S)], {"broader": "continuum"}),
    ("special_school", "Special school", "placement_setting", "300.115(b)(1)", [("special schools", P)], {"broader": "continuum"}),
    ("home_instr", "Home instruction", "placement_setting", "300.115(b)(1)", [("homebound instruction", S)], {"broader": "continuum"}),
    ("hospital_instr", "Instruction in hospitals and institutions", "placement_setting", "300.115(b)(1)", [("hospital instruction", S)], {"broader": "continuum"}),
    ("resource_room", "Resource room", "placement_setting", "300.115(b)(2)", [], {"broader": "continuum"}),
    ("itinerant", "Itinerant instruction", "placement_setting", "300.115(b)(2)", [("itinerant services", S)], {"broader": "continuum"}),
    ("residential", "Residential placement", "placement_setting", "300.104", [], {"broader": "continuum"}),
    ("nondisabled", "Nondisabled peers", "placement_setting", "300.320(a)(4)(iii)", [("non-disabled peers", V), ("typically developing peers", S)], {}),

    # --- IEP content, 300.320-300.324 ---
    ("plaafp", "Present levels of academic achievement and functional performance", "iep_component", "300.320(a)(1)",
     [("PLAAFP", A), ("present levels of performance", L), ("PLOP", A), ("PLEP", A), ("present levels", AB)], {}),
    ("annual_goals", "Measurable annual goals", "iep_component", "300.320(a)(2)(i)", [("annual goals", S), ("annual goal", P)], {}),
    ("sto", "Benchmarks or short-term objectives", "iep_component", "300.320(a)(2)(ii)", [("short-term objectives", S), ("STOs", A), ("benchmarks", AB)], {}),
    ("progress", "Periodic reports on progress", "iep_component", "300.320(a)(3)(ii)", [("progress reports", S), ("progress monitoring", S)], {}),
    ("saas", "Supplementary aids and services", "iep_component", "300.42", [("supplementary aids", AB), ("supplemental aids and services", V)], {}),
    ("program_mods", "Program modifications or supports for school personnel", "accommodation_modification", "300.320(a)(4)", [("program modifications", S), ("modifications", AB)], {}),
    ("prr", "Peer-reviewed research", "iep_component", "300.320(a)(4)", [], {}),
    ("removal_expl", "Explanation of the extent of nonparticipation", "iep_component", "300.320(a)(5)", [("LRE justification", S)], {}),
    ("test_accom", "Testing accommodations", "accommodation_modification", "300.320(a)(6)(i)", [("assessment accommodations", S), ("accommodations", AB)], {}),
    ("alt_assess", "Alternate assessment", "iep_component", "300.320(a)(6)(ii)", [("alternate academic achievement standards", S), ("AA-AAAS", A)], {}),
    ("fld", "Frequency, location, and duration", "iep_component", "300.320(a)(7)", [("service minutes", S), ("projected date for the beginning of the services", S)], {}),
    ("postsecondary", "Measurable postsecondary goals", "transition", "300.320(b)(1)", [("postsecondary goals", S), ("independent living skills", S)], {}),
    ("transition", "Transition services", "transition", "300.43", [("transition plan", S), ("coordinated set of activities", S)], {}),
    ("course_study", "Courses of study", "transition", "300.320(b)(2)", [("course of study", P)], {"broader": "transition"}),
    ("pbis", "Positive behavioral interventions and supports", "iep_component", "300.324(a)(2)(i)", [("PBIS", A), ("positive behavior supports", S)], {}),
    ("braille", "Instruction in Braille", "accommodation_modification", "300.324(a)(2)(iii)", [("Braille", AB)],
     {"flags": ["eponym", "surname"]}),
    ("comm_mode", "Language and communication mode", "iep_component", "300.324(a)(2)(iv)", [("communication needs", S), ("mode of communication", S)], {}),
    ("annual_review", "Annual review", "iep_component", "300.324(b)", [("annual IEP review", S)], {}),
    ("amendment", "IEP amendment", "iep_component", "300.324(a)(4)", [("amend or modify the IEP", S)], {}),
    ("gen_curr", "General education curriculum", "iep_component", "300.320(a)(1)(i)", [("general curriculum", S)], {}),

    # --- IEP team roles, 300.321 ---
    ("gen_teacher", "Regular education teacher", "personnel_role", "300.321(a)(2)", [("general education teacher", S), ("gen ed teacher", AB)], {}),
    ("sped_teacher", "Special education teacher", "personnel_role", "300.321(a)(3)", [("special education provider", S), ("case manager", S)], {}),
    ("lea_rep", "Representative of the public agency", "personnel_role", "300.321(a)(4)", [("LEA representative", S), ("district representative", S)], {}),
    ("eval_interp", "Individual who can interpret the instructional implications of evaluation results", "personnel_role", "300.321(a)(5)", [], {}),

    # --- Evaluation & SLD identification, 300.302-300.311 ---
    ("screening", "Screening for instructional purposes", "evaluation_eligibility", "300.302", [("universal screening", S)], {}),
    ("eligibility", "Eligibility determination", "evaluation_eligibility", "300.306", [("determination of eligibility", S), ("eligibility meeting", S)], {}),
    ("discrepancy", "Severe discrepancy", "evaluation_eligibility", "300.307(a)(1)", [("ability-achievement discrepancy", S), ("IQ-achievement discrepancy", S)], {}),
    ("rti", "Response to scientific, research-based intervention", "evaluation_eligibility", "300.307(a)(2)",
     [("response to intervention", S), ("RTI", A), ("RtI", A)], {}),
    ("srbi", "Scientific, research-based intervention", "evaluation_eligibility", "300.309(a)(2)(i)", [("research-based intervention", S), ("evidence-based intervention", S)], {}),
    ("psw", "Pattern of strengths and weaknesses", "evaluation_eligibility", "300.309(a)(2)(ii)", [("PSW", A)], {}),
    ("exclusionary", "Exclusionary factors", "evaluation_eligibility", "300.309(a)(3)", [("environmental, cultural, or economic disadvantage", S)], {}),
    ("data_doc", "Data-based documentation of repeated assessments", "evaluation_eligibility", "300.309(b)(2)", [("repeated assessments of achievement at reasonable intervals", S)], {}),
    ("observation", "Classroom observation", "evaluation_eligibility", "300.310", [("observation", AB)], {}),
    ("oral_expr", "Oral expression", "academic_skill", "300.309(a)(1)(i)", [], {"broader": "sld"}),
    ("listen_comp", "Listening comprehension", "academic_skill", "300.309(a)(1)(ii)", [], {"broader": "sld"}),
    ("written_expr", "Written expression", "academic_skill", "300.309(a)(1)(iii)", [], {"broader": "sld"}),
    ("basic_reading", "Basic reading skill", "academic_skill", "300.309(a)(1)(iv)", [("basic reading skills", P)], {"broader": "sld"}),
    ("fluency", "Reading fluency skills", "academic_skill", "300.309(a)(1)(v)", [("reading fluency", S), ("oral reading fluency", S), ("ORF", A)], {"broader": "sld"}),
    ("reading_comp", "Reading comprehension", "academic_skill", "300.309(a)(1)(vi)", [], {"broader": "sld"}),
    ("math_calc", "Mathematics calculation", "academic_skill", "300.309(a)(1)(vii)", [("math calculation", S)], {"broader": "sld"}),
    ("math_ps", "Mathematics problem solving", "academic_skill", "300.309(a)(1)(viii)", [("math problem solving", S), ("math reasoning", S)], {"broader": "sld"}),

    # --- Discipline, 300.530-300.536 ---
    ("cop", "Change of placement", "discipline", "300.536", [("change in placement", V)], {}),
    ("mdr", "Manifestation determination", "discipline", "300.530(e)", [("manifestation determination review", S), ("MDR", A)], {}),
    ("iaes", "Interim alternative educational setting", "discipline", "300.530(b)(1)", [("IAES", A)], {}),
    ("fba", "Functional behavioral assessment", "discipline", "300.530(d)(1)(ii)", [("FBA", A), ("functional behavior assessment", V)], {}),
    ("bip", "Behavioral intervention plan", "discipline", "300.530(f)(1)(ii)", [("BIP", A), ("behavior intervention plan", V), ("behavior plan", S)], {}),
    ("code_conduct", "Code of student conduct", "discipline", "300.530(a)", [("student code of conduct", V)], {}),
    ("special_circ", "Special circumstances", "discipline", "300.530(g)", [], {}),
    ("sbi", "Serious bodily injury", "discipline", "300.530(i)(3)", [], {}),
    ("controlled", "Controlled substance", "discipline", "300.530(i)(1)", [], {}),
    ("illegal_drug", "Illegal drug", "discipline", "300.530(i)(2)", [], {}),
    ("weapon", "Dangerous weapon", "discipline", "300.530(i)(4)", [], {}),

    # --- Early intervention bridge (Part 300 references to Part C) ---
    ("ifsp", "Individualized family service plan", "early_intervention", "300.24", [("IFSP", A)], {}),
    ("itd", "Infant or toddler with a disability", "early_intervention", "300.25", [("infants and toddlers with disabilities", P)], {}),
    ("part_c_transition", "Transition from Part C to preschool programs", "early_intervention", "300.124", [("Part C", AB), ("Part B", AB), ("early intervention services", S)], {}),
]


ILLUSTRATIVE = [
    None,  # was phonological awareness; now attested by the Texas Dyslexia Handbook
    ("exec_fn", "Executive functioning", "functional_skill", [("executive function", S), ("executive functions", P), ("EF", A)], "termhood_cvalue", [], "corpus"),
    ("wisc5", "Wechsler Intelligence Scale for Children, Fifth Edition", "instrument", [("WISC-V", A), ("WISC-5", V)], "instrument_harvest", ["eponym", "surname"], "instrument_catalog"),
    ("wj4ach", "Woodcock-Johnson IV Tests of Achievement", "instrument", [("WJ IV ACH", A), ("WJ-IV", A), ("Woodcock-Johnson", AB)], "instrument_harvest", ["eponym", "surname"], "instrument_catalog"),
    ("ctopp2", "Comprehensive Test of Phonological Processing, Second Edition", "instrument", [("CTOPP-2", A)], "instrument_harvest", [], "instrument_catalog"),
    ("rsn", "Rapid Symbol Naming", "instrument_subtest", [], "instrument_harvest", [], "instrument_catalog"),
    ("brief2", "Behavior Rating Inventory of Executive Function, Second Edition", "instrument", [("BRIEF-2", A), ("BRIEF2", V)], "instrument_harvest", ["common_english_word"], "instrument_catalog"),
    ("vineland3", "Vineland Adaptive Behavior Scales, Third Edition", "instrument", [("Vineland-3", A), ("Vineland", AB)], "instrument_harvest", ["place_name"], "instrument_catalog"),
    ("kabc2", "Kaufman Assessment Battery for Children, Second Edition", "instrument", [("KABC-II", A), ("Kaufman", AB)], "instrument_harvest", ["eponym", "surname"], "instrument_catalog"),
    ("std_score", "Standard score", "score_metric", [("standard scores", P), ("SS", A)], "termhood_cvalue", [], "corpus"),
    ("pct_rank", "Percentile rank", "score_metric", [("percentile", AB), ("PR", A)], "termhood_cvalue", [], "corpus"),
    ("scaled", "Scaled score", "score_metric", [("scaled scores", P)], "termhood_cvalue", [], "corpus"),
    None,  # was extended time; now attested by the Texas Dyslexia Handbook
    ("pref_seat", "Preferential seating", "accommodation_modification", [], "termhood_cvalue", [], "corpus"),
    ("ortongill", "Orton-Gillingham approach", "academic_skill", [("Orton-Gillingham", AB), ("OG", A)], "instrument_harvest", ["eponym", "surname"], "instrument_catalog"),
]
