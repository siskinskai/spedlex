"""
Minnesota layer for SPEDLex.

Sources reviewed 2026-10-03:
  ELIG  Minn. R. 3525.1325-3525.1354, entrance and exit criteria (headings)
  DEF   Minn. R. 3525.0210 definitions, and terms used elsewhere in chapter 3525
  STAT  Minn. Stat. §125A.091, alternative dispute resolution and due process
  POL   A Minnesota district's Policy 615 on testing accommodations (rev. 2026),
        used for state assessment names

Minnesota's procedural safeguards notice was not readable (a district link
returned 404 and a shared copy redirected off-site), so the statute stands
in for it. Rule and statute records are 'machine_validated'; the district
policy is 'candidate'.
"""

ELIG_URL = "https://regulations.justia.com/states/minnesota/agency-129/chapter-3525/entrance-and-exit-criteria"
DEF_URL = "https://www.revisor.mn.gov/rules/3525/full"
STAT_URL = "https://www.revisor.mn.gov/statutes/cite/125A.091"
POL_URL = "https://www.isd622.org/about/policies/policy/~board/policies/post/615"


def src(doc, loc=""):
    if doc == "ELIG":
        return {"source_type": "state_regulation", "citation": f"Minn. R. {loc}", "url": ELIG_URL}
    if doc == "DEF":
        return {"source_type": "state_regulation", "citation": f"Minn. R. {loc}", "url": DEF_URL}
    if doc == "STAT":
        return {"source_type": "state_regulation", "citation": f"Minn. Stat. §125A.091{(', ' + loc) if loc else ''}", "url": STAT_URL}
    return {"source_type": "secondary_guidance", "citation": "Minnesota district Policy 615, Testing Accommodations (rev. 2026)", "url": POL_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
MN = ["US-MN"]
MNJ = {"jurisdiction": "US-MN"}
REG = {"status": "machine_validated"}

STRINGS = [
    ("autism", [("autism spectrum disorders", P, None)], src("ELIG", "3525.1325")),
    ("deafblind", [], src("ELIG", "3525.1327")),
    ("ed", [("emotional or behavioral disorders", S, MN), ("emotional or behavioral disorder", P, MN)], src("ELIG", "3525.1329")),
    ("hi", [("deaf and hard of hearing", S, MN)], src("ELIG", "3525.1331")),
    ("id", [("developmental cognitive disability", S, MN), ("DCD", A, MN)], src("ELIG", "3525.1333")),
    ("ohi", [("other health disabilities", S, MN), ("other health disability", P, MN)], src("ELIG", "3525.1335")),
    ("oi", [("physically impaired", REL, MN)], src("ELIG", "3525.1337")),
    ("md", [("severely multiply impaired", S, MN)], src("ELIG", "3525.1339")),
    ("sld", [], src("ELIG", "3525.1341")),
    ("sli", [("speech or language impairments", P, None)], src("ELIG", "3525.1343")),
    ("vi", [("visually impaired", S, MN)], src("ELIG", "3525.1345")),
    ("tbi", [], src("ELIG", "3525.1348")),
    ("itd", [("infant and toddler intervention services", REL, MN)], src("ELIG", "3525.1350")),
    ("ecse", [], src("ELIG", "3525.1351")),
    ("pe", [("developmental adapted physical education", REL, MN), ("DAPE", A, MN)], src("ELIG", "3525.1352")),
    ("adr", [], src("DEF", "3525.0210, subp. 4")),
    ("iep_facil", [("facilitated IEP meeting", S, None), ("facilitated team meeting", S, MN)], src("DEF", "3525.0210, subp. 20")),
    ("dp_hearing", [], src("DEF", "3525.0210, subps. 16, 25")),
    ("evaluation", [], src("DEF", "3525.0210, subp. 18")),
    ("esy", [], src("DEF", "3525.0210, subp. 19")),
    ("fba", [], src("DEF", "3525.0210, subp. 22")),
    ("init_place", [], src("DEF", "3525.0210, subp. 26")),
    ("ifsp", [], src("DEF", "3525.0210, subp. 28")),
    ("mediation", [], src("DEF", "3525.0210, subp. 31")),
    ("para", [], src("DEF", "3525.0210, subp. 33")),
    ("regular_class", [("regular education program", S, None)], src("DEF", "3525.0210, subp. 38")),
    ("special_ed", [], src("DEF", "3525.0210, subp. 42")),
    ("sped_teacher", [("IEP manager", S, MN)], src("DEF", "3525.0550")),
    ("child_find", [], src("DEF", "3525.1100")),
    ("eval_report", [], src("DEF", "3525.1325")),
    ("pbis", [("positive behavioral interventions", S, None)], src("DEF", "3525.0850")),
    ("pwn", [], src("STAT", "subd. 3a")),
    ("exp_hearing", [], src("STAT", "subd. 19")),
    ("resolution", [], src("STAT", "subd. 19")),
    ("alt_assess", [], src("POL")),
    ("sig_cog", [], src("POL")),
    ("access_ell", [("ACCESS for ELs", V, None), ("Alternate ACCESS for ELLs", S, None)], src("POL")),
]

CONCEPTS = [
    ("mde_mn", "Minnesota Department of Education", "legal_procedural", [], src("DEF", "3525.0210, subp. 12"),
     {**MNJ, **REG, "broader": "sea", "note": "The rules call it 'the department'. Its acronym MDE is shared with other states, so it is not safelisted alone."}),
    ("conciliation", "Conciliation conference", "legal_procedural", [("conciliation conference memorandum", REL, MN)], src("STAT", "subd. 7"),
     {**MNJ, **REG, "broader": "adr", "note": "Minnesota's meeting with IEP team members to resolve a dispute before mediation or a hearing."}),
    ("iiip", "Individualized Interagency Intervention Plan", "iep_component", [("IIIP", A, MN)], src("DEF", "3525.0210"),
     {**MNJ, **REG, "note": "Minnesota's plan for a child who receives services from several agencies."}),
    ("cultural_liaison", "Cultural liaison", "personnel_role", [], src("DEF", "3525.0210, subp. 10"), {**MNJ, **REG}),
    ("func_skills", "Functional skills", "functional_skill", [("functional skills evaluation", S, None)], src("DEF", "3525.0210, subps. 23-24"), REG),
    ("voc_eval", "Vocational evaluation", "transition", [], src("DEF", "3525.0210, subp. 48"), REG),
    ("tech_adequate", "Technically adequate instrument", "evaluation_eligibility", [], src("DEF", "3525.0210, subp. 45"), {**MNJ, **REG}),
    ("sig_change", "Significant change in program or placement", "iep_component", [], src("DEF", "3525.0210, subp. 41"), {**MNJ, **REG}),
    ("resident_dist", "Resident district", "legal_procedural", [("providing district", S, MN)], src("DEF", "3525.0210, subps. 35, 39"), {**REG}),
    ("indirect_svc", "Indirect services", "related_service", [], src("DEF", "3525.0210, subp. 27"), REG),
    ("team_override", "Team override", "evaluation_eligibility", [("team override on eligibility decisions", S, MN)], src("ELIG", "3525.1354"),
     {**MNJ, **REG, "note": "Lets the team find a student eligible when the data do not meet the criteria, with a written justification."}),
    ("mca", "Minnesota Comprehensive Assessments", "iep_component", [("MCA", A, MN), ("MCAs", P, MN)], src("POL"), MNJ),
    ("mtas", "Minnesota Test of Academic Skills", "iep_component", [("MTAS", A, MN), ("Alt MCA", S, MN), ("Alternate Minnesota Comprehensive Assessment", S, MN)], src("POL"),
     {**MNJ, "broader": "alt_assess", "note": "Minnesota's alternate assessment; newer documents call it the Alt MCA."}),
]

JURISDICTION = "US-MN"
LAYER_NAME = "Minnesota"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.12.0"
