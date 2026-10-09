"""
Pennsylvania layer, second pass (fills gaps from the first pass).

Sources reviewed 2026-10-03:
  R101  22 Pa. Code §14.101, definitions
  R161  22 Pa. Code §16.1, gifted education definitions

Both are regulations read from their text: 'machine_validated'. The
Reevaluation Report (RR), NORA, the gifted written report, and PaTTAN were
still not attested by an official source.
"""

R101_URL = "https://www.law.cornell.edu/regulations/pennsylvania/22-Pa-Code-SS-14-101"
R161_URL = "https://www.law.cornell.edu/regulations/pennsylvania/22-Pa-Code-SS-16-1"


def src(doc, loc=""):
    sec, url = {"R101": ("14.101", R101_URL), "R161": ("16.1", R161_URL)}[doc]
    return {"source_type": "state_regulation", "citation": f"22 Pa. Code §{sec}{(', ' + loc) if loc else ''}", "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
PA = ["US-PA"]
PAJ = {"jurisdiction": "US-PA", "status": "machine_validated"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("dd", [], src("R101", "'Developmental delay'")),
    ("esy", [], src("R101", "'ESY'")),
    ("iep", [], src("R101", "'IEP'")),
    ("mdt", [], src("R101", "'MDT'")),
    ("sst", [("IST", A, PA)], src("R101", "'IST'")),
    ("part_c_transition", [], src("R101", "'Early intervention services'")),
    ("cwd", [], src("R101", "'Student with a disability'")),
    ("gifted", [("mentally gifted", S, PA), ("gifted student", S, None)], src("R161", "'Mentally gifted'")),
    ("sdi", [], src("R161", "'Specially designed instruction'")),
]

CONCEPTS = [
    ("eyc", "Eligible young child", "early_intervention", [("eligible young children", P, PA)], src("R101", "'Eligible young child'"),
     {**PAJ, "note": "Pennsylvania's term for a preschool child (age 3 to school age) with a disability."}),
    ("age_beginners", "Age of beginners", "early_intervention", [], src("R101", "'Age of beginners'"),
     {**PAJ, "note": "The minimum age for first grade; preschool eligibility ends there."}),
    ("school_entity", "School entity", "legal_procedural", [("school entities", P, PA)], src("R101", "'School entity'"), PAJ),
    ("ei_agency", "Early intervention agency", "early_intervention", [], src("R101", "'Early intervention agency'"), PAJ),
    ("ch16", "22 Pa. Code Chapter 16", "legal_procedural", [("Chapter 16", AB, PA)], src("R161"), PAJ),
    ("giep", "Gifted Individualized Education Plan", "iep_component", [("GIEP", A, PA)], src("R161", "'GIEP'"), {**PAJ, "broader": "gifted"}),
    ("gmdt", "Gifted Multidisciplinary Team", "personnel_role", [("GMDT", A, PA)], src("R161", "'GMDT'"), {**PAJ, "broader": "gifted"}),
    ("gme", "Gifted Multidisciplinary Evaluation", "evaluation_eligibility", [], src("R161", "'Gifted Multidisciplinary Evaluation'"), {**PAJ, "broader": "gifted"}),
]

JURISDICTION = "US-PA"
LAYER_NAME = "Pennsylvania (preschool and gifted)"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.16.0"
