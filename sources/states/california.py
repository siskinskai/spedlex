"""
California layer for SPEDLex.

Sources reviewed 2026-10-03:
  NPS    CDE Notice of Procedural Safeguards, revised June 2022, as posted by
         the Office of Administrative Hearings (CDE's own PDF link returned 404)
  CCR    5 CCR §3030, eligibility criteria (amended 2023)
  EC361  Cal. Educ. Code §56361, continuum of program options
  EC363  Cal. Educ. Code §56363, designated instruction and services
  CAA    CDE, Alternate Assessment IEP Team Guidance (CAASPP), reviewed July 2026
  ACC    CDE, Student Accessibility Resources (CAASPP), reviewed Dec. 2025
  DIP    CDE letter, Diploma Pathway for Students who Qualify for the CAA, Nov. 2024
  EQS    CDE, Equitable Services for Students with Disabilities page, reviewed July 2026

Not read: Cornell's listing of 5 CCR Article 5 (the DIS standards, §3051.x);
the fetch service rate-limited it. EC §56363 covers the same service list.

NPS, CAA, ACC, DIP and EQS references come from text extraction and are
'candidate'. CCR and Education Code records are 'machine_validated'.
'SDC' and 'special day class' are practitioner names for special classes and
did not appear in the sources read. Student study team, ITP, ERMHS and
Behavior Emergency Report are common in California IEPs but were not attested
by these sources, so they are left for the next pass.
"""

NPS_URL = "https://www.dgs.ca.gov/en/OAH/Case-Types/Special-Education/Resources/Page-Content/Special-Education-Resources-List-Folder/Notice-of-Procedural-Safeguards"
CCR_URL = "https://www.law.cornell.edu/regulations/california/5-CCR-3030"
EC_URL = "https://california.public.law/codes/ca_educ_code_section_{}"
CAA_URL = "https://www.cde.ca.gov/TA/tg/ca/caaiepteamrev.asp"
ACC_URL = "https://www.cde.ca.gov/TA/TG/ca/accesssupport.asp"
DIP_URL = "https://www.cde.ca.gov/sp/se/om082523.asp"
EQS_URL = "https://www.cde.ca.gov/Sp/se/qa/pssummary.asp"


def src(doc, loc=""):
    if doc in ("EC361", "EC363"):
        sec = "56361" if doc == "EC361" else "56363"
        return {"source_type": "state_regulation", "citation": f"Cal. Educ. Code §{sec}{loc}", "url": EC_URL.format(sec)}
    stype, title, url = {
        "NPS": ("procedural_safeguards_notice", "CDE Notice of Procedural Safeguards (rev. June 2022)", NPS_URL),
        "CCR": ("state_regulation", "5 CCR §3030", CCR_URL),
        "CAA": ("state_guidance", "CDE Alternate Assessment IEP Team Guidance", CAA_URL),
        "ACC": ("state_guidance", "CDE Student Accessibility Resources (CAASPP)", ACC_URL),
        "DIP": ("state_guidance", "CDE letter, Diploma Pathway for Students who Qualify for the CAA (Nov. 2024)", DIP_URL),
        "EQS": ("state_guidance", "CDE Equitable Services for Students with Disabilities page", EQS_URL),
    }[doc]
    if doc == "CCR":
        return {"source_type": stype, "citation": f"{title}{loc}", "url": url}
    return {"source_type": stype, "citation": f"{title}, {loc}" if loc else title, "url": url}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
CA = ["US-CA"]
CAJ = {"jurisdiction": "US-CA"}
REG = {"status": "machine_validated"}

STRINGS = [
    # Eligibility, 5 CCR §3030(b)
    ("autism", [], src("CCR", "(b)(1)")),
    ("deafblind", [], src("CCR", "(b)(2)")),
    ("deafness", [], src("CCR", "(b)(3)")),
    ("ed", [], src("CCR", "(b)(4)")),
    ("hi", [], src("CCR", "(b)(5)")),
    ("id", [], src("CCR", "(b)(6)")),
    ("md", [], src("CCR", "(b)(7)")),
    ("oi", [], src("CCR", "(b)(8)")),
    ("ohi", [], src("CCR", "(b)(9)")),
    ("sld", [], src("CCR", "(b)(10)")),
    ("sli", [("language or speech disorder", S, CA)], src("CCR", "(b)(11)")),
    ("tbi", [], src("CCR", "(b)(12)")),
    ("vi", [], src("CCR", "(b)(13)")),
    ("cwd", [("individuals with exceptional needs", S, CA), ("students with exceptional needs", S, CA)], src("EC363")),

    # Services and placements, Educ. Code §§56361, 56363
    ("continuum", [("continuum of program options", S, CA)], src("EC361")),
    ("regular_class", [("regular education programs", S, None)], src("EC361", "(a)")),
    ("special_class", [("special day class", S, CA), ("SDC", A, CA)], src("EC361", "(d)")),
    ("itinerant", [], src("EC361", "(h)")),
    ("home_instr", [("instruction in the home or hospital", S, CA), ("home or hospital instruction", S, CA)], src("EC363", "(b)(4)")),
    ("related", [("designated instruction and services", S, CA), ("DIS", A, CA)], src("EC363")),
    ("slp", [("language and speech development and remediation", S, CA)], src("EC363", "(b)(1)")),
    ("audiology", [], src("EC363", "(b)(2)")),
    ("om", [], src("EC363", "(b)(3)")),
    ("pe", [], src("EC363", "(b)(5)")),
    ("pt", [], src("EC363", "(b)(6)")),
    ("ot", [], src("EC363", "(b)(6)")),
    ("counseling", [("counseling and guidance services", S, CA)], src("EC363", "(b)(9)")),
    ("psych", [], src("EC363", "(b)(10)")),
    ("parent_training", [], src("EC363", "(b)(11)")),
    ("nursing", [("health and nursing services", S, CA)], src("EC363", "(b)(12)")),
    ("social_work", [("social worker services", S, CA)], src("EC363", "(b)(13)")),
    ("voc_ed", [("specially designed vocational education and career development", S, CA)], src("EC363", "(b)(14)")),
    ("recreation", [("recreation services", S, None)], src("EC363", "(b)(15)")),
    ("interpreting", [], src("EC363", "(b)(17)")),

    # Procedural safeguards notice
    ("iep_team", [], src("NPS", "sec. 3")),
    ("evaluation", [("initial assessment", S, CA)], src("NPS", "sec. 6")),
    ("iee", [("independent educational assessment", S, CA)], src("NPS", "sec. 6")),
    ("pwn", [], src("NPS", "sec. 6")),
    ("surrogate", [], src("NPS", "sec. 6")),
    ("ward", [("adjudicated dependent or ward of the court", S, CA)], src("NPS", "sec. 6")),
    ("uhy", [], src("NPS", "sec. 6")),
    ("mediation", [("prehearing mediation conference", S, CA), ("pre-hearing mediation conference", V, CA)], src("NPS", "sec. 7")),
    ("resolution", [], src("NPS", "sec. 7")),
    ("stay_put", [("current educational placement", S, None)], src("NPS", "sec. 7")),
    ("state_complaint", [("state compliance complaint", S, CA)], src("NPS", "sec. 9")),
    ("iaes", [("interim alternative education setting", V, None), ("alternative interim educational setting", V, CA)], src("NPS", "sec. 8")),
    ("mdr", [("manifestation determination meeting", S, None)], src("NPS", "sec. 8")),
    ("exp_hearing", [], src("NPS", "sec. 8")),
    ("pti", [("Parent Training and Information Center", S, None), ("PTIC", A, None)], src("NPS", "sec. 4")),
    ("audio_rec", [("electronically audiotape", S, CA)], src("NPS", "sec. 3")),

    # Assessment, diplomas, data
    ("alt_assess", [], src("CAA")),
    ("sig_cog", [], src("CAA")),
    ("des_sup", [], src("ACC")),
    ("test_accom", [], src("ACC")),
    ("s504", [], src("ACC")),
    ("alt_diploma", [("state-defined alternate diploma", S, None)], src("DIP")),
    ("cert_completion", [("certificate of completion", S, CA)], src("DIP")),
    ("state_panel", [("Advisory Commission on Special Education", S, CA), ("ACSE", A, CA)], src("EQS")),
    ("services_plan", [], src("EQS")),
    ("ifsp", [], src("EQS")),
]

CONCEPTS = [
    # --- Agencies and law ---
    ("cde", "California Department of Education", "legal_procedural", [("CDE", A, CA)], src("NPS", "sec. 4"), {**CAJ, "broader": "sea"}),
    ("cde_sed", "Special Education Division", "legal_procedural", [], src("NPS", "sec. 7"), {**CAJ, "broader": "cde"}),
    ("oah", "Office of Administrative Hearings", "legal_procedural", [("OAH", A, CA)], src("NPS", "sec. 7"),
     {"broader": "dp_hearing", "note": "California and Washington both route special education hearings to a state Office of Administrative Hearings instead of the education agency."}),
    ("ca_ec", "California Education Code", "legal_procedural", [("Education Code", AB, CA)], src("NPS", "sec. 12"),
     {**CAJ, "note": "The notice abbreviates it 'EC'; two capital letters are too ambiguous to safelist alone."}),
    ("ca_ccr", "California Code of Regulations, Title 5", "legal_procedural", [("5 CCR", A, CA), ("Title 5", AB, CA)], src("CCR"), {**CAJ, **REG}),
    ("selpa", "Special Education Local Plan Area", "legal_procedural", [("SELPA", A, CA), ("SELPAs", P, CA)], src("NPS", "sec. 4"),
     {**CAJ, "note": "Regional consortium of districts that plans and funds special education; California-specific."}),
    ("fec", "Family Empowerment Center", "legal_procedural", [("Family Empowerment Centers on Disability", S, CA), ("FEC", A, CA), ("FECs", P, CA)], src("NPS", "secs. 4, 11"),
     {**CAJ, "broader": "pti"}),
    ("adr", "Alternative dispute resolution", "legal_procedural", [("ADR", A, None)], src("NPS", "sec. 7"), {}),
    ("assess_plan", "Assessment plan", "evaluation_eligibility", [], src("NPS", "sec. 6"),
     {**CAJ, "note": "California calls evaluations 'assessments'; the assessment plan is the consent form for one."}),
    ("nondisc", "Nondiscriminatory assessment", "evaluation_eligibility", [("nondiscriminatory evaluation", S, None)], src("NPS", "sec. 6"), {}),
    ("state_sp_sch", "State special schools", "placement_setting", [("California School for the Deaf", S, CA), ("California School for the Blind", S, CA)], src("EC361", "(f)"),
     {**REG}),
    ("calpads", "California Longitudinal Pupil Achievement Data System", "legal_procedural", [("CALPADS", A, CA)], src("DIP"), CAJ),
    ("workability", "WorkAbility I", "transition", [("WorkAbility", AB, CA)], src("EQS"),
     {**CAJ, "note": "The page's abbreviation 'WAI' is too short and ambiguous to safelist."}),

    # --- Program options and services ---
    ("rsp", "Resource specialist program", "placement_setting", [("RSP", A, CA), ("resource specialist", S, CA)], src("EC361", "(b)"),
     {**CAJ, **REG, "broader": "continuum"}),
    ("nps", "Nonpublic, nonsectarian school", "placement_setting", [("nonpublic school", S, CA), ("nonpublic schools", P, CA), ("NPS", A, CA)], src("EC361", "(e)"),
     {**CAJ, **REG, "broader": "continuum", "note": "'NPS' also abbreviates 'Notice of Procedural Safeguards' in some documents."}),
    ("npa", "Nonpublic, nonsectarian agency", "related_service", [("nonpublic agency", S, CA), ("NPA", A, CA)], src("NPS", "sec. 3"), CAJ),
    ("telecom", "Instruction using telecommunication", "placement_setting", [], src("EC361", "(i)"), {**CAJ, **REG, "broader": "continuum"}),
    ("vision_svc", "Vision services", "related_service", [], src("EC363", "(b)(7)"), {**CAJ, **REG, "broader": "related"}),
    ("driver", "Specialized driver training instruction", "related_service", [], src("EC363", "(b)(8)"), {**CAJ, **REG, "broader": "related"}),
    ("low_inc", "Specialized services for low-incidence disabilities", "related_service", [("low-incidence disabilities", AB, CA), ("low incidence", AB, CA)], src("EC363", "(b)(16)"),
     {**CAJ, **REG, "broader": "related"}),

    # --- Speech/language subtypes, 5 CCR §3030(b)(11) ---
    ("artic", "Articulation disorder", "health_condition", [], src("CCR", "(b)(11)(A)"), {**REG, "broader": "sli"}),
    ("voice", "Abnormal voice", "health_condition", [("voice disorder", S, None)], src("CCR", "(b)(11)(B)"), {**REG, "broader": "sli"}),
    ("fluency_dis", "Fluency disorder", "health_condition", [("fluency disorders", P, None), ("stuttering", S, None)], src("CCR", "(b)(11)(C)"), {**REG, "broader": "sli"}),
    ("lang_dis", "Language disorder", "health_condition", [("receptive language", S, None), ("expressive language", S, None)], src("CCR", "(b)(11)(D)"),
     {**REG, "broader": "sli", "note": "'Receptive' and 'expressive language' are practitioner usage, not from the rule."}),

    # --- Assessment ---
    ("caaspp", "California Assessment of Student Performance and Progress", "iep_component", [("CAASPP", A, CA)], src("CAA"), CAJ),
    ("caa", "California Alternate Assessments", "iep_component", [("CAA", A, CA), ("California Alternate Assessment", P, CA)], src("CAA"), {**CAJ, "broader": "alt_assess"}),
    ("cast", "California Science Test", "iep_component", [("CAST", A, CA)], src("ACC"),
     {**CAJ, "broader": "caaspp", "note": "Acronym from CDE; the full name is from prior knowledge."}),
    ("csa_ca", "California Spanish Assessment", "iep_component", [("CSA", A, CA)], src("ACC"),
     {**CAJ, "broader": "caaspp", "note": "'CSA' also means Virginia's Children's Services Act; both are tagged by state."}),
    ("elpac", "English Language Proficiency Assessments for California", "iep_component", [("ELPAC", A, CA)], src("ACC"), CAJ),
    ("alt_elpac", "Alternate ELPAC", "iep_component", [("Alternate English Language Proficiency Assessments for California", S, CA)], src("CAA"), {**CAJ, "broader": "elpac"}),
    ("ccc", "Core Content Connectors", "academic_skill", [("Content Connectors", AB, None)], src("CAA"),
     {"note": "Reduced-complexity standards behind alternate assessments; compare Texas essence statements and Virginia's VESOL."}),
    ("eld_conn", "ELD Connectors", "academic_skill", [], src("CAA"), {**CAJ, "broader": "alt_elpac"}),
    ("univ_tools", "Universal tools", "accommodation_modification", [("universal tool", P, None)], src("ACC"), {"broader": "test_accom"}),
    ("unlisted", "Unlisted resources", "accommodation_modification", [("unlisted resource", P, CA)], src("ACC"),
     {**CAJ, "broader": "test_accom", "note": "Non-embedded supports that need CDE approval; compare Texas's supports requiring TEA approval."}),

    # --- Diploma pathway ---
    ("ca_alt_path", "Alternative pathway to a high school diploma", "transition",
     [("diploma pathway for students who qualify for the California Alternate Assessment", S, CA), ("state standards aligned coursework", S, CA)], src("DIP"),
     {**CAJ, "note": "Created by AB 181 (Educ. Code §§51225.31, 51225.32) for students eligible for the CAA."}),
]

JURISDICTION = "US-CA"
LAYER_NAME = "California"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.6.0"
