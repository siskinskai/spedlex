"""
Missouri layer for SPEDLex.

Sources reviewed 2026-10-03:
  CAT   MPACT (Missouri's parent training center), Missouri Disability
        Categories, Definitions, and Criteria (2023)
  PSN   MO DESE, Special Education Procedural Safeguards (undated, IDEA 1997
        era), district copy; only a table of contents-level list of rights
  MAPA  MO DESE, MAP-A page (2026-27 testing information)
  MSSD  MO DESE, Missouri Schools for the Severely Disabled parents page
  SSD   Special School District of St. Louis County, Young Child with a
        Developmental Delay page

Missouri's current procedural safeguards notice and Parent's Guide links
returned 404 errors. All records here are 'candidate'. The Administrative
Hearing Commission, child complaints, First Steps, and the Notice of Action
form were not attested in these sources.
"""

CAT_URL = "https://www.missouriparentsact.org/wp-content/uploads/MissouriDisabilityCategories-7.2023-1.pdf"
PSN_URL = "https://www.isdschools.org/wp-content/uploads/2015/08/Special-Education-Procedural-Safeguards.pdf"
MAPA_URL = "https://dese.mo.gov/quality-schools/assessment/map-a"
MSSD_URL = "https://oembed-dese.mo.gov/special-education/missouri-schools-severely-disabled/parents"
SSD_URL = "https://www.ssdmo.org/students-families/ssd-family-handbook/section-4-information-resources-by-educational-category/young-child-with-a-developmental-delay"


def src(doc, loc=""):
    stype, title, url = {
        "CAT": ("secondary_guidance", "MPACT, Missouri Disability Categories, Definitions, and Criteria (2023)", CAT_URL),
        "PSN": ("procedural_safeguards_notice", "MO DESE Special Education Procedural Safeguards (district copy, undated)", PSN_URL),
        "MAPA": ("state_guidance", "MO DESE MAP-A page", MAPA_URL),
        "MSSD": ("state_guidance", "MO DESE Missouri Schools for the Severely Disabled parents page", MSSD_URL),
        "SSD": ("secondary_guidance", "Special School District of St. Louis County, Young Child with a Developmental Delay", SSD_URL),
    }[doc]
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
MO = ["US-MO"]
MOJ = {"jurisdiction": "US-MO"}

STRINGS = [
    ("autism", [], src("CAT")),
    ("deafblind", [("deaf/blindness", V, MO)], src("CAT")),
    ("ed", [], src("CAT")),
    ("hi", [("hearing impairment and deafness", S, MO)], src("CAT")),
    ("id", [], src("CAT")),
    ("md", [], src("CAT")),
    ("oi", [], src("CAT")),
    ("ohi", [], src("CAT")),
    ("sld", [], src("CAT")),
    ("tbi", [], src("CAT")),
    ("vi", [("visual impairment/blindness", V, MO)], src("CAT")),
    ("lang_dis", [("language impairment", S, MO)], src("CAT")),
    ("artic", [("sound system disorder", S, MO), ("sound system impairment", V, MO)], src("CAT")),
    ("fluency_dis", [("speech/fluency", S, MO)], src("CAT")),
    ("voice", [("speech/voice", S, MO)], src("CAT")),
    ("dd", [("young child with a developmental delay", S, MO), ("YCDD", A, MO)], src("SSD")),
    ("ecse", [], src("SSD")),
    ("iee", [("independent education evaluation", V, None)], src("PSN")),
    ("stay_put", [("placement during pendency", S, None)], src("PSN")),
    ("ppps", [("PPPSS", A, MO)], src("MSSD")),
    ("alt_assess", [], src("MAPA")),
    ("sig_cog", [], src("MAPA")),
    ("dlm", [], src("MAPA")),
    ("eoc", [], src("MAPA")),
    ("mediation", [], src("PSN")),
    ("pwn", [], src("PSN")),
    ("state_complaint", [], src("PSN")),
    ("iaes", [], src("PSN")),
]

CONCEPTS = [
    ("dese_mo", "Missouri Department of Elementary and Secondary Education", "legal_procedural", [("DESE", A, MO), ("MO DESE", S, MO)], src("MAPA"),
     {**MOJ, "broader": "sea", "note": "'DESE' is also Massachusetts's education department; both are tagged by state."}),
    ("mo_ose", "Missouri Office of Special Education", "legal_procedural", [], src("MSSD"), {**MOJ, "broader": "dese_mo"}),
    ("mo_state_plan", "Missouri State Plan for Special Education", "legal_procedural", [("State Plan for Special Education", AB, MO)], src("MSSD"),
     {**MOJ, "note": "Missouri sets most special education rules through this plan, not a separate chapter of regulations."}),
    ("mpact", "Missouri Parents Act", "legal_procedural", [("MPACT", A, MO), ("Missouri Parent Act", V, MO)], src("CAT"), {**MOJ, "broader": "pti"}),
    ("mo_pa", "Missouri Protection and Advocacy Services", "legal_procedural", [], src("MSSD"), MOJ),
    ("mssd", "Missouri Schools for the Severely Disabled", "placement_setting", [("MSSD", A, MO)], src("MSSD"), {**MOJ, "broader": "state_sp_sch"}),
    ("mo_blind", "Missouri School for the Blind", "placement_setting", [], src("MSSD"), {**MOJ, "broader": "state_sp_sch"}),
    ("mo_deaf", "Missouri School for the Deaf", "placement_setting", [], src("MSSD"), {**MOJ, "broader": "state_sp_sch"}),
    ("ssd_stl", "Special School District of St. Louis County", "legal_procedural", [("Special School District", AB, MO)], src("SSD"),
     {**MOJ, "flags": ["place_name"], "note": "A county-wide district that serves special education students for 22 St. Louis County districts. Contains a place name and a first name, so only the full phrase is protected."}),
    ("prof_judgment", "Professional judgment", "evaluation_eligibility", [], src("SSD"),
     {"note": "Missouri allows eligibility by documented professional judgment when scores do not meet the criteria; compare Minnesota's team override."}),
    ("mo_map", "Missouri Assessment Program", "iep_component", [("MAP", A, MO), ("MAP Grade-Level", REL, MO)], src("MAPA"),
     {**MOJ, "flags": ["common_english_word"], "note": "'MAP' is protected only as an all-caps match."}),
    ("mapa", "Missouri Assessment Program-Alternate", "iep_component", [("MAP-A", A, MO)], src("MAPA"), {**MOJ, "broader": "dlm"}),
    ("ess_elements", "Essential Elements", "academic_skill", [], src("MAPA"),
     {"note": "Dynamic Learning Maps' reduced-complexity standards; used by every DLM state. Compare Florida's access points and Texas essence statements."}),
    ("mls", "Missouri Learning Standards", "academic_skill", [], src("MAPA"), MOJ),
]

JURISDICTION = "US-MO"
LAYER_NAME = "Missouri"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.13.0"
