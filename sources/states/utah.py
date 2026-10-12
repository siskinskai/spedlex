"""
Utah layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN    USBE, Special Education Rights of Parents and Students: Procedural
         Safeguards Notice (Jan. 2023)
  RULES  USBE, Special Education Rules (June 2023): §I.E definitions and the
         disability list under 'Student with a disability'

PSN references are 'candidate'; definitions from the Rules are
'machine_validated'. Utah's alternate assessment is Dynamic Learning Maps
(the Rules name its Essential Elements), so no separate Utah test record
was added.
"""

PSN_URL = "https://www.schools.utah.gov/parent/_parent_/ProceduralSafeguardsNotice2023SpEd.pdf"
RULES_URL = "https://schools.utah.gov/parent/_parent_/RulesSpecialEducationReport.pdf"


def src(doc, loc=""):
    if doc == "RULES":
        return {"source_type": "state_regulation", "citation": f"USBE Special Education Rules (June 2023){(', ' + loc) if loc else ''}", "url": RULES_URL}
    return {"source_type": "procedural_safeguards_notice", "citation": f"USBE Procedural Safeguards Notice (Jan. 2023){(', ' + loc) if loc else ''}", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
UT = ["US-UT"]
UTJ = {"jurisdiction": "US-UT"}
REG = {"status": "machine_validated"}

R = lambda n: src("RULES", f"I.E.{n}")

STRINGS = [
    ("autism", [], R(54)), ("sli", [], R(54)), ("id", [], R(54)), ("md", [], R(54)), ("oi", [], R(54)),
    ("ohi", [], R(54)), ("sld", [], R(54)), ("tbi", [], R(54)), ("vi", [], R(54)), ("deafblind", [], R(54)),
    ("ed", [("emotional-behavioral disability", S, UT)], R(54)),
    ("hi", [("hearing loss including deafness", S, UT), ("hearing loss", AB, None)], R(54)),
    ("dd", [], R(54)),
    ("cwd", [], R(54)),
    ("pe", [], R(1)),
    ("adaptive", [], R(2)),
    ("ess_elements", [], R(3)),
    ("at_device", [], R(4)),
    ("at_service", [], R(5)),
    ("bip", [], R(6)),
    ("voc_ed", [], R(7)),
    ("coteach", [], R(10)),
    ("lep", [("EL student", S, UT)], R(14)),
    ("evaluation", [], R(16)),
    ("srbi", [("evidence-based instruction", S, None)], R(17)),
    ("esy", [], R(18)),
    ("fba", [], R(21)),
    ("gen_curr", [], R(23)),
    ("iep", [], R(26)),
    ("iep_team", [], R(27)),
    ("inclusive", [], R(28)),
    ("ifsp", [], R(29)),
    ("iaes", [], R(30)),
    ("lre", [], R(31)),
    ("lea", [], R(32)),
    ("rti", [], R(33)),
    ("para", [], R(35)),
    ("transition", [("postsecondary transition services", S, UT)], R(39)),
    ("std_diploma", [("regular high school diploma", S, None)], R(44)),
    ("related", [], R(45)),
    ("special_ed", [], R(50)),
    ("sdi", [], R(51)),
    ("homeless", [("student experiencing homelessness", S, None), ("students experiencing homelessness", P, None)], R(55)),
    ("age_majority", [("student who is an adult", REL, UT)], R(56)),
    ("saas", [], R(57)),
    ("travel_training", [], R(58)),
    ("ward", [], R(59)),
    # Procedural safeguards notice
    ("pwn", [], src("PSN", "Rules IV.C")),
    ("iee", [], src("PSN", "Rules IV.B")),
    ("surrogate", [], src("PSN", "Rules IV.T")),
    ("uhy", [("unaccompanied youth experiencing homelessness", S, None)], src("PSN", "Rules IV.T")),
    ("state_complaint", [], src("PSN", "Rules IV.E")),
    ("mediation", [], src("PSN", "Rules IV.F")),
    ("dp_complaint", [], src("PSN", "Rules IV.G")),
    ("resolution", [], src("PSN", "Rules IV.J")),
    ("dp_hearing", [], src("PSN", "Rules IV.K")),
    ("stay_put", [("student's status during proceedings", S, UT)], src("PSN", "Rules IV.S")),
    ("mdr", [], src("PSN", "Rules V.E")),
    ("state_panel", [("Utah Special Education Advisory Panel", S, UT), ("USEAP", A, UT)], src("PSN", "p. 44")),
]

CONCEPTS = [
    ("usbe", "Utah State Board of Education", "legal_procedural", [("USBE", A, UT)], src("PSN", "p. 1"), {**UTJ, "broader": "sea"}),
    ("ut_rules", "USBE Special Education Rules", "legal_procedural", [("Special Education Rules", AB, UT)], src("RULES"), {**UTJ, **REG}),
    ("usdb", "Utah Schools for the Deaf and the Blind", "placement_setting", [("USDB", A, UT)], src("PSN", "pp. 24-26"), {**UTJ, "broader": "state_sp_sch"}),
    ("ut_parent_center", "Utah Parent Center", "legal_procedural", [], src("PSN", "p. 2"), {**UTJ, "broader": "pti"}),
    ("dlc_ut", "Disability Law Center", "legal_procedural", [], src("PSN", "p. 2"), UTJ),
    ("state_dir", "State Director of Special Education", "personnel_role", [], src("PSN", "pp. 30-31"), {}),
    ("uradd", "Utah Registry of Autism and Developmental Disabilities", "legal_procedural", [("URADD", A, UT)], src("PSN", "p. 6"), UTJ),
    ("carson_smith", "Carson Smith Special Needs Scholarship", "legal_procedural", [], src("PSN", "p. 3"),
     {**UTJ, "flags": ["eponym", "surname"], "note": "Named for a person; protected only as the full phrase."}),
    ("snos", "Special Needs Opportunity Scholarship Program", "legal_procedural", [], src("PSN", "p. 3"), UTJ),
    ("func_perf", "Functional performance", "functional_skill", [], R(22), REG),
    ("sor", "Science of Reading", "academic_skill", [], R(46), REG),
    ("slt", "Speech-Language Technician", "personnel_role", [], R(52), {**UTJ, **REG, "broader": "slp"}),
    ("service_animal", "Service animal", "accommodation_modification", [("service animals", P, None)], R(49), REG),
    ("utah_core", "Utah Core Standards", "academic_skill", [], src("RULES"), {**UTJ, **REG}),
]

JURISDICTION = "US-UT"
LAYER_NAME = "Utah"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.17.0"
