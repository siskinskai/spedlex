"""
Hawaii layer for SPEDLex.

Sources reviewed 2026-10-07:
  RULE   Hawaii Administrative Rules, Title 8, Chapter 60, Provision of a
         Free Appropriate Public Education for a Student with a Disability
         (Board of Education PDF file, 108 pp.; sections show "Eff 11/23/09"),
         cited by section, e.g. "§ 8-60-39(e)"
  PSN    Hawaii State Department of Education, Procedural Safeguards Notice for
         Parents and Students (May 2022, PDF file, 44 pp.), cited by PDF page
         (the printed page numbers are four lower)
  GUIDE  Hawaii State Department of Education brochure "Special Education: Is
         it for your child?" (RS 26-0535, November 2025, PDF file, 2 pp.),
         cited by PDF page

All three were read as text extracted from the PDF files on the Board of
Education and Department websites; ligatures were normalized. RULE
§§ 8-60-2 (definitions) and 8-60-39 (eligibility criteria) were read in full;
the other sections were read by heading and searched. PSN pp. 1-2, 19-21 and
44 were read in full and the rest searched; it follows the federal model
notice. GUIDE was read in full. GUIDE p. 1 also carries text from the
brochure's June 2021 edition behind the November 2025 text; only terms
also present in the 2025 text are cited ("conciliation" appears only in the
2021 layer and was dropped). RULE records are
'machine_validated'; the others are 'candidate'.

Left out on purpose: the complex area office names and phone numbers in
GUIDE and PSN (place names with contact details), the Legal Aid Society,
Hawaii State Bar Association and Mediation Center of the Pacific (general
legal and mediation providers named only as contacts), and all addresses.
"""

RULE_URL = ("https://boe.hawaii.gov/wp-content/uploads/2024/07/"
            "60-Provision-of-a-Free-Appropriate-Public-Education-for-a-Student-with-a-Disability.pdf")
PSN_URL = "https://hawaiipublicschools.org/wp-content/uploads/ProceduralSafeguards.pdf"
GUIDE_URL = "https://hawaiipublicschools.org/wp-content/uploads/Special-Education-Is-It-For-Your-Child-RS-26-0535.pdf"


def src(doc, loc=""):
    """RULE loc is a section, e.g. '8-60-39(e)'; PSN and GUIDE loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"Haw. Code R. § {loc}", "doc_id": "hi-har860-2009", "url": RULE_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"HIDOE brochure Special Education: Is it for your child? (Nov. 2025), PDF p. {loc}",
                "doc_id": "hi-brochure-2025", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"HIDOE Procedural Safeguards Notice (May 2022), PDF p. {loc}", "doc_id": "hi-psn-2022", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
HI = ["US-HI"]
HIJ = {"jurisdiction": "US-HI"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # Haw. Code R. § 8-60-39: eligibility categories
    ("autism", [], R("8-60-39(a)")),
    ("deafness", [], R("8-60-39(b)")),
    ("deafblind", [], R("8-60-39(c)")),
    ("dd", [], R("8-60-39(d)")),
    ("ed", [("emotional disability", S, HI)], R("8-60-39(e)")),
    ("hi", [], R("8-60-39(f)")),
    ("id", [], R("8-60-39(g)")),
    ("md", [], R("8-60-39(h)")),
    ("oi", [("orthopedic disability", S, HI)], R("8-60-39(i)")),
    ("ohi", [("other health disability", S, HI)], R("8-60-39(j)")),
    ("sld", [], R("8-60-39(k)")),
    ("sli", [("speech or language disability", S, HI)], R("8-60-39(l)")),
    ("tbi", [], R("8-60-39(m)")),
    ("vi", [("visual disability including blindness", S, HI)], R("8-60-39(n)")),
    # § 8-60-2: definitions
    ("charter_school", [], R("8-60-2")),
    ("cwd", [], R("8-60-2")),
    ("resolution", [], R("8-60-2")),
    ("sto", [], R("8-60-2")),
    ("iaes", [], R("8-60-2")),
    ("pwn", [], R("8-60-2")),
    ("surrogate", [], R("8-60-73")),
    # Procedural Safeguards Notice
    ("safeguards_notice", [], PS(1)),
]

CONCEPTS = [
    # Department of Education
    ("hi_doe", "Hawai'i State Department of Education", "legal_procedural", [], G(1),
     {**HIJ, "broader": "sea", "flags": ["place_name"]}),
    ("hi_ossss", "Office of Student Support Services", "legal_procedural", [], G(1), {**HIJ, "broader": "hi_doe"}),
    ("hi_esb", "Exceptional Support Branch", "legal_procedural", [], G(1), {**HIJ, "broader": "hi_ossss"}),
    ("hi_mcb", "Monitoring and Compliance Branch", "legal_procedural", [], PS(19), {**HIJ, "broader": "hi_doe"}),
    ("hi_cmp", "Complaints Management Program", "legal_procedural", [], PS(19),
     {**HIJ, "broader": "hi_mcb", "note": "The Department office that receives written state complaints."}),
    ("hi_cas", "Complex Area Superintendent", "personnel_role", [], PS(19),
     {**HIJ, "note": "Heads a complex area, the Department's regional unit; receives complaints and hearing requests."}),
    # family and advocacy organizations
    ("hi_ldah", "Leadership in Disabilities & Achievement of Hawaii", "legal_procedural", [], PS(44),
     {**HIJ, "broader": "pti"}),
    ("hi_drc", "Hawaii Disability Rights Center", "legal_procedural", [], PS(44), HIJ),
    ("hi_spin", "Special Parent Information Network", "legal_procedural", [], PS(44), HIJ),
    ("hi_ccc", "Community Children's Council Office", "legal_procedural", [], PS(44), HIJ),
    ("hi_hfaa", "Hawaii Families as Allies", "legal_procedural", [], PS(44), HIJ),
]

JURISDICTION = "US-HI"
LAYER_NAME = "Hawaii"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.31.0"
