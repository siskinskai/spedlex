"""
Indiana layer, audit additions.

Terms the independent audit of the Indiana layer (provenance/in/in-layer-audit-
2026-10-08.md) found in the same documents but missing from the first pass.
Sources reviewed 2026-10-08 (the Indiana layer's documents and citation format):
  RULE  511 IAC 7 (IDOE compilation, May 2024), cited by rule section
  PSN   IDOE Notice of Procedural Safeguards (Aug. 2025), cited by PDF page

The `ceis` attestation is here, not in the Indiana layer, because that
concept is defined by a later layer (Alabama). RULE records are
'machine_validated'; PSN records are 'candidate'. Left out on purpose: "ESA"
on its own, which already means educational service agency, and "ESA
account".
"""

from .indiana import src, A, S, V, L, AB, P, IN, INJ, R, PS

STRINGS = [
    ("ceis", [], R("7-32-29")),
]

CONCEPTS = [
    ("in_esa", "Indiana education scholarship account", "legal_procedural",
     [("education scholarship account", S, IN)], R("7-50-2"),
     {**INJ, "note": "An account set up under IC 20-51.4 for an eligible student; 511 IAC 7-50 sets the special education rules for these students."}),
    ("in_esa_plan", "Education scholarship account education service plan", "iep_component",
     [("ESA service plan", AB, IN)], R("7-50-2"),
     {**INJ, "broader": "services_plan"}),
    ("in_ichamp", "Indiana Complaint, Hearing, and Mediation Process", "legal_procedural", [("I-CHAMP", A, IN)], PS(16),
     {**INJ, "note": "IDOE's online portal for filing state complaints."}),
    ("expedited_eval", "Expedited evaluation", "evaluation_eligibility", [], R("7-32-38"),
     {"note": "An initial evaluation conducted while disciplinary action is pending for a student not yet found eligible."}),
    ("print_disability", "Student with a print disability", "legal_procedural", [("print disability", S, None)], R("7-32-93"),
     {"note": "A student who may qualify for print instructional materials in accessible formats."}),
    ("virtual_instr", "Virtual instruction", "placement_setting", [], R("7-32-103.5"), {}),
]

JURISDICTION = "US-IN"
LAYER_NAME = "Indiana (audit additions)"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.38.0"
