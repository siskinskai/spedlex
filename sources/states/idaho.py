"""
Idaho layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN  Idaho Department of Education, Procedural Safeguards Notice for
       Students with Disabilities and their Parents (2026)
  MAN  Idaho Department of Education, Idaho Special Education Manual (2024):
       chapter 4 eligibility categories and Idaho-specific terms

Both are state documents read by text extraction: 'candidate'.
"""

PSN_URL = "https://www.sde.idaho.gov/wp-content/uploads/2026/07/Idaho-Special-Education-Procedural-Safeguards-2026.pdf"
MAN_URL = "https://sde.idaho.gov/sped/files/shared/Idaho-Special-Education-Manual-2024.pdf"


def src(doc, loc=""):
    if doc == "MAN":
        return {"source_type": "state_guidance", "citation": f"Idaho Special Education Manual (2024){(', ' + loc) if loc else ''}", "url": MAN_URL}
    return {"source_type": "procedural_safeguards_notice", "citation": f"Idaho Procedural Safeguards Notice (2026){(', ' + loc) if loc else ''}", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
ID = ["US-ID"]
IDJ = {"jurisdiction": "US-ID"}
C4 = src("MAN", "ch. 4, sec. 7.B")

STRINGS = [
    ("autism", [], C4), ("id", [], C4), ("deafblind", [], C4), ("hi", [], C4), ("dd", [], C4),
    ("ed", [("emotional behavioral disorder", S, ID)], C4),
    ("ohi", [], C4), ("sld", [], C4), ("md", [], C4), ("oi", [], C4), ("tbi", [], C4), ("vi", [], C4),
    ("lang_dis", [("speech or language impairment: language", S, ID)], C4),
    ("sli", [("speech or language impairment: speech", S, ID)], C4),
    ("mdt", [], src("MAN", "ch. 4, sec. 1")),
    ("esy", [], src("MAN")),
    ("ccc", [], src("MAN")),
    ("iep_facil", [("special education facilitation", S, ID)], src("MAN", "ch. 13")),
    ("adr", [("informal conflict resolution", S, ID)], src("MAN", "ch. 13")),
    ("state_panel", [("Special Education Advisory Panel", S, ID), ("SEAP", A, ID)], src("MAN")),
    ("pwn", [], src("PSN", "p. 1")),
    ("consent", [], src("PSN", "pp. 2-3")),
    ("revoke", [("withdrawal of consent", S, None)], src("PSN", "pp. 3-4")),
    ("iee", [], src("PSN", "pp. 6-7")),
    ("state_complaint", [], src("PSN", "pp. 12-14")),
    ("mediation", [], src("PSN", "pp. 17-18")),
    ("resolution", [], src("PSN", "pp. 19-20")),
    ("dp_hearing", [], src("PSN", "p. 21")),
    ("stay_put", [], src("PSN", "p. 26")),
    ("mdr", [], src("PSN", "p. 30")),
    ("cop", [], src("PSN", "p. 32")),
    ("exp_hearing", [], src("PSN", "p. 34")),
    ("basis_know", [], src("PSN", "p. 35")),
]

CONCEPTS = [
    ("idaho_doe", "Idaho Department of Education", "legal_procedural", [("Idaho State Department of Education", V, ID)], src("PSN", "p. ii"),
     {**IDJ, "broader": "sea", "note": "Formerly the State Department of Education; its acronym SDE is too generic to safelist alone."}),
    ("id_manual", "Idaho Special Education Manual", "legal_procedural", [], src("PSN"), IDJ),
    ("id_dr", "Special Education Dispute Resolution", "legal_procedural", [], src("PSN", "p. ii"), {**IDJ, "broader": "idaho_doe"}),
    ("ipul", "Idaho Parents Unlimited", "legal_procedural", [("IPUL", A, ID), ("Idaho Parents Unlimited, Inc.", S, ID)], src("PSN", "p. ii"), {**IDJ, "broader": "pti"}),
    ("dri", "Disability Rights Idaho", "legal_procedural", [], src("PSN", "p. ii"), IDJ),
    ("consent_assess", "Written Notice and Consent for Assessment", "evaluation_eligibility", [], src("MAN", "ch. 4, sec. 3"),
     {**IDJ, "broader": "consent", "note": "Idaho's combined notice and consent form for an evaluation."}),
    ("isat", "Idaho Standards Achievement Test", "iep_component", [("ISAT", A, ID)], src("MAN"), IDJ),
    ("id_content", "Idaho Content Standards", "academic_skill", [], src("MAN"), IDJ),
    ("iesdb", "Idaho Educational Services for the Deaf and the Blind", "placement_setting", [("IESDB", A, ID)], src("MAN"), {**IDJ, "broader": "state_sp_sch"}),
    ("id_itp", "Infant/Toddler Program", "early_intervention", [("Infant Toddler Program", V, ID)], src("MAN"),
     {**IDJ, "note": "Idaho's Part C program. Its abbreviation ITP collides with 'individual transition plan', so it is not safelisted."}),
    ("medicaid_sbs", "Medicaid school-based services", "related_service", [], src("MAN"), {}),
]

JURISDICTION = "US-ID"
LAYER_NAME = "Idaho"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.20.0"
