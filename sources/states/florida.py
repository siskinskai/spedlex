"""
Florida layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN   Part B Procedural Safeguards Notice: Florida (FDOE, Aug. 2021), read
        from a school district's copy (Indian River County)
  R11   Fla. Admin. Code R. 6A-6.03411, definitions (amended Dec. 2014)
  FAC   Fla. Admin. Code chapter 6A-6 rule headings (eligibility categories,
        procedures, scholarships)
  FAA   FDOE Florida Alternate Assessment page
  GRAD  Fla. Admin. Code R. 6A-1.09963, graduation requirements for students
        with disabilities (amended Sept. 2025)

PSN and FAA references come from text extraction and are 'candidate'.
Rule records are 'machine_validated'. FDLRS, BEESS, the matrix of services,
and Project 10 are common in Florida paperwork but were not attested here.
"""

PSN_URL = "https://www.indianriverschools.org//Userfiles/DBFiles/server_1549441/202110/48743347/procedural_safeguards_notice_florida.pdf"
R11_URL = "https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-6A-6-03411"
FAC_URL = "https://regulations.justia.com/states/florida/6/6a/chapter-6a-6"
FAA_URL = "https://fldoe.org/accountability/assessments/k-12-student-assessment/fl-alternate-assessment.stml"
GRAD_URL = "https://state-rules.com/florida/fac/6A-1.09963/"


def src(doc, loc=""):
    stype, title, url = {
        "PSN": ("procedural_safeguards_notice", "Part B Procedural Safeguards Notice: Florida (Aug. 2021)", PSN_URL),
        "R11": ("state_regulation", "Fla. Admin. Code R. 6A-6.03411(1)", R11_URL),
        "FAC": ("state_regulation", "Fla. Admin. Code R.", FAC_URL),
        "FAA": ("state_guidance", "FDOE Florida Alternate Assessment page", FAA_URL),
        "GRAD": ("state_regulation", "Fla. Admin. Code R. 6A-1.09963", GRAD_URL),
    }[doc]
    if doc == "FAC":
        return {"source_type": stype, "citation": f"{title} {loc}", "url": url}
    if doc in ("R11", "GRAD"):
        return {"source_type": stype, "citation": f"{title}{loc}", "url": url}
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
FL = ["US-FL"]
FLJ = {"jurisdiction": "US-FL"}
REG = {"status": "machine_validated"}

STRINGS = [
    # Definitions, 6A-6.03411(1)
    ("iep", [("individual educational plan", V, FL)], src("R11", "(u)")),
    ("iep_team", [("individual educational plan team", V, FL)], src("R11", "(v)")),
    ("special_ed", [("exceptional student education", S, FL), ("ESE", A, FL)], src("R11", "(n)")),
    ("test_accom", [], src("R11", "(a)")),
    ("program_mods", [], src("R11", "(z)")),
    ("bip", [], src("R11", "(d)")),
    ("esy", [], src("R11", "(o)")),
    ("fba", [], src("R11", "(q)")),
    ("gen_curr", [], src("R11", "(r)")),
    ("homeless", [("homeless student or youth", S, None)], src("R11", "(s)")),
    ("ifsp", [("individualized family support plan", V, FL)], src("R11", "(w)")),
    ("itd", [], src("R11", "(x)")),
    ("lep", [], src("R11", "(y)")),
    ("related", [], src("R11", "(dd)")),
    ("services_plan", [], src("R11", "(hh)")),
    ("sdi", [], src("R11", "(jj)")),
    ("saas", [], src("R11", "(mm)")),
    ("transition", [], src("R11", "(nn)")),
    ("ward", [], src("R11", "(oo)")),
    # Eligibility rules (chapter 6A-6 headings)
    ("id", [], src("FAC", "6A-6.03011")),
    ("sli", [("speech impairment", S, FL), ("speech impairments", P, FL)], src("FAC", "6A-6.03012")),
    ("lang_dis", [("language impairment", S, FL), ("language impairments", P, FL)], src("FAC", "6A-6.030121")),
    ("hi", [("deaf or hard-of-hearing", V, FL)], src("FAC", "6A-6.03013")),
    ("vi", [("visually impaired", S, FL)], src("FAC", "6A-6.03014")),
    ("oi", [], src("FAC", "6A-6.030151")),
    ("ohi", [], src("FAC", "6A-6.030152")),
    ("tbi", [], src("FAC", "6A-6.030153")),
    ("ed", [("emotional/behavioral disabilities", S, FL), ("emotional/behavioral disability", V, FL), ("E/BD", A, FL)], src("FAC", "6A-6.03016")),
    ("sld", [], src("FAC", "6A-6.03018")),
    ("gifted", [], src("FAC", "6A-6.03019")),
    ("home_instr", [("homebound or hospitalized", S, FL), ("hospital/homebound", S, FL)], src("FAC", "6A-6.03020")),
    ("deafblind", [("dual sensory impairment", S, FL), ("dual sensory impairments", P, FL)], src("FAC", "6A-6.03022")),
    ("autism", [], src("FAC", "6A-6.03023")),
    ("ot", [], src("FAC", "6A-6.03024")),
    ("pt", [], src("FAC", "6A-6.03024")),
    ("dd", [], src("FAC", "6A-6.03027")),
    ("ppps", [], src("FAC", "6A-6.030281")),
    ("surrogate", [], src("FAC", "6A-6.0333")),
    # Procedural safeguards notice
    ("pwn", [], src("PSN", "pp. 1-2")),
    ("iee", [], src("PSN", "pp. 4-5")),
    ("state_complaint", [], src("PSN", "pp. 10-11")),
    ("mediation", [], src("PSN", "pp. 13-14")),
    ("resolution", [("resolution agreement", S, None)], src("PSN", "pp. 14-15")),
    ("dp_hearing", [], src("PSN", "pp. 16-17")),
    ("mdr", [], src("PSN", "pp. 22-23")),
    ("iaes", [], src("PSN", "pp. 22-23")),
    ("exp_hearing", [], src("PSN", "p. 25")),
    ("basis_know", [], src("PSN", "p. 25")),
    ("child_find", [], src("PSN", "p. 6")),
    # Assessment
    ("alt_assess", [], src("FAA")),
    ("sig_cog", [], src("FAA")),
    ("eoc", [], src("FAA")),
]

CONCEPTS = [
    ("fldoe", "Florida Department of Education", "legal_procedural", [("FDOE", A, FL)], src("PSN", "p. 1"), {**FLJ, "broader": "sea"}),
    ("doah", "Division of Administrative Hearings", "legal_procedural", [("DOAH", A, FL)], src("PSN", "p. 16"),
     {**FLJ, "broader": "dp_hearing", "note": "Runs Florida's due process hearings, as OAH does in California."}),
    ("fl_fac", "Florida Administrative Code", "legal_procedural", [("F.A.C.", A, FL)], src("R11"), {**FLJ, **REG}),
    ("exc_student", "Exceptional student", "legal_procedural", [("exceptional students", P, FL)], src("R11", "(m)"),
     {**REG, "note": "Covers students with disabilities and students who are gifted. Florida and Kansas both use the term."}),
    ("ep_gifted", "Educational plan", "iep_component", [("educational plans", P, FL)], src("R11", "(j)"),
     {**FLJ, **REG, "broader": "gifted", "note": "Florida's plan for students identified only as gifted. The abbreviation 'EP' is too ambiguous to safelist."}),
    ("ese_center", "ESE center", "placement_setting", [("exceptional student education center", S, FL), ("ESE center school", S, FL)], src("PSN", "p. 4"),
     {**FLJ, "broader": "special_school", "note": "Florida requires separate parental consent for this placement."}),
    ("alt_std_consent", "Consent for instruction in alternate academic achievement standards", "legal_procedural", [], src("PSN", "p. 4"),
     {**FLJ, "broader": "consent", "note": "Florida requires parental consent before instruction in access points and before certain instructional accommodations."}),
    ("access_points", "Access points", "academic_skill", [("access point", P, FL)], src("GRAD", "(2)(a)"),
     {**FLJ, **REG, "note": "Reduced-complexity standards; compare Texas essence statements, Virginia's VESOL, and California's Core Content Connectors."}),
    ("access_courses", "Access courses", "transition", [], src("GRAD", "(2)(b)"), {**FLJ, **REG, "broader": "access_points"}),
    ("emp_trans", "Employment transition plan", "transition", [], src("GRAD", "(2)(d)"), {**FLJ, **REG}),
    ("acad_emp", "Mastery of academic and employment competencies", "transition", [("academic and employment competencies", AB, FL)], src("GRAD", "(4)"), {**FLJ, **REG}),
    ("defer_dip", "Deferral of diploma", "transition", [("diploma deferral", S, FL), ("defer receipt of the diploma", S, FL)], src("GRAD", "(6)"), {**FLJ, **REG}),
    ("faa", "Florida Alternate Assessment", "iep_component", [("FAA", A, FL), ("FAA Performance Task", S, FL), ("FAA Datafolio", REL, FL),
                                                             ("Florida Standards Alternate Assessment", REL, FL), ("FSAA", A, FL)], src("FAA"),
     {**FLJ, "broader": "alt_assess", "note": "Renamed from the Florida Standards Alternate Assessment (FSAA); older IEPs use the old name."}),
    ("fast", "Florida Assessment of Student Thinking", "iep_component", [("FAST", A, FL)], src("FAA"),
     {**FLJ, "flags": ["common_english_word"], "note": "'FAST' is protected only as an all-caps match."}),
    ("best", "Benchmarks for Excellent Student Thinking", "academic_skill", [("B.E.S.T. Standards", S, FL), ("B.E.S.T.", A, FL)], src("FAA"), FLJ),
    ("gen_ed_int", "General education intervention procedures", "evaluation_eligibility", [("general education interventions", S, None)], src("FAC", "6A-6.0331"),
     {**REG, "broader": "rti"}),
    ("prek_cwd", "Prekindergarten children with disabilities", "early_intervention", [], src("FAC", "6A-6.03026"), {**FLJ, **REG}),
    ("est_cond", "Established conditions", "early_intervention", [("established condition", P, None)], src("FAC", "6A-6.03030"), REG),
    ("vpk", "Voluntary Prekindergarten", "early_intervention", [("VPK", A, FL)], src("FAC", "6A-6.03033"), {**FLJ, **REG}),
    ("sis_vpk", "Specialized instructional services", "related_service", [("SIS", A, FL)], src("FAC", "6A-6.03033"), {**FLJ, **REG, "broader": "vpk"}),
    ("fes", "Family Empowerment Scholarship", "legal_procedural", [("Family Empowerment Scholarship Program", S, FL)], src("FAC", "6A-6.0952"), {**FLJ, **REG}),
    ("mckay", "John M. McKay Scholarship for Students with Disabilities", "legal_procedural", [("McKay Scholarship", AB, FL)], src("FAC", "6A-6.0970"),
     {**FLJ, **REG, "flags": ["eponym", "surname"], "note": "Repealed program that still appears in older records; protected only as the full phrase."}),
    ("gardiner", "Gardiner Scholarship", "legal_procedural", [("Gardiner Scholarship Program", REL, FL)], src("FAC", "6A-6.0961"),
     {**FLJ, **REG, "flags": ["eponym", "surname"], "note": "Repealed program; protected only as the full phrase."}),
]

JURISDICTION = "US-FL"
LAYER_NAME = "Florida"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.8.0"
