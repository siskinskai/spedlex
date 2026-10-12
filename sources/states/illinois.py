"""
Illinois layer for SPEDLex.

Sources reviewed 2026-10-03:
  PG   ISBE, Educational Rights and Responsibilities: Understanding Special
       Education in Illinois ("The Parent Guide"), May 2025
  R75  23 Ill. Adm. Code §226.75, definitions

ISBE's Explanation of Procedural Safeguards (form 34-57j) could not be
fetched (the server timed out); the Parent Guide covers the same safeguards.
PG references come from text extraction and are 'candidate'; §226.75
records are 'machine_validated'. Special education cooperatives, regional
offices of education, and the Illinois Assessment of Readiness were not
attested in these sources.
"""

PG_URL = "https://www.isbe.net/Documents/Parent-Guide-Special-Ed.pdf"
R75_URL = "https://www.law.cornell.edu/regulations/illinois/IL-Admin-Code-23-226-75"


def src(doc, loc=""):
    if doc == "R75":
        return {"source_type": "state_regulation", "citation": f"23 Ill. Adm. Code §226.75{(', ' + loc) if loc else ''}", "url": R75_URL}
    return {"source_type": "state_guidance", "citation": f"ISBE Parent Guide, Educational Rights and Responsibilities (May 2025), {loc}", "url": PG_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
IL = ["US-IL"]
ILJ = {"jurisdiction": "US-IL"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("iep_team", [], src("R75", "'Individualized education program team'")),
    ("evaluation", [], src("R75", "'Evaluation'")),
    ("iee", [], src("R75", "'Independent educational evaluation'")),
    ("esy", [], src("R75", "'Extended school year services'")),
    ("fba", [], src("R75", "'Functional behavioral assessment'")),
    ("gen_curr", [], src("R75", "'General curriculum'")),
    ("ifsp", [], src("R75", "'Individualized Family Service Plan'")),
    ("lre", [], src("R75", "'Least Restrictive Environment'")),
    ("lep", [("English learner", S, None)], src("R75", "'Limited English proficient'")),
    ("related", [], src("R75", "'Related services'")),
    ("saas", [], src("R75", "'Supplementary aids and services'")),
    ("transition", [("secondary transition", S, None)], src("R75", "'Transition services'")),
    ("ed", [("emotional disability", S, IL)], src("PG", "p. 31")),
    ("id", [("mental retardation", L, IL)], src("PG", "p. 31")),
    ("autism", [], src("PG", "pp. 30, 46-47")),
    ("dd", [], src("PG", "pp. 30-31")),
    ("dyslexia", [], src("PG", "p. 35")),
    ("discrepancy", [], src("PG", "p. 36")),
    ("child_find", [], src("PG", "pp. 9-12")),
    ("screening", [], src("PG", "pp. 10-12")),
    ("rti", [("problem-solving method", S, None)], src("PG", "pp. 13-19")),
    ("tier1", [], src("PG", "pp. 14-16")),
    ("progress", [], src("PG", "pp. 14, 17-18")),
    ("reeval", [], src("PG", "pp. 26-27")),
    ("eligibility", [("eligibility conference", S, IL)], src("PG", "pp. 21-22")),
    ("plaafp", [("PLAAFPs", P, None)], src("PG", "p. 41")),
    ("annual_goals", [], src("PG", "p. 41")),
    ("sto", [], src("PG", "p. 41")),
    ("fld", [], src("PG", "p. 42")),
    ("age_majority", [], src("PG", "pp. 43, 109")),
    ("bip", [], src("PG", "pp. 44, 67-69")),
    ("pbis", [], src("PG", "p. 44")),
    ("braille", [], src("PG", "p. 45")),
    ("at_device", [], src("PG", "pp. 45-46")),
    ("iep_facil", [], src("PG", "p. 48")),
    ("pwn", [], src("PG", "p. 49")),
    ("revoke", [], src("PG", "p. 50")),
    ("mdr", [], src("PG", "p. 72")),
    ("exp_hearing", [], src("PG", "p. 75")),
    ("mediation", [], src("PG", "p. 83")),
    ("state_complaint", [], src("PG", "pp. 85-87")),
    ("dp_hearing", [("due process hearing officer", S, None)], src("PG", "p. 92")),
    ("stay_put", [("stay-put provision", S, None)], src("PG", "p. 91")),
    ("resolution", [], src("PG", "pp. 93-95")),
    ("ecse", [], src("PG", "p. 112")),
    ("s504", [("504 complaint", S, None)], src("PG", "pp. 115-118")),
    ("state_panel", [("Advisory Council on the Education of Children with Disabilities", S, IL)], src("PG", "p. 120")),
    ("sop", [], src("PG", "key definitions")),
    ("pti", [("PTIs", P, None)], src("PG", "p. 23")),
    ("test_accom", [], src("PG", "key definitions")),
    ("program_mods", [], src("PG", "key definitions")),
]

CONCEPTS = [
    ("isbe", "Illinois State Board of Education", "legal_procedural", [("ISBE", A, IL)], src("PG", "p. 3"), {**ILJ, "broader": "sea"}),
    ("il_school_code", "Illinois School Code", "legal_procedural", [("School Code", AB, IL)], src("R75", "'School Code'"), {**ILJ, **REG}),
    ("domain", "Domain", "evaluation_eligibility", [("domains", P, IL), ("assessment domains", S, IL)], src("R75", "'Domain'"),
     {**ILJ, **REG, "note": "Illinois evaluations are planned by domain (areas such as academic achievement, health, communication)."}),
    ("qbs", "Qualified bilingual specialist", "personnel_role", [], src("R75", "'Qualified bilingual specialist'"), {**ILJ, **REG}),
    ("less_common_lang", "Less common language", "legal_procedural", [("common languages", S, IL)], src("R75", "'Less common language'"), {**ILJ, **REG}),
    ("vital_docs", "Vital Documents List", "legal_procedural", [], src("R75", "'Vital Documents List'"),
     {**ILJ, **REG, "note": "Illinois's list of special education documents that must be translated."}),
    ("student_record", "Student record", "legal_procedural", [("school student records", S, IL)], src("R75", "'Student record'"), {**ILJ, **REG}),
    ("dlm_aa", "Dynamic Learning Maps Alternate Assessment", "iep_component", [("DLM-AA", A, IL), ("Illinois Alternate Assessment", S, IL),
                                                                              ("DLM-AA Participation Guidelines", REL, IL)], src("PG", "p. 42"),
     {**ILJ, "broader": "dlm"}),
    ("access_ell", "ACCESS for ELLs", "iep_component", [("ACCESS", A, None), ("Alternate ACCESS", S, None)], src("PG", "p. 46"),
     {"flags": ["common_english_word"], "note": "English language proficiency test used in many states; 'ACCESS' is protected only as an all-caps match."}),
    ("delegation", "Delegation of Rights", "transition", [("Delegation of Rights form", REL, IL)], src("PG", "p. 43"),
     {"broader": "age_majority", "note": "Lets a student who has reached 18 delegate educational decisions to a parent or other adult (in Illinois on ISBE form 34-57k). General concept: Arizona uses the term too."}),
    ("restraint", "Physical restraint", "discipline", [("physical restraints", P, None)], src("PG", "p. 69"), {}),
    ("time_out", "Time out", "discipline", [("isolated time out", REL, IL), ("time-out", V, None)], src("PG", "p. 69"), {}),
    ("inclusive", "Inclusive education", "placement_setting", [("inclusion", AB, None)], src("PG", "p. 57"), {"broader": "lre"}),
    ("gen_ed_env", "General education environment", "placement_setting", [], src("PG", "p. 58"), {"broader": "lre"}),
    ("nonpublic_fac", "Nonpublic facility", "placement_setting", [("nonpublic facilities", P, IL)], src("PG", "p. 105"), ILJ),
    ("prehearing", "Pre-hearing conference", "legal_procedural", [("prehearing conference", V, None)], src("PG", "p. 96"), {"broader": "dp_hearing"}),
    ("cfc", "Child and Family Connections", "early_intervention", [], src("PG", "p. 10"),
     {**ILJ, "note": "Regional intake offices for Illinois's Part C early intervention program."}),
    ("family_matters", "Family Matters Parent Training and Information Center", "legal_procedural", [("Family Matters", AB, IL)], src("PG", "p. 23"), {**ILJ, "broader": "pti"}),
    ("arc_il", "The Arc of Illinois", "legal_procedural", [("Arc of Illinois", AB, IL)], src("PG", "resources"), ILJ),
    ("parent_mentor", "Parent mentor", "personnel_role", [("parent mentors", P, IL)], src("PG", "p. 23"), {}),
    ("istac", "Illinois Statewide Technical Assistance Center", "legal_procedural", [("ISTAC", A, IL)], src("PG", "p. 16"), ILJ),
    ("il_drs", "Division of Rehabilitation Services", "transition", [("Illinois Department of Human Services, Division of Rehabilitation Services", S, IL)], src("PG", "resources"), ILJ),
    ("rosas_law", "Rosa's Law", "legal_procedural", [], src("PG", "p. 31"),
     {"flags": ["eponym"], "note": "2010 federal law replacing 'mental retardation' with 'intellectual disability'. 'Rosa' is a first name, so only the full phrase is protected."}),

    # Older autism diagnoses the guide still lists (DSM-IV terms)
    ("autistic_dis", "Autistic disorder", "health_condition", [], src("PG", "pp. 30, 46-47"), {"broader": "autism"}),
    ("asperger", "Asperger's disorder", "health_condition", [("Asperger syndrome", S, None), ("Asperger's syndrome", V, None)], src("PG", "pp. 30, 46-47"),
     {"broader": "autism", "flags": ["eponym", "surname"], "note": "Eponym; protected only as the full phrase."}),
    ("pdd", "Pervasive developmental disorder", "health_condition", [("PDD", A, None), ("PDD-NOS", A, None),
                                                                     ("pervasive developmental disorder not otherwise specified", S, None)], src("PG", "pp. 30, 46-47"), {"broader": "autism"}),
    ("cdd", "Childhood disintegrative disorder", "health_condition", [], src("PG", "pp. 30, 46-47"), {"broader": "autism"}),
    ("rett", "Rett syndrome", "health_condition", [("Rett's syndrome", V, None)], src("PG", "p. 47"),
     {"broader": "autism", "flags": ["eponym", "surname"], "note": "Eponym; protected only as the full phrase."}),
]

JURISDICTION = "US-IL"
LAYER_NAME = "Illinois"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.10.0"
