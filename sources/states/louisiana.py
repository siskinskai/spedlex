"""
Louisiana layer for SPEDLex.

Sources reviewed 2026-10-03:
  B1508  Louisiana Administrative Code, Title 28, Part CI (Bulletin 1508, the
         Pupil Appraisal Handbook): section headings for chapters 3, 5, 7, 9,
         11, 13, and 15, plus §CI-303 on the School Building Level Committee
  LC     LDOE, Parent Guide to the LEAP Connect Assessments (rev. Dec. 2024)

Louisiana's procedural safeguards notice was not found online; searches
returned only other states' notices. Bulletin 1706 (Louisiana's IDEA
regulations) was not read. Rule records are 'machine_validated'; the LDOE
guide is 'candidate'.
"""

B_URL = "https://regulations.justia.com/states/louisiana/title-28/part-ci"
LC_URL = "https://doe.louisiana.gov/docs/default-source/assessment/parent-guide-to-leap-connect.pdf"


def src(doc, loc=""):
    if doc == "B1508":
        return {"source_type": "state_regulation", "citation": f"La. Admin. Code tit. 28, pt. CI (Bulletin 1508), §{loc}", "url": B_URL}
    return {"source_type": "state_guidance", "citation": "LDOE Parent Guide to the LEAP Connect Assessments (rev. Dec. 2024)", "url": LC_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
LA = ["US-LA"]
LAJ = {"jurisdiction": "US-LA"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("rti", [], src("B1508", "CI-301")),
    ("sst", [("School Building Level Committee", S, LA), ("SBLC", A, LA)], src("B1508", "CI-303")),
    ("screening", [], src("B1508", "CI-305")),
    ("evaluation", [("required initial individual evaluation", S, LA)], src("B1508", "CI-509")),
    ("eligibility", [], src("B1508", "CI-515")),
    ("iee", [], src("B1508", "CI-517")),
    ("autism", [], src("B1508", "CI-701")),
    ("deafblind", [], src("B1508", "CI-703")),
    ("dd", [], src("B1508", "CI-705")),
    ("ed", [], src("B1508", "CI-707")),
    ("hi", [("deaf and/or hard of hearing", S, LA)], src("B1508", "CI-709")),
    ("id", [], src("B1508", "CI-711")),
    ("md", [], src("B1508", "CI-713")),
    ("oi", [], src("B1508", "CI-715")),
    ("ohi", [], src("B1508", "CI-717")),
    ("sld", [], src("B1508", "CI-719")),
    ("sli", [], src("B1508", "CI-721")),
    ("tbi", [], src("B1508", "CI-723")),
    ("vi", [], src("B1508", "CI-725")),
    ("gifted", [], src("B1508", "CI-901")),
    ("pe", [], src("B1508", "CI-1303")),
    ("at_device", [], src("B1508", "CI-1305")),
    ("related", [], src("B1508", "CI-1501")),
    ("ot", [], src("B1508", "CI-1503")),
    ("om", [], src("B1508", "CI-1505")),
    ("pt", [], src("B1508", "CI-1507")),
    ("nursing", [], src("B1508", "CI-1509")),
    ("psych", [], src("B1508", "CI-1511")),
    ("social_work", [], src("B1508", "CI-1513")),
    ("slp", [], src("B1508", "CI-1515")),
    ("alt_assess", [], src("LC")),
    ("sig_cog", [], src("LC")),
]

CONCEPTS = [
    ("ldoe", "Louisiana Department of Education", "legal_procedural", [("LDOE", A, LA)], src("LC"), {**LAJ, "broader": "sea"}),
    ("b1508", "Bulletin 1508", "legal_procedural", [("Pupil Appraisal Handbook", S, LA)], src("B1508", "CI-101"), {**LAJ, **REG,
     "note": "Louisiana numbers its education rules as Board bulletins; 1508 covers evaluation and eligibility."}),
    ("b1530", "Bulletin 1530", "legal_procedural", [], src("LC"), {**LAJ, "note": "Louisiana's rules for students with disabilities in statewide assessment."}),
    ("pupil_appraisal", "Pupil appraisal", "personnel_role", [("pupil appraisal personnel", S, LA), ("pupil appraisal services", S, LA)], src("B1508", "CI-303"),
     {**LAJ, **REG, "note": "Louisiana's name for the evaluation staff (school psychologists, educational diagnosticians, and others)."}),
    ("exceptionality", "Exceptionality", "legal_procedural", [("exceptionalities", P, None)], src("B1508", "CI-303"),
     {**REG, "note": "Louisiana's umbrella word covering disabilities and giftedness or talent."}),
    ("talented", "Talented", "evaluation_eligibility", [], src("B1508", "CI-903"),
     {**LAJ, **REG, "broader": "gifted", "note": "Louisiana identifies students talented in visual arts, music, or theater as a separate exceptionality."}),
    ("leap_connect", "LEAP Connect", "iep_component", [], src("LC"), {**LAJ, "broader": "alt_assess"}),
    ("la_connectors", "Louisiana Connectors", "academic_skill", [("LCs", A, LA)], src("LC"),
     {**LAJ, "note": "Reduced-complexity standards behind LEAP Connect; compare Core Content Connectors and Essential Elements."}),
    ("la_standards", "Louisiana Student Standards", "academic_skill", [], src("LC"), LAJ),
    ("alds", "Achievement Level Descriptors", "iep_component", [("ALDs", A, None)], src("LC"), {}),
]

JURISDICTION = "US-LA"
LAYER_NAME = "Louisiana"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.14.0"
