"""
Kentucky layer for SPEDLex.

Sources reviewed 2026-10-09 (listed in sources/documents.tsv; local copies in .sources-cache/ky/):
  RULE   707 KAR 1:002, Definitions (Kentucky Board of Education, Department of
         Education), engrossed text as served by the Legislative Research
         Commission, 9 pp. The history note ends "49 Ky.R. 1525, 1928; eff.
         7-5-2023" and the heading says "(Amended at ARRS Committee)". Cited by
         the numbered definition in Section 1, e.g. "Section 1(24)".
  PSN    Kentucky Department of Education, Part B Procedural Safeguards Notice,
         35 pp. The cover says "Revised September 26, 2008"; the PDF's own
         metadata says it was modified 2023-08-22. Cited by PDF page. The
         printed page number is the PDF page minus three (PDF p. 4 is printed
         p. 1).
  GUIDE  Kentucky Department of Education, The Individuals with Disabilities
         Education Act (IDEA) Part B Special Education Process (6 pp., "Reviewed
         April 2025"). Cited by page; PDF page = printed page.
  YOUTH  KY-SPIN, Inc., A Youth Guide to the IEP (c) 2025, 67 pp., hosted on the
         KDE site. Cited by PDF page (the guide prints no page numbers). It
         is an advocacy group's guide, not a KDE document, so its records are
         typed secondary_guidance. It repeats KDE's IEP-development guidance and
         cites 707 KAR 1:320 and 707 KAR 1:350 section by section; those two
         rules, 707 KAR 1:300 and 707 KAR 1:310 were not provided.

Documents not provided or not read: the rest of 707 KAR Chapter 1 (only 1:002 was
read), KDE's Guidance Document for Individual Education Program (IEP)
Development, the Kentucky Guide to Special Education Due Process, the
alternate-assessment and diploma pages (704 KAR 3:305). Where the documents
name them, they appear only as the names the documents give. The GUIDE and
YOUTH pages were read by text extraction (pdftotext); several Youth Guide pages
are partly raster images (pp. 17, 19, 21), so the words on those pages were
read from the text layer only and cited when the wording was clear.

Records from the rule text are 'machine_validated'; the others are 'candidate'.
"""

RULE_URL = "https://apps.legislature.ky.gov/law/kar/downloads/docs/14098/document.engrossed.pdf"
PSN_URL = "https://www.education.ky.gov/specialed/excep/GuidanceResources/Documents/Procedural_Safeguards_Notice.pdf"
GUIDE_URL = "https://www.education.ky.gov/specialed/excep/GuidanceResources/Documents/IDEASpecialEducationProcess.pdf"
YOUTH_URL = "https://www.education.ky.gov/specialed/excep/Documents/Youth-IEP.pdf"


def src(doc, loc=""):
    """RULE loc is 'Section 1(n)'; PSN loc is a PDF page; GUIDE and YOUTH loc is a PDF page, e.g. 'p. 4'."""
    if doc == "RULE":
        return {"source_type": "state_regulation",
                "citation": f"707 KAR 1:002 (history note through eff. 7-5-2023), {loc}",
                "doc_id": "ky-707kar1002-2023", "url": RULE_URL}
    if doc == "PSN":
        return {"source_type": "procedural_safeguards_notice",
                "citation": f"Kentucky Department of Education, Part B Procedural Safeguards Notice (rev. September 26, 2008), PDF p. {loc}",
                "doc_id": "ky-psn-2008", "url": PSN_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"Kentucky Department of Education, IDEA Part B Special Education Process (reviewed April 2025), {loc}",
                "doc_id": "ky-sped-process-2025", "url": GUIDE_URL}
    return {"source_type": "secondary_guidance",
            "citation": f"KY-SPIN, A Youth Guide to the IEP (2025), PDF {loc}",
            "doc_id": "ky-youth-iep-2025", "url": YOUTH_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
KY = ["US-KY"]                    # regional tag for strings only used in Kentucky
KYJ = {"jurisdiction": "US-KY"}   # opts for concepts that only exist in Kentucky

R = lambda n: src("RULE", f"Section 1({n})")       # a numbered definition in 707 KAR 1:002
PS = lambda page: src("PSN", str(page))
G = lambda page: src("GUIDE", f"p. {page}")
Y = lambda page: src("YOUTH", f"p. {page}")

STRINGS = [
    # 707 KAR 1:002: the thirteen disability categories (Section 1(9)) and their definitions
    ("cwd", [], R(9)),
    ("autism", [], R(5)),
    ("deafblind", [], R(21)),
    ("dd", [], R(22)),
    ("ed", [("emotional-behavioral disability", S, KY)], R(24)),
    ("ed", [("emotional-behavior disability", S, KY)], R(5)),
    ("hi", [], R(29)),
    ("id", [("mental disability", L, KY), ("mild mental disability", S, KY), ("functional mental disability", S, KY),
            ("MMD", A, KY), ("FMD", A, KY)], R(37)),
    ("md", [], R(39)),
    ("oi", [], R(41)),
    ("ohi", [], R(42)),
    ("adhd", [], R(42)), ("epilepsy", [], R(42)), ("sickle", [], R(42)), ("tourette", [], R(42)),
    ("sld", [], R(59)),
    ("dyslexia", [], R(59)), ("dyscalculia", [], R(59)), ("dysgraphia", [], R(59)), ("aphasia", [], R(59)),
    ("perceptual", [("perceptual/motor disabilities", S, KY)], R(59)),
    ("sli", [], R(60)),
    ("artic", [("impaired articulation", S, KY)], R(60)),
    ("fluency_dis", [], R(60)), ("voice", [], R(60)), ("lang_dis", [], R(60)),
    ("tbi", [], R(63)),
    ("vi", [], R(65)),
    # 707 KAR 1:002: other definitions
    ("adverse", [("adverse effect", S, None)], R(2)),
    ("at_device", [], R(3)), ("at_service", [], R(4)),
    ("school_day", [], R(6)),
    ("cop", [("change of placement because of disciplinary removals", S, None)], R(8)),
    ("special_class", [], R(7)),
    ("sped_teacher", [("teacher of exceptional children", S, KY)], R(7)),
    ("resource_room", [("resource classes", S, KY)], R(10)),
    ("consent", [], R(15)),
    ("controlled", [], R(16)),
    ("core_acad", [], R(17)),
    ("course_study", [], R(19)),
    ("ed_records", [], R(23)),
    ("esy", [], R(26)),
    ("fape", [], R(27)),
    ("std_diploma", [("high school diploma", S, KY)], R(30)),
    ("cert_completion", [], R(30)), ("ged", [], R(30)),
    ("home_education", [("home school", S, KY)], R(31)),
    ("idea", [], R(32)),
    ("iee", [], R(33)),
    ("iep", [], R(34)),
    ("interpreting", [], R(35)), ("cart", [], R(35)),
    ("lea", [], R(36)),
    ("native_language", [], R(40)),
    ("surrogate", [], R(43)), ("foster", [], R(43)),
    ("part_agency", [], R(44)),
    ("pii", [], R(45)),
    ("postsecondary", [], R(46)),
    ("ppps", [("private school children with disabilities", S, KY)], R(47)),
    ("related", [], R(51)), ("slp", [], R(51)), ("audiology", [], R(51)), ("psych", [], R(51)),
    ("pt", [], R(51)), ("ot", [], R(51)), ("recreation", [], R(51)), ("early_id", [], R(51)),
    ("counseling", [], R(51)), ("rehab", [], R(51)), ("om", [], R(51)), ("medical", [], R(51)),
    ("transport", [], R(51)),
    ("nursing", [], R(51)), ("social_work", [], R(51)), ("parent_training", [], R(51)),
    ("sbi", [], R(54)),
    ("services_plan", [], R(55)),
    ("special_ed", [], R(56)),
    ("sdi", [("specially-designed instruction", V, KY)], R(58)),
    ("saas", [], R(61)),
    ("transition", [], R(62)),
    ("fve", [], R(62)),
    ("travel_training", [], R(64)),
    ("ward", [], R(66)),
    ("weapon", [], R(67)),
    ("exc_student", [("exceptional children", P, KY)], PS(1)),
    # Procedural Safeguards Notice
    ("safeguards_notice", [("Kentucky Procedural Safeguards Notice", S, KY)], PS(1)),
    ("pwn", [], PS(4)),
    ("native_language", [], PS(5)),
    ("ppps", [], PS(7)), ("services_plan", [], PS(7)),
    ("iee", [], PS(7)),
    ("ed_records", [], PS(9)), ("pii", [], PS(9)), ("part_agency", [], PS(9)), ("ferpa", [], PS(9)),
    ("child_find", [], PS(9)),
    ("state_complaint", [("state formal written complaint", S, None), ("formal written complaint", S, None)], PS(13)),
    ("dp_complaint", [], PS(16)),
    ("homeless", [("homeless child or youth", S, None)], PS(15)),
    ("mediation", [], PS(18)),
    ("stay_put", [], PS(19)),
    ("resolution", [], PS(19)),
    ("dp_hearing", [], PS(21)),
    ("state_panel", [("state special education advisory panel", S, KY)], PS(24)),
    ("iaes", [], PS(28)),
    ("cop", [], PS(31)),
    ("mdr", [], PS(29)),
    ("fba", [], PS(29)), ("bip", [], PS(30)),
    ("exp_hearing", [], PS(32)),
    # Special Education Process guide
    ("child_find", [], G(1)),
    ("rti", [], G(2)),
    ("mtss", [("Kentucky Multi-Tiered System of Supports", S, KY), ("KyMTSS", A, KY)], G(2)),
    ("referral", [], G(2)),
    ("iep_team", [("Admissions and Release Committee", S, KY), ("ARC", A, KY)], R(1)),
    ("evaluation", [], G(3)),
    ("eligibility", [], G(4)),
    ("fva", [("functional vision/learning media assessment", S, KY)], G(4)),
    ("reeval", [], G(5)),
    ("annual_review", [], G(5)),
    ("progress", [], G(5)),
    ("pwn", [], G(5)),
    ("sped_admin", [("DoSE", A, KY)], G(5)),
    ("part_c_transition", [], G(6)),
    ("osep", [], G(6)),
    # A Youth Guide to the IEP
    ("iep", [], Y(3)),
    ("iep_team", [("ARC meeting", S, KY)], Y(5)),
    ("lea_rep", [], Y(6)),
    ("sped_teacher", [], Y(6)),
    ("plaafp", [], Y(11)),
    ("fva", [("functional vision and learning media assessment", S, KY)], Y(14)),
    ("transition", [], Y(17)),
    ("postsecondary", [], Y(17)),
    ("age_majority", [], Y(19)),
    ("dc_educ_rep", [], Y(19)),
    ("co_special_factors", [], Y(21)),
    ("lep", [], Y(22)), ("aac", [], Y(22)), ("at_device", [], Y(22)), ("braille", [], Y(23)),
    ("pbis", [], Y(23)),
    ("annual_goals", [], Y(24)),
    ("cbm", [], Y(32)),
    ("fluency", [], Y(32)),
    ("sdi", [], Y(34)),
    ("saas", [], Y(37)),
    ("graphic_org", [], Y(37)), ("ext_time", [], Y(37)), ("large_print", [], Y(37)), ("calc_aids", [], Y(37)),
    ("sto", [("short-term instructional objectives", S, KY), ("short term instructional objectives", S, KY)], Y(40)),
    ("test_accom", [], Y(43)),
    ("alt_assess", [], Y(46)),
    ("program_mods", [("supports for school personnel", S, KY)], Y(48)),
    ("lre", [], Y(51)),
    ("regular_class", [], Y(52)), ("special_class", [], Y(52)), ("special_school", [], Y(52)),
    ("home_instr", [], Y(52)), ("hospital_instr", [], Y(52)), ("gen_curr", [], Y(52)),
    ("related", [], Y(58)),
    ("esy", [], Y(63)),
    ("fape", [], Y(64)),
    ("safeguards_notice", [("Procedural Safeguard Notice", S, KY)], Y(64)),
    ("consent", [], Y(64)),
    ("self_det", [], Y(4)),
]

CONCEPTS = [
    # Kentucky agencies, offices and programs
    ("ky_kde", "Kentucky Department of Education", "legal_procedural", [("KDE", A, KY)], PS(9),
     {**KYJ, "broader": "sea"}),
    ("ky_oseel", "Office of Special Education and Early Learning", "legal_procedural", [("OSEEL", A, KY)], G(5),
     {**KYJ, "broader": "ky_kde"}),
    ("ky_idea_monitoring", "Division of IDEA Monitoring and Results", "legal_procedural", [], PS(15),
     {**KYJ, "broader": "ky_kde"}),
    ("ky_ecab", "Exceptional Children Appeals Board", "legal_procedural", [("ECAB", A, KY)], PS(25),
     {**KYJ, "note": "The state-level body that reviews a due process hearing officer's decision."}),
    ("ky_chfs", "Cabinet for Health and Family Services", "legal_procedural",
     [("Cabinet for Families and Children", L, KY)], src("PSN", "6 (the legacy name 'Cabinet for Families and Children' is in 707 KAR 1:002, Section 1(66))"), KYJ),
    ("ky_djj", "Department of Juvenile Justice", "legal_procedural", [], PS(6), KYJ),
    ("ky_ksb", "Kentucky School for the Blind", "placement_setting", [("KSB", A, KY)], R(36),
     {**KYJ, "flags": ["place_name"]}),
    ("ky_ksd", "Kentucky School for the Deaf", "placement_setting", [("KSD", A, KY)], R(36),
     {**KYJ, "flags": ["place_name"]}),
    ("ky_ksis", "Kentucky Student Information System", "legal_procedural", [("KSIS", A, KY)], G(1), KYJ),
    ("ky_spin", "Kentucky Special Parent Involvement Network", "legal_procedural", [("KY-SPIN", A, KY)], G(6), KYJ),
    ("ky_kar", "Kentucky Administrative Regulations", "legal_procedural", [("KAR", A, KY), ("KARs", P, KY)], G(1), KYJ),
    # Kentucky rule terms
    ("ky_sped_mentor", "Special education mentor", "personnel_role", [], R(57),
     {**KYJ, "note": "Defined in the rule by reference to KRS 157.197."}),
    ("ky_cap", "Corrective action plan", "legal_procedural", [("CAP", A, KY)], R(18), {}),
    ("ky_compliance_report", "Compliance monitoring report", "legal_procedural", [], R(14), {}),
    ("ky_program_of_studies", "Program of Studies", "academic_skill", [], R(27), KYJ),
    # Kentucky assessments
    ("ky_ksa", "Kentucky Summative Assessment", "iep_component", [("KSA", A, KY)], Y(43), KYJ),
    ("ky_aksa", "Alternative Kentucky Summative Assessment", "iep_component",
     [("AKSA", A, KY), ("Kentucky Alternate Assessment", S, KY)], src("YOUTH", "p. 46 ('Kentucky Alternate Assessment' is on p. 47)"), {**KYJ, "broader": "alt_assess"}),
    # Terms from the IEP forms and the Youth Guide that exist outside Kentucky
    ("func_hearing_assess", "Functional hearing, listening, and communication assessment", "evaluation_eligibility",
     [("functional hearing, listening and communication", AB, KY),
      ("functional hearing, listening, communication assessment", V, KY)],
     src("YOUTH", "p. 16 (also p. 15; the Special Education Process guide, p. 4, has the third form)"), {}),
    ("wioa", "Workforce Innovation and Opportunity Act", "transition", [("WIOA", A, None)], Y(47), {}),
    ("smart_goals", "SMART goals", "iep_component", [("S.M.A.R.T. goals", V, None)], Y(25),
     {"flags": ["common_english_word"]}),
    ("meas_method", "Methods of measurement", "iep_component", [], Y(31), {}),
    ("meas_direct", "Direct measure", "iep_component", [("direct measures", P, None)], Y(32), {"broader": "meas_method"}),
    ("meas_indirect", "Indirect measure", "iep_component", [("indirect measures", P, None)], Y(32), {"broader": "meas_method"}),
    ("meas_authentic", "Authentic assessment", "iep_component", [], Y(32), {"broader": "meas_method"}),
]

JURISDICTION = "US-KY"
LAYER_NAME = "Kentucky"
RETRIEVED = "2026-10-09"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.47.0"  # tools/add_state.py sets this
