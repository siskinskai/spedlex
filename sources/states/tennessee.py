"""
Tennessee layer for SPEDLex.

Sources reviewed 2026-10-03:
  R02   Tenn. Comp. R. & Regs. 0520-01-09-.02, definitions
  R03   Tenn. Comp. R. & Regs. 0520-01-09-.03, recognized disability categories
  OV    Overview of Procedural Safeguards (Family Engagement Network / The Arc
        Tennessee, accessible PDF, 2026 upload)
  TCAP  TDOE, TCAP-Alt Fact Sheet

TDOE's full procedural safeguards notice was not readable (a district copy
returned 404). Rule records are 'machine_validated'; the others are
'candidate'.
"""

R02_URL = "https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0520-01-09-.02"
R03_URL = "https://regulations.justia.com/states/tennessee/title-0520/subtitle-0520-01/chapter-0520-01-09/section-0520-01-09-03"
OV_URL = "https://familyengagementtn.com/wp-content/uploads/2026/03/overview_of_procedural_safeguards_508_accessible.pdf"
TCAP_URL = "https://tennessee.gov/education/districts/lea-operations/assessment/alternate-assessment/tcap-alt-fact-sheet.html"


def src(doc, loc=""):
    if doc in ("R02", "R03"):
        sec, url = {"R02": (".02", R02_URL), "R03": (".03", R03_URL)}[doc]
        return {"source_type": "state_regulation", "citation": f"Tenn. Comp. R. & Regs. 0520-01-09-{sec}{(', ' + loc) if loc else ''}", "url": url}
    if doc == "OV":
        return {"source_type": "secondary_guidance", "citation": f"Tennessee Overview of Procedural Safeguards (Arc Tennessee){(', ' + loc) if loc else ''}", "url": OV_URL}
    return {"source_type": "state_guidance", "citation": "TDOE TCAP-Alt Fact Sheet", "url": TCAP_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
TN = ["US-TN"]
TNJ = {"jurisdiction": "US-TN"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("bip", [], src("R02")), ("cwd", [], src("R02")), ("fba", [], src("R02")), ("iep", [], src("R02")),
    ("iep_team", [], src("R02")), ("related", [], src("R02")), ("special_ed", [], src("R02")),
    ("autism", [], src("R03")), ("deafblind", [], src("R03")), ("deafness", [], src("R03")),
    ("dd", [], src("R03")), ("ed", [], src("R03")), ("hi", [], src("R03")), ("id", [], src("R03")),
    ("md", [], src("R03")), ("oi", [], src("R03")), ("ohi", [], src("R03")), ("sld", [], src("R03")),
    ("sli", [], src("R03")), ("tbi", [], src("R03")), ("vi", [], src("R03")),
    ("gifted", [("intellectually gifted", S, TN)], src("R03")),
    ("consent", [], src("OV", "p. 1")),
    ("lre", [("peers without disabilities", S, None)], src("OV", "p. 1")),
    ("mediation", [], src("OV", "p. 2")),
    ("dp_hearing", [("impartial administrative law judge", S, None)], src("OV", "p. 2")),
    ("state_complaint", [("administrative complaint", S, TN)], src("OV", "p. 2")),
    ("alt_assess", [], src("TCAP")),
    ("sig_cog", [], src("TCAP")),
]

CONCEPTS = [
    ("tdoe", "Tennessee Department of Education", "legal_procedural", [], src("OV", "p. 2"),
     {**TNJ, "broader": "sea", "note": "Its acronym TDOE is not safelisted alone because several states use similar ones."}),
    ("functional_delay", "Functional delay", "disability_category", [], src("R03"),
     {**TNJ, **REG, "note": "Tennessee-only category: below-average intellectual functioning and achievement with adaptive behavior in the typical range."}),
    ("lba", "Licensed behavior analyst", "personnel_role", [("licensed behavior analysts", P, None)], src("R02"), REG),
    ("tcap", "Tennessee Comprehensive Assessment Program", "iep_component", [("TCAP", A, TN)], src("TCAP"),
     {**TNJ, "note": "The acronym is from TDOE; the full name is from prior knowledge."}),
    ("tcap_alt", "TCAP-Alt", "iep_component", [("TCAP Alternate Assessment", S, TN)], src("TCAP"), {**TNJ, "broader": "alt_assess"}),
    ("msaa", "Multi-State Alternate Assessment", "iep_component", [("MSAA", A, None)], src("TCAP"),
     {"broader": "alt_assess", "note": "Multistate alternate assessment consortium; Tennessee uses it for TCAP-Alt ELA and math."}),
    ("tn_standards", "Tennessee Academic Standards", "academic_skill", [], src("TCAP"), TNJ),
]

JURISDICTION = "US-TN"
LAYER_NAME = "Tennessee"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.19.0"
