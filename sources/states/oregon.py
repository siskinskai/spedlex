"""
Oregon layer for SPEDLex.

Sources reviewed 2026-10-03:
  R2000  OAR 581-015-2000, definitions (includes the disability list)
  PSN    ODE, Procedural Safeguards Notice: Parent Rights for Special
         Education K-21 (2020-21 edition, still in effect)
  EXT    ODE, Oregon Extended Assessment (ORExt) page

OAR records are 'machine_validated'; the others are 'candidate'.
"""

R_URL = "https://www.law.cornell.edu/regulations/oregon/Or-Admin-Code-SS-581-015-2000"
PSN_URL = "https://www.oregon.gov/ode/students-and-family/SpecialEducation/publications/Documents/proceduralsafeguards/englishk21.pdf"
EXT_URL = "https://www.oregon.gov/ode/educator-resources/assessment/AltAssessment/Pages/default.aspx"


def src(doc, loc=""):
    if doc == "R2000":
        return {"source_type": "state_regulation", "citation": f"OAR 581-015-2000{(', ' + loc) if loc else ''}", "url": R_URL}
    if doc == "EXT":
        return {"source_type": "state_guidance", "citation": "ODE Oregon Extended Assessment (ORExt) page", "url": EXT_URL}
    return {"source_type": "procedural_safeguards_notice", "citation": f"ODE Procedural Safeguards Notice K-21 (2020-21){(', ' + loc) if loc else ''}", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
OR = ["US-OR"]
ORJ = {"jurisdiction": "US-OR"}
REG = {"status": "machine_validated"}
D = lambda term: src("R2000", f"'{term}'")

STRINGS = [
    ("autism", [], D("Children with disabilities")), ("sli", [], D("Children with disabilities")),
    ("deafblind", [], D("Children with disabilities")), ("dd", [], D("Children with disabilities")),
    ("ed", [("emotional behavior disability", S, OR)], D("Children with disabilities")),
    ("hi", [], D("Children with disabilities")), ("id", [], D("Children with disabilities")),
    ("oi", [], D("Children with disabilities")), ("ohi", [], D("Children with disabilities")),
    ("sld", [], D("Children with disabilities")), ("tbi", [], D("Children with disabilities")),
    ("vi", [], D("Children with disabilities")),
    ("cwd", [("students with disabilities", S, None)], D("Children with disabilities")),
    ("age_majority", [], D("Adult student")),
    ("at_device", [], D("Assistive technology device")),
    ("at_service", [], D("Assistive technology service")),
    ("evaluation", [], D("Evaluation")),
    ("gen_curr", [], D("General education curriculum")),
    ("homeless", [], D("Homeless children")),
    ("iep", [], D("Individualized Education Program")),
    ("ifsp", [], D("Individualized Family Service Plan")),
    ("lep", [], D("Limited English proficient")),
    ("mediation", [], D("Mediation")),
    ("related", [], D("Related services")),
    ("services_plan", [], D("Services plan")),
    ("sto", [("short term objectives", V, None)], D("Short term objectives")),
    ("special_ed", [], D("Special education")),
    ("sdi", [], D("Specially designed instruction")),
    ("saas", [], D("Supplementary aids and services")),
    ("surrogate", [], D("Surrogate parent")),
    ("transition", [], D("Transition services")),
    ("ward", [], D("Ward of the state")),
    ("social_work", [("developmental history", S, None)], D("Developmental History")),
    ("pwn", [], src("PSN", "pp. 5-6")),
    ("consent", [], src("PSN", "p. 7")),
    ("iee", [], src("PSN", "pp. 10-11")),
    ("state_complaint", [], src("PSN", "pp. 18-20")),
    ("dp_complaint", [], src("PSN", "pp. 21-23")),
    ("resolution", [], src("PSN", "pp. 24-25")),
    ("dp_hearing", [], src("PSN", "pp. 26-27")),
    ("mdr", [], src("PSN", "pp. 33-34")),
    ("iaes", [], src("PSN", "pp. 34-35")),
    ("exp_hearing", [], src("PSN", "p. 36")),
    ("emancipated", [], src("PSN", "p. 2")),
    ("alt_assess", [], src("EXT")),
    ("sig_cog", [("SWSCD", A, OR)], src("EXT")),
    ("plaafp", [], src("EXT")),
]

CONCEPTS = [
    ("ode_or", "Oregon Department of Education", "legal_procedural", [], src("PSN", "p. 1"),
     {**ORJ, "broader": "sea", "note": "Its acronym ODE is shared with Ohio, so it is not safelisted alone."}),
    ("or_eso", "Office of Enhancing Student Opportunities", "legal_procedural", [], src("PSN", "p. 1"), {**ORJ, "broader": "ode_or"}),
    ("ei_ecse", "Early Intervention/Early Childhood Special Education", "early_intervention", [("EI/ECSE", A, OR)], D("EI/ECSE"),
     {**ORJ, **REG, "broader": "ecse", "note": "Oregon runs Part C and preschool special education as one program."}),
    ("esd", "Education service district", "legal_procedural", [("ESD", A, OR), ("educational service district", V, OR)], D("Public agency"),
     {**ORJ, **REG, "broader": "esa"}),
    ("audiological_assess", "Audiological assessment", "evaluation_eligibility", [], D("Audiological assessment"), REG),
    ("vision_exam", "Vision examination", "evaluation_eligibility", [("medical examination", S, None)], D("Vision examination"), REG),
    ("sheltered", "Sheltered workshop", "transition", [], D("Sheltered Workshop"),
     {**ORJ, **REG, "note": "Oregon ended placements of students in sheltered workshops; the term remains in the rule."}),
    ("drot", "Disability Rights Oregon", "legal_procedural", [], src("PSN", "p. 2"), ORJ),
    ("fact_or", "FACT Oregon", "legal_procedural", [], src("PSN"), {**ORJ, "broader": "pti"}),
    ("orext", "Oregon Extended Assessment", "iep_component", [("ORExt", A, OR), ("Extended Assessment", AB, OR)], src("EXT"), {**ORJ, "broader": "alt_assess"}),
    ("eaf", "Essentialized Assessment Frameworks", "academic_skill", [("EAFs", A, OR)], src("EXT"),
     {**ORJ, "note": "Oregon's reduced-complexity standards behind ORExt; compare Virginia's VESOL."}),
    ("osas", "Oregon Statewide Assessment System", "iep_component", [("OSAS", A, OR)], src("EXT"), ORJ),
    ("qa_or", "Qualified Assessor", "personnel_role", [("Qualified Training Coordinator", S, OR)], src("EXT"), ORJ),
]

JURISDICTION = "US-OR"
LAYER_NAME = "Oregon"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.21.0"
