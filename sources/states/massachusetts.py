"""
Massachusetts layer for SPEDLex.

Sources reviewed 2026-10-03:
  PNPS  DESE, Parent's Notice of Procedural Safeguards (updated May 30, 2025)
  R02   603 CMR 28.02, definitions (including the disability types)
  PG    Federation for Children with Special Needs and the Massachusetts
        Department of Education, A Parent's Guide to Special Education (undated;
        uses the department's former name)

PNPS and PG references come from text extraction and are 'candidate';
603 CMR records are 'machine_validated'. The N1 notice code, IEP form codes,
SEPAC, and the inclusion/substantially-separate placement labels were not
attested in these sources.
"""

PNPS_URL = "https://www.doe.mass.edu/specialeducation/families/prb/pnps.pdf"
R02_URL = "https://www.doe.mass.edu/lawsregs/603CMR28.html?section=02"
PG_URL = "https://www.mass.gov/doc/a-parents-guide-to-special-education/download"


def src(doc, loc=""):
    if doc == "R02":
        return {"source_type": "state_regulation", "citation": f"603 CMR 28.02{loc}", "url": R02_URL}
    stype, title, url = {
        "PNPS": ("procedural_safeguards_notice", "DESE Parent's Notice of Procedural Safeguards (updated May 2025)", PNPS_URL),
        "PG": ("state_guidance", "FCSN/Massachusetts DOE, A Parent's Guide to Special Education", PG_URL),
    }[doc]
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
MA = ["US-MA"]
MAJ = {"jurisdiction": "US-MA"}
REG = {"status": "machine_validated"}

STRINGS = [
    # 603 CMR 28.02 and its disability types
    ("autism", [], src("R02", "(7)")),
    ("dd", [], src("R02", "(7)")),
    ("id", [("intellectual impairment", S, MA), ("mental retardation", L, MA)], src("R02", "(7)")),
    ("ed", [("emotional impairment", S, MA)], src("R02", "(7)")),
    ("sli", [("communication impairment", S, MA)], src("R02", "(7)")),
    ("oi", [("physical impairment", REL, MA)], src("R02", "(7)")),
    ("ohi", [("health impairment", S, MA)], src("R02", "(7)")),
    ("sld", [], src("R02", "(7)")),
    ("hi", [("hearing impairment/deaf", V, MA)], src("R02", "(7)")),
    ("vi", [("vision impairment/blind", V, MA), ("vision impairment", S, MA)], src("R02", "(7)")),
    ("deafblind", [("deafblind", V, MA)], src("R02", "(7)")),
    ("iep", [], src("R02", "(11)")),
    ("lre", [], src("R02", "(12)")),
    ("related", [], src("R02", "(18)")),
    ("special_ed", [], src("R02", "(20)")),
    ("iep_team", [("Team meeting", REL, MA)], src("R02", "(21)")),
    ("sped_teacher", [("certified special educator", S, MA)], src("R02", "(3)")),
    ("approved_priv", [("approved private special education school", S, MA)], src("R02", "(1)")),
    # Parent's notice of procedural safeguards
    ("pwn", [("Notice of Proposed School District Action", S, MA)], src("PNPS", "p. 2")),
    ("consent", [], src("PNPS", "p. 3")),
    ("revoke", [], src("PNPS", "pp. 3-4")),
    ("reeval", [("three-year reevaluation", S, None)], src("PNPS", "pp. 3-4")),
    ("iee", [], src("PNPS", "p. 5")),
    ("surrogate", [("special education surrogate parent", S, MA), ("educational surrogate parent", S, None)], src("PNPS", "p. 4")),
    ("age_majority", [], src("PNPS", "p. 4")),
    ("stay_put", [], src("PNPS", "p. 7")),
    ("state_complaint", [], src("PNPS", "p. 8")),
    ("mediation", [], src("PNPS", "p. 9")),
    ("resolution", [], src("PNPS", "p. 11")),
    ("transition", [], src("PNPS", "p. 13")),
    ("mdr", [], src("PNPS", "p. 14")),
    ("iaes", [], src("PNPS", "p. 14")),
    ("fba", [], src("PNPS", "p. 15")),
    ("exp_hearing", [], src("PNPS", "p. 15")),
    # Parent guide
    ("vision_future", [], src("PG", "pp. 19-20, 26")),
    ("seac", [("Parent Advisory Council", S, MA), ("PAC", A, MA)], src("PG", "p. 10")),
    ("s504", [], src("PG", "p. 31")),
    ("gen_curr", [], src("PG", "pp. 20, 27")),
    ("annual_goals", [], src("PG", "pp. 21-22")),
]

CONCEPTS = [
    ("dese_ma", "Massachusetts Department of Elementary and Secondary Education", "legal_procedural",
     [("DESE", A, MA), ("Massachusetts Department of Education", L, MA)], src("PNPS", "p. 1"), {**MAJ, "broader": "sea"}),
    ("bsea", "Bureau of Special Education Appeals", "legal_procedural", [("BSEA", A, MA), ("BSEA Hearing Request Form", REL, MA)], src("PNPS", "p. 10"),
     {**MAJ, "broader": "dp_hearing", "note": "Runs Massachusetts's mediations and due process hearings."}),
    ("prs", "Problem Resolution System", "legal_procedural", [("PRS", A, MA), ("Problem Resolution System Office", S, MA)], src("PNPS", "p. 8"),
     {**MAJ, "broader": "state_complaint", "note": "DESE's state complaint office."}),
    ("pqa", "Program Quality Assurance", "legal_procedural", [("PQA", A, MA)], src("PG", "p. 32"), {**MAJ, "broader": "dese_ma"}),
    ("ch766", "Chapter 766", "legal_procedural", [("M.G.L. c. 71B", A, MA), ("Chapter 71B", S, MA)], src("PNPS", "p. 14"),
     {**MAJ, "note": "Popular name for Massachusetts's special education law (1972)."}),
    ("cmr28", "603 CMR 28.00", "legal_procedural", [("603 CMR 28", AB, MA)], src("PNPS", "p. 14"), MAJ),
    ("masshealth", "MassHealth", "legal_procedural", [], src("PNPS", "pp. 3-4"), {**MAJ, "note": "Massachusetts Medicaid; schools may bill it for IEP services with consent."}),
    ("fcsn", "Federation for Children with Special Needs", "legal_procedural", [("FCSN", A, MA)], src("PG", "pp. 4-5"), {**MAJ, "broader": "pti"}),

    ("sensory_imp", "Sensory impairment", "disability_category", [], src("R02", "(7)"),
     {**MAJ, **REG, "note": "Massachusetts umbrella type covering hearing impairment/deaf, vision impairment/blind, and deafblind."}),
    ("neuro_imp", "Neurological impairment", "disability_category", [], src("R02", "(7)"),
     {**MAJ, **REG, "note": "Massachusetts disability type with no single federal equivalent; often maps to OHI or TBI federally."}),
    ("eff_progress", "Effective progress", "evaluation_eligibility", [("progress effectively in the general education program", S, MA)], src("R02", "(17)"),
     {**MAJ, **REG, "note": "Massachusetts eligibility test: the disability prevents effective progress without specialized instruction."}),
    ("team_chair", "Team Chairperson", "personnel_role", [("Team chair", AB, MA)], src("PG", "p. 24"), MAJ),
    ("in_district", "In-district program", "placement_setting", [], src("R02", "(10)"), {**MAJ, **REG}),
    ("out_district", "Out-of-district program", "placement_setting", [("out-of-district placement", S, MA)], src("R02", "(14)"), {**MAJ, **REG}),
    ("pre_eval_conf", "Pre-evaluation conference", "evaluation_eligibility", [], src("PG", "p. 12"), MAJ),
    ("home_assess", "Home assessment", "evaluation_eligibility", [], src("PG", "p. 14"), MAJ),
    ("spec_assess", "Specialist assessment", "evaluation_eligibility", [], src("PG", "p. 14"), MAJ),
    ("ch688", "Chapter 688 referral", "transition", [("Chapter 688", AB, MA), ("Chapter 688 planning", REL, MA)], src("PG", "pp. 26-27"),
     {**MAJ, "note": "Massachusetts's referral of students with severe disabilities to adult service agencies."}),
    ("tpf", "Transition Planning Form", "transition", [("TPF", A, MA)], src("PNPS", "p. 13"), {**MAJ, "note": "'TPF' is practitioner usage."}),
    ("mcas", "Massachusetts Comprehensive Assessment System", "iep_component", [("MCAS", A, MA)], src("PG", "pp. 23-24"), MAJ),
    ("mcas_alt", "MCAS Alternate Assessment", "iep_component", [("MCAS-Alt", A, MA)], src("PG", "p. 24"), {**MAJ, "broader": "alt_assess"}),
    ("ma_frameworks", "Massachusetts Curriculum Frameworks", "academic_skill", [("curriculum frameworks", AB, MA)], src("PG", "pp. 20, 23-24"), MAJ),
]

JURISDICTION = "US-MA"
LAYER_NAME = "Massachusetts"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.11.0"
