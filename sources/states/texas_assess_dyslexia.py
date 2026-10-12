"""
Texas layer, wave 2: state assessment and dyslexia vocabulary.

Sources reviewed 2026-10-03:
  ALT2  TEA, STAAR Alternate 2 Educator Guide, 2025-2026
  ACC   TEA, STAAR Accommodations Educator Guide, 2025-2026
  DH    TEA/SBOE, The Dyslexia Handbook: Procedures Concerning Dyslexia and
        Related Disorders, 2024 Update (effective August 2024)

All page references come from a text extraction of the PDFs, so every
record here is 'candidate' until a person checks the page. The Chapter 4
and 5 page numbers in the handbook were the least certain and are noted.
"""

ALT2_URL = "https://tea2.tea.texas.gov/data-reports/test-administration/2025-2026-staar-alternate-2-educator-guide.pdf"
ACC_URL = "https://tea.texas.gov/data-reports/test-administration/2025-2026-staar-accommodations-educator-guide.pdf"
DH_URL = "https://tea.texas.gov/academics/special-student-populations/special-education/texas-dyslexia-handbook.pdf"


def src(doc, loc):
    title, url = {
        "ALT2": ("TEA STAAR Alternate 2 Educator Guide (2025-26)", ALT2_URL),
        "ACC": ("TEA STAAR Accommodations Educator Guide (2025-26)", ACC_URL),
        "DH": ("TEA Dyslexia Handbook (2024 update)", DH_URL),
    }[doc]
    return {"source_type": "state_guidance", "citation": f"{title}, {loc}", "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
TX = ["US-TX"]
TXJ = {"jurisdiction": "US-TX"}

STRINGS = [
    ("alt_assess", [], src("ALT2", "p. 5")),
    ("test_accom", [("testing accommodations", S, None), ("STAAR accommodations", REL, TX)], src("ACC", "p. 6")),
    ("teks", [], src("ALT2", "p. 19")),
    ("lpac", [], src("ACC", "p. 34")),
    ("sst", [("student assistance team", S, None)], src("ACC", "p. 34")),
    ("s504", [("Section 504 committee", S, None), ("individual accommodation plan", REL, TX), ("IAP", A, TX)], src("ACC", "p. 34")),
    ("lep", [("EB", A, TX)], src("ACC", "p. 34")),
    ("plaafp", [], src("ALT2", "p. 6")),
    ("adaptive", [("adaptive behavior deficits", S, None)], src("ALT2", "p. 6")),
    ("dyslexia", [], src("DH", "p. 7")),
    ("related_dis", [("dyslexia and related disorders", S, None)], src("DH", "p. 7")),
    ("evaluation", [("full individual and initial evaluation", V, TX)], src("DH", "pp. 25-26")),
    ("dys_instr", [("direct dyslexia instruction", S, TX), ("standard protocol dyslexia instruction", L, TX), ("standard protocol", AB, TX)], src("DH", "p. 6")),
    ("dys_handbook", [("The Dyslexia Handbook", S, TX), ("Procedures Concerning Dyslexia and Related Disorders", S, TX)], src("DH", "title page")),
    ("multisensory", [("simultaneous multisensory instruction", S, None), ("multisensory approach", S, None)], src("DH", "p. 38")),
    ("explicit", [("systematic and cumulative instruction", S, None), ("systematic direct instruction", S, None), ("systematic instruction", S, None)], src("DH", "p. 38")),
    ("rti", [("tiered intervention process", S, None)], src("DH", "p. 23")),
    ("srbi", [("targeted intervention", S, None)], src("DH", "p. 18")),
    ("screening", [], src("DH", "p. 14")),
    ("progress", [], src("DH", "p. 18")),
    ("fluency", [], src("DH", "p. 30")),
    ("reading_comp", [], src("DH", "p. 30")),
    ("written_expr", [], src("DH", "p. 30")),
    ("listen_comp", [], src("DH", "p. 30")),
    ("sld", [], src("DH", "p. 31")),
    ("sdi", [], src("DH", "p. 31")),
    ("ot", [], src("DH", "ch. 5")),
    ("prr", [], src("DH", "p. 38")),
]

CONCEPTS = [
    # --- State assessments ---
    ("staar", "State of Texas Assessments of Academic Readiness", "iep_component", [("STAAR", A, TX)], src("ALT2", "p. 5"), TXJ),
    ("staar_alt2", "STAAR Alternate 2", "iep_component", [("STAAR Alt 2", AB, TX), ("STAAR Alt", AB, TX)], src("ALT2", "p. 5"),
     {**TXJ, "broader": "alt_assess", "note": "Texas's alternate assessment for students with the most significant cognitive disabilities."}),
    ("staar_sp", "STAAR Spanish", "iep_component", [], src("ACC", "p. 38"), {**TXJ, "broader": "staar"}),
    ("eoc", "End-of-course assessment", "iep_component", [("EOC", A, None), ("end-of-course", AB, None)], src("ALT2", "p. 5"), {}),
    ("telpas", "Texas English Language Proficiency Assessment System", "iep_component", [("TELPAS", A, TX)], src("DH", "p. 28"), TXJ),
    ("telpas_alt", "TELPAS Alternate", "iep_component", [], src("ALT2", "p. 7"), {**TXJ, "broader": "telpas"}),
    ("sig_cog", "Most significant cognitive disability", "evaluation_eligibility", [("most significant cognitive disabilities", P, None), ("significant cognitive disability", S, None)], src("ALT2", "p. 6"),
     {"note": "Federal ESSA term for students eligible for an alternate assessment."}),
    ("alt2_partreq", "STAAR Alternate 2 Participation Requirements form", "iep_component", [("participation requirements", AB, TX)], src("ALT2", "p. 6"), {**TXJ, "broader": "staar_alt2"}),
    ("med_exc", "Medical exception", "iep_component", [("medical exception eligibility requirements", S, TX)], src("ALT2", "p. 7"), {**TXJ, "broader": "staar_alt2"}),
    ("naar", "No authentic academic response", "iep_component", [("NAAR", A, TX)], src("ALT2", "p. 7"), {**TXJ, "broader": "staar_alt2"}),
    ("prereq", "Prerequisite skills", "academic_skill", [("prerequisite skill", P, None)], src("ALT2", "p. 6"), {}),
    ("essence", "Essence statement", "academic_skill", [("essence statements", P, TX), ("strand statement", S, TX)], src("ALT2", "p. 20"), TXJ),
    ("resp_mode", "Response mode", "accommodation_modification", [("student response mode", S, None)], src("ALT2", "pp. 14-16"), {}),
    ("tide", "Test Information Distribution Engine", "legal_procedural", [("TIDE", A, TX)], src("ACC", "p. 7"),
     {**TXJ, "flags": ["common_english_word"], "note": "'TIDE' is protected only as an all-caps match."}),
    ("peims", "Public Education Information Management System", "legal_procedural", [("PEIMS", A, TX)], src("DH", "p. 18"), TXJ),

    # --- Accessibility tiers and supports (STAAR Accommodations Educator Guide) ---
    ("acc_feat", "Accessibility features", "accommodation_modification", [("accessibility feature", P, None)], src("ACC", "p. 8"), {"broader": "test_accom"}),
    ("des_sup", "Designated supports", "accommodation_modification", [("designated support", P, None), ("locally-approved designated supports", REL, TX),
                                                                    ("designated supports requiring TEA approval", REL, TX)], src("ACC", "pp. 7, 16"),
     {"broader": "test_accom", "note": "TEA's tier names for testing supports; the guide still uses 'accommodations' for the decisions."}),
    ("acc_req", "Accommodation Request Form", "accommodation_modification", [], src("ACC", "p. 7"), {**TXJ, "broader": "des_sup"}),
    ("tts", "Text-to-speech", "accommodation_modification", [("TTS", A, None), ("auto text-to-speech", S, None)], src("ACC", "pp. 17-19"), {"broader": "des_sup"}),
    ("stt", "Speech-to-text", "accommodation_modification", [("STT", A, None)], src("ACC", "p. 20"), {"broader": "des_sup"}),
    ("word_pred", "Word prediction", "accommodation_modification", [], src("ACC", "p. 22"), {"broader": "des_sup"}),
    ("spell_check", "Spell check", "accommodation_modification", [("spelling assistance", S, None)], src("ACC", "pp. 23, 34"), {"broader": "des_sup"}),
    ("calc_aids", "Calculation aids", "accommodation_modification", [("calculator", AB, None)], src("ACC", "pp. 16, 34"), {"broader": "des_sup"}),
    ("asl", "American Sign Language", "accommodation_modification", [("ASL", A, None), ("ASL videos", S, None)], src("ACC", "p. 24"), {"broader": "des_sup"}),
    ("rbd", "Refreshable braille display", "accommodation_modification", [], src("ACC", "p. 25"),
     {"broader": "des_sup", "flags": ["eponym"], "note": "Contains 'braille'; protected only as the full phrase."}),
    ("cls", "Content and language supports", "accommodation_modification", [("pop-ups", S, None), ("rollovers", S, None), ("prereading", S, None)], src("ACC", "pp. 26-30"),
     {"broader": "des_sup"}),
    ("supp_mat", "Supplementary materials", "accommodation_modification", [("writing checklist", S, None)], src("ACC", "p. 30"), {"broader": "cls"}),
    ("extra_day", "Extra day", "accommodation_modification", [], src("ACC", "p. 7"), {**TXJ, "broader": "des_sup", "note": "Requires TEA approval."}),
    ("complex_tr", "Complex transcribing", "accommodation_modification", [], src("ACC", "p. 7"), {**TXJ, "broader": "des_sup"}),
    ("basic_tr", "Basic transcribing", "accommodation_modification", [], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("math_scribe", "Mathematics scribe", "accommodation_modification", [("scribe", AB, None)], src("ACC", "p. 7"), {"broader": "des_sup"}),
    ("isr", "Individualized structured reminders", "accommodation_modification", [("structured reminders", AB, None)], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("large_print", "Large print", "accommodation_modification", [("large-print", V, None)], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("manip_mat", "Manipulating test materials", "accommodation_modification", [], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("math_manip", "Mathematics manipulatives", "accommodation_modification", [("math manipulatives", S, None)], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("oral_admin", "Oral and signed administration", "accommodation_modification", [("oral administration", AB, None), ("signed administration", AB, None)], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("supp_aids", "Supplemental aids", "accommodation_modification", [], src("ACC", "p. 34"), {"broader": "des_sup"}),
    ("line_reader", "Line reader", "accommodation_modification", [], src("ACC", "p. 11"), {"broader": "acc_feat"}),

    # --- Dyslexia and dysgraphia (Dyslexia Handbook, 2024 update) ---
    ("dysgraphia", "Dysgraphia", "health_condition", [("developmental dysgraphia", S, None)], src("DH", "p. 7; ch. 5"), {"broader": "related_dis"}),
    ("dys_screen", "Dyslexia screening", "evaluation_eligibility", [("kindergarten and first grade screening", REL, TX)], src("DH", "p. 14"), {"broader": "screening"}),
    ("reading_instr", "Reading instrument", "evaluation_eligibility", [("Commissioner's List of Reading Instruments", REL, TX)], src("DH", "p. 13"), TXJ),
    ("at_risk_dys", "At risk for dyslexia", "evaluation_eligibility", [], src("DH", "p. 18"), {}),
    ("mdt", "Multidisciplinary team", "personnel_role", [("MDT", A, None)], src("DH", "p. 28"), {}),
    ("ldt", "Licensed dyslexia therapist", "personnel_role", [("LDT", A, TX)], src("DH", "p. 28"), TXJ),
    ("calt", "Certified academic language therapist", "personnel_role", [("CALT", A, None)], src("DH", "p. 28"),
     {"note": "'CALT' is practitioner usage, not from the handbook."}),
    ("dys_provider", "Provider of dyslexia instruction", "personnel_role", [("providers of dyslexia instruction", P, TX)], src("DH", "p. 28"), TXJ),
    ("tda", "Texas Dyslexia Academies", "legal_procedural", [("TDAs", A, TX)], src("DH", "p. 28"), TXJ),
    ("rbd_prog", "Reading by Design", "academic_skill", [("Texas Dyslexia Program", S, TX)], src("DH", "p. 43"), {**TXJ, "note": "Page from the least certain part of the extraction."}),
    ("ida", "International Dyslexia Association", "legal_procedural", [("IDA", A, None)], src("DH", "p. 7"), {}),
    ("alta", "Academic Language Therapy Association", "legal_procedural", [("ALTA", A, None)], src("DH", "p. 28"), {}),
    ("imslec", "International Multisensory Structured Language Education Council", "legal_procedural", [("IMSLEC", A, None)], src("DH", "p. 28"), {}),
    ("twice_ex", "Twice-exceptional", "evaluation_eligibility", [("2e", A, None), ("twice exceptional", V, None)], src("DH", "p. 21"), {"broader": "gifted"}),
    ("three_cue", "Three-cueing", "academic_skill", [("three-cueing system", S, None)], src("DH", "p. 8"),
     {"note": "Texas law bars three-cueing in K-3 phonics instruction (TEC §28.0062)."}),
    ("accel_read", "Accelerated reading instruction", "academic_skill", [("accelerated reading program", S, TX), ("intensive reading program", S, TX)], src("DH", "p. 13"), TXJ),
    ("tier1", "Tier 1 instruction", "academic_skill", [("core reading instruction", S, None), ("Tier 2", AB, None), ("Tier 3", AB, None)], src("DH", "p. 18"), {"broader": "rti"}),

    # Evaluation domains (DH Figure 3.4)
    ("phon_aware", "Phonological awareness", "academic_skill", [("phonemic awareness", S, None), ("phonological/phonemic awareness", V, None), ("phonological processing", S, None)], src("DH", "pp. 7, 30"), {}),
    ("phon_mem", "Phonological memory", "academic_skill", [], src("DH", "p. 7"), {}),
    ("ran", "Rapid automatized naming", "academic_skill", [("rapid naming", S, None), ("RAN", A, None), ("rapid naming of symbols or objects", S, None)], src("DH", "pp. 7, 32"), {}),
    ("orth_proc", "Orthographic processing", "academic_skill", [("memory for letter or symbol sequences", S, None), ("orthographic coding", S, None)], src("DH", "p. 30"), {}),
    ("letter_know", "Letter knowledge", "academic_skill", [("letter-sound knowledge", S, None), ("letter naming fluency", S, None), ("letter sounds knowledge", V, None)], src("DH", "pp. 16, 30"), {}),
    ("decoding", "Decoding", "academic_skill", [("decoding unfamiliar words", S, None)], src("DH", "p. 30"), {}),
    ("word_recog", "Word recognition", "academic_skill", [("reading words in isolation", S, None), ("word reading accuracy", S, None)], src("DH", "pp. 7, 16"), {}),
    ("prosody", "Prosody", "academic_skill", [], src("DH", "p. 30"), {"broader": "fluency"}),
    ("vwm", "Verbal working memory", "evaluation_eligibility", [("working memory", AB, None)], src("DH", "p. 30"), {}),
    ("proc_speed", "Processing speed", "evaluation_eligibility", [], src("DH", "p. 30"), {}),
    ("spelling", "Spelling", "academic_skill", [], src("DH", "p. 30"), {}),

    # Instruction components and delivery (DH ch. 4)
    ("ssa", "Sound-symbol association", "academic_skill", [("sound-symbol correspondence", S, None)], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("syllab", "Syllabication", "academic_skill", [("syllabification", V, None)], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("orthography", "Orthography", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("morphology", "Morphology", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("syntax", "Syntax", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("diag_teach", "Diagnostic teaching", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("synthetic", "Synthetic instruction", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),
    ("analytic", "Analytic instruction", "academic_skill", [], src("DH", "p. 38"), {"broader": "dys_instr"}),

    # Dysgraphia evaluation and instruction (DH ch. 5)
    ("handwriting", "Handwriting", "academic_skill", [("handwriting instruction", S, None)], src("DH", "pp. 30, 60"), {"broader": "dysgraphia"}),
    ("legibility", "Legibility", "academic_skill", [], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("letter_form", "Letter formation", "academic_skill", [], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("graphomotor", "Graphomotor skills", "functional_skill", [("graphomotor", AB, None)], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("fine_motor", "Fine motor skills", "functional_skill", [("fine motor control", S, None)], src("DH", "ch. 5"), {}),
    ("motor_plan", "Motor planning", "functional_skill", [], src("DH", "ch. 5"), {}),
    ("transcription", "Transcription skills", "academic_skill", [("transcription", AB, None)], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("keyboarding", "Keyboarding", "accommodation_modification", [], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("sentence_con", "Sentence construction", "academic_skill", [], src("DH", "ch. 5"), {"broader": "dysgraphia"}),
    ("ext_time", "Extended time", "accommodation_modification", [("extended time on tests", S, None), ("time and a half", S, None)], src("DH", "ch. 5"), {}),
]

JURISDICTION = "US-TX"
LAYER_NAME = "Texas (assessment and dyslexia)"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.4.0"
