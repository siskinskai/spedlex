"""
North Carolina layer for SPEDLex.

Sources reviewed 2026-10-07 (both published by the North Carolina
Department of Public Instruction, NCDPI):
  POL  Policies Governing Services for Children with Disabilities (State
       Board of Education policies NC 1500-1508, revised March 2021, PDF file,
       132 pp.), cited by policy section, e.g. "NC 1500-2.4"
  PSN  Notice of Procedural Safeguards: Parent Rights and Responsibilities in
       Special Education (PDF file, updated July 2026, 44 pp.), cited by PDF
       page (the printed page numbers are one lower)

Both were read as text extracted from the PDF files on NCDPI's site;
ligatures were normalized. POL sections NC 1500-2 (definitions), NC 1501-13,
NC 1504-1.12 to 1504-1.15 and NC 1508 (class size and service levels) were
read in full; the rest was read by section heading and searched. PSN pages
1-7 and 29 were read and the rest searched; it follows the federal model
notice closely. North Carolina publishes no separate statewide parent guide;
the PSN's title, "Parent Rights and Responsibilities in Special Education",
is the parent-facing document. A one-page "Quick Guide to Special Education
Dispute Resolution Processes" linked from NCDPI was also read but not cited:
it is a national CADRE document, not North Carolina's own. POL records are
'machine_validated'; PSN records are 'candidate'.

Left out on purpose: the State Board members and NCDPI staff named on POL
pp. 2-3 (personal names, listed with home towns), and "NCDPI", which POL
uses without spelling it out next to the full name.
"""

POL_URL = "https://www.dpi.nc.gov/policies-governing-students-children-disabilities/download?attachment"
PSN_URL = ("https://www.dpi.nc.gov/documents/publications/catalog/"
           "ec145-parent-rights-responsibilities-procedural-safeguards-english/open")


def src(doc, loc=""):
    """POL loc is a policy section, e.g. '1500-2.4(b)(5)'; PSN loc is a PDF page number."""
    if doc == "POL":
        return {"source_type": "state_regulation",
                "citation": f"NC Policies Governing Services for Children with Disabilities, NC {loc}", "doc_id": "nc-policies-2021", "url": POL_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"NCDPI Notice of Procedural Safeguards (July 2026), PDF p. {loc}", "doc_id": "nc-psn-2026", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
NC = ["US-NC"]
NCJ = {"jurisdiction": "US-NC"}
R = lambda loc: src("POL", loc)
PS = lambda page: src("PSN", page)

STRINGS = [
    # NC 1500-2: definitions and disability categories
    ("autism", [], R("1500-2.4(b)(1)")), ("deafblind", [], R("1500-2.4(b)(2)")),
    ("deafness", [], R("1500-2.4(b)(3)")), ("dd", [], R("1500-2.4(b)(4)")),
    ("ed", [("emotional disability", S, NC)], R("1500-2.4(b)(5)")),
    ("hi", [], R("1500-2.4(b)(6)")), ("id", [], R("1500-2.4(b)(7)")), ("md", [], R("1500-2.4(b)(8)")),
    ("oi", [], R("1500-2.4(b)(9)")), ("ohi", [], R("1500-2.4(b)(10)")), ("sld", [], R("1500-2.4(b)(11)")),
    ("sli", [], R("1500-2.4(b)(12)")), ("tbi", [], R("1500-2.4(b)(13)")), ("vi", [], R("1500-2.4(b)(14)")),
    ("pe", [], R("1500-2.1")),
    ("dyslexia", [], R("1500-2.9")),
    ("rti", [("responsiveness to instruction", S, NC), ("responsiveness to intervention", S, NC)], R("1500-2.33")),
    ("screening", [], R("1500-2.43")),
    ("pti", [], R("1500-2.28")),
    ("state_panel", [("Council on Educational Services for Exceptional Children", S, NC)], R("1501-13.1")),
    ("charter_school", [("charter schools", P, None)], R("1502-10")),
    ("sro", [("impartial review officer", S, NC)], R("1504-1.15")),
    ("itinerant", [("Itinerant Preschool Services", S, NC)], R("1508-2")),
    # Notice of Procedural Safeguards
    ("safeguards_notice", [("Parent Rights and Responsibilities in Special Education", S, NC)], PS(1)),
    ("oah", [], PS(29)),
    ("dp_hearing", [], PS(29)),
]

CONCEPTS = [
    # agencies
    ("nc_dpi", "North Carolina Department of Public Instruction", "legal_procedural", [], R("1506-1.11"),
     {**NCJ, "broader": "sea"}),
    ("nc_ecd", "Exceptional Children Division", "legal_procedural", [], R("1506-1.11"), {**NCJ, "broader": "nc_dpi"}),
    ("nc_ecac", "Exceptional Children's Assistance Center", "legal_procedural", [("ECAC", A, NC)], R("1500-2.28"),
     {**NCJ, "broader": "pti"}),
    ("nc_psu", "Public school unit", "legal_procedural", [], PS(7),
     {**NCJ, "broader": "lea", "note": "The term the notice uses for the school district or other public school responsible for the child."}),
    # evaluation
    ("nc_comp_assess", "Comprehensive assessment system", "evaluation_eligibility", [], R("1500-2.5"),
     {**NCJ, "note": "Formative, benchmark, outcome, screening, progress-monitoring and diagnostic data used in SLD evaluations."}),
    ("mtss", "Multi-tiered system of support", "evaluation_eligibility",
     [("multi-tiered system of supports", V, None), ("MTSS", A, None)], R("1500-2.25"),
     {"note": "A school-wide framework of tiered academic and behavioral supports for all students. "
              "Distinct from response to intervention (rti), which uses tiered data to evaluate a child for a learning disability."}),
    ("nc_sps", "Systematic problem-solving process", "evaluation_eligibility", [], R("1500-2.40"),
     {"broader": "rti"}),
    # placements and service levels
    ("nc_recp", "Regular Early Childhood Program", "placement_setting", [("RECP", A, NC)], R("1508-2"), {}),
    ("nc_general_skills", "Special Education General Skills", "placement_setting", [], R("1508-3.1"),
     {**NCJ, "broader": "level_support", "note": "Services outside the general classroom for 20% or less of the day."}),
    ("nc_targeted_skills", "Special Education Targeted Skills", "placement_setting", [], R("1508-3.1"),
     {**NCJ, "broader": "level_support", "note": "Services outside the general classroom for 21% to 60% of the day."}),
    ("nc_sustained_support", "Special Education Sustained Support", "placement_setting", [], R("1508-3.1"),
     {**NCJ, "broader": "level_support", "note": "Services outside the general classroom for more than 60% of the day."}),
    ("nc_intensive_needs", "Special Education Intensive Needs", "placement_setting", [], R("1508-3.1"),
     {**NCJ, "broader": "level_support",
      "note": "More than 60% of the day outside the general classroom, with constant immediate supervision."}),
    # transition
    ("nc_ocs", "Occupational Course of Study", "transition", [], R("1508-3.1"), NCJ),
]

JURISDICTION = "US-NC"
LAYER_NAME = "North Carolina"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.30.0"
