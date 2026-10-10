"""
Texas layer, consistency additions.

A second reading of the Texas layer's own documents, plus two more sections
of 19 TAC Chapter 89, Subchapter AA, for terms the first pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  NPS   TEA Notice of Procedural Safeguards (Jan. 2025), cited by page
  ARD   TEA Parent's Guide to the ARD Process (Jan. 2025), cited by page
  TAC   19 TAC §89.1040 (eligibility criteria), cited by subsection
  T55   19 TAC §89.1055 (content of the IEP), cited by subsection
"""

from .texas import src, A, S, V, L, AB, P, TX

TXJ = {"jurisdiction": "US-TX"}
T55 = lambda loc: {"source_type": "state_regulation", "citation": f"19 TAC §89.1055{loc}",
                   "url": "https://www.law.cornell.edu/regulations/texas/19-Tex-Admin-Code-SS-89-1055"}

STRINGS = [
    ("iep_facil", [("State IEP Facilitation Project", S, TX)], src("NPS", "p. 21")),
    ("fva", [("functional vision evaluation", V, None)], src("TAC", "(c)(12)")),
    ("hats", [("hearing assistive technology", AB, None)], src("TAC", "(c)(3)")),
]

CONCEPTS = [
    ("tx_hhsc", "Texas Health and Human Services Commission", "legal_procedural", [], src("ARD", "p. 3"), TXJ),
    ("tx_sboe", "Texas State Board of Education", "legal_procedural", [], src("ARD", "p. 6"), {**TXJ, "broader": "sea"}),
    ("tx_complaints_unit", "Special Education Complaints Unit", "legal_procedural", [], src("NPS", "p. 21"), {**TXJ, "broader": "tea"}),
    ("tx_mediation_program", "Special Mediation Program", "legal_procedural", [], src("NPS", "p. 13"), {**TXJ, "broader": "tea"}),
    ("tx_beyond_eci", "Beyond ECI", "early_intervention", [], src("ARD", "p. 3"), TXJ),
    ("tx_family_code", "Texas Family Code", "legal_procedural", [], src("NPS", "p. 11"), TXJ),
    ("tx_parent_family_training", "Parent/family training and support", "related_service", [], T55("(g)"), {**TXJ, "broader": "autism_strat"}),
    ("tx_comm_interventions", "Communication interventions", "related_service", [], T55("(g)"), {**TXJ, "broader": "autism_strat"}),
    ("tx_staff_support", "Professional educator/staff support", "related_service", [], T55("(g)"), {**TXJ, "broader": "autism_strat"}),
    ("discrete_trial", "Discrete-trial training", "related_service", [], T55("(g)"), {}),
    ("visual_supports", "Visual supports", "accommodation_modification", [], T55("(g)"), {}),
    ("lssp", "Licensed specialist in school psychology", "personnel_role", [("LSSP", A, TX)], src("TAC", "(b)"),
     {**TXJ, "broader": "school_psych"}),
    ("dyslexia_screener", "Dyslexia screener", "instrument", [], src("TAC", "(c)(9)"), {}),
    ("remedial_reading_teacher", "Remedial reading teacher", "personnel_role", [], src("TAC", "(c)(9)"), {}),
    ("om_eval", "Orientation and mobility evaluation", "evaluation_eligibility", [], src("TAC", "(c)(12)"), {"broader": "om"}),
    ("low_vision_eval", "Clinical low vision evaluation", "evaluation_eligibility", [], src("TAC", "(c)(12)"), {}),
    ("sem", "Standard error of measurement", "score_metric", [("SEM", A, None)], src("TAC", "(c)(13)"), {}),
    ("play_based_assess", "Play-based assessment", "evaluation_eligibility", [("play-based assessments", P, None)], src("TAC", "(c)(13)"), {}),
    ("written_translation", "Written translation", "legal_procedural", [], src("ARD", "p. 16"), {}),
    ("dual_enrollment", "Dual enrollment", "placement_setting", [], src("ARD", "p. 3"), {}),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-TX"
LAYER_NAME = "Texas (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"  # tools/add_state.py sets this
