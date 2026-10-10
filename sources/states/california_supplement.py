"""
California layer, consistency additions.

A second reading of the California layer's safeguards notice, plus 5 CCR §3001
(definitions) and Education Code §§56026, 56345 and 56521.1, for terms the
first pass left out. Behavior Emergency Report, which the layer's docstring
deferred, is attested here from §56521.1.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  NPS     CDE Notice of Procedural Safeguards, as posted by OAH, cited by section heading
  CCR01   5 CCR §3001 (definitions), cited by subdivision
  EC      Cal. Educ. Code §§56026, 56345 and 56521.1, cited by subdivision
"""

from .california import src, A, S, V, L, AB, P, CA, CAJ, EC_URL

CCR01 = lambda loc: {"source_type": "state_regulation", "citation": f"5 CCR §3001{loc}",
                     "url": "https://www.law.cornell.edu/regulations/california/5-CCR-3001"}
EC = lambda sec, loc: {"source_type": "state_regulation", "citation": f"Cal. Educ. Code §{sec}{loc}", "url": EC_URL.format(sec)}

STRINGS = [
    ("pti", [("Parent Training and Information Centers", P, None), ("PTICs", P, CA)], src("NPS", "Where can I get more help?")),
    ("state_sp_sch", [("California Schools for the Deaf", P, CA)], src("NPS", "What if my child is deaf, hard of hearing, blind, visually impaired, or deaf-blind?")),
    ("native_language", [("primary language", S, CA)], CCR01("(q)")),
]

CONCEPTS = [
    ("ca_ber", "Behavioral emergency report", "discipline", [("behavioral emergency reports", P, CA)], EC("56521.1", "(e)"), CAJ),
    ("emergency_intervention", "Emergency intervention", "discipline", [("emergency interventions", P, None)], EC("56521.1", "(a)"), {}),
    ("ca_systematic_bip", "Systematic behavioral intervention plan", "discipline", [], EC("56521.1", "(b)"), {**CAJ, "broader": "bip"}),
    ("locked_seclusion", "Locked seclusion", "discipline", [], EC("56521.1", "(d)(1)"), {}),
    ("ca_complaint_support_unit", "Complaint Support Unit", "legal_procedural", [], src("NPS", "State Complaint Procedures"),
     {**CAJ, "broader": "cde_sed"}),
    ("ca_isa", "Individual Services Agreement", "legal_procedural", [], CCR01("(j)"), CAJ),
    ("ca_master_contract", "Master contract", "legal_procedural", [], CCR01("(o)"), CAJ),
    ("sphcs", "Specialized physical health care services", "related_service", [], CCR01("(s)"), {}),
    ("ca_specified_placement", "Specified education placement", "placement_setting", [], CCR01("(t)"), CAJ),
    ("ca_temp_phys_disability", "Temporary physical disability", "evaluation_eligibility", [], CCR01("(v)"), CAJ),
    ("ca_ctc", "California Commission on Teacher Credentialing", "legal_procedural", [("CTC", A, CA)], CCR01("(g)"), CAJ),
    ("ca_sspi", "California State Superintendent of Public Instruction", "personnel_role", [("SSPI", A, CA)], CCR01("(u)"), CAJ),
    ("ca_contracting_agency", "Contracting education agency", "legal_procedural", [], CCR01("(f)"), CAJ),
    ("ca_linguistic_goals", "Linguistically appropriate goals, objectives, and programs", "iep_component", [], CCR01("(m)"), CAJ),
    ("ca_wic", "Welfare and Institutions Code", "legal_procedural", [], src("NPS", "Surrogate Parent Appointment"), CAJ),
    ("ca_year_round", "Year-round school program", "placement_setting", [], EC("56026", "(c)(4)(B)"), CAJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-CA"
LAYER_NAME = "California (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
