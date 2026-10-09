"""
Maryland layer for SPEDLex.

Sources reviewed 2026-10-07 (all published by the State of Maryland):
  RULE   COMAR 13A.05.01, Provision of a Free Appropriate Public Education,
         Regulations .01-.16, from the Library of Maryland Regulations
         (regs.maryland.gov; .03B last amended effective Aug. 17, 2026,
         53:16 Md. R. 687, per the chapter history on that site),
         cited by regulation and subsection, e.g. "COMAR 13A.05.01.03B(39)"
  PSN    Maryland State Department of Education (MSDE), Parental Rights:
         Maryland Procedural Safeguards Notice (Infants and Toddlers Early
         Intervention, Preschool Special Education and Special Education,
         July 2024, PDF file, 51 pp.), cited by PDF page
  IEPG   MSDE Parent Information Series, Special Education Services in
         Maryland: The Individualized Education Program (IEP) (2023, PDF file,
         20 pp.), cited by PDF page

RULE has no official PDF; the text of each regulation page was copied from
regs.maryland.gov through the browser into .sources-cache/md/MD-COMAR-13A.05.01.txt.
PSN and IEPG were downloaded from MSDE's website and read as text extracted
from the PDFs. RULE .02, .03 (definitions) and .09 were read in full; the
other regulations were read by heading and searched. IEPG was read in full.
PSN covers both Part C and Part B; pp. 1-2, 14-17 and 36 were read and the
rest searched. A second Parent Information Series guide (The Special
Education Process) could not be downloaded and was not used. RULE records
are 'machine_validated'; the others are 'candidate'.

Left out on purpose: the State Board members, superintendents and governor
named on PSN p. 2 and IEPG p. 19; the 24 local school systems and their
phone numbers on IEPG p. 18 (county names); the two-letter acronym "AA"
(alternate assessments); and all addresses.
"""

RULE_URL = "https://regs.maryland.gov/us/md/exec/comar/13A.05.01"
PSN_URL = "https://marylandpublicschools.org/programs/Documents/Special-Ed/MITP/about/Maryland-Procedural-Safeguards-Notice-A.pdf"
IEPG_URL = "https://marylandpublicschools.org/programs/documents/special-ed/fsdr/parent-information-series/iep-guide-a.pdf"


def src(doc, loc=""):
    """RULE loc is a regulation and subsection, e.g. '.03B(39)'; PSN and IEPG loc is a PDF page number."""
    if doc == "RULE":
        reg = loc[:3]
        return {"source_type": "state_regulation", "citation": f"COMAR 13A.05.01{loc}", "doc_id": "md-comar13a-2026", "url": f"{RULE_URL}{reg}"}
    if doc == "IEPG":
        return {"source_type": "state_guidance",
                "citation": f"MSDE Parent Information Series: The Individualized Education Program (2023), PDF p. {loc}",
                "doc_id": "md-iepguide-2023", "url": IEPG_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"MSDE Parental Rights: Maryland Procedural Safeguards Notice (July 2024), PDF p. {loc}", "doc_id": "md-psn-2024", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
MD = ["US-MD"]
MDJ = {"jurisdiction": "US-MD"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("IEPG", page)

STRINGS = [
    # COMAR 13A.05.01.03B: definitions and disability categories
    ("alt_assess", [("AAAS", A, MD)], R(".03B(2-1)")),
    ("alt_assess", [], R(".03B(2-2)")),
    ("at_device", [], R(".03B(4)")), ("at_service", [], R(".03B(5)")),
    ("audiology", [], R(".03B(7)")),
    ("autism", [], R(".03B(8)")),
    ("voc_ed", [("career and technology education", S, MD)], R(".03B(10)")),
    ("charter_school", [], R(".03B(11)")),
    ("consent", [], R(".03B(12)")),
    ("consult", [("consultation", S, MD)], R(".03B(13)")),
    ("counseling", [], R(".03B(14)")),
    ("critical_skill", [("critical life skill", S, MD)], R(".03B(15)")),
    ("deafblind", [], R(".03B(17)")), ("deafness", [], R(".03B(18)")),
    ("ed", [("emotional disability", S, MD)], R(".03B(23)")),
    ("evaluation", [], R(".03B(25)")),
    ("esy", [], R(".03B(26)")), ("fape", [], R(".03B(27)")), ("gen_curr", [], R(".03B(28)")),
    ("hi", [], R(".03B(29)")), ("homeless", [], R(".03B(30)")),
    ("dp_hearing", [], R(".03B(31)")),
    ("iee", [], R(".03B(33)")), ("iep", [], R(".03B(34)")), ("iep_team", [], R(".03B(35)")),
    ("id", [], R(".03B(36)")),
    ("interpreting", [], R(".03B(37)")), ("cart", [], R(".03B(37)")),
    ("lep", [], R(".03B(38)")),
    ("lea", [("local school system", S, MD), ("LSS", A, MD)], R(".03B(39)")),
    ("md", [], R(".03B(44)")), ("native_language", [], R(".03B(45)")),
    ("nonacademic", [], R(".03B(46)")),
    ("ot", [], R(".03B(48)")), ("om", [], R(".03B(49)")), ("oi", [], R(".03B(50)")), ("ohi", [], R(".03B(51)")),
    ("adhd", [], R(".03B(51)")), ("epilepsy", [], R(".03B(51)")), ("sickle", [], R(".03B(51)")),
    ("tourette", [], R(".03B(51)")),
    ("parent_training", [], R(".03B(53)")), ("part_agency", [], R(".03B(54)")), ("pii", [], R(".03B(55)")),
    ("pe", [], R(".03B(56)")), ("pt", [], R(".03B(57)")), ("psych", [], R(".03B(58)")),
    ("public_agency", [], R(".03B(59)")), ("recreation", [], R(".03B(62)")), ("reeval", [], R(".03B(63)")),
    ("rehab", [], R(".03B(64)")), ("related", [], R(".03B(65)")), ("school_day", [], R(".03B(66)")),
    ("nursing", [], R(".03B(67)")), ("services_plan", [], R(".03B(69)")), ("social_work", [], R(".03B(70)")),
    ("special_ed", [], R(".03B(71)")), ("sdi", [], R(".03B(72)")),
    ("sld", [], R(".03B(73)")), ("perceptual", [], R(".03B(73)")), ("mbd", [], R(".03B(73)")),
    ("dyslexia", [], R(".03B(73)")), ("aphasia", [], R(".03B(73)")),
    ("sli", [], R(".03B(74)")), ("slp", [], R(".03B(75)")),
    ("dd", [("student with a developmental delay", S, MD)], R(".03B(77)")),
    ("cwd", [], R(".03B(78)")), ("saas", [], R(".03B(79)")), ("transition", [], R(".03B(80)")),
    ("transport", [], R(".03B(81)")), ("tbi", [], R(".03B(82)")), ("travel_training", [], R(".03B(83)")),
    ("vi", [], R(".03B(84)")), ("ward", [], R(".03B(85)")),
    # other regulations
    ("referral", [], R(".04A")),
    ("std_diploma", [], R(".06E(10)")),
    ("state_panel", [], R(".15C(23)")),
    ("ppps", [], R(".16")),
    ("early_id", [("early identification", S, None)], R(".03B(20)")),
    # Procedural Safeguards Notice
    ("safeguards_notice", [("Maryland Procedural Safeguards Notice", S, MD)], PS(1)),
    ("oah", [], PS(17)),
    # IEP guide
    ("cert_completion", [], G(7)),
    ("plaafp", [], G(8)),
    ("acc_feat", [], G(10)),
    ("esy", [], G(12)),
]

CONCEPTS = [
    # agencies and offices
    ("md_msde", "Maryland State Department of Education", "legal_procedural", [("MSDE", A, MD)], PS(36),
     {**MDJ, "broader": "sea"}),
    ("md_deises", "Division of Early Intervention and Special Education Services", "legal_procedural", [], PS(36),
     {**MDJ, "broader": "md_msde", "note": "MSDE's division for special education and the Maryland Infants and Toddlers Program."}),
    ("md_mitp", "Maryland Infants and Toddlers Program", "early_intervention", [], G(19),
     {**MDJ, "note": "Maryland's Part C early intervention program."}),
    ("md_extended_ifsp", "Extended IFSP", "early_intervention", [], PS(15),
     {**MDJ, "broader": "ifsp", "note": "Lets a family keep early intervention services, with an educational component, after age 3."}),
    ("md_fss_coord", "Local Family Support Services Coordinator", "personnel_role", [], G(16),
     {**MDJ, "note": "A local school system contact who helps families with the special education process."}),
    # public agencies named in COMAR 13A.05.01.02A
    ("md_seed", "SEED School", "placement_setting", [], R(".02A"),
     {**MDJ, "note": "A public boarding school that COMAR lists among the public agencies responsible for FAPE."}),
    ("md_msb", "Maryland School for the Blind", "placement_setting", [], R(".02A"), {**MDJ, "broader": "state_sp_sch"}),
    ("md_msd", "Maryland School for the Deaf", "placement_setting", [], R(".02A"), {**MDJ, "broader": "state_sp_sch"}),
    ("md_mdh", "Maryland Department of Health", "legal_procedural", [], R(".02A"), MDJ),
    ("md_djs", "Department of Juvenile Services", "legal_procedural", [], R(".02A"), MDJ),
    ("md_labor", "Maryland Department of Labor", "transition", [], R(".02A"), MDJ),
    # IEP and assessment
    ("md_mam", "Maryland Accommodations Manual", "accommodation_modification", [], R(".03B(1)"),
     {**MDJ, "note": "The state manual that governs accommodations and modifications for instruction and assessment."}),
    ("md_moiep", "Maryland Online IEP", "iep_component", [("MOIEP", A, MD)], G(6),
     {**MDJ, "broader": "iep", "note": "The statewide IEP form and system that public agencies must use or match."}),
    ("md_lcp", "Learning Continuity Plan", "iep_component", [], R(".03B(37-1)"),
     {**MDJ, "broader": "iep", "note": "The IEP sections that say how FAPE continues during emergency conditions."}),
    ("md_emergency", "Emergency conditions", "legal_procedural", [], R(".03B(22-1)"),
     {**MDJ, "note": "A period of 10 or more school days when a school cannot provide IEP services in person."}),
    ("md_hs_diploma", "Maryland High School Diploma", "transition", [], PS(14), {**MDJ, "broader": "std_diploma"}),
]

JURISDICTION = "US-MD"
LAYER_NAME = "Maryland"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.34.0"
