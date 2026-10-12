"""
West Virginia layer for SPEDLex.

Sources reviewed 2026-10-09 (listed in sources/documents.tsv; local copies in .sources-cache/wv/):
  RULE   West Virginia Board of Education, Policy 2419, Regulations for the
         Education of Students with Exceptionalities (W. Va. 126CSR16),
         legislative rule filed 2/9/2023, effective 3/13/2023, with the West
         Virginia Procedures Manual for the Education of Students with
         Exceptionalities incorporated by reference (WV-Policy-2419-126CSR16.pdf,
         155 pp.). The file is a scanned image with no text layer. The words
         were read from an OCR text layer I produced with tesseract
         (WV-Policy-2419-ocr-text.txt, same folder), so every quoted string was
         checked by eye against the surrounding wording and OCR slips were
         corrected (for example "Parentaily-Placed" is read as
         "Parentally-Placed"). Cited by chapter and section where the text
         gives one, plus the PDF page. For this file the PDF page is the
         printed page number plus one.
  PSN    West Virginia Department of Education, Procedural Safeguards Available
         to Parents and Students with Exceptionalities (revised August 2024,
         51 pp.). Cited by PDF page. The printed page number is the PDF page
         minus three.
  GUIDE  OSEP QA 23-01, State General Supervision Responsibilities under Parts
         B and C of the IDEA (U.S. Department of Education, 7/24/2023, 45 pp.),
         a federal document that the WVDE policies page links as guidance
         (WV-OSEP-General-Supervision-Guidance-2023.pdf). It was read in full
         as extracted text. Because it is not a West Virginia document it is
         not used as a source for any record; it only corroborates the general
         supervision, State Performance Plan and monitoring wording that
         Policy 2419 itself uses.

Both West Virginia documents were read in full. No main parent guide or IEP
manual was provided, so none of the parent-guide vocabulary is here. The rule
text is from 2023 and the notice is from 2024. RULE records are
'machine_validated'; PSN records are 'candidate'. The notice is mostly the
federal model notice, so most of its entries only record that West Virginia
attests an existing concept.

Left out on purpose: the street address, phone numbers and web addresses of the
Department; case-law names (Endrew F. v. Douglas County, a student's name;
Shaffer v. Weast); the statewide test brand "SAT School Day" and the textbook
brands C-Print and TypeWell (products); funding terms (high cost/high acuity);
Board policy numbers other than 2419, 4350 and 4373 (2340, 2510, 2520 series,
2525, 3300, 5202, 5500, 6200); the OHI conditions cancer, stroke, asthma,
diabetes, heart condition, hemophilia, lead poisoning, leukemia, nephritis and
rheumatic fever (no SPEDLex concept for them, as in the Wyoming layer); medical
specialists named in the eligibility criteria (ophthalmologist, optometrist,
otologist, otolaryngologist, neurologist); the DSM-5 adaptive-functioning severity
words (mild, moderate, severe, profound); the SLD cut-off numbers; the
staffing charts and class-size limits; the acronyms GEE (a given name) and PA
(the Pennsylvania postal code), whose full phrases are attested without them; the
placeholder key exec_fn (executive skills); the Level I, II and III service-need
lists; the W. Va. Code sections on classroom video cameras; and the individual
state-complaint, mediation and due process form names the Department hosts.

Corrected 2026-10-09 after an independent audit by claude-opus-5-5
(provenance/wv/wv-layer-audit-2026-10-09.md). Every string was rechecked against a
second OCR of Policy 2419. Within one layer, STRINGS are applied before
CONCEPTS, so a new concept with a string on another page cites both pages
("PDF p. 124 (also ... p. 84)"). Removed: two variants that neither document
prints ("West Virginia Birth to Three", "Division of Federal Programs and
Support"), the "Augmentative/Alternative Communication Evaluation" string (an
evaluation, not AAC itself), and two attestations that rested on other wording
(edu_interpreter, already covered by wv_esli; homeless at PSN p. 27). "APR"
(Annual Performance Report) is kept: it is also the month abbreviation, and
the matcher now skips any month name with a number next to it, so it cannot
shelter part of a date of birth.
"""

RULE_URL = "https://wveis.k12.wv.us/wvboe/policies/policy.php?p=2419"
PSN_URL = "https://wvde.us/wp-content/uploads/2024/09/33078-Procedural-Safeguards-v1.pdf"


def src(doc, loc=""):
    """RULE loc is a part of the rule with its PDF page, e.g. 'Ch. 4, § 3.E, PDF p. 55';
    PSN loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation",
                "citation": f"West Virginia Board of Education Policy 2419 (126CSR16, eff. March 13, 2023), {loc}",
                "doc_id": "wv-policy2419-2023", "url": RULE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"West Virginia Department of Education, Procedural Safeguards Available to Parents and Students with Exceptionalities (rev. August 2024), PDF p. {loc}",
            "doc_id": "wv-psn-2024", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
WV = ["US-WV"]
WVJ = {"jurisdiction": "US-WV"}
D = lambda pdf: src("RULE", f"Definitions, PDF p. {pdf}")          # the Definitions section
AC = lambda pdf: src("RULE", f"Acronyms and Abbreviations, PDF p. {pdf}")
C = lambda part, pdf: src("RULE", f"{part}, PDF p. {pdf}")          # a chapter and section
PS = lambda page: src("PSN", page)

STRINGS = [
    # Policy 2419: definitions
    ("exceptionality", [], D(16)),
    ("exc_student", [("students with exceptionalities", S, WV), ("eligible students with exceptionalities", S, WV)], D(16)),
    ("cwd", [("eligible students with disabilities", S, WV)], D(16)),
    ("lea", [], D(20)), ("fape", [], D(17)), ("iep", [], D(19)), ("iep_team", [], D(19)),
    ("evaluation", [], D(16)), ("iee", [], D(19)), ("consent", [], D(14)),
    ("pwn", [], D(25)), ("mediation", [], D(20)), ("lre", [], D(19)), ("continuum", [("Continuum of Services/Placements", S, WV)], D(14)),
    ("esy", [], D(17)), ("transition", [], D(30)), ("related", [], D(26)),
    ("at_device", [], D(13)), ("at_service", [], D(13)), ("audiology", [], D(13)),
    ("counseling", [], D(15)), ("interpreting", [], D(19)), ("ot", [], D(22)), ("pt", [], D(24)),
    ("psych", [], D(25)), ("recreation", [], D(25)), ("rehab", [], D(26)), ("om", [], D(22)),
    ("nursing", [], D(26)), ("social_work", [], D(28)), ("parent_training", [], D(23)),
    ("transport", [], D(31)), ("medical", [], D(20)), ("slp", [], D(29)), ("speech_path", [], D(29)),
    ("saas", [], D(30)), ("sdi", [], D(29)), ("plaafp", [("PLEPs", P, WV)], D(24)),
    ("annual_goals", [], D(12)), ("fba", [], D(17)), ("bip", [], D(13)), ("mdr", [], D(20)),
    ("weapon", [], D(15)), ("sbi", [], D(27)), ("controlled", [], D(14)), ("illegal_drug", [], D(18)),
    ("iaes", [], D(19)), ("iss", [], D(19)), ("oss", [], D(22)),
    ("ward", [], D(31)), ("homeless", [], D(18)), ("age_majority", [], D(12)),
    ("ferpa", [], AC(10)), ("pii", [], D(23)), ("ed_records", [], D(16)), ("part_agency", [], D(23)),
    ("ifsp", [], D(23)), ("native_language", [], D(21)), ("universal_design", [], D(31)),
    ("mtss", [], D(21)), ("psw", [], D(23)), ("sig_cog", [], D(28)), ("alt_diploma", [], D(12)),
    ("sb_iep", [("SB-IEP", A, WV), ("Standards-Based Individualized Education Program", S, None)], D(30)),
    ("sst", [("SAT", A, WV)], D(30)),
    ("gen_ed_env", [], AC(10)),
    ("adaptive", [("adaptive skills", S, None)], D(12)),
    ("critical_skill", [], D(15)), ("regression", [("regression/recoupment", S, None)], D(26)),
    ("fva", [], D(17)), ("cart", [], D(19)),
    ("travel_training", [], D(31)), ("sdm", [], D(30)), ("gen_curr", [], D(17)), ("pbis", [], D(24)),
    ("slp_assistant", [("SLPA", A, None)], D(29)), ("essa", [], AC(10)),
    ("special_class", [], D(27)), ("resource_room", [], D(26)), ("coteach", [], D(15)),
    ("ppps", [("Special Education: Parentally-Placed in Private School", S, WV)], C("Ch. 5, § 2.J", 87)),
    # Policy 2419: Chapters 2 and 3, child find, referral and evaluation
    ("child_find", [], C("Ch. 2", 37)),
    ("mdt", [("MDET", A, WV)], C("Ch. 2, § 3.D", 40)),
    ("reeval", [], C("Ch. 3, § 2.B", 42)),
    ("ward", [], C("Ch. 3, § 3.C", 46)),
    # Chapter 4, eligibility
    ("eligibility", [("EC", A, WV)], C("Ch. 4, § 1", 49)),
    ("adverse", [], C("Ch. 4, § 3", 51)),
    ("autism", [], C("Ch. 4, § 3.A", 52)),
    ("cortical_vi", [("cortical visual impairment", V, None)], D(17)),
    ("cortical_vi", [], C("Ch. 4, § 3.B", 53)),
    ("vi", [("blindness and low vision", S, WV)], C("Ch. 4, § 3.B", 53)),
    ("school_psych", [], C("Ch. 4, § 3.A", 53)),
    ("tvi", [], C("Ch. 4, § 3.B", 53)),
    ("deafblind", [], C("Ch. 4, § 3.C", 54)),
    ("deafness", [], C("Ch. 4, § 3.D", 54)),
    ("audiologist", [], C("Ch. 4, § 3.D", 54)),
    ("dd", [], C("Ch. 4, § 3.E", 55)),
    ("ed", [("emotional disorder", S, WV)], D(16)),
    ("gifted", [("exceptional gifted", S, WV)], C("Ch. 4, § 3.G", 58)),
    ("hi", [("deaf and hard of hearing", S, WV)], D(16)),
    ("hi", [], C("Ch. 4, § 3.H", 58)),
    ("id", [], C("Ch. 4, § 3.I", 59)),
    ("oi", [], C("Ch. 4, § 3.J", 59)),
    ("ohi", [], C("Ch. 4, § 3.K", 60)),
    ("adhd", [], C("Ch. 4, § 3.K", 60)), ("epilepsy", [], C("Ch. 4, § 3.K", 60)),
    ("sickle", [], C("Ch. 4, § 3.K", 60)), ("tourette", [], C("Ch. 4, § 3.K", 60)),
    ("sld", [], C("Ch. 4, § 3.L", 60)),
    ("perceptual", [], C("Ch. 4, § 3.L", 60)), ("mbd", [], C("Ch. 4, § 3.L", 60)),
    ("dyslexia", [], C("Ch. 4, § 3.L", 60)), ("aphasia", [], C("Ch. 4, § 3.L", 60)),
    ("dyscalculia", [], C("Ch. 4, § 3.L", 60)),
    ("rti", [], C("Ch. 4, § 3.L, MTSS", 61)),
    ("oral_expr", [], C("Ch. 4, § 3.L, Standard 1", 62)), ("listen_comp", [], C("Ch. 4, § 3.L, Standard 1", 62)),
    ("written_expr", [], C("Ch. 4, § 3.L, Standard 1", 62)), ("basic_reading", [], C("Ch. 4, § 3.L, Standard 1", 62)),
    ("fluency", [], C("Ch. 4, § 3.L, Standard 1", 62)), ("reading_comp", [], C("Ch. 4, § 3.L, Standard 1", 62)),
    ("math_calc", [], C("Ch. 4, § 3.L, Standard 1", 62)), ("math_ps", [], C("Ch. 4, § 3.L, Standard 1", 62)),
    ("exclusionary", [("exclusion factors", S, WV)], C("Ch. 4, § 3.L, Standard 3", 63)),
    ("observation", [], C("Ch. 4, § 3.L, Observation Requirement", 64)),
    ("sli", [("speech/language impairment", V, WV)], D(16)),
    ("norm_ref", [], C("Ch. 4, § 3.M", 66)),
    ("lang_dis", [], C("Ch. 4, § 3.M", 66)),
    ("artic", [("speech sound disorder", S, None), ("articulation/phonology disorder", S, None)],
     C("Ch. 4, § 3.M", 67)),
    ("fluency_dis", [("childhood-onset fluency disorder", S, None)], C("Ch. 4, § 3.M", 68)),
    ("voice", [], C("Ch. 4, § 3.M", 71)),
    ("aac", [], D(14)),
    ("aac", [("augmentative/alternative communication", V, WV)], C("Ch. 4, § 3.M", 72)),
    ("tbi", [], C("Ch. 4, § 3.N", 72)),
    # Chapter 5, IEP
    ("iep_team", [], C("Ch. 5, § 1.D", 74)),
    ("braille", [], C("Ch. 5, § 2.C", 78)),
    ("nimas", [], C("Ch. 5, § 2.C", 78)),
    ("postsecondary", [], C("Ch. 5, § 2.F", 80)),
    ("sop", [], C("Ch. 5, § 2.F", 80)),
    ("sdm", [], C("Ch. 5, § 2.F", 80)),
    ("alt_assess", [], C("Ch. 5, § 2.I", 84)),
    ("special_school", [("special education: special school", S, WV)], C("Ch. 5, § 2.J", 87)),
    ("residential", [("special education: residential facility", S, WV)], C("Ch. 5, § 2.J", 87)),
    ("nc_recp", [], C("Ch. 5, § 2.J", 88)),
    ("head_start", [], C("Ch. 5, § 2.J", 88)),
    ("revoke", [], C("Ch. 5, § 2.K", 89)),
    ("amendment", [("IEP Amendment Form", REL, WV)], C("Ch. 5, § 3.B", 90)),
    ("annual_review", [], C("Ch. 5, § 3.A", 90)),
    ("part_c_transition", [], C("Ch. 5, § 5", 92)),
    # Chapters 6 to 10
    ("ar_integrated", [], C("Ch. 6, § 4.B", 98)),
    ("cop", [], C("Ch. 7", 104)),
    ("basis_know", [], C("Ch. 7", 103)),
    ("exp_hearing", [], C("Ch. 7, § 3.A", 107)),
    ("unilateral_pl", [], C("Ch. 8, § 1.C", 110)),
    ("services_plan", [], D(28)),
    ("safeguards_notice", [], C("Ch. 10, § 2", 128)),
    ("surrogate", [], C("Ch. 10, § 8", 135)),
    ("uhy", [], C("Ch. 10, § 8.A", 135)),
    ("state_complaint", [], C("Ch. 11, § 2", 138)),
    ("dp_complaint", [], C("Ch. 11, § 4", 142)),
    ("dp_hearing", [], C("Ch. 11, § 4", 142)),
    ("iep_facil", [("Facilitated IEP Team meeting", S, None)], C("Ch. 11, § 1", 137)),
    # Added after the 2026-10-09 audit (existing concepts the documents use)
    ("test_accom", [], C("Ch. 5, § 2.I", 84)),
    ("program_mods", [], C("Ch. 5, § 2.G", 80)),
    ("regular_class", [], C("Ch. 5, § 2.G", 81)),
    ("sped_teacher", [], D(14)),
    ("disprop", [], C("Ch. 9, § 1", 118)),
    ("gen_teacher", [], C("Ch. 5, § 1.C", 74)), ("lea_rep", [], C("Ch. 5, § 1.B", 74)),
    ("public_agency", [], D(23)), ("func_perf", [], D(24)),
    ("referral", [], C("Ch. 2, § 3", 38)),
    ("foster", [], D(22)), ("lep", [], D(21)), ("pe", [], D(12)), ("std_diploma", [], D(12)),
    ("para", [], D(16)), ("sea", [], D(17)), ("indirect_svc", [], D(19)),
    ("init_place", [], C("Ch. 5, § 2.K", 89)),
    ("nonacademic", [], C("Ch. 1, § 2.E", 36)),
    ("daily_living", [], C("Ch. 5, § 2.F", 80)), ("trans_assess", [], C("Ch. 5, § 2.F", 80)),
    ("primary_disability", [], C("Ch. 4, § 3.M", 67)),
    ("plaafp", [("PLEP", A, WV)], C("Ch. 5, § 2.D", 78)),
    ("referral", [], PS(43)), ("foster", [], PS(11)), ("lep", [], PS(9)), ("public_agency", [], PS(21)),
    # Procedural safeguards notice
    ("pwn", [], PS(8)), ("consent", [], PS(10)), ("ward", [], PS(11)), ("revoke", [], PS(10)),
    ("equitable", [], PS(13)), ("iee", [], PS(13)), ("ed_records", [], PS(15)), ("ferpa", [], PS(16)),
    ("pii", [], PS(16)), ("part_agency", [], PS(16)), ("child_find", [], PS(17)), ("record_access", [], PS(17)),
    ("age_majority", [], PS(19)), ("native_language", [], PS(9)), ("comm_mode", [], PS(9)),
    ("iep_facil", [], PS(20)), ("adr", [], PS(23)), ("pti", [], PS(23)), ("cprc", [], PS(23)),
    ("state_complaint", [], PS(21)), ("mediation", [], PS(21)), ("dp_complaint", [], PS(21)),
    ("stay_put", [], PS(29)), ("part_c_transition", [], PS(29)), ("resolution", [], PS(30)),
    ("dp_hearing", [], PS(32)), ("s504", [], PS(35)), ("ada", [], PS(35)),
    ("code_conduct", [], PS(37)), ("school_day", [], PS(37)), ("iaes", [], PS(38)), ("gen_curr", [], PS(38)),
    ("mdr", [], PS(39)), ("fba", [], PS(39)), ("bip", [], PS(39)), ("special_circ", [], PS(39)),
    ("weapon", [], PS(40)), ("controlled", [], PS(40)), ("sbi", [], PS(40)), ("cop", [], PS(40)),
    ("exp_hearing", [], PS(41)), ("basis_know", [], PS(43)),
    ("unilateral_pl", [], PS(44)),
]

CONCEPTS = [
    # state agencies, boards and organizations
    ("wv_wvde", "West Virginia Department of Education", "legal_procedural", [("WVDE", A, WV)], AC(11),
     {**WVJ, "broader": "sea", "note": "The state educational agency; the rule and notice both call it WVDE."}),
    ("wv_wvbe", "West Virginia Board of Education", "legal_procedural", [("WVBE", A, WV)], AC(11),
     {**WVJ, "note": "The state board that adopts Policy 2419 and oversees the department."}),
    ("wv_dhhr", "West Virginia Department of Health and Human Resources", "legal_procedural",
     [("WVDHHR", A, WV)], D(23),
     {**WVJ, "note": "The lead agency for Part C early intervention in West Virginia."}),
    ("wv_birth_to_three", "WV Birth to Three", "early_intervention",
     [], C("Ch. 2, § 2.A", 37),
     {**WVJ, "note": "The state's Part C early intervention program for infants and toddlers."}),
    ("wv_osp", "West Virginia Department of Education, Office of Special Education", "legal_procedural", [], PS(24),
     {**WVJ, "broader": "wv_wvde", "note": "The department office where state complaints and other dispute filings are sent."}),
    ("wv_dfps", "Division of Federal Programs & Support", "legal_procedural",
     [], PS(50),
     {**WVJ, "broader": "wv_wvde", "note": "The department division named on the notice's contact page."}),
    ("wv_advisory_council", "West Virginia Advisory Council for the Education of Exceptional Children",
     "legal_procedural", [], PS(34),
     {**WVJ, "broader": "state_panel", "note": "The state advisory panel that receives hearing findings with identifying details removed."}),
    ("wv_pti", "West Virginia Parent Training and Information", "legal_procedural", [("WVPTI", A, WV)], PS(5),
     {**WVJ, "broader": "pti", "note": "The state parent training and information center named in the notice."}),
    ("wv_perc", "Parent/Educator Resource Center", "legal_procedural", [], PS(50),
     {**WVJ, "note": "A local parent resource contact the notice lists next to the district special education director."}),
    ("wv_drs", "West Virginia Division of Rehabilitation Services", "transition", [], D(24),
     {**WVJ, "note": "The state vocational rehabilitation agency that shares pre-employment transition services with schools."}),
    ("wv_wvsdb", "West Virginia Schools for the Deaf and the Blind", "placement_setting", [], C("Ch. 4, § 2", 50),
     {**WVJ, "broader": "state_sp_sch", "note": "State schools whose options must be shared when a student meets certain sensory eligibility criteria."}),
    ("wv_sdt", "West Virginia Schools of Diversion and Transition", "placement_setting", [], C("Ch. 3, § 3.D", 46),
     {**WVJ, "note": "State-run schools the rule names when it allows records to move without parent consent."}),
    ("wv_registry", "West Virginia Registry of Interpreters", "personnel_role", [], C("Ch. 9, § 3.A", 126),
     {**WVJ, "note": "The registry whose renewal costs the employer pays for educational sign language interpreters."}),
    # policies and statewide systems
    ("wv_policy_2419", "Policy 2419", "legal_procedural",
     [("Policy 2419: Regulations for the Education of Students with Exceptionalities", S, WV),
      ("Regulations for the Education of Students with Exceptionalities", S, WV),
      ("West Virginia Procedures Manual for the Education of Students with Exceptionalities", S, WV),
      ("126CSR16", AB, WV)], C("§ 126-16-1.5", "2 (also § 126-16-3.1, p. 3)"),
     {**WVJ, "note": "The state board rule that sets special education procedures in West Virginia."}),
    ("wv_policy_4350", "Policy 4350", "legal_procedural",
     [("Procedures for the Collection, Maintenance and Disclosure of Student Information", S, WV),
      ("Regulations for the Collection, Maintenance and Disclosure of Student Data", S, WV)], PS("8 (also p. 16)"),
     {**WVJ, "note": "The state board policy on student records and confidentiality."}),
    ("wv_policy_4373", "Policy 4373", "discipline",
     [("Expected Behavior in Safe and Supportive Schools", S, WV)], D(17),
     {**WVJ, "note": "The state board policy that sets the student code of conduct."}),
    ("wv_wveis", "West Virginia Education Information System", "legal_procedural", [("WVEIS", A, WV)], AC(11),
     {**WVJ, "note": "The statewide student record system where consent dates and special education data are kept."}),
    ("wv_online_iep", "WVDE Online IEP", "iep_component", [("Online IEP", S, WV)], C("Ch. 5, § 2", 77),
     {**WVJ, "broader": "iep", "note": "The state's required online system for writing and finalizing IEPs."}),
    ("wv_taaes", "Temporary Assessment Accommodations Entry System", "accommodation_modification",
     [("TAAES", A, WV)], C("Ch. 5, § 4.B", "91 (also p. 92)"),
     {**WVJ, "note": "The tool used to enter test accommodations from an out-of-state IEP until eligibility is decided."}),
    ("wv_rcsp", "West Virginia Results and Compliance System Procedures", "legal_procedural",
     [("RCSP", A, WV)], C("Ch. 9, § 2", "121 (also p. 122)"),
     {**WVJ, "note": "The state monitoring process in which districts submit self-assessment data."}),
    ("wv_wvtss", "West Virginia Tiered System of Support", "evaluation_eligibility", [("WVTSS", A, WV)],
     C("Ch. 4, § 3.L, MTSS", 62),
     {**WVJ, "broader": "mtss", "note": "The state's multi-tiered framework used before an SLD decision."}),
    ("wv_wvmap", "West Virginia Measures of Academic Progress", "iep_component", [("WV-MAP", A, WV)], AC(11),
     {**WVJ, "note": "The state's statewide assessment program that the IEP team plans participation in."}),
    ("wv_wvgsa", "West Virginia General Summative Assessment", "iep_component", [("WVGSA", A, WV)],
     C("Ch. 9, § 2.C", 124), {**WVJ, "broader": "wv_wvmap"}),
    ("wv_alt_summative", "West Virginia Alternate Summative Assessment", "iep_component",
     [("WV Alternate Assessment", S, WV), ("West Virginia Alternate Assessment", S, WV)],
     C("Ch. 9, § 2.C", "124 (also Ch. 5, § 2.I, p. 84)"),
     {**WVJ, "broader": "alt_assess", "note": "The alternate statewide test for students who cannot take the general test."}),
    ("wv_participation_guidelines", "Participation Guidelines for West Virginia State Assessments", "iep_component", [],
     C("Ch. 5, § 2.I", 84),
     {**WVJ, "note": "The state guide to allowable testing accommodations."}),
    ("wv_ccrs", "West Virginia College- and Career-Readiness Standards", "iep_component", [("CCRS", A, WV)],
     D("17 (also Ch. 4, p. 50)"), {**WVJ, "note": "The grade-level standards that the general curriculum is built on."}),
    ("wv_aaas", "West Virginia Alternate Academic Achievement Standards", "iep_component",
     [("Policy 2520.16", REL, WV)], C("Ch. 5, § 2.E", "79 (also Ch. 1, § 3, p. 36)"),
     {**WVJ, "broader": "alt_assess", "note": "The standards for students taught on the alternate curriculum; each goal needs at least two objectives."}),
    ("wv_prek", "West Virginia Pre-K", "placement_setting", [("Universal Pre-K", S, WV)], C("Ch. 6, § 3", "96 (also Ch. 5, p. 75)"),
     {**WVJ, "note": "The state's pre-kindergarten system, including classrooms that serve students with IEPs."}),
    ("wv_b8_survey", "IDEA Indicator B-8 Parent Involvement Survey", "legal_procedural", [], PS(5),
     {**WVJ, "note": "A statewide survey mailed to parents of students receiving special education."}),
    # eligibility, evaluation and reports
    ("wv_ec_report", "Eligibility Committee Report", "evaluation_eligibility", [("EC Report", S, WV)],
     C("Ch. 4, § 2", 50), {**WVJ, "broader": "eligibility"}),
    ("wv_sld_team_report", "SLD Team Report", "evaluation_eligibility", [], C("Ch. 4, § 3.L", 65),
     {**WVJ, "broader": "sld", "note": "The written report the eligibility committee completes for a suspected learning disability."}),
    ("wv_reeval_determination", "Reevaluation Determination form", "evaluation_eligibility", [], C("Ch. 3, § 2.B", 43),
     {**WVJ, "broader": "reeval"}),
    ("wv_eval_request_notice", "Notice of Individual Evaluation/Reevaluation Request", "evaluation_eligibility", [],
     C("Ch. 3, § 3.A", 44), {**WVJ, "note": "The form sent with prior written notice when the district asks to evaluate."}),
    ("wv_three_prong", "Three-prong test of eligibility", "evaluation_eligibility",
     [("three-pronged test of eligibility", V, WV)], C("Ch. 4, § 3", 51),
     {**WVJ, "broader": "eligibility", "note": "The state's test: meets criteria, adverse effect, and needs special education."}),
    ("wv_primary_exceptionality", "Primary exceptionality", "evaluation_eligibility", [], C("Ch. 4, § 1", 50),
     {**WVJ, "broader": "exceptionality",
      "note": "Kept apart from primary_disability because a West Virginia exceptionality includes giftedness; the rule uses both terms."}),
    ("wv_psych_adjustment", "Psychological adjustment disorder", "evaluation_eligibility", [], D(25),
     {**WVJ, "note": "One way a student can qualify as exceptional gifted, documented by a psychological evaluation."}),
    ("wv_underachievement", "Underachievement", "evaluation_eligibility", [], D(31),
     {**WVJ, "flags": ["common_english_word"], "note": "Defined as performance well below ability; also a route to exceptional gifted."}),
    ("wv_hurgp", "Historically under-represented gifted population", "evaluation_eligibility", [], D(18),
     {**WVJ, "broader": "gifted"}),
    ("wv_fle", "Functional Listening Evaluation", "evaluation_eligibility", [("FLE", A, WV)], D(17),
     {**WVJ, "note": "An assessment of how noise, distance and visual input affect a student's listening."}),
    ("wv_severity_levels", "Severity Levels for Adaptive Functioning", "evaluation_eligibility", [],
     C("Appendix, DSM-5 table", 153), {**WVJ, "broader": "id"}),
    ("wv_fcas", "Functional Communication Assessment Summary", "instrument", [], C("Ch. 4, § 3.M", 67),
     {**WVJ, "note": "A form for speech-language eligibility for students who cannot take standard tests."}),
    ("wv_spas", "Speech Production Assessment Summary", "instrument", [], C("Ch. 4, § 3.M", 67),
     {**WVJ, "broader": "artic"}),
    ("wv_vas", "Voice Assessment Summary", "instrument", [], C("Ch. 4, § 3.M", 71), {**WVJ, "broader": "voice"}),
    ("social_comm_dis", "Social communication disorder", "health_condition", [], C("Ch. 4, § 3.M", 70),
     {"note": "A DSM-5 communication disorder the rule gives its own eligibility criteria."}),
    ("cluttering", "Cluttering", "health_condition", [], C("Ch. 4, § 3.M", 68),
     {"broader": "fluency_dis", "note": "A fluency disorder with rapid, disorganized speech."}),
    ("cognitive_referencing", "Cognitive referencing", "evaluation_eligibility", [], C("Ch. 4, § 3.M", 72),
     {"note": "Denying speech-language services because language matches cognitive level."}),
    ("language_sample", "Language sample analysis", "evaluation_eligibility", [], C("Ch. 4, § 3.M", 66),
     {"broader": "lang_dis"}),
    ("dynamic_assessment", "Dynamic assessment", "evaluation_eligibility", [], C("Ch. 4, § 3.M", 67),
     {"note": "A test-teach-retest approach used to tell a language difference from a disorder."}),
    ("pcc", "Percentage of consonants correct", "score_metric", [], C("Ch. 4, § 3.M", 68),
     {"broader": "artic"}),
    ("dsm5", "Diagnostic and Statistical Manual of Mental Disorders", "instrument", [("DSM-5", A, None)],
     C("Ch. 4, § 3.A", 52), {"note": "The diagnostic manual the autism and speech criteria are based on."}),
    # placements and service delivery
    ("wv_geft", "General Education: Full-Time", "placement_setting",
     [("GEFT", A, WV), ("General Education Full-Time", V, WV)], D(18),
     {**WVJ, "broader": "regular_class", "note": "Services mostly inside general education for 80 percent or more of the day."}),
    ("wv_gept", "General Education: Part-Time", "placement_setting",
     [("GEPT", A, WV), ("General Education Part-Time", V, WV)], D(18),
     {**WVJ, "broader": "resource_room", "note": "Services in general education for 40 to 79 percent of the day."}),
    ("wv_separate_class", "Special Education: Separate Class", "placement_setting", [], C("Ch. 5, § 2.J", 86),
     {**WVJ, "broader": "special_class", "note": "Less than 40 percent of the day in general education."}),
    ("wv_out_of_school_env", "Special Education: Out-of-School Environment", "placement_setting", [],
     C("Ch. 5, § 2.J", 87), {**WVJ, "note": "Services in a non-school place such as a hospital or the home."}),
    ("wv_correctional", "Special Education: Correctional Facilities", "placement_setting", [],
     C("Ch. 5, § 2.J", 87), {**WVJ}),
    ("service_provider_location", "Service provider location", "placement_setting", [], C("Ch. 5, § 2.J", 88),
     {"note": "A preschool placement where all services come from a provider outside school."}),
    ("wv_see", "Special education environment", "placement_setting", [("SEE", A, WV)], C("Ch. 5, § 2.G", 83),
     {**WVJ, "flags": ["common_english_word"],
      "note": "The IEP lists a service location as SEE or GEE."}),
    ("wv_shared_models", "Shared instructional models", "placement_setting", [], D(28),
     {**WVJ, "note": "Co-teaching and consultation models shared by general and special educators."}),
    ("wv_case_mgmt", "Case management", "personnel_role", [], D(14),
     {**WVJ, "note": "The paperwork and scheduling duties assigned to a special education teacher."}),
    ("wv_close_supervision", "Close adult supervision", "related_service", [], D(14),
     {**WVJ, "note": "Staff support so a student can reach IEP goals and stay in the least restrictive setting."}),
    ("wv_pep", "Personalized Education Plan", "transition", [("PEP", A, WV)], D(23),
     {**WVJ, "note": "A course and career plan that a gifted student not found exceptional gifted continues on."}),
    ("wv_targeted_iep", "Targeted IEP review", "iep_component",
     [("Targeted IEP meeting", S, WV), ("targeted IEP", AB, WV)], D(30),
     {**WVJ, "broader": "annual_review", "note": "A meeting that reviews one part of an IEP without moving the annual review date."}),
    ("wv_in_lieu", "IEP Team Member In-Lieu-of Attendance Report", "iep_component",
     [("In-Lieu of Attendance Report", V, WV)], C("Ch. 5, § 1.D", 76),
     {**WVJ, "note": "A written input form from a team member who is excused from a meeting."}),
    ("wv_darf", "Disciplinary Action Review Form", "discipline", [("DARF", A, WV)], AC(10),
     {**WVJ, "note": "The form that records service decisions and pattern-of-removal reviews."}),
    ("expulsion", "Expulsion", "discipline", [], D(17), {}),
    # dispute resolution
    ("wv_early_resolution", "Early resolution", "legal_procedural", [], PS(26),
     {**WVJ, "broader": "state_complaint", "note": "A voluntary local conference to settle a state complaint within 15 days."}),
    ("wv_ver_early_resolution", "Verification of Early Resolution", "legal_procedural", [], PS(26),
     {**WVJ, "broader": "wv_early_resolution"}),
    ("meeting_encourage_mediation", "Meeting to encourage mediation", "legal_procedural", [], C("Ch. 11, § 3.C", 140),
     {"broader": "mediation"}),
    ("agreement_review_period", "Agreement review period", "legal_procedural", [], PS(32),
     {"broader": "resolution", "note": "Either side may void a resolution agreement within three business days."}),
    ("attorneys_fees", "Attorneys' fees", "legal_procedural", [], PS(36), {}),
    ("civil_action", "Civil action", "legal_procedural", [], PS(35), {}),
    ("destruction_pii", "Destruction of information", "legal_procedural", [], PS(20), {"broader": "ed_records"}),
    ("public_benefits_consent", "Parental consent to access public benefits or insurance", "legal_procedural",
     [("public benefits or insurance", S, None)], PS(47),
     {"note": "The annual notice and consent before a district bills Medicaid or similar coverage."}),
    ("general_supervision", "General supervision", "legal_procedural", [], C("Ch. 9, § 1", 117), {}),
    ("spp", "State Performance Plan", "legal_procedural", [("SPP", A, None)], C("Ch. 9, § 1.B", 120), {}),
    ("apr", "Annual Performance Report", "legal_procedural", [("APR", A, None)], C("Ch. 9, § 1.B", 120), {}),
    # personnel and supports
    ("intervener", "Intervener", "personnel_role", [], D(19),
     {"note": "A specially trained one-to-one person who helps a student who is deafblind."}),
    ("wv_esli", "Educational Sign Language Interpreter", "personnel_role",
     [("educational sign language interpreter I", REL, WV), ("educational sign language interpreter II", REL, WV)],
     D("16 (also Ch. 9, § 3.A, p. 126)"),
     {**WVJ, "broader": "edu_interpreter"}),
    ("wv_sign_support", "Sign Support Specialist", "personnel_role", [], D(28),
     {**WVJ, "note": "A person who provides signed support in place of an interpreter when none is available."}),
    ("wv_eccat", "Early Childhood Classroom Assistant Teacher", "personnel_role", [("ECCAT", A, WV)], AC(10),
     {**WVJ}),
    ("aprn", "Advanced practice registered nurse", "personnel_role", [("APRN", A, None)], D(20), {}),
    ("physician_assistant", "Physician assistant", "personnel_role",
     [("physician's assistant", S, None)], D(20), {}),
    ("pre_ets", "Pre-employment transition services", "transition", [("Pre-ETS", A, None)], D(24), {}),
    ("supported_employment", "Supported employment", "transition", [], D(30), {}),
    ("hats", "Hearing assistive technology system", "accommodation_modification", [("HATS", A, None)],
     C("Ch. 5, § 2.G", 81), {}),
    ("cic", "Clean intermittent catheterization", "related_service", [("CIC", A, None)], D(26), {}),
]

JURISDICTION = "US-WV"
LAYER_NAME = "West Virginia"
# Documents listed in sources/documents.tsv that no record cites, and why.
UNCITED_DOCS = {"us-osepqa2301-2023": "Federal OSEP document; corroboration only, no record cites it."}

RETRIEVED = "2026-10-09"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.43.0"  # tools/add_state.py sets this
