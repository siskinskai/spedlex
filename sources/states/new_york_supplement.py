"""
New York layer, consistency additions.

A second reading of the New York layer's own documents for terms the first
pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PSN  NYSED Procedural Safeguards Notice (July 2017), cited by page
  R1   8 NYCRR §200.1 (definitions), cited by paragraph
  R6   8 NYCRR §200.6 (continuum of services), cited by subdivision
"""

from .new_york import src, A, S, V, L, AB, P, NY, NYJ

STRINGS = [
    ("co_boces", [("board of cooperative educational services", S, NY)], src("R6", "(l)")),
]

CONCEPTS = [
    ("ny_ocfs", "Office of Children and Family Services", "legal_procedural", [], src("PSN", "p. 3"), NYJ),
    ("ny_statewide_coord", "Statewide Coordinator for Special Education", "personnel_role", [], src("PSN", "p. 13"), NYJ),
    ("ny_supt_hearing", "Superintendent's hearing", "discipline", [], src("PSN", "p. 30"), NYJ),
    ("ny_ssl", "Social Services Law", "legal_procedural", [], src("PSN", "p. 3"), NYJ),
    ("ny_fca", "Family Court Act", "legal_procedural", [], src("PSN", "p. 3"), NYJ),
    ("ny_education_law", "Education Law", "legal_procedural", [], src("PSN", "p. 30"),
     {**NYJ, "note": "New York's Education Law; Article 89 governs special education."}),
    ("ny_usny", "University of the State of New York", "legal_procedural", [], src("PSN", "cover"), NYJ),
    ("class_size", "Class size", "placement_setting", [], src("R1", "(i)"), {"flags": ["common_english_word"]}),
    ("sd_reading_instr", "Specially designed reading instruction", "academic_skill", [], src("R6", "(b)(6)"), {"broader": "sdi"}),
    ("ny_seven_day_residential", "Seven-day residential program", "placement_setting", [], src("R6", "(k)"), NYJ),
    ("ny_state_supported_school", "State-supported school", "placement_setting", [], src("R6", "(l)"), NYJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-NY"
LAYER_NAME = "New York (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
