"""
Georgia layer for SPEDLex.

Sources reviewed 2026-10-03:
  RULES  Ga. Comp. R. & Regs. 160-4-7 rule headings, and the text of
         160-4-7-.05 (eligibility), -.09 (procedural safeguards),
         -.12 (dispute resolution), and -.15 (GNETS)
  DIP    GaDOE IEP help page, Alternate Diploma Requirements

GaDOE's Parent Rights notice could not be read (district copies returned
404). Rule records are 'machine_validated'; the diploma page is 'candidate'.
"""

RULES_URL = "https://regulations.justia.com/states/georgia/department-160/chapter-160-4/subject-160-4-7"
R_URL = "https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-160-4-7-{}"
DIP_URL = "https://sped.gadoe.org/iephelpweb/AlternateDiplomaRequirements.html"


def src(doc, loc=""):
    if doc == "DIP":
        return {"source_type": "state_guidance", "citation": "GaDOE Alternate Diploma Requirements", "url": DIP_URL}
    url = R_URL.format(doc) if doc != "list" else RULES_URL
    rule = doc if doc != "list" else loc
    return {"source_type": "state_regulation", "citation": f"Ga. Comp. R. & Regs. 160-4-7-{rule}{(', ' + loc) if loc and doc != 'list' else ''}", "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
GA = ["US-GA"]
GAJ = {"jurisdiction": "US-GA", "status": "machine_validated"}
REG = {"status": "machine_validated"}
E = src(".05", "(1)")

STRINGS = [
    ("autism", [], E), ("deafblind", [], E), ("oi", [], E), ("ohi", [], E), ("sld", [], E), ("tbi", [], E), ("vi", [], E),
    ("hi", [("deaf/hard of hearing", V, GA)], E),
    ("ed", [("emotional and behavioral disorder", S, GA)], E),
    ("id", [], E),
    ("dd", [("significant developmental delay", S, GA), ("SDD", A, GA)], E),
    ("sli", [("speech-language impairment", V, None)], E),
    ("eligibility", [("eligibility team", S, None)], E),
    ("eval_report", [("eligibility report", S, GA)], E),
    ("sst", [], src(".05")),
    ("child_find", [], src("list", ".03")),
    ("evaluation", [], src("list", ".04")),
    ("lre", [], src("list", ".07")),
    ("safeguards_notice", [("Parent Rights", AB, GA)], src(".09", "(1)(a)")),
    ("iee", [], src(".09", "(4)")),
    ("pwn", [], src(".09", "(5)")),
    ("consent", [], src(".09", "(6)(a)")),
    ("revoke", [], src(".09", "(6)(l)")),
    ("age_majority", [], src(".09", "(2)")),
    ("surrogate", [], src("list", ".11")),
    ("state_complaint", [], src(".12", "(1)")),
    ("mediation", [], src(".12", "(2)")),
    ("resolution", [], src(".12", "(3)(e)")),
    ("dp_hearing", [], src(".12", "(3)(i)")),
    ("stay_put", [], src(".12", "(3)(hh)")),
    ("ppps", [], src("list", ".13")),
    ("alt_diploma", [], src("DIP")),
    ("alt_assess", [], src("DIP")),
    ("sig_cog", [], src("DIP")),
]

CONCEPTS = [
    ("gadoe", "Georgia Department of Education", "legal_procedural", [("GaDOE", A, GA)], src("list", ".01"), {**GAJ, "broader": "sea"}),
    ("gnets", "Georgia Network for Educational and Therapeutic Support", "placement_setting", [("GNETS", A, GA)], src(".15"),
     {**GAJ, "broader": "continuum", "note": "Regional programs for students with intense social, emotional, or behavioral needs."}),
    ("therapeutic_sup", "Therapeutic supports", "related_service", [], src(".15"), GAJ),
    ("resa", "Regional Educational Service Agency", "legal_procedural", [("RESA", A, GA)], src(".15"), {**GAJ, "broader": "esa"}),
    ("glrs", "Georgia Learning Resources System", "legal_procedural", [("GLRS", A, GA)], src("list", ".16"), GAJ),
    ("zoned_school", "Zoned school", "placement_setting", [], src(".15"), {**REG, "note": "Also a field on Nevada's statewide IEP form."}),
    ("agency_placed", "Agency-placed students", "placement_setting", [], src("list", ".19"), GAJ),
    ("gaa2", "Georgia Alternate Assessment 2.0", "iep_component", [("GAA 2.0", A, GA), ("GAA", A, GA)], src("DIP"),
     {"jurisdiction": "US-GA", "broader": "alt_assess"}),
    ("gse", "Georgia Standards of Excellence", "academic_skill", [("GSE", A, GA)], src("DIP"), {"jurisdiction": "US-GA"}),
    ("ga_milestones", "Georgia Milestones Assessment System", "iep_component", [("Georgia Milestones", AB, GA)], src("DIP"), {"jurisdiction": "US-GA"}),
]

JURISDICTION = "US-GA"
LAYER_NAME = "Georgia"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.22.0"
