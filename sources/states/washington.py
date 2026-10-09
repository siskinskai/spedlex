"""
Washington layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN  OSPI, Notice of Special Education Procedural Safeguards for Students
       and Their Families (rev. Mar. 2022)
  WAC  WAC 392-172A-01035, disability categories
  AIM  OSPI, Assessment for Students with Cognitive Disabilities (WA-AIM) page

PSN and AIM references are 'candidate'; the WAC section is
'machine_validated'.
"""

PSN_URL = "https://ospi.k12.wa.us/sites/default/files/2023-08/proceduralsafeguards.pdf"
WAC_URL = "https://app.leg.wa.gov/wac/default.aspx?cite=392-172A-01035"
AIM_URL = "https://ospi.k12.wa.us/student-success/testing/state-testing/assessment-students-cognitive-disabilities-wa-aim"


def src(doc, loc=""):
    if doc == "WAC":
        return {"source_type": "state_regulation", "citation": "WAC 392-172A-01035", "url": WAC_URL}
    if doc == "AIM":
        return {"source_type": "state_guidance", "citation": "OSPI WA-AIM page", "url": AIM_URL}
    return {"source_type": "procedural_safeguards_notice", "citation": f"OSPI Notice of Special Education Procedural Safeguards (Mar. 2022){(', ' + loc) if loc else ''}", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
WA = ["US-WA"]
WAJ = {"jurisdiction": "US-WA"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("id", [], src("WAC")), ("sli", [], src("WAC")), ("vi", [], src("WAC")), ("oi", [], src("WAC")),
    ("autism", [], src("WAC")), ("tbi", [], src("WAC")), ("ohi", [], src("WAC")), ("sld", [], src("WAC")),
    ("deafblind", [], src("WAC")), ("md", [], src("WAC")), ("dd", [], src("WAC")),
    ("deafness", [("deafness including hard of hearing", S, WA)], src("WAC")),
    ("ed", [("emotional/behavioral disability", V, WA)], src("WAC")),
    ("pwn", [], src("PSN", "pp. 6-7")),
    ("safeguards_notice", [], src("PSN", "p. 6")),
    ("consent", [], src("PSN", "pp. 8-10")),
    ("ward", [], src("PSN", "p. 9")),
    ("iee", [], src("PSN", "pp. 11-12")),
    ("mediation", [], src("PSN", "pp. 16-17")),
    ("state_complaint", [("community complaint", S, WA), ("special education community complaint", S, WA)], src("PSN", "pp. 18-19")),
    ("dp_complaint", [], src("PSN", "pp. 20-21")),
    ("stay_put", [("student placement while due process pending", S, WA)], src("PSN", "p. 22")),
    ("resolution", [], src("PSN", "pp. 22-24")),
    ("dp_hearing", [("administrative law judge", S, None), ("ALJ", A, None)], src("PSN", "pp. 24-26")),
    ("oah", [("OAH", A, WA)], src("PSN", "p. 20")),
    ("state_panel", [], src("PSN", "p. 27")),
    ("cop", [], src("PSN", "p. 30")),
    ("mdr", [], src("PSN", "pp. 30-31")),
    ("special_circ", [], src("PSN", "p. 32")),
    ("exp_hearing", [], src("PSN", "p. 34")),
    ("basis_know", [], src("PSN", "p. 34")),
    ("alt_assess", [], src("AIM")),
    ("sig_cog", [], src("AIM")),
]

CONCEPTS = [
    ("ospi", "Office of Superintendent of Public Instruction", "legal_procedural", [("OSPI", A, WA)], src("PSN", "p. 6"), {**WAJ, "broader": "sea"}),
    ("wac392", "Chapter 392-172A WAC", "legal_procedural", [("WAC 392-172A", A, WA)], src("PSN", "p. 6"), WAJ),
    ("pave", "Partnerships for Action, Voices for Empowerment", "legal_procedural", [("PAVE", A, WA)], src("PSN", "p. 6"),
     {**WAJ, "broader": "pti", "flags": ["common_english_word"], "note": "'PAVE' is protected only as an all-caps match."}),
    ("dcyf", "Department of Children, Youth, and Families", "legal_procedural", [("DCYF", A, WA)], src("PSN", "p. 9"), WAJ),
    ("wa_aim", "Washington Access to Instruction and Measurement", "iep_component", [("WA-AIM", A, WA)], src("AIM"), {**WAJ, "broader": "alt_assess"}),
    ("apf", "Access Point Frameworks", "academic_skill", [], src("AIM"),
     {**WAJ, "note": "Washington's reduced-complexity standards behind WA-AIM; compare Florida's access points."}),
    ("grad_pathway", "Graduation pathway", "transition", [("graduation pathway requirement", S, WA)], src("AIM"), WAJ),
]

JURISDICTION = "US-WA"
LAYER_NAME = "Washington"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.18.0"
