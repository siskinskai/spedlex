"""
Maine layer for SPEDLex.

Sources reviewed 2026-10-09 (listed in sources/documents.tsv; local copies in .sources-cache/me/):
  RULE   05-071 Chapter 101, Maine Unified Special Education Regulation, Birth to
         Age Twenty-Two (MUSER), Maine Department of Education, "Effective Date:
         July 26, 2024", as posted on 8.21.2024 (263 pp.). Cited by section and
         by the page number printed in the rule's page header, e.g.
         "Section II(21), p. 7". Appendix 1 of the rule is the Notice of
         Procedural Safeguards; it is cited as "Appendix 1" and typed as part of
         the rule.
  EMERG  The same chapter as a 6.12.2026 "FILED Chapter 101 Emergency Changes
         Clean Copy" (264 pp.). It was compared with RULE sentence by sentence.
         The differences are the highly-qualified-teacher table, a new Section
         XVI(1-A) on private schools as parties in disputes, margin-comment
         removal and a November 14, 2024 history entry. It adds or removes no
         term recorded here, so nothing is cited to it. It is recorded in
         sources/documents.tsv only. Whether those changes are in effect was not
         checked.

Documents not provided or not read: Maine's English Procedural Safeguards
Notice (7.26.2024), the Procedural Manual (7.1.2024) and the Maine special
education glossary were not downloaded, so Maine has no safeguards-notice or
parent-guide records in this layer. Chapter 115 (educator certification), the
Child Development Services pages and any alternate-assessment or diploma page
were not provided. The RULE was read by text extraction (pdftotext -layout);
the large finance tables in Section XVIII (state subsidy and tuition formulas)
were scanned for named programs and offices, not read line by line.

Records from the rule text are 'machine_validated'.
"""

RULE_URL = "https://www.maine.gov/doe/sites/maine.gov.doe/files/inline-files/Special%20Services%20-%20MUSER%20-%208.21.2024.pdf"


def src(doc, loc=""):
    """RULE loc is 'Section II(21), p. 7' (section, then the printed page number)."""
    return {"source_type": "state_regulation",
            "citation": f"05-071 Chapter 101, Maine Unified Special Education Regulation (eff. July 26, 2024; posted 8.21.2024), {loc}",
            "doc_id": "me-muser-2024", "url": RULE_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
ME = ["US-ME"]                    # regional tag for strings only used in Maine
MEJ = {"jurisdiction": "US-ME"}   # opts for concepts that only exist in Maine

R = lambda sec, page: src("RULE", f"{sec}, p. {page}")

STRINGS = [
    ("nh_sau", [("SAU", A, None), ("SAUs", P, None), ("school administrative units", P, None)], R("Section I", 1)),
    ("wy_ieu", [("IEU", A, ME), ("State Intermediate Educational Unit", S, ME)], R("Section II(21)", 7)),
    ("co_abbrev_day", [], R("Section II(1)", 3)),
    ("test_accom", [], R("Section II(2)", 3)),
    ("adverse", [], R("Section II(3)", 3)),
    ("consent", [], R("Section II(6)", 4)),
    ("school_day", [], R("Section II(7)", 3)),
    ("ifsp", [], R("Section II(9)", 4)),
    ("evaluation", [], R("Section II(11)", 5)),
    ("fape", [], R("Section II(13)", 5)),
    ("fba", [], R("Section II(14)", 6)),
    ("iep_team", [], R("Section II(14)", 6)),
    ("func_perf", [], R("Section II(15)", 6)),
    ("gen_ed_int", [], R("Section II(16)", 6)),
    ("homeless", [], R("Section II(17)", 6)),
    ("iee", [], R("Section II(18)", 7)),
    ("lea", [], R("Section II(21)", 7)),
    ("program_mods", [], R("Section II(22)", 7)),
    ("native_language", [], R("Section II(24)", 8)),
    ("surrogate", [], R("Section II(25)", 8)),
    ("ppps", [], R("Section II(26)", 8)),
    ("pbis", [("positive reinforcement interventions and supports", S, ME)], R("Section II(27)", 9)),
    ("postsecondary", [], R("Section II(28)", 9)),
    ("public_agency", [], R("Section II(30)", 9)),
    ("screening", [], R("Section II(35)", 10)),
    ("service_coord", [], R("Section II(36)", 10)),
    ("special_ed", [], R("Section II(37)", 11)),
    ("voc_ed", [], R("Section II(37)", 11)),
    ("travel_training", [], R("Section II(37)", 11)),
    ("ward", [("state ward", S, ME)], R("Section II(41)", 12)),
    ("lep", [], R("Section II(24)", 8)),
    ("sea", [], R("Section I", 1)),
    ("idea", [], R("Section I", 1)),
    ("s504", [], R("Section I(2)", 2)),
    ("ada", [], R("Section I(2)", 2)),
    ("ceis", [], R("Section III(3)", 14)),
    ("child_find", [], R("Section IV", 15)),
    ("autism", [], R("Section VII(2)(A)", 75)),
    ("pdd", [("PDDNOS", A, ME)], R("Section VII(2)(A)", 76)),
    ("asperger", [], R("Section VII(2)(A)", 76)),
    ("autistic_dis", [], R("Section VII(2)(A)", 76)),
    ("rett", [], R("Section VII(2)(A)", 76)),
    ("cdd", [], R("Section VII(2)(A)", 76)),
    ("deafblind", [], R("Section VII(2)(B)", 76)),
    ("deafness", [("deafness, including hearing loss", S, None)], R("Section VII(2)(C)", 77)),
    ("tdhh", [("Teacher of the Deaf/Hearing Impaired", S, ME)], R("Section VII(2)(C)", 77)),
    ("dd", [], R("Section VII(2)(D)", 77)),
    ("ed", [], R("Section VII(2)(E)", 79)),
    ("hi", [("hearing loss", S, None)], R("Section VII(2)(F)", 79)),
    ("id", [], R("Section VII(2)(G)", 80)),
    ("md", [], R("Section VII(2)(H)", 80)),
    ("oi", [], R("Section VII(2)(I)", 81)),
    ("ohi", [], R("Section VII(2)(J)", 81)),
    ("adhd", [], R("Section VII(2)(J)", 81)),
    ("tourette", [], R("Section VII(2)(J)", 81)),
    ("epilepsy", [], R("Section VII(2)(J)", 81)),
    ("sickle", [], R("Section VII(2)(J)", 81)),
    ("sli", [], R("Section VII(2)(K)", 83)),
    ("artic", [], R("Section VII(2)(K)", 83)),
    ("voice", [], R("Section VII(2)(K)", 83)),
    ("fluency_dis", [], R("Section VII(2)(K)", 83)),
    ("sld", [], R("Section VII(2)(L)", 84)),
    ("mbd", [], R("Section VII(2)(L)", 84)),
    ("dyslexia", [], R("Section VII(2)(L)", 84)),
    ("aphasia", [], R("Section VII(2)(L)", 84)),
    ("perceptual", [], R("Section VII(2)(L)", 84)),
    ("tbi", [], R("Section VII(2)(M)", 89)),
    ("vi", [], R("Section VII(2)(N)", 90)),
    ("fasd", [], R("Section VII(1)(A)", 72)),
    ("sdi", [], R("Section X(2)(A)(2)", 111)),
    ("consult", [], R("Section X(2)(A)(1)", 111)),
    ("slp", [], R("Section X(2)(A)(3)", 113)),
    ("esy", [], R("Section X(2)(A)(7)", 119)),
    ("hqt", [], R("Section X(2)(A)(6)", 115)),
    ("lre", [], R("Section X(2)(B)", 120)),
    ("continuum", [], R("Section X(2)(B)", 120)),
    ("itinerant", [], R("Section X(2)(B)", 121)),
    ("head_start", [("Headstart", V, None)], R("Section X(2)(C)(1)", 121)),
    ("resource_room", [], R("Section X(2)(C)(2)", 123)),
    ("special_class", [], R("Section X(2)(C)(2)", 123)),
    ("residential", [], R("Section X(2)(C)(2)", 124)),
    ("home_instr", [], R("Section X(2)(C)(2)", 124)),
    ("related", [], R("Section XI", 126)),
    ("audiology", [], R("Section XI", 127)),
    ("om", [], R("Section XI", 130)),
    ("counseling", [], R("Section XI", 127)),
    ("bcba", [("Board Certified Behavior Analyst", V, None)], R("Section XI", 140)),
    ("ecse", [], R("Section XII(1)", 141)),
    ("child_count", [], R("Section VIII", 91)),
    ("mediation", [("stand-alone mediation", S, None)], R("Section XVI(2)", 159)),
    ("state_complaint", [], R("Section XVI(4)", 162)),
    ("dp_hearing", [], R("Section XVI(13)", 175)),
    ("civil_action", [], R("Section XVI(19)", 182)),
    ("stay_put", [], R("Section XVI(20)", 183)),
    ("ferpa", [], R("Section XIV(1)", 152)),
]

CONCEPTS = [
    ("me_muser", "Maine Unified Special Education Regulation", "legal_procedural", [("MUSER", A, ME)], R("Section VI(2)", 62), {**MEJ, "flags": ["place_name"]}),
    ("me_cds", "Child Development Services", "early_intervention", [("CDS", A, ME)], R("Section II(21)", 7), {**MEJ, "broader": "wy_ieu"}),
    ("me_doe", "Maine Department of Education", "legal_procedural", [], R("Section I(3)", 2), {**MEJ, "broader": "sea", "flags": ["place_name"]}),
    ("me_state_agency_client", "State agency client", "legal_procedural", [], R("Section II(40)", 11), {**MEJ}),
    ("me_psp", "Primary service provider", "early_intervention", [("PSP", A, ME)], R("Section X(1)", 107), {**MEJ}),
    ("me_ed_tech", "Educational technician", "personnel_role", [("educational technicians", P, ME), ("Educational Technician III", S, ME)], R("Section X(1)", 109), {**MEJ, "broader": "para"}),
    ("me_tutorial", "Tutorial instruction", "placement_setting", [], R("Section X(2)(A)(4)", 114), {**MEJ}),
    ("me_special_purpose_school", "Special purpose private school", "placement_setting", [], R("Section XII(3)(A)", 147), {**MEJ}),
    ("me_general_purpose_school", "General purpose private school", "placement_setting", [], R("Section XII(3)(A)", 147), {**MEJ}),
    ("me_special_purpose_service", "Special purpose service", "placement_setting", [], R("Section II(39)", 11), {**MEJ}),
    ("me_regional_program", "Regional special education program", "placement_setting", [], R("Section II(32)", 9), {**MEJ}),
    ("me_eut", "Education in the Unorganized Territories", "legal_procedural", [("EUT", A, ME)], R("Section IV(4)(I)", 38), {**MEJ}),
    ("me_mssm", "Maine School of Science and Mathematics", "placement_setting", [("MSSM", A, ME)], R("Section IV(4)(J)", 39), {**MEJ, "flags": ["place_name"]}),
    ("me_nta", "Neurocognitive Testing Assistant", "personnel_role", [("NTA", A, ME), ("NTAs", P, ME), ("Neurocognitive Testing Assistants", P, ME)], R("Section IV(2)", 25), {**MEJ}),
    ("me_psych_board", "Board of Examiners of Psychologists", "legal_procedural", [], R("Section IV(2)", 25), {**MEJ}),
    ("me_mepa", "Maine Psychological Association", "legal_procedural", [("MePA", A, ME)], R("Section XI", 132), {**MEJ, "flags": ["place_name"]}),
    ("me_slp_board", "Maine Board of Speech, Audiology and Hearing", "legal_procedural", [], R("Section X(2)(A)(3)", 113), {**MEJ, "flags": ["place_name"]}),
    ("me_counsel_board", "Maine State Board of Counseling Professionals Licensure", "legal_procedural", [], R("Section XI", 127), {**MEJ, "flags": ["place_name"]}),
    ("me_mpf", "Maine Parent Federation", "legal_procedural", [], R("Appendix 1", 219), {**MEJ, "flags": ["place_name"]}),
    ("me_drc", "Disability Rights Center", "legal_procedural", [], R("Appendix 1", 219), {**MEJ}),
    ("me_smpa", "Southern Maine Parent Awareness", "legal_procedural", [], R("Appendix 1", 219), {**MEJ, "flags": ["place_name"]}),
    ("me_kids_legal", "KIDS LEGAL", "legal_procedural", [], R("Appendix 1", 219), {**MEJ}),
    ("me_due_process_office", "Due Process Office", "legal_procedural", [], R("Section XVI(4)", 162), {**MEJ, "broader": "me_doe"}),
    ("me_due_process_coord", "Due Process Coordinator", "personnel_role", [], R("Section XVI(2)", 159), {**MEJ}),
    ("me_notif_placement", "Notification of Placement for Children with Disabilities", "legal_procedural", [("EF-S-01", AB, ME)], R("Section XII(3)(A)", 147), {**MEJ}),
    ("me_learning_results", "Maine's Learning Results", "academic_skill", [("Learning Results", AB, ME)], R("Section II(4)", 3), {**MEJ, "flags": ["place_name"]}),
    ("housse", "HOUSSE", "legal_procedural", [], R("Section X(2)(A)(6)", 116), {"broader": "hqt"}),
    ("me_atp", "Assistive technology professional", "personnel_role", [("ATP", A, ME)], R("Section XI", 136), {**MEJ}),
    ("me_dhhs", "Maine Department of Health and Human Services", "legal_procedural", [], R("Section VI(2)", 64), {**MEJ, "flags": ["place_name"]}),
    ("me_doc", "Department of Corrections", "legal_procedural", [], R("Section II(40)", 12), {**MEJ}),
    ("me_dol", "Maine Department of Labor", "legal_procedural", [], R("Section VI(2)", 64), {**MEJ, "flags": ["place_name"]}),
    ("me_bvr", "Bureau of Vocational Rehabilitation", "legal_procedural", [], R("Section VI(2)", 64), {**MEJ}),
    ("me_long_creek", "Long Creek Youth Development Center", "placement_setting", [], R("Section II(40)", 12), {**MEJ, "flags": ["place_name"]}),
    ("me_mountain_view", "Mountain View Youth Development Center", "placement_setting", [], R("Section II(40)", 12), {**MEJ, "flags": ["place_name"]}),
    ("me_b2", "Birth to under age three", "early_intervention", [("B-2", AB, ME)], R("Section II(42)", 12), {**MEJ}),
    ("iep_case_manager", "IEP case manager", "personnel_role", [], R("Section II(19)", 7), {}),
    ("informed_clinical_opinion", "Informed clinical opinion", "early_intervention", [], R("Section II(20)", 7), {}),
    ("diagnostic_impression", "Diagnostic impression", "evaluation_eligibility", [], R("Section II(8)", 4), {}),
    ("composite_score", "Composite score", "score_metric", [], R("Section II(5)", 3), {}),
    ("formative_assessment", "Formative assessment", "evaluation_eligibility", [], R("Section II(12)", 5), {}),
    ("sb_interventions", "Scientifically based interventions", "evaluation_eligibility", [("scientifically-based interventions", V, None)], R("Section II(33)", 9), {"broader": "sbr"}),
    ("early_childhood_program", "Early childhood program", "placement_setting", [], R("Section X(2)(C)(1)", 121), {}),
    ("reverse_mainstream", "Reverse mainstream", "placement_setting", [], R("Section X(2)(C)(1)", 121), {}),
    ("asthma", "Asthma", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("diabetes", "Diabetes", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("hemophilia", "Hemophilia", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("lead_poisoning", "Lead poisoning", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("leukemia", "Leukemia", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("nephritis", "Nephritis", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("rheumatic_fever", "Rheumatic fever", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi"}),
    ("heart_condition", "Heart condition", "health_condition", [], R("Section VII(2)(J)", 81), {"broader": "ohi", "flags": ["common_english_word"]}),
    ("cerebral_palsy", "Cerebral palsy", "health_condition", [], R("Section VII(2)(I)", 81), {"broader": "oi"}),
    ("poliomyelitis", "Poliomyelitis", "health_condition", [], R("Section VII(2)(I)", 81), {"broader": "oi"}),
    ("bone_tuberculosis", "Bone tuberculosis", "health_condition", [], R("Section VII(2)(I)", 81), {"broader": "oi"}),
    ("schizophrenia", "Schizophrenia", "health_condition", [], R("Section VII(2)(E)", 79), {"broader": "ed"}),
]

JURISDICTION = "US-ME"
LAYER_NAME = "Maine"
RETRIEVED = "2026-10-09"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.48.0"  # tools/add_state.py sets this

UNCITED_DOCS = {"me-muser-emergency-2026": "Emergency-changes copy of the same chapter; compared with the cited posting, it adds or removes no term, so no record cites it."}
