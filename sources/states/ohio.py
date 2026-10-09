"""
Ohio layer for SPEDLex.

Sources reviewed 2026-10-07 (both published by the Ohio Department of
Education and Workforce, DEW):
  RULE  Operating Standards for the Education of Children with Disabilities
        (DEW booklet, June 2025, 185 pp.): Ohio Adm.Code 3301-51-01 to
        3301-51-11 and 3301-51-21, cited by rule and paragraph
  PR    A Guide to Parent Rights in Special Education: Special Education
        Procedural Safeguards Notice (April 2025, 36 pp.), cited by PDF page
        (the printed page numbers are one lower)

Both were read as text extracted from the PDF files on DEW's "Operating
Standards and Guidance" page; ligatures (ff, fi) were normalized. RULE
3301-51-01 (definitions), 3301-51-05(K) (dispute resolution), 3301-51-09
(delivery of services) and 3301-51-11 (preschool) were read in full; the
other rules were read by paragraph heading and searched. PR pages 1-5 and
13-14 and 35-36 were read in full and the rest searched. Ohio has no
separate parent handbook: the PR guide is both the safeguards notice and the
main parent guide. RULE records are 'machine_validated'; the others are
'candidate'.

Left out on purpose: "Educational agency" and "Other educational agency"
(Ohio-defined but ordinary phrases), the funding definitions in 3301-51-01
(average daily membership, excess costs), and the blank regional contact
lines on PR p. 13.
"""

RULE_URL = ("https://education.ohio.gov/getattachment/Topics/Special-Education/Federal-and-State-Requirements/"
            "Operational-Standards-and-Guidance/Operating-Standards-Booklet-June-2025.pdf.aspx?lang=en-US")
PR_URL = ("https://education.ohio.gov/getattachment/Topics/Special-Education/Federal-and-State-Requirements/"
          "Operational-Standards-and-Guidance/Parent-Rights-Document-2025.pdf.aspx?lang=en-US")


def src(doc, loc=""):
    """RULE loc is a rule and paragraph, e.g. '3301-51-01(B)(14)'; PR loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"Ohio Adm.Code {loc}", "doc_id": "oh-standards-2025", "url": RULE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"DEW A Guide to Parent Rights in Special Education (Apr. 2025), PDF p. {loc}", "doc_id": "oh-psn-2025", "url": PR_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
OH = ["US-OH"]
OHJ = {"jurisdiction": "US-OH"}
R = lambda loc: src("RULE", loc)
PR = lambda page: src("PR", page)

STRINGS = [
    # Ohio Adm.Code 3301-51-01(B): definitions and disability categories
    ("autism", [], R("3301-51-01(B)(10)")), ("id", [], R("3301-51-01(B)(10)")),
    ("deafblind", [], R("3301-51-01(B)(10)")), ("deafness", [], R("3301-51-01(B)(10)")),
    ("ed", [], R("3301-51-01(B)(10)")), ("hi", [], R("3301-51-01(B)(10)")), ("md", [], R("3301-51-01(B)(10)")),
    ("oi", [], R("3301-51-01(B)(10)")), ("ohi", [], R("3301-51-01(B)(10)")), ("sld", [], R("3301-51-01(B)(10)")),
    ("sli", [], R("3301-51-01(B)(10)")), ("tbi", [], R("3301-51-01(B)(10)")), ("vi", [], R("3301-51-01(B)(10)")),
    ("dd", [], R("3301-51-01(B)(10)")),
    ("mdt", [], R("3301-51-01(B)(22)")),
    ("referral", [], R("3301-51-01(B)(55)")),
    ("resident_dist", [("school district of residence", S, OH)], R("3301-51-01(B)(58)")),
    ("esa", [("educational service center", S, OH)], R("3301-51-01(B)(18)")),
    ("surrogate", [], R("3301-51-01(B)(66)")),
    ("pti", [], R("3301-51-01(B)(49)")),
    ("ppps", [("parentally placed nonpublic school children with disabilities", S, OH)], R("3301-51-01(B)(50)")),
    ("eval_report", [("evaluation team report", S, OH)], R("3301-51-06")),
    ("itinerant", [], R("3301-51-11")),
    ("state_sp_sch", [("state residential school", S, OH)], R("3301-51-01(B)(64)")),
    # Guide to Parent Rights
    ("eval_report", [("ETR", A, OH)], PR(5)),
    ("parent_mentor", [], PR(13)),
    ("safeguards_notice", [("A Guide to Parent Rights in Special Education", S, OH)], PR(1)),
]

CONCEPTS = [
    # agencies and offices
    ("oh_dew", "Ohio Department of Education and Workforce", "legal_procedural", [], PR(13),
     {**OHJ, "broader": "sea"}),
    ("oh_oec", "Office for Exceptional Children", "legal_procedural", [], PR(13), {**OHJ, "broader": "oh_dew"}),
    ("oh_sst", "State Support Team", "legal_procedural", [], PR(13),
     {**OHJ, "note": "Regional teams whose parent and family consultants help families resolve disagreements."}),
    ("oh_ocecd", "Ohio Coalition for the Education of Children with Disabilities", "legal_procedural",
     [("OCECD", A, OH)], PR(14), {**OHJ, "broader": "pti"}),
    ("oh_county_bdd", "County board of developmental disabilities", "legal_procedural", [], R("3301-51-01(B)(14)"),
     {**OHJ, "note": "A county agency that can be the educational agency serving a child with a disability."}),
    ("oh_odys", "Ohio Department of Youth Services", "legal_procedural", [], R("3301-51-01(B)(18)"), OHJ),
    ("oh_jvsd", "Joint vocational school district", "legal_procedural", [], R("3301-51-01(B)(44)"),
     {**OHJ, "broader": "lea"}),
    ("oh_district_of_service", "School district of service", "legal_procedural", [], R("3301-51-01(B)(59)"),
     {**OHJ, "broader": "lea"}),
    # schools
    ("charter_school", "Charter school", "legal_procedural", [("community school", S, OH)], R("3301-51-01(B)(8)"), {}),
    ("oh_chartered_nonpublic", "Chartered nonpublic school", "legal_procedural", [], R("3301-51-01(B)(9)"),
     {**OHJ, "note": "A private school chartered by the state board; not a charter school."}),
    ("oh_osd", "Ohio School for the Deaf", "placement_setting", [], R("3301-51-01(B)(64)"),
     {**OHJ, "broader": "state_sp_sch"}),
    ("oh_ossb", "Ohio State School for the Blind", "placement_setting", [], R("3301-51-01(B)(64)"),
     {**OHJ, "broader": "state_sp_sch"}),
    # eligibility
    ("oh_ohi_major", "Other health impairment - major", "disability_category", [], R("3301-51-01(B)(45)"),
     {**OHJ, "broader": "ohi", "note": "Used for children whose condition is on the state's medically fragile list."}),
    ("oh_ohi_minor", "Other health impairment - minor", "disability_category", [], R("3301-51-01(B)(46)"),
     {**OHJ, "broader": "ohi"}),
    # personnel
    ("oh_intervention_specialist", "Intervention specialist", "personnel_role",
     [("early childhood intervention specialist", S, OH)], R("3301-51-11"),
     {**OHJ, "broader": "sped_teacher", "note": "Ohio's title for a licensed special education teacher."}),
    ("oh_ttw", "Transition to Work endorsement", "transition", [], R("3301-51-09(H)(7)"), OHJ),
    # dispute resolution
    ("oh_admin_review", "Administrative review", "legal_procedural", [], R("3301-51-05(K)(1)"),
     {**OHJ, "note": "An optional review by the superintendent or a designee before other dispute options."}),
    ("oh_early_complaint", "Early complaint resolution", "legal_procedural", [], PR(14),
     {**OHJ, "broader": "adr"}),
    # scholarships
    ("oh_autism_scholarship", "Autism Scholarship Program", "legal_procedural", [], PR(36), OHJ),
    ("oh_jon_peterson", "Jon Peterson Special Needs Scholarship Program", "legal_procedural",
     [("Jon Peterson Scholarship", AB, OH)], PR(36), {**OHJ, "flags": ["eponym"]}),
]

JURISDICTION = "US-OH"
LAYER_NAME = "Ohio"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.29.0"
