"""
Pennsylvania layer for SPEDLex.

Sources reviewed 2026-10-03:
  PG     PDE Bureau of Special Education, Pennsylvania Parent Guide to Special
         Education for School-Age Children (July 2008), district copy. Old,
         but the only statewide parent guide found.
  R105   22 Pa. Code §14.105, personnel (types and levels of support)
  DR     PDE, Special Education Dispute Resolution page
  NOREP  Notice of Recommended Educational Placement / Prior Written Notice
         form (rev. Oct. 2014), state form, intermediate unit copy
  ASM    PDE, Statewide Assessment for Students with Disabilities page

Pennsylvania's full Procedural Safeguards Notice was not found: school
sites post the state cover letter, which has no terms of art. PG, DR, NOREP
and ASM references are 'candidate'; 22 Pa. Code records are
'machine_validated'. The Reevaluation Report (RR), Chapter 16 gifted IEP
(GIEP), the Annotated IEP, and the PaTTAN network were not attested here.
"""

PG_URL = "https://www.cityhigh.org/Files/Content/Parental%2DResources/PA-Parent-Guide-To-SPED-for-School-Age.pdf"
R105_URL = "https://law.cornell.edu/regulations/pennsylvania/22-Pa-Code-SS-14-105"
DR_URL = "https://www.pa.gov/agencies/education/programs-and-services/instruction/elementary-and-secondary-education/special-education/state-complaints-and-dispute-resolution.html"
NOREP_URL = "https://www.iu9.org/accnt_742651/site_742652/Documents/NOREP-PWN.pdf"
ASM_URL = "https://www.pa.gov/agencies/education/programs-and-services/instruction/elementary-and-secondary-education/special-education/assessment.html"


def src(doc, loc=""):
    stype, title, url = {
        "PG": ("state_guidance", "PDE Pennsylvania Parent Guide to Special Education (July 2008)", PG_URL),
        "R105": ("state_regulation", "22 Pa. Code §14.105", R105_URL),
        "DR": ("state_guidance", "PDE Special Education Dispute Resolution page", DR_URL),
        "NOREP": ("state_guidance", "PDE NOREP/PWN form (rev. Oct. 2014)", NOREP_URL),
        "ASM": ("state_guidance", "PDE Statewide Assessment for Students with Disabilities page", ASM_URL),
    }[doc]
    if doc == "R105":
        return {"source_type": stype, "citation": f"{title}{loc}", "url": url}
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
PA = ["US-PA"]
PAJ = {"jurisdiction": "US-PA"}
REG = {"status": "machine_validated"}

LEVELS = ["itinerant", "supplemental", "full-time"]

STRINGS = [
    ("pwn", [("Notice of Recommended Educational Placement", S, PA), ("NOREP", A, PA), ("NOREP/PWN", V, PA)], src("NOREP")),
    ("consent", [("consent to evaluate", S, None)], src("PG", "p. 3")),
    ("mdt", [("evaluation team", S, None)], src("PG", "pp. 1, 29")),
    ("eval_report", [("ER", A, PA)], src("PG", "pp. 4, 29")),
    ("dp_hearing", [], src("PG", "pp. 19-21")),
    ("dp_complaint", [], src("PG", "p. 20")),
    ("resolution", [("resolution meeting facilitation", REL, PA)], src("DR")),
    ("iep_facil", [], src("DR")),
    ("adr", [], src("DR")),
    ("mediation", [], src("PG", "p. 19")),
    ("stay_put", [("stay put rule", S, None)], src("PG", "p. 21")),
    ("mdr", [], src("PG", "p. 16")),
    ("iaes", [], src("PG", "p. 16")),
    ("fba", [], src("PG", "p. 16")),
    ("bip", [("behavior management plan", S, PA)], src("PG", "p. 9")),
    ("coteach", [], src("PG", "p. 10")),
    ("id", [("mental retardation", L, PA)], src("PG", "pp. 1, 5, 29")),
    ("ed", [], src("PG", "p. 1")),
    ("sld", [], src("PG", "pp. 1, 4, 29")),
    ("esy", [], src("NOREP", "sec. 1")),
    ("iee", [], src("NOREP", "sec. 1")),
    ("s504", [("Chapter 15", AB, PA)], src("PG", "p. 1")),
    ("related", [], src("PG", "pp. 6, 30")),
    ("sdi", [], src("PG", "pp. 2, 30")),
    ("transition", [], src("PG", "pp. 9-10")),
    ("lre", [], src("PG", "pp. 6, 10")),
    ("braille", [], src("PG", "pp. 9, 11")),
    ("alt_assess", [], src("ASM")),
    ("sig_cog", [], src("ASM")),
]

# Types of support (22 Pa. Code §14.105(c)(2)); each also carries the 3 level
# combinations the NOREP uses, e.g. "itinerant learning support".
TYPES = [
    ("ls", "Learning support", []),
    ("lss", "Life skills support", []),
    ("es", "Emotional support", []),
    ("dhhs", "Deaf and hearing impaired support", [("deaf and hard of hearing support", S, PA)]),
    ("bvis", "Blind and visually impaired support", []),
    ("sls", "Speech and language support", []),
    ("phs", "Physical support", []),
    ("aus", "Autistic support", [("autism support", V, PA)]),
    ("mds", "Multiple disabilities support", []),
]

CONCEPTS = [
    # --- Agencies, dispute resolution ---
    ("pde", "Pennsylvania Department of Education", "legal_procedural", [("PDE", A, PA)], src("PG", "cover"), {**PAJ, "broader": "sea"}),
    ("bse", "Bureau of Special Education", "legal_procedural", [("BSE", A, PA)], src("DR"), {**PAJ, "broader": "pde"}),
    ("odr_pa", "Office for Dispute Resolution", "legal_procedural", [("ODR", A, PA)], src("DR"),
     {**PAJ, "broader": "dp_hearing", "note": "Runs Pennsylvania's mediation, IEP facilitation, and due process hearings."}),
    ("consultline", "Special Education ConsultLine", "legal_procedural", [("ConsultLine", AB, PA)], src("DR"), {**PAJ, "broader": "bse"}),
    ("dcmp", "Division of Compliance Monitoring and Planning", "legal_procedural", [], src("DR"), {**PAJ, "broader": "bse"}),
    ("iu", "Intermediate unit", "legal_procedural", [("intermediate units", P, PA), ("IU", A, PA)], src("PG", "p. 28"),
     {**PAJ, "broader": "esa", "note": "Pennsylvania's regional educational service agencies; compare New York's BOCES."}),
    ("ch14", "22 Pa. Code Chapter 14", "legal_procedural", [("Chapter 14", AB, PA)], src("PG", "p. 29"),
     {**PAJ, "note": "Pennsylvania's special education regulations. Chapter 15 covers Section 504 and Chapter 16 covers gifted education."}),
    ("peal", "Parent Education and Advocacy Leadership Center", "legal_procedural", [("PEAL Center", AB, PA), ("PEAL", A, PA)], src("PG", "p. 28"), {**PAJ, "broader": "pti"}),
    ("pen", "Parent Education Network", "legal_procedural", [("PEN", A, PA)], src("PG", "p. 28"),
     {**PAJ, "broader": "pti", "flags": ["common_english_word"], "note": "'PEN' is protected only as an all-caps match."}),

    # --- Evaluation forms ---
    ("pte", "Permission to Evaluate", "evaluation_eligibility", [("Permission to Evaluate Consent Form", REL, PA), ("Permission to Evaluate Evaluation Request Form", REL, PA),
                                                                ("Permission to Reevaluate", S, PA), ("PTE", A, PA)], src("PG", "pp. 3, 5"),
     {**PAJ, "broader": "consent", "note": "'PTE' is practitioner usage, not from the guide."}),

    # --- Support types and levels ---
    ("type_support", "Type of support", "placement_setting", [("types of support", P, PA)], src("R105", "(c)(2)"), {**PAJ, **REG, "broader": "continuum"}),
    ("level_support", "Level of support", "placement_setting", [("levels of support", P, PA), ("itinerant support", REL, PA), ("supplemental support", REL, PA),
                                                               ("full-time support", REL, PA)], src("R105", "(c)(1)"),
     {**PAJ, **REG, "broader": "continuum",
      "note": "Itinerant is 20% of the day or less, supplemental more than 20% but less than 80%, full-time 80% or more. Compare Virginia's Level I and Level II."}),
    ("mech_restraint", "Mechanical restraints", "discipline", [("mechanical restraint", P, None)], src("PG", "p. 15"), {}),
    ("exit_sped", "Exiting special education", "transition", [], src("NOREP", "sec. 1"), {}),

    # --- Assessment and graduation ---
    ("pssa", "Pennsylvania System of School Assessment", "iep_component", [("PSSA", A, PA)], src("ASM"), PAJ),
    ("keystone", "Keystone Exams", "iep_component", [("Keystone Exam", P, PA)], src("ASM"), {**PAJ, "broader": "eoc"}),
    ("pasa", "Pennsylvania Alternate System of Assessment", "iep_component", [("PASA", A, PA), ("PASA DLM", S, PA)], src("ASM"), {**PAJ, "broader": "alt_assess"}),
    ("dlm", "Dynamic Learning Maps", "iep_component", [("DLM", A, None)], src("ASM"),
     {"broader": "alt_assess", "note": "Multistate alternate assessment consortium; Pennsylvania's PASA now uses it."}),
    ("act158", "Act 158 pathways to graduation", "transition", [("Act 158", AB, PA), ("pathways to graduation", S, PA)], src("ASM"), PAJ),
]

# Generate one concept per type of support, with its level combinations.
for key, pref, extra in TYPES:
    strings = list(extra) + [(f"{lvl} {pref.lower()}", REL, PA) for lvl in LEVELS]
    CONCEPTS.append((key, pref, "placement_setting", strings, src("R105", "(c)(2)"), {**PAJ, **REG, "broader": "type_support"}))

JURISDICTION = "US-PA"
LAYER_NAME = "Pennsylvania"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.9.0"
