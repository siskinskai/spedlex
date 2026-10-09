"""
Michigan layer for SPEDLex.

Sources reviewed 2026-10-06 (all published by the Michigan Department of
Education, MDE):
  RULE  Michigan Administrative Rules for Special Education (MARSE),
        R 340.1701 to R 340.1873, as promulgated June 27, 2024 (MDE's
        "Download a PDF of All Rules" file, 62 pp.)
  PSN   MDE Office of Special Education, Procedural Safeguards Notice
        (last updated 10/16/18, 53 pp.)
  PROG  MDE guidance, Individualized Education Program (IEP) Development:
        Special Education Programs and Services (May 2022, 7 pp.)
  ALT   MDE MI-Access web page (Michigan's alternate assessment)

The three PDFs were read as text extracted from the official files; PSN and
PROG page numbers are the printed page numbers. ALT is a web page, read as
page text. MARSE parts 1-3, 8, 9 and 10 were read in full; parts 4-7
(personnel qualifications, financing and intermediate school district
plans) were read by section heading plus R 340.1793, R 340.1799e-g,
R 340.1832 and R 340.1838. The PSN follows the federal model notice; it was
read for Michigan-specific content (pages 1-11 in full, then by search).
MDE publishes no single parent guide; PROG is its IEP-development
guidance. RULE records are 'machine_validated'; the others are 'candidate'.

Left out on purpose: the PSN's list of State Board members (names), and
local districts named as examples.
"""

RULE_URL = "https://www.michigan.gov/mde/-/media/Project/Websites/mde/specialeducation/MI-rules/MARSE-R3401701toR3401873.pdf"
PSN_URL = "https://www.michigan.gov/mde/-/media/Project/Websites/mde/specialeducation/proc-safe/Procedural_Safeguards_Notice.pdf"
PROG_URL = "https://www.michigan.gov/mde/-/media/Project/Websites/mde/specialeducation/iep/IEP_Development_SpecialEducationProgramsServices.pdf"
ALT_URL = "https://www.michigan.gov/mde/services/student-assessment/mi-access"


def src(doc, loc=""):
    """RULE loc is a rule number, e.g. '340.1705'; other loc is a page, e.g. 'p. 11'."""
    tail = f", {loc}" if loc else ""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"Mich Admin Code, R {loc}", "doc_id": "mi-marse-2024", "url": RULE_URL}
    if doc == "PROG":
        return {"source_type": "state_guidance",
                "citation": f"MDE, IEP Development: Special Education Programs and Services (May 2022){tail}",
                "doc_id": "mi-iepdev-2022", "url": PROG_URL}
    if doc == "ALT":
        return {"source_type": "state_guidance", "citation": "MDE MI-Access page", "url": ALT_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"MDE Procedural Safeguards Notice (updated 10/16/18){tail}", "doc_id": "mi-psn-2018", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
MI = ["US-MI"]
MIJ = {"jurisdiction": "US-MI"}
R = lambda rule: src("RULE", rule)
N = lambda page: src("PSN", f"p. {page}")
G = lambda page: src("PROG", f"p. {page}")

STRINGS = [
    # MARSE eligibility categories, R 340.1705-340.1717
    ("id", [("cognitive impairment", S, MI)], R("340.1705")),
    ("ed", [("emotional impairment", S, MI)], R("340.1706")),
    ("hi", [], R("340.1707")), ("deafness", [], R("340.1707")),
    ("vi", [], R("340.1708")),
    ("fva", [], R("340.1708")), ("lma", [], R("340.1708")),
    ("tvi", [("teacher of students with visual impairment", V, None)], R("340.1708")),
    ("oi", [("physical impairment", S, MI)], R("340.1709")),
    ("ohi", [], R("340.1709a")),
    ("adhd", [], R("340.1709a")), ("epilepsy", [], R("340.1709a")), ("sickle", [], R("340.1709a")),
    ("sli", [("speech and language impairment", S, MI)], R("340.1710")),
    ("lang_dis", [], R("340.1710")), ("artic", [], R("340.1710")),
    ("fluency_dis", [("fluency impairment", S, None)], R("340.1710")),
    ("voice", [("voice impairment", S, None)], R("340.1710")),
    ("dd", [("early childhood developmental delay", S, MI)], R("340.1711")),
    ("sld", [], R("340.1713")),
    ("dyslexia", [], R("340.1713")), ("perceptual", [], R("340.1713")), ("mbd", [], R("340.1713")),
    ("aphasia", [], R("340.1713")),
    ("discrepancy", [], R("340.1713")), ("rti", [], R("340.1713")), ("gen_teacher", [], R("340.1713")),
    ("md", [("severe multiple impairment", S, MI)], R("340.1714")),
    ("autism", [], R("340.1715")),
    ("tbi", [], R("340.1716")),
    ("deafblind", [], R("340.1717")),
    ("tdhh", [("teacher of students with hearing impairment", S, MI)], R("340.1717")),
    ("adaptive", [], R("340.1701a")),
    ("mdt", [("multidisciplinary evaluation team", S, MI)], R("340.1701b")),
    ("cwd", [], R("340.1702")),
    # evaluation, IEP, timelines
    ("evaluation", [], R("340.1721a")),
    ("plaafp", [], R("340.1721a")),
    ("annual_goals", [], R("340.1721e")), ("sto", [], R("340.1721e")),
    ("esy", [], R("340.1721e")), ("regression", [], R("340.1721e")),
    ("resident_dist", [("district of residence", S, None)], R("340.1721e")),
    ("iee", [], R("340.1723c")),
    # dispute resolution
    ("mediation", [], R("340.1724d")),
    ("dp_complaint", [], R("340.1724f")),
    ("iaes", [], R("340.1724f")), ("mdr", [], R("340.1724f")),
    ("dp_hearing", [], R("340.1725e")), ("prehearing", [], R("340.1725e")), ("adr", [], R("340.1725e")),
    ("surrogate", [], R("340.1725f")),
    ("state_complaint", [], R("340.1851")),
    # programs and services
    ("transition", [], R("340.1733")),
    ("home_instr", [("homebound and hospitalized services", S, MI)], R("340.1746")),
    ("hospital_instr", [], R("340.1746")),
    ("resource_room", [("resource program", S, MI)], R("340.1749a")),
    ("sped_admin", [], R("340.1750")),
    ("ecse", [("early childhood special education services", S, None)], R("340.1755")),
    ("para", [("paraprofessional personnel", S, None)], R("340.1793")),
    ("ifsp", [], R("340.1862")),
    # notice
    ("safeguards_notice", [], N(1)),
    ("pwn", [], N(11)),
    ("age_majority", [], N(52)),
    # IEP development guidance
    ("continuum", [], G(4)), ("itinerant", [], G(4)),
    ("sdi", [], G(3)),
    ("transport", [("special transportation", S, MI)], G(5)),
    ("alt_assess", [], src("ALT")), ("sig_cog", [], src("ALT")),
]

CONCEPTS = [
    ("mi_mde", "Michigan Department of Education", "legal_procedural", [("MDE", A, MI)], N(3),
     {**MIJ, "broader": "sea"}),
    ("mi_isd", "Intermediate school district", "legal_procedural", [("ISD", A, MI)], N(28),
     {**MIJ, "broader": "esa", "note": "Regional agency that plans special education for its constituent districts."}),
    ("mi_isd_plan", "Intermediate school district plan", "legal_procedural", [], R("340.1832"),
     {**MIJ, "broader": "mi_isd"}),
    ("mi_psa", "Public school academy", "legal_procedural", [], R("340.1733"),
     {**MIJ, "broader": "lea", "note": "Treated as a school district for special education; the notice counts it as one."}),
    ("mi_pac", "Parent advisory committee", "legal_procedural", [], R("340.1838"),
     {**MIJ, "broader": "mi_isd", "note": "Parents of students with disabilities appointed by each intermediate school district board."}),
    ("mi_moahr", "Michigan Office of Administrative Hearings and Rules", "legal_procedural", [], R("340.1724f"),
     {**MIJ, "broader": "dp_hearing", "note": "Appoints the administrative law judge for a due process hearing."}),
    ("mi_offer_fape", "Notice of an offer of a free appropriate public education", "legal_procedural", [], R("340.1721b"),
     {**MIJ, "broader": "pwn", "note": "Sent within 7 school days of the IEP meeting, with where and when services begin."}),
    ("mi_operating_district", "Operating district", "legal_procedural", [], R("340.1721e"),
     {**MIJ, "note": "The district that runs a program, as distinct from the district of residence."}),
    ("mi_instr_services", "Instructional services", "iep_component", [], R("340.1701b"),
     {**MIJ, "broader": "special_ed", "note": "Specially designed services by teaching personnel, as opposed to related services."}),
    ("mi_juvenile", "Youth placed in a juvenile detention facility", "placement_setting", [], R("340.1701c"), MIJ),
    ("mi_tc", "Teacher consultant", "personnel_role", [], R("340.1749"),
     {**MIJ, "broader": "sped_teacher", "note": "Supports students and staff; may not grade or teach a course."}),
    ("mi_departmentalize", "Departmentalization of special education programs", "placement_setting",
     [("departmentalize", V, MI)], R("340.1749c"), MIJ),
    ("mi_sci_program", "Severe cognitive impairment program", "placement_setting", [], R("340.1738"),
     {**MIJ, "broader": "special_class"}),
    ("mi_sxi_program", "Severe multiple impairments program", "placement_setting", [], R("340.1748"),
     {**MIJ, "broader": "special_class"}),
    ("mi_slp_provider", "Authorized provider of speech and language services", "personnel_role", [], R("340.1745"),
     {**MIJ, "broader": "slp"}),
    ("mi_msd", "Michigan School for the Deaf", "placement_setting", [], R("340.1721e"),
     {**MIJ, "broader": "special_school"}),
    ("school_social_worker", "School social worker", "personnel_role", [], R("340.1799f"), {"broader": "social_work"}),
    ("transition_coord", "Transition coordinator", "personnel_role", [], R("340.1799g"), {"broader": "transition"}),
    ("worksite_learning", "Worksite-based learning", "transition", [], R("340.1733"), {"broader": "transition"}),
    ("mi_access", "MI-Access", "iep_component", [], src("ALT"),
     {**MIJ, "broader": "alt_assess", "note": "Michigan's alternate assessment, with Functional Independence, Supported Independence and Participation levels."}),
    ("mi_fi", "Functional Independence", "iep_component", [], src("ALT"),
     {**MIJ, "broader": "mi_access", "flags": ["common_english_word"]}),
    ("mi_si", "Supported Independence", "iep_component", [], src("ALT"),
     {**MIJ, "broader": "mi_access", "flags": ["common_english_word"]}),
    ("mi_ace", "Alternate content expectations", "academic_skill", [], src("ALT"),
     {**MIJ, "note": "Michigan's alternate standards behind MI-Access."}),
    ("mi_mstep", "M-STEP", "iep_component", [], src("ALT"),
     {**MIJ, "note": "Michigan's general statewide assessment; the source does not expand the name."}),
]

JURISDICTION = "US-MI"
LAYER_NAME = "Michigan"
RETRIEVED = "2026-10-06"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.25.0"
