"""
Kansas layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN  KSDE, Parent Rights in Special Education (Procedural Safeguards
       Notice), rev. Feb. 2020
  PH   KSDE, Kansas Special Education Process Handbook (2018, updated
       through Mar. 2025): chapter list and Kansas terms of art

Both are KSDE documents read by text extraction, so records are
'candidate'. The K.A.R. 91-40 citations in the notice were not read in the
regulation itself.
"""

PSN_URL = "https://www.ksde.gov/docs/default-source/sets/proceduralsafeguardskansas_english.pdf"
PH_URL = "https://www.ksde.gov/Portals/0/SES/PH/PH-complete.pdf"


def src(doc, loc=""):
    stype, title, url = {
        "PSN": ("procedural_safeguards_notice", "KSDE Parent Rights in Special Education (Feb. 2020)", PSN_URL),
        "PH": ("state_guidance", "KSDE Kansas Special Education Process Handbook (updated Mar. 2025)", PH_URL),
    }[doc]
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
KS = ["US-KS"]
KSJ = {"jurisdiction": "US-KS"}

STRINGS = [
    ("exc_student", [("exceptional child", S, KS), ("exceptional children", P, KS)], src("PSN", "p. 1")),
    ("exceptionality", [], src("PH")),
    ("gifted", [], src("PSN", "pp. 1-2")),
    ("ed", [("emotional disability", S, KS)], src("PH")),
    ("dd", [], src("PH")),
    ("iep_team", [], src("PSN")),
    ("eval_report", [], src("PSN", "p. 1")),
    ("pwn", [], src("PSN", "pp. 1-2")),
    ("consent", [], src("PSN", "p. 3")),
    ("reeval", [], src("PSN", "p. 4")),
    ("ward", [], src("PSN", "p. 4")),
    ("revoke", [], src("PSN", "p. 5")),
    ("iee", [], src("PSN", "pp. 5-6")),
    ("child_find", [], src("PSN", "p. 8")),
    ("state_complaint", [("formal complaint", S, KS)], src("PSN", "pp. 11-13")),
    ("dp_complaint", [], src("PSN", "pp. 14-16")),
    ("mediation", [("mediation agreement", S, None)], src("PSN", "p. 16")),
    ("resolution", [], src("PSN", "pp. 17-18")),
    ("dp_hearing", [], src("PSN", "p. 19")),
    ("sro", [("review officer", S, KS)], src("PSN", "p. 22")),
    ("stay_put", [], src("PSN", "p. 24")),
    ("mdr", [], src("PSN", "p. 27")),
    ("bip", [], src("PSN", "p. 27")),
    ("fba", [], src("PSN", "pp. 26-27")),
    ("iaes", [], src("PSN", "pp. 26-29")),
    ("gen_ed_int", [("General Education Intervention", S, KS), ("GEI", A, KS)], src("PH", "ch. 2")),
    ("surrogate", [("education advocate", S, KS)], src("PH")),
    ("exit_sped", [("discontinuing special education services", S, KS)], src("PH", "ch. 8")),
    ("ifsp", [], src("PH")),
    ("lre", [], src("PH", "ch. 6")),
    ("saas", [], src("PH")),
    ("esy", [], src("PH")),
    ("transition", [], src("PSN", "p. 3")),
    ("related", [], src("PH", "ch. 5")),
]

CONCEPTS = [
    ("ksde", "Kansas State Department of Education", "legal_procedural", [("KSDE", A, KS)], src("PSN", "p. i"), {**KSJ, "broader": "sea"}),
    ("sets", "Special Education and Title Services", "legal_procedural", [("SETS", A, KS), ("KSDE SETS", S, KS)], src("PH"),
     {**KSJ, "broader": "ksde", "flags": ["common_english_word"], "note": "'SETS' is protected only as an all-caps match."}),
    ("secea", "Special Education for Exceptional Children Act", "legal_procedural", [("K.A.R. 91-40", A, KS)], src("PH"), KSJ),
    ("ks_handbook", "Kansas Special Education Process Handbook", "legal_procedural", [("Process Handbook", AB, KS)], src("PSN", "p. ii"), KSJ),
    ("kesa", "Kansas Education Systems Accreditation", "legal_procedural", [("KESA", A, KS)], src("PH"), KSJ),
    ("families_together", "Families Together", "legal_procedural", [("Families Together, Inc.", S, KS)], src("PSN", "p. ii"), {**KSJ, "broader": "pti"}),
    ("kmtss", "Kansas MTSS and Alignment", "evaluation_eligibility", [], src("PH"), {**KSJ, "broader": "mtss"}),
    ("elig_indicators", "Eligibility indicators", "evaluation_eligibility", [], src("PH"), KSJ),
    ("two_prong", "Two-prong test", "evaluation_eligibility", [("two-prong eligibility", S, None)], src("PH"),
     {"note": "Eligibility needs both an exceptionality and a need for special education."}),
    ("material_change", "Material change in services", "iep_component", [], src("PSN", "p. 5"),
     {**KSJ, "note": "Kansas requires parental consent for a material change in services or a substantial change in placement."}),
    ("subst_change", "Substantial change in placement", "placement_setting", [], src("PSN", "p. 5"), KSJ),
    ("interrelated", "Interrelated", "placement_setting", [("interrelated classroom", S, KS), ("interrelated special education", S, KS)], src("PH"),
     {**KSJ, "note": "Kansas term for a cross-categorical program and teacher license; the longer strings are practitioner usage."}),
]

JURISDICTION = "US-KS"
LAYER_NAME = "Kansas"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.15.0"
