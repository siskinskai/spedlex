"""
Pennsylvania layer, second consistency additions.

A second reading of the Pennsylvania layer's documents (and 22 Pa. Code §14.101,
already read by pennsylvania_supplement) for terms the first passes left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PG    PDE Pennsylvania Parent Guide to Special Education (July 2008), cited by page
  R105  22 Pa. Code §14.105 (personnel), cited by subsection
  R101  22 Pa. Code §14.101 (definitions)
"""

from .pennsylvania import src, A, S, V, L, AB, P, PA, PAJ
from .pennsylvania_supplement import src as src101

CONCEPTS = [
    ("pattan", "Pennsylvania Training and Technical Assistance Network", "legal_procedural", [("PaTTAN", A, PA)],
     src("PG", "inside cover (unnumbered)"), PAJ),
    ("pa_waive_reeval", "Agreement to Waive Reevaluation", "evaluation_eligibility", [], src("PG", "p. 5"), PAJ),
    ("pa_phrc", "Pennsylvania Human Relations Commission", "legal_procedural", [], src("PG", "back cover (unnumbered)"), PAJ),
    ("pa_eisa", "Early Intervention Services System Act", "legal_procedural", [], src101("R101"), PAJ),
    ("pa_mawa", "Mutually agreed-upon written arrangement", "early_intervention", [("MAWA", A, PA)], src101("R101"), PAJ),
    ("pa_avts", "Area vocational-technical school", "placement_setting", [], src101("R101"), PAJ),
    ("cyber_charter", "Cyber charter school", "placement_setting", [], src101("R101"), {"broader": "charter_school"}),
    ("personal_care_assistant", "Personal care assistant", "personnel_role", [], src("R105", "(a)(4)"), {}),
    ("transliterator", "Qualified transliterator", "personnel_role", [], src("R105", "(b)(1)(ii)"), {"broader": "interpreting"}),
    ("pbsp", "Positive behavior support plan", "discipline", [("positive behavior support plans", P, None)], src("R105", "(a)(1)"),
     {"broader": "bip"}),
    ("pa_sped_plan", "Special education plan", "legal_procedural", [], src("R105", "(c)(4)"), PAJ),
    ("caseload", "Caseload", "placement_setting", [], src("R105", "(c)(2)"), {"flags": ["common_english_word"]}),
    ("pa_sbap", "School-based access program", "legal_procedural", [], src("R105", "(a)(4)"), PAJ),
    ("pa_chartered_deaf_blind", "Chartered schools for the deaf and blind", "placement_setting", [], src("R105", "(c)(6)"), PAJ),
]

STRINGS = []

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-PA"
LAYER_NAME = "Pennsylvania (second consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
