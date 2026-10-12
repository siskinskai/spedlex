"""
Delaware layer for SPEDLex.

Sources reviewed 2026-10-08:
  RULE922  14 DE Admin. Code 922, Children with Disabilities Subpart A,
           Purposes and Definitions (authenticated PDF from
           regulations.delaware.gov, amendments through 28 DE Reg. 727,
           04/01/25). Cited by section, e.g. "14 DE Admin. Code 922.3.0";
           the definitions in 3.0 are not numbered, so the citation adds
           the defined term.
  RULE925  14 DE Admin. Code 925, Children with Disabilities Subpart D,
           Evaluations, Eligibility Determination, Individualized Education
           Programs (authenticated PDF, amendments through 28 DE Reg. 731,
           04/01/25). Cited by subsection, e.g. "14 DE Admin. Code 925.6.14.1".
  PSN      Delaware Department of Education (DDOE), Exceptional Children
           Resources, "Delaware Procedural Safeguards: Parent and Child Rights
           in Special Education" (July 2026, 46 pp. including the three
           request forms in the appendix). Cited by PDF page; the printed
           page number is PDF page minus 4 from PDF p. 5 on.
  GUIDE    Parent Information Center of Delaware (PIC), "Parents Are the Key:
           A Manual about the Rights and Responsibilities for Parents of
           Children with Special Education Needs in Delaware", second edition
           (2013, 56 pp.), produced with DDOE support and linked from DDOE's
           family pages. Cited by PDF page; the printed page number is PDF
           page minus 4 from PDF p. 5 on. It is a parent center's guide, so
           its records use the secondary_guidance source type. It predates
           the 2021-2025 rule amendments: its category list (Multiple
           Disabilities, Deafness, Emotional Disturbance), its state test
           (DCAS) and its web links are out of date.

All four were read as text: the rule pages as rendered on
regulations.delaware.gov (sections 922.1.0-3.0 and 925.6.0 in full;
925.1.0-5.0 and 7.0-15.0 searched for Delaware terms, not read line by
line) and the two PDFs as text extracted with pdf.js page by page (checked
afterwards with pdftotext). Subparts 923, 924, 926, 927, 928 and 929 were
not read; the PSN covers the procedural safeguards of 926. RULE records for
new concepts are 'machine_validated'; the others are 'candidate'.
Copies of all four documents are listed in sources/documents.tsv; local copies are in .sources-cache/de/. "DOE" (922.3.0) is also a
surname in the census list; the reviewer accepted it as a known all-caps
collision in tests/test_match.py. The acronym "DDOE" appears only in the
PSN and GUIDE, so it is attached to de_doe in delaware_supplement.

Left out on purpose: every person named in the documents (the 2013 state
director, the PIC director, the guide's cited authors) and every address,
phone number and e-mail address; the John G. Townsend Building (named for
a person, and an address, not a term); "ED" as
the GUIDE's acronym for Educational Diagnostician (it already means
emotional disturbance); Autism Delaware and The Arc of Delaware (named only
in the GUIDE's acknowledgments); Delaware Volunteer Legal Services and the
Community Legal Aid Society (general legal aid); the "Conflict Resolution
Program" on its own (a common phrase; SPARC is recorded); the unit funding
system (a funding formula); the parent questionnaire (the PSN calls it only
"a questionnaire"); the progress-report codes M, S and N (single letters);
the GUIDE's NICHCY and TA Alliance entries (national centers that have
closed); the Interagency Release of Information form; and the long
eligibility-criteria wording of each classification.
"""

R922_URL = "https://regulations.delaware.gov/AdminCode/title14/922"
R925_URL = "https://regulations.delaware.gov/AdminCode/title14/925"
PSN_URL = "https://education.delaware.gov/legacy/wp-content/uploads/sites/4/2026/07/de-procedural-safeguards-july-2026.pdf"
GUIDE_URL = "https://education.delaware.gov/legacy/wp-content/uploads/sites/4/2024/05/parentsarethekey.pdf"


def src(doc, loc=""):
    """RULE922/RULE925 loc is a section, e.g. '3.0' or '6.14.1'; PSN and GUIDE loc is a PDF page."""
    if doc in ("RULE922", "RULE925"):
        part = doc[4:]
        return {"source_type": "state_regulation", "citation": f"14 DE Admin. Code {part}.{loc}",
                "doc_id": "de-code922-2025" if part == "922" else "de-code925-2025",
                "url": R922_URL if part == "922" else R925_URL}
    if doc == "GUIDE":
        return {"source_type": "secondary_guidance",
                "citation": f"PIC of Delaware, Parents Are the Key (2d ed. 2013), PDF p. {loc}", "doc_id": "de-pickey-2013", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"DDOE Delaware Procedural Safeguards (July 2026), PDF p. {loc}", "doc_id": "de-psn-2026", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
DE = ["US-DE"]
DEJ = {"jurisdiction": "US-DE"}
R2 = lambda loc: src("RULE922", loc)
R5 = lambda loc: src("RULE925", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # 14 DE Admin. Code 922: applicability (2.0) and definitions (3.0)
    ("lea", [], R2("2.2.2")), ("esa", [], R2("2.2.2")), ("charter_school", [], R2("2.2.2")),
    ("ppps", [], R2("2.2.5")),
    ("adverse", [("Adverse Effect on Educational Performance", S, DE)], R2("3.0 (Adverse Effect on Educational Performance)")),
    ("at_device", [], R2("3.0 (Assistive Technology Device)")),
    ("at_service", [], R2("3.0 (Assistive Technology Service)")),
    ("cwd", [], R2("3.0 (Child with a Disability)")),
    ("consent", [], R2("3.0 (Consent)")), ("core_acad", [], R2("3.0 (Core Academic Subjects)")),
    ("school_day", [], R2("3.0 (School Day)")), ("essa", [], R2("3.0 (ESSA)")),
    ("evaluation", [], R2("3.0 (Evaluation)")),
    ("eval_report", [("Evaluation Summary Report", S, DE), ("ESR", A, DE)], R2("3.0 (Evaluation Summary Report)")),
    ("excess_costs", [], R2("3.0 (Excess Costs)")), ("fape", [], R2("3.0 (Free Appropriate Public Education)")),
    ("home_instr", [("Homebound or Hospital Placement", S, DE)], R2("3.0 (Homebound or Hospital Placement)")),
    ("homeless", [], R2("3.0 (Homeless Children)")), ("iep", [], R2("3.0 (Individualized Education Program)")),
    ("iep_team", [], R2("3.0 (Individualized Education Program Team)")),
    ("lep", [], R2("3.0 (Limited English Proficient)")), ("mtss", [], R2("3.0 (Multi-Tiered System of Support)")),
    ("native_language", [], R2("3.0 (Native Language)")), ("braille", [], R2("3.0 (Native Language)")),
    ("pti", [], R2("3.0 (Parent Training and Information Center)")),
    ("surrogate", [], R2("3.0 (Parent)")), ("pii", [], R2("3.0 (Personally Identifiable)")),
    ("print_disability", [], R2("3.0 (Print Disability)")), ("public_agency", [], R2("3.0 (Public Agency)")),
    ("related", [], R2("3.0 (Related Services)")), ("implant", [], R2("3.0 (Related Services)")),
    ("audiology", [], R2("3.0 (Audiology)")), ("counseling", [], R2("3.0 (Counseling Services)")),
    ("early_id", [], R2("3.0 (Early Identification and Assessment of Disabilities in Children)")),
    ("interpreting", [], R2("3.0 (Interpreting Services)")), ("cart", [], R2("3.0 (Interpreting Services)")),
    ("medical", [], R2("3.0 (Medical Services)")), ("ot", [], R2("3.0 (Occupational Therapy)")),
    ("om", [], R2("3.0 (Orientation and Mobility Services)")),
    ("parent_training", [], R2("3.0 (Parent Counseling and Training)")),
    ("pt", [], R2("3.0 (Physical Therapy)")), ("psych", [], R2("3.0 (Psychological Services)")),
    ("recreation", [], R2("3.0 (Recreation)")), ("rehab", [], R2("3.0 (Rehabilitation Counseling Services)")),
    ("nursing", [], R2("3.0 (School Health Services)")), ("sbr", [], R2("3.0 (Scientifically Based Research)")),
    ("services_plan", [], R2("3.0 (Services Plan)")), ("social_work", [], R2("3.0 (Social Work Services)")),
    ("special_ed", [], R2("3.0 (Special Education)")), ("slp", [], R2("3.0 (Speech Language Pathology Services)")),
    ("transport", [], R2("3.0 (Transportation)")), ("pe", [], R2("3.0 (Physical Education)")),
    ("sdi", [], R2("3.0 (Specially Designed Instruction)")), ("sea", [], R2("3.0 (State Educational Agency)")),
    ("saas", [], R2("3.0 (Supplementary Aids and Services)")), ("transition", [], R2("3.0 (Transition Services)")),
    ("travel_training", [], R2("3.0 (Travel Training)")), ("universal_design", [], R2("3.0 (Universal Design)")),
    ("voc_ed", [], R2("3.0 (Vocational Education)")), ("ward", [], R2("3.0 (Ward of the State)")),
    # 14 DE Admin. Code 925: eligibility (6.0) and IEP (7.0-15.0)
    ("eligibility", [], R5("6.1")), ("exclusionary", [], R5("6.2")), ("adaptive", [], R5("6.3.1")),
    ("school_psych", [("certified school psychologist", S, DE)], R5("6.3.2")),
    ("primary_disability", [("primary educational classification", S, DE)], R5("6.5.4")),
    ("exit_sped", [("Exit Criteria", REL, DE)], R5("6.5.5")),
    ("std_diploma", [], R5("6.5.5.2")), ("ged", [], R5("6.5.5.2")),
    ("autism", [], R5("6.6")), ("dd", [], R5("6.7")),
    ("deafblind", [("Dual Sensory Impairment", S, DE)], R5("6.8")),
    ("ed", [("Emotional Disability", S, DE)], R5("6.9")),
    ("hi", [], R5("6.10")), ("sld", [], R5("6.11")),
    ("oral_expr", [], R5("6.11.1.1.1")), ("listen_comp", [], R5("6.11.1.1.2")),
    ("written_expr", [], R5("6.11.1.1.3")), ("basic_reading", [], R5("6.11.1.1.4")),
    ("fluency", [], R5("6.11.1.1.5")), ("reading_comp", [], R5("6.11.1.1.6")),
    ("math_calc", [], R5("6.11.1.1.7")), ("math_ps", [], R5("6.11.1.1.8")),
    ("psw", [], R5("6.11.1.3")), ("discrepancy", [], R5("6.11.1.4")),
    ("data_doc", [], R5("6.11.3.7.2")), ("observation", [], R5("6.11.4.2")),
    ("id", [("Mild Intellectual Disability", REL, DE), ("Moderate Intellectual Disability", REL, DE),
            ("Severe Intellectual Disability", REL, DE)], R5("6.12.1")),
    ("oi", [], R5("6.13")), ("ohi", [], R5("6.14")), ("adhd", [], R5("6.14.1.2")),
    ("epilepsy", [], R5("6.14.1")), ("sickle", [], R5("6.14.1")), ("tourette", [], R5("6.14.1")),
    ("sli", [], R5("6.15")), ("tbi", [], R5("6.16")), ("vi", [], R5("6.17")),
    ("tdhh", [], R5("6.10.7")), ("tvi", [], R5("6.17.7")),
    ("test_accom", [], R5("7.1.6")), ("alt_assess", [], R5("7.1.6")),
    ("postsecondary", [], R5("7.2.1")), ("trans_assess", [], R5("7.2.1")), ("course_study", [], R5("7.2.2")),
    ("age_majority", [], R5("7.3")),
    # Added after the 2026-10-08 audit (existing concepts the documents use)
    ("func_perf", [], R5("3.1")), ("gen_curr", [], R5("4.2.1")),
    ("audiological_assess", [], R5("6.8.4.2")), ("gross_motor", [], R5("6.7.1")),
    ("program_mods", [], R5("7.1.4")), ("regular_class", [], R5("7.1.5")),
    ("part_agency", [], R5("8.2.2")), ("service_coord", [], R5("8.6")), ("annual_review", [], R5("11.4")),
    ("comm_mode", [], R2("3.0 (Consent)")),
    ("controlled", [], PS(31)), ("nondisabled", [], G(24)), ("special_class", [], G(38)), ("state_dir", [], G(46)),
    # Procedural Safeguards Notice (July 2026)
    ("safeguards_notice", [("Delaware Procedural Safeguards Parent and Child Rights in Special Education", S, DE)], PS(5)),
    ("idea", [], PS(6)), ("fape", [], PS(6)), ("annual_goals", [], PS(6)), ("progress", [], PS(6)),
    ("lre", [], PS(6)),
    ("sped_admin", [("supervisor of special education", S, DE)], PS(6)),
    ("gen_teacher", [], PS(8)), ("sped_teacher", [], PS(8)),
    ("voc_ed", [], PS(9)), ("notice_meeting", [], PS(10)), ("pwn", [], PS(11)),
    ("consent", [], PS(12)), ("revoke", [], PS(12)), ("ward", [], PS(13)), ("uhy", [], PS(13)),
    ("surrogate", [("Educational Surrogate Parent", S, DE)], PS(13)),
    ("dc_educ_rep", [], PS(14)), ("evaluation", [], PS(14)), ("reeval", [], PS(14)), ("iee", [], PS(14)),
    ("eligibility", [], PS(15)), ("eval_report", [], PS(15)), ("iep", [], PS(16)), ("iep_team", [], PS(8)),
    ("transition", [], PS(16)), ("postsecondary", [], PS(16)), ("trans_assess", [], PS(16)),
    ("age_majority", [], PS(17)), ("ed_records", [], PS(17)), ("ferpa", [], PS(18)), ("pii", [], PS(18)),
    ("mediation", [], PS(19)), ("dp_hearing", [], PS(20)), ("dp_complaint", [], PS(20)),
    ("resolution", [], PS(23)), ("stay_put", [], PS(23)), ("state_complaint", [], PS(26)),
    ("code_conduct", [], PS(29)), ("iaes", [], PS(29)), ("fba", [], PS(29)), ("cop", [], PS(29)),
    ("mdr", [], PS(30)), ("bip", [], PS(30)), ("sbi", [], PS(31)), ("exp_hearing", [], PS(32)),
    ("expedited_eval", [], PS(33)), ("ppps", [], PS(34)),
    # Parents Are the Key (PIC, 2013)
    ("services_plan", [], G(8)), ("surrogate", [("ESP", A, DE)], G(9)),
    ("autism", [], G(11)), ("asperger", [], G(11)), ("pdd", [], G(11)),
    ("deafblind", [], G(11)), ("deafness", [], G(11)), ("dd", [], G(11)),
    ("ed", [], G(12)), ("hi", [], G(12)), ("id", [], G(12)),
    ("md", [], G(12)), ("oi", [], G(12)), ("ohi", [], G(12)), ("adhd", [], G(12)),
    ("sld", [], G(13)), ("dyslexia", [], G(13)), ("perceptual", [], G(13)), ("mbd", [], G(13)),
    ("aphasia", [], G(13)), ("sli", [], G(13)), ("tbi", [], G(13)), ("vi", [], G(13)),
    ("ifsp", [], G(13)), ("child_find", [], G(15)), ("rti", [], G(15)), ("tier1", [], G(15)),
    ("sst", [("Intervention Support Team", S, DE), ("IST", A, DE)], G(15)),
    ("referral", [], G(16)),
    ("sped_admin", [("Special Education Coordinator", S, DE)], G(16)),
    ("statewide_assess", [], G(16)),
    ("fba", [], G(18)), ("bip", [], G(19)),
    ("pbis", [("Positive Behavior Support", S, None), ("PBS", A, DE)], G(55)),
    ("eval_report", [], G(20)), ("pwn", [], G(20)), ("iee", [], G(21)),
    ("braille", [], G(24)), ("nimas", [], G(25)), ("plaafp", [], G(25)), ("sto", [], G(26)),
    ("esy", [], G(27)), ("in_transition_iep", [], G(29)),
    ("course_study", [], G(30)), ("age_majority", [], G(31)),
    ("lre", [], G(38)), ("coteach", [("team classrooms", S, DE)], G(38)),
    ("iaes", [], G(41)), ("special_circ", [], G(41)), ("iss", [], G(42)), ("mdr", [], G(42)),
    ("iep_facil", [], G(45)), ("mediation", [], G(45)), ("state_complaint", [], G(45)),
    ("dp_hearing", [], G(46)), ("dp_complaint", [], G(46)), ("resolution", [], G(47)), ("stay_put", [], G(48)),
    ("ceis", [], G(53)), ("nimac", [], G(54)), ("pti", [], G(54)), ("universal_design", [], G(56)),
    # Former Delaware labels in the 2013 GUIDE glossary (not in the current rule)
    ("id", [("mental disability", L, DE)], G(52)),
    ("sli", [("Preschool Speech Delay", REL, DE), ("Speech and/or Language Impairment", V, DE)], G(52)),
    ("sld", [], G(52)),
]

CONCEPTS = [
    # Agencies, offices and programs named in the rule
    ("de_doe", "Delaware Department of Education", "legal_procedural", [("DOE", A, DE)],
     R2("2.2.1, 3.0 (Department of Education)"),
     {**DEJ, "broader": "sea", "note": "The acronym DDOE, used in the PSN and GUIDE, is in delaware_supplement."}),
    ("de_regs", "14 DE Admin. Code 922 to 929", "legal_procedural",
     [("Regulations 922 through 929", V, DE)], R2("1.1-1.2"),
     {**DEJ, "note": "Delaware's special education regulations, Children with Disabilities Subparts A through I."}),
    ("de_pic", "Parent Information Center of Delaware", "legal_procedural", [("PIC", A, DE)], G(3),
     {**DEJ, "broader": "pti", "note": "Delaware's federally funded Parent Training and Information Center."}),
    ("de_dsd", "Delaware School for the Deaf", "placement_setting", [], R2("2.2.3"),
     {**DEJ, "broader": "state_ops"}),
    ("de_dap", "Delaware Autism Program", "placement_setting", [], R2("2.2.3"),
     {**DEJ, "broader": "state_ops"}),
    ("de_dscyf", "Department of Services for Children, Youth and Their Families", "legal_procedural",
     [("Department of Services for Children, Youth, and their Families", V, DE)],
     R2("2.2.3, 3.0 (Ward of the State)"), DEJ),
    ("de_dhss", "Department of Health and Social Services", "legal_procedural", [], R2("2.2.3"), DEJ),
    ("de_prison_ed", "Prison Education Program", "placement_setting", [], R2("2.2.4"),
     {**DEJ, "note": "Department of Corrections program for students with disabilities in adult facilities."}),
    ("de_relative_caregiver", "Relative Caregiver's School Authorization", "legal_procedural", [],
     R2("3.0 (Parent)"),
     {**DEJ, "note": "Lets a relative the child lives with act as the parent; executed under 14 Del.C. 202(f)(1)."}),
    ("de_secretary", "Secretary of Education", "legal_procedural", [], R2("3.0 (Secretary)"),
     {**DEJ, "note": "In Delaware, the head of the Department of Education, who receives due process complaints."}),
    ("de_ed_class", "Educational classification", "evaluation_eligibility",
     [("educational classifications", P, DE)], R2("3.0 (Educational Classification)"),
     {**DEJ, "note": "Delaware's term for the 12 disability categories."}),
    # Concepts from the eligibility rules (925.6.0) that are not state-specific
    ("ansd", "Auditory Neuropathy Spectrum Disorder", "health_condition", [("ANSD", A, None)],
     R5("6.10.1.1.3"), {"broader": "hi"}),
    ("abr", "Auditory Brainstem Response", "instrument", [("ABR", A, None)], R5("6.10.1.1.3"), {}),
    ("cortical_vi", "Cortical vision impairment", "health_condition", [], R5("6.17.1.1.2"), {"broader": "vi"}),
    # IEP and graduation rules (925.7.0-15.0)
    ("de_emp_first", "Employment First Policy", "transition", [("Employment First", AB, DE)], R5("7.2.2.1"),
     {**DEJ, "note": "Delaware policy (19 Del.C. 743) the IEP Team discusses with transition-age students."}),
    ("de_12month", "Twelve-month program", "placement_setting", [("12-month program", V, DE)], R5("7.6"),
     {**DEJ, "note": "Year-round program for students in listed classifications under 14 Del.C. 1703; separate from ESY."}),
    ("de_daas", "Diploma of Alternate Achievement Standards", "transition", [], R5("15.0"),
     {**DEJ, "broader": "alt_diploma"}),
    # Procedural Safeguards Notice
    ("de_ecr", "Exceptional Children Resources", "legal_procedural", [], PS(1),
     {**DEJ, "broader": "de_doe", "note": "The DDOE office responsible for special education."}),
    ("de_sparc", "Special Education Partnership for the Amicable Resolution of Conflict", "legal_procedural",
     [("SPARC", A, DE)], PS(7),
     {**DEJ, "broader": "mediation", "note": "University of Delaware program that runs DDOE's mediation and IEP facilitation."}),
    ("de_drd", "Disability Rights Delaware", "legal_procedural", [], PS(7), DEJ),
    ("draft_iep", "Draft IEP", "iep_component", [], PS(9), {"broader": "iep"}),
    ("de_hearing_panel", "Hearing panel", "legal_procedural", [], PS(21),
     {**DEJ, "broader": "dp_hearing", "note": "Delaware hears due process complaints before a three-member panel."}),
    ("de_med_form", "Request for Special Education Mediation Form", "legal_procedural", [], PS(19),
     {**DEJ, "broader": "mediation"}),
    ("de_dp_form", "Due Process Complaint Form and Request for Due Process Hearing", "legal_procedural", [],
     PS(20), {**DEJ, "broader": "dp_complaint"}),
    ("de_sc_form", "Special Education State Complaint Form", "legal_procedural", [], PS(28),
     {**DEJ, "broader": "state_complaint"}),
    # Parents Are the Key (PIC, 2013)
    ("de_cdw", "Child Development Watch", "early_intervention", [("CDW", A, DE)], G(49),
     {**DEJ, "note": "Delaware's Part C early intervention program for birth to three."}),
    ("educ_diag", "Educational Diagnostician", "personnel_role", [], G(16), {}),
    ("de_dcas", "Delaware Comprehensive Assessment System", "instrument", [("DCAS", A, DE)], G(16),
     {**DEJ, "broader": "statewide_assess", "note": "Former state test (from 2009) named in the 2013 guide."}),
    ("de_dstp", "DE Student Testing Program", "instrument", [("DSTP", A, DE)], G(52),
     {**DEJ, "broader": "statewide_assess", "note": "State test replaced by DCAS in 2009."}),
    ("de_dati", "Delaware Assistive Technology Initiative", "related_service", [("DATI", A, DE)], G(50),
     {**DEJ, "broader": "at_service"}),
    ("de_ssp", "Student Success Plan", "transition", [("SSP", A, DE)], G(29), DEJ),
    ("de_dvr", "Division of Vocational Rehabilitation", "transition", [("DVR", A, DE)], G(30),
     {**DEJ, "broader": "vr_services"}),
    ("de_ddds", "Developmental Disabilities Services", "transition", [("DDDS", A, DE)], G(30), DEJ),
    ("case_by_case", "Case-by-case determination", "discipline", [], G(41), {}),
    ("oss", "Out-of-school suspension", "discipline", [], G(42), {}),
    ("de_gacec", "Governor's Advisory Council for Exceptional Citizens", "legal_procedural",
     [("GACEC", A, DE)], G(50), {**DEJ, "broader": "state_panel"}),
    ("cprc", "Community Parent Resource Center", "legal_procedural",
     [("Community Parent Resource Centers", P, None)], G(54), {"broader": "pti"}),
]

JURISDICTION = "US-DE"
LAYER_NAME = "Delaware"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.40.0"  # tools/add_state.py sets this
