"""
Illinois layer, consistency additions.

A second reading of the Illinois layer's own documents for terms the first
pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  R75  23 Ill. Adm. Code §226.75 (definitions)
  PG   ISBE Parent Guide, Educational Rights and Responsibilities, cited by page
"""

from .illinois import src, A, S, V, L, AB, P, IL, ILJ

STRINGS = [
    ("tier1", [("core instruction", S, None)], src("PG", "p. 14")),
]

CONCEPTS = [
    ("home_language_survey", "Home Language Survey", "evaluation_eligibility", [], src("PG", "p. 46"), {}),
    ("preferred_language", "Preferred language", "legal_procedural", [], src("R75"), {}),
    ("qualified_interpreter", "Qualified interpreter", "personnel_role", [], src("R75"), {}),
    ("interpretation_services", "Interpretation services", "legal_procedural", [], src("R75"),
     {"note": "Spoken-language interpretation for parents; sign language and other services for deaf students are under interpreting."}),
    ("il_qualified_specialist", "Qualified specialist", "personnel_role", [], src("R75"), ILJ),
    ("il_notif_conference", "Parent/Guardian Notification of Conference", "legal_procedural", [], src("R75", "Vital Documents List"), ILJ),
    ("il_notif_conf_recs", "Parent/Guardian Notification of Conference Recommendations", "legal_procedural", [],
     src("R75", "Vital Documents List"), ILJ),
    ("il_consent_placement", "Consent for Placement", "legal_procedural", [], src("PG", "p. 22"), ILJ),
    ("il_date_of_referral", "Date of referral", "evaluation_eligibility", [], src("PG", "p. 40"), ILJ),
    ("chronic_absence", "Chronic absence", "discipline", [], src("PG", "p. 18"), {}),
    ("ebi", "Evidence-based interventions", "evaluation_eligibility", [], src("PG", "p. 14"), {}),
    ("il_dyslexia_guide", "The Dyslexia Guide: A Handbook for Parents, Educators, and Students", "legal_procedural", [],
     src("PG", "p. 35"), ILJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-IL"
LAYER_NAME = "Illinois (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
