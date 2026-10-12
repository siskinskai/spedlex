"""
Texas layer for SPEDLex.

Sources reviewed 2026-10-03:
  NPS  TEA, Notice of Procedural Safeguards, January 2025 (English, accessible PDF)
  ARD  TEA, Parent's Guide to the Admission, Review, and Dismissal Process, January 2025
  TAC  19 Tex. Admin. Code §89.1040 (Eligibility Categories), amended eff. July 30, 2024

Page numbers for NPS/ARD come from a text extraction of the PDFs, not a
human read, so every record that relies on them is review status
'candidate' until someone checks the page. TAC citations were read from
the rule text and are 'machine_validated'.

Two kinds of entries:
  TX_STRINGS   Texas surface forms attached to an existing concept. They get
               regional=["US-TX"] unless the form is national usage.
  TX_CONCEPTS  New concepts. jurisdiction is US-TX for Texas-only things
               (forms, agencies, Texas rules) and US for national concepts
               that the federal seed simply missed.
"""

NPS_URL = "https://spedtex.tea.texas.gov/sites/spedtex.tea.texas.gov/files/2026-05/English%20Notice%20of%20Procedural%20Safeguards%20-%20English%202025%20ACC.pdf"
ARD_URL = "https://spedtex.tea.texas.gov/sites/spedtex.tea.texas.gov/files/2026-05/ARD%20Guide%202025%20-%20English%20-%20ACC.pdf"
TAC_URL = "https://www.law.cornell.edu/regulations/texas/19-Tex-Admin-Code-SS-89-1040"

DOCS = {
    "NPS": ("procedural_safeguards_notice", "TEA Notice of Procedural Safeguards (Jan. 2025)", NPS_URL),
    "ARD": ("state_guidance", "TEA Parent's Guide to the ARD Process (Jan. 2025)", ARD_URL),
    "TAC": ("state_regulation", "19 TAC §89.1040", TAC_URL),
}


def src(doc, loc):
    """('ARD', 'p. 14') -> source dict fields (retrieved is added by the builder)."""
    stype, title, url = DOCS[doc]
    cit = f"{title}{loc}" if doc == "TAC" else f"{title}, {loc}"
    return {"source_type": stype, "citation": cit, "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
TX = ["US-TX"]

# (existing concept key, [(text, string_type, regional or None)], source)
# regional None = national usage; the source is still recorded on the concept.
TX_STRINGS = [
    ("iep_team", [("Admission, Review, and Dismissal committee", S, TX), ("ARD committee meeting", REL, TX), ("ARD", A, TX)], src("ARD", "p. 7")),
    ("iep", [("individualized educational program", V, None)], src("NPS", "p. 1")),
    ("hi", [("deaf or hard of hearing", S, None), ("auditory impairment", L, TX)], src("TAC", "(c)(3)")),
    ("ed", [("emotional disability", S, TX)], src("TAC", "(c)(4)")),
    ("sli", [("speech impairment", REL, TX)], src("TAC", "(c)(10)")),
    ("vi", [], src("TAC", "(c)(12)")),
    ("dd", [], src("TAC", "(c)(13)")),
    ("autism", [], src("TAC", "(c)(1)")),
    ("evaluation", [("full and individual initial evaluation", S, None), ("FIIE", A, TX)], src("ARD", "p. 6")),
    ("bip", [("behavior improvement plan", S, TX), ("behavioral improvement plan", V, TX)], src("ARD", "p. 14")),
    ("rti", [], src("ARD", "p. 4")),
    ("home_instr", [], src("ARD", "p. 15")),
    ("continuum", [("continuum of placement options", S, None)], src("ARD", "p. 15")),
    ("lep", [("emergent bilingual", S, TX), ("emergent bilingual student", S, TX)], src("ARD", "p. 7")),
    ("safeguards_notice", [], src("NPS", "p. 1")),
    ("state_complaint", [("special education complaint", S, TX), ("special education complaint resolution process", S, TX)], src("NPS", "p. 13")),
    ("dp_hearing", [("special education due process hearing", S, TX)], src("NPS", "p. 14")),
    ("resolution", [("resolution period", S, None)], src("NPS", "pp. 16-17")),
    ("stay_put", [], src("NPS", "p. 16")),
    ("age_majority", [("adult student", S, None)], src("ARD", "p. 13")),
    ("cop", [("pattern of removals", S, None), ("disciplinary removals", S, None), ("10-day rule", S, None)], src("ARD", "p. 19")),
    ("code_conduct", [], src("ARD", "p. 19")),
    ("slp", [], src("ARD", "p. 2")),
    ("transport", [("transportation services", S, None)], src("ARD", "p. 2")),
    ("child_find", [("child find duty", S, None)], src("ARD", "p. 7")),
    ("esy", [("ESY services", S, None)], src("ARD", "p. 14")),
    ("esa", [("education service center", S, TX), ("ESC", A, TX), ("regional education service center", S, TX)], src("ARD", "p. 2")),
    ("om", [("orientation and mobility instruction", S, None)], src("ARD", "p. 14")),
    ("braille", [("Braille instruction", S, None), ("use of Braille", S, None)], src("ARD", "p. 10")),
    ("progress", [], src("ARD", "p. 10")),
    ("mdr", [], src("ARD", "p. 20")),
    ("iee", [("IEE at public expense", S, None)], src("NPS", "pp. 4-5")),
    ("plaafp", [], src("ARD", "p. 10")),
    ("gen_teacher", [], src("ARD", "p. 7")),
    ("pwn", [("written notice", AB, None)], src("ARD", "p. 5")),
    ("voc_ed", [("career and technical education teacher", S, None)], src("ARD", "p. 7")),
]

# (key, preferred, category, [(text, type, regional)], source, opts)
# opts: jurisdiction ("US" default), broader (key), note, flags, status
TX_CONCEPTS = [
    # --- Texas agencies, forms, and legal frame ---
    ("tea", "Texas Education Agency", "legal_procedural", [("TEA", A, TX)], src("NPS", "p. 1"),
     {"jurisdiction": "US-TX", "broader": "sea", "flags": ["common_english_word"], "note": "'TEA' is protected only as an all-caps, case-sensitive match."}),
    ("tec", "Texas Education Code", "legal_procedural", [("TEC", A, TX)], src("ARD", "p. 2"), {"jurisdiction": "US-TX"}),
    ("tac", "Texas Administrative Code", "legal_procedural", [("TAC", A, TX), ("commissioner's rules", S, TX)], src("NPS", "p. 2"), {"jurisdiction": "US-TX"}),
    ("legal_fw", "Legal Framework for the Child-Centered Special Education Process", "legal_procedural", [("Legal Framework", AB, TX)], src("NPS", "p. 2"), {"jurisdiction": "US-TX"}),
    ("spedtex", "Special Education Information Center", "legal_procedural", [("SPEDTex", A, TX)], src("NPS", "p. 12"), {"jurisdiction": "US-TX"}),
    ("overview_form", "Overview of Special Education for Parents", "legal_procedural", [], src("NPS", "p. 3"),
     {"jurisdiction": "US-TX", "note": "TEA form given with the procedural safeguards notice."}),
    ("model_iep", "Model IEP form", "iep_component", [], src("ARD", "p. 10"), {"jurisdiction": "US-TX"}),
    ("state_panel", "State advisory panel", "legal_procedural", [("Continuing Advisory Committee", S, TX)], src("NPS", "p. 18"),
     {"note": "Federal concept (34 CFR 300.167); Texas's panel is the Continuing Advisory Committee."}),
    ("iep_facil", "IEP facilitation", "legal_procedural", [("state IEP facilitation", S, TX), ("facilitated IEP", S, None), ("FIEP", A, None)], src("NPS", "p. 12"),
     {"note": "Texas runs a state facilitation program under 19 TAC §89.1197."}),
    ("ard_recess", "ARD recess and reconvene", "legal_procedural", [("recess and reconvene", S, TX), ("mutual agreement", REL, TX), ("ten-day recess", S, TX)], src("ARD", "p. 15"),
     {"jurisdiction": "US-TX", "note": "When the ARD committee does not reach mutual agreement it may recess and reconvene. 'Ten-day recess' is practitioner usage, not from the guide."}),
    ("disagree_stmt", "Written statement of disagreement", "legal_procedural", [], src("ARD", "p. 15"), {"jurisdiction": "US-TX"}),
    ("lpac", "Language Proficiency Assessment Committee", "personnel_role", [("LPAC", A, TX)], src("ARD", "p. 7"), {}),
    ("sst", "Campus-based student support team", "personnel_role", [("student support team", S, None)], src("ARD", "p. 3"), {}),
    ("teks", "Texas Essential Knowledge and Skills", "iep_component", [("TEKS", A, TX)], src("ARD", "p. 11"), {"jurisdiction": "US-TX"}),

    # --- Eligibility (19 TAC §89.1040) ---
    ("ncec", "Noncategorical early childhood", "disability_category", [("noncategorical", AB, TX), ("NCEC", A, TX)], src("TAC", "(c)(14)"),
     {"jurisdiction": "US-TX", "status": "machine_validated"}),

    # --- Evaluation ---
    ("reed", "Review of existing evaluation data", "evaluation_eligibility", [("REED", A, None)], src("ARD", "p. 17"),
     {"note": "Federal process (34 CFR 300.305(a)); the acronym is common in Texas paperwork."}),
    ("eval_report", "Evaluation report", "evaluation_eligibility", [("full and individual evaluation report", S, None)], src("ARD", "pp. 6-7"), {}),
    ("suspected", "Suspected disability", "evaluation_eligibility", [], src("ARD", "p. 4"), {}),
    ("revoke", "Revocation of consent", "legal_procedural", [("revocation of consent for services", S, None)], src("ARD", "p. 18"), {}),

    # --- Dyslexia (19 TAC §74.28, 2024 SBOE rule) ---
    ("dys_instr", "Dyslexia instruction", "academic_skill", [("evidence-based dyslexia program", S, TX)], src("ARD", "p. 10"),
     {"jurisdiction": "US-TX", "broader": "dyslexia", "note": "Under the 2024 SBOE rule, dyslexia instruction is delivered as specially designed instruction through the IEP."}),
    ("related_dis", "Related disorders", "health_condition", [("related disorder", P, None)], src("ARD", "p. 6"),
     {"broader": "dyslexia", "note": "In Texas usage this means disorders related to dyslexia, chiefly dysgraphia."}),
    ("dys_handbook", "Dyslexia Handbook", "legal_procedural", [("Texas Dyslexia Handbook", S, TX)], src("ARD", "p. 6"), {"jurisdiction": "US-TX"}),

    # --- Autism strategies (19 TAC §89.1055) ---
    ("autism_strat", "Strategies for students with autism", "iep_component", [("autism supplement", REL, TX)], src("ARD", "p. 13"),
     {"jurisdiction": "US-TX", "broader": "autism", "note": "Texas requires the ARD committee to consider a set of strategies for students with autism. 'Autism supplement' is practitioner usage."}),
    ("ext_ed_prog", "Extended educational programming", "iep_component", [], src("ARD", "p. 13"), {"jurisdiction": "US-TX", "broader": "autism_strat"}),
    ("in_home_cbt", "In-home and community-based training", "iep_component", [("community-based training", AB, None)], src("ARD", "p. 13"), {"jurisdiction": "US-TX", "broader": "autism_strat"}),
    ("staff_ratio", "Staff-to-child ratio", "iep_component", [("suitable staff-to-child ratio", S, TX)], src("ARD", "p. 13"), {"jurisdiction": "US-TX", "broader": "autism_strat"}),
    ("social_skills", "Social skills supports and strategies", "functional_skill", [("social skills", AB, None)], src("ARD", "p. 13"), {"broader": "autism_strat"}),
    ("futures", "Futures planning", "transition", [], src("ARD", "p. 13"), {"jurisdiction": "US-TX", "broader": "autism_strat"}),
    ("daily_sched", "Daily schedules with minimal unstructured time", "iep_component", [], src("ARD", "p. 13"), {"jurisdiction": "US-TX", "broader": "autism_strat"}),

    # --- Visual impairment: expanded core curriculum areas ---
    ("ecc", "Expanded core curriculum", "functional_skill", [("ECC", A, None)], src("ARD", "p. 14"),
     {"note": "The guide lists the areas; 'expanded core curriculum' is the national name for them."}),
    ("comp_skills", "Compensatory skills", "functional_skill", [], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("concept_dev", "Concept development", "functional_skill", [], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("sensory_eff", "Sensory efficiency", "functional_skill", [], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("optical", "Optical devices", "accommodation_modification", [("low vision aids", S, None)], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("social_int", "Social interaction skills", "functional_skill", [], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("rec_leisure", "Recreation and leisure enjoyment", "functional_skill", [], src("ARD", "p. 14"), {"broader": "ecc"}),
    ("tvi", "Teacher of students with visual impairments", "personnel_role", [("TVI", A, None), ("teacher certified in the education of students with visual impairments", S, TX)], src("ARD", "p. 8"),
     {"note": "'TVI' is practitioner usage, not from the guide."}),
    ("tdhh", "Teacher of students who are deaf or hard of hearing", "personnel_role", [("TDHH", A, None), ("teacher certified in the education of students who are deaf or hard of hearing", S, TX)], src("ARD", "p. 8"),
     {"note": "'TDHH' is practitioner usage, not from the guide."}),

    # --- ESY ---
    ("regression", "Severe or substantial regression", "evaluation_eligibility", [("substantial regression", AB, None), ("recoupment", S, None)], src("ARD", "p. 14"),
     {"broader": "esy", "note": "Texas ESY eligibility standard. 'Recoupment' is practitioner usage, not from the guide."}),

    # --- Transition and graduation ---
    ("sdm", "Supported decision-making agreement", "transition", [("supported decision-making", AB, None), ("SDMA", A, TX)], src("ARD", "p. 12"),
     {"note": "Texas Estates Code alternative to guardianship. 'SDMA' is practitioner usage."}),
    ("cie", "Competitive integrated employment", "transition", [("CIE", A, None)], src("ARD", "p. 12"), {}),
    ("fve", "Functional vocational evaluation", "transition", [], src("ARD", "p. 12"), {}),
    ("self_det", "Self-determination", "functional_skill", [("self-determination skills", S, None), ("self-advocacy", S, None)], src("ARD", "p. 12"), {}),
    ("sop", "Summary of academic achievement and functional performance", "transition", [("summary of performance", S, None), ("SOP", A, None)], src("ARD", "pp. 18-19"),
     {"note": "Federal requirement (34 CFR 300.305(e)(3)) at graduation or aging out."}),
    ("postsec_ed", "Postsecondary education", "transition", [("postsecondary training", S, None)], src("ARD", "p. 12"), {}),

    # --- Early childhood ---
    ("eci", "Early Childhood Intervention", "early_intervention", [("ECI", A, TX)], src("ARD", "p. 3"),
     {"jurisdiction": "US-TX", "note": "Texas's Part C program, run by the Health and Human Services Commission."}),
    ("ecse", "Early childhood special education", "early_intervention", [("ECSE", A, None), ("Preschool Program for Children with Disabilities", L, TX), ("PPCD", A, TX)], src("ARD", "p. 3"),
     {"note": "'PPCD' is the older Texas name for preschool special education; not in the 2025 guide."}),

    # --- Discipline ---
    ("daep", "Disciplinary alternative education program", "discipline", [("DAEP", A, TX)], src("ARD", "p. 15"), {"jurisdiction": "US-TX"}),
    ("expellable", "Expellable offense", "discipline", [], src("ARD", "p. 15"), {"jurisdiction": "US-TX"}),
    ("basis_know", "Basis of knowledge", "discipline", [], src("NPS", "p. 8"),
     {"note": "Federal concept (34 CFR 300.534) for students not yet found eligible."}),
    ("exp_hearing", "Expedited due process hearing", "discipline", [("expedited hearing", AB, None)], src("ARD", "p. 21"), {"broader": "dp_hearing"}),
    ("cum_removal", "Cumulative removals", "discipline", [], src("ARD", "p. 19"), {"broader": "cop"}),

    # --- Parents and records ---
    ("foster", "Foster parent", "legal_procedural", [("foster parents", P, None)], src("NPS", "p. 1"), {}),
    ("uhy", "Unaccompanied homeless youth", "legal_procedural", [], src("NPS", "p. 1"), {"broader": "homeless"}),
    ("ed_records", "Education records", "legal_procedural", [("educational records", V, None)], src("NPS", "p. 9"), {}),
    ("part_agency", "Participating agency", "legal_procedural", [], src("NPS", "p. 9"), {}),
    ("ferpa", "Family Educational Rights and Privacy Act", "legal_procedural", [("FERPA", A, None)], src("NPS", "pp. 9-10"), {}),
    ("idea", "Individuals with Disabilities Education Act", "legal_procedural", [("IDEA", A, None), ("IDEA 2004", AB, None), ("IDEA Part B", S, None)], src("NPS", "p. 1"),
     {"flags": ["common_english_word"], "note": "'IDEA' is protected only as an all-caps match; 'idea' is an ordinary word."}),
    ("s504", "Section 504", "section_504", [("Section 504 of the Rehabilitation Act", S, None), ("504 plan", S, None)], src("NPS", "p. 19"), {}),
    ("ada", "Americans with Disabilities Act", "section_504", [("ADA", A, None)], src("NPS", "p. 19"), {}),
]

# Generic names used by the state-layer builder.
STRINGS = TX_STRINGS
CONCEPTS = TX_CONCEPTS
JURISDICTION = "US-TX"
LAYER_NAME = "Texas"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.2.0"
