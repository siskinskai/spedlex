"""
Arizona layer for SPEDLex.

Sources reviewed 2026-10-07:
  RULE   Ariz. Admin. Code R7-2-401, Special Education Standards for Public
         Agencies Providing Educational Services, from the Secretary of
         State's text of 7 A.A.C. 2 (Supp. 25-4, current through Dec. 31,
         2025, PDF file, 186 pp.), cited by subsection, e.g. "R7-2-401(B)(16)"
  PSN    Arizona Department of Education (ADE), IDEA Part B Procedural
         Safeguards Notice (Rev. 08-28-25, PDF file, 30 pp.), cited by PDF page
  HWY    ADE Exceptional Student Services, Traveling the Special Education
         Highway: A Parent's Guide to a Successful Journey (revised 2019, PDF
         file, 17 pp.), cited by PDF page
  GLOSS  ADE Exceptional Student Services, ESS Glossary of Acronyms and Terms
         (revised May 2026, PDF file, 60 pp.), cited by PDF page

All four were downloaded from the ADE and Secretary of State websites and
read as text extracted from the PDFs. RULE: only R7-2-401 was read (in
full); the rest of the chapter is general education rules. HWY was read in
full. GLOSS is a three-column table whose extracted text breaks many
multi-word names across columns; it was searched, and it is cited only where
the full name appears unbroken. PSN follows the federal model notice; p. 1
was read in full and the rest searched. Arizona's disability categories are
defined in statute (A.R.S. 15-761), which was not provided; they are cited
from HWY p. 7. RULE records are 'machine_validated'; the others are
'candidate'.

Arizona's mild, moderate and severe intellectual disability categories are
filed as strings under the existing intellectual disability concept, as
Nevada's are. Left out on purpose: the acronym "SID" (severe intellectual
disability), which is also a given name; "MIOD", HWY's misprint of MOID;
"ED-P", "SEAP" and "AZ-TAS", whose full names appear only broken across
GLOSS columns; the category acronym "A" (autism), a single letter; and all
addresses and phone numbers. The Arizona Schools for the Deaf and the Blind
were left out here because GLOSS breaks the name across columns; R7-2-404(A)
has it unbroken, and the arizona_supplement layer adds it from there.
"""

RULE_URL = "https://apps.azsos.gov/public_services/Title_07/7-02.pdf"
PSN_URL = "https://www.azed.gov/sites/default/files/2025/08/Procedural%20Safeguards%20Rev%20_8-28-25.pdf"
HWY_URL = ("https://www.azed.gov/sites/default/files/2016/12/"
           "Traveling%20the%20Special%20Education%20Highway%20%2719.pdf")
GLOSS_URL = ("https://www.azed.gov/sites/default/files/2017/06/"
             "Glossary%20of%20Acronyms%20%26%20Terms%20%285.20.2020%29.pdf")


def src(doc, loc=""):
    """RULE loc is a subsection of R7-2-401, e.g. '(B)(16)'; other loc is a PDF page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"Ariz. Admin. Code R7-2-401{loc}", "doc_id": "az-aac7-2025", "url": RULE_URL}
    if doc == "HWY":
        return {"source_type": "state_guidance",
                "citation": f"ADE Traveling the Special Education Highway (2019), PDF p. {loc}", "doc_id": "az-highway-2019", "url": HWY_URL}
    if doc == "GLOSS":
        return {"source_type": "state_guidance",
                "citation": f"ADE ESS Glossary of Acronyms and Terms (May 2026), PDF p. {loc}", "doc_id": "az-glossary-2026", "url": GLOSS_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"ADE IDEA Part B Procedural Safeguards Notice (Rev. 08-28-25), PDF p. {loc}", "doc_id": "az-psn-2025", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
AZ = ["US-AZ"]
AZJ = {"jurisdiction": "US-AZ"}
R = lambda loc: src("RULE", loc)
H = lambda page: src("HWY", page)
G = lambda page: src("GLOSS", page)

STRINGS = [
    # R7-2-401(B): definitions
    ("cwd", [], R("(B)(4)")),
    ("evaluation", [("full and individual evaluation", S, None)], R("(B)(8)")),
    ("iee", [], R("(B)(9)")),
    ("consent", [("informed written consent", S, AZ)], R("(B)(10)")),
    ("mdt", [("Multidisciplinary Evaluation Team", S, AZ)], R("(B)(12)")),
    ("mdt", [("MET", A, AZ)], R("(E)(3)")),
    ("lea", [("public education agency", REL, AZ), ("PEA", A, AZ)], R("(B)(16)")),
    ("sdi", [], R("(B)(18)")),
    ("sped_teacher", [], R("(B)(19)")),
    # R7-2-401(D)-(L)
    ("psw", [], R("(E)(7)")),
    ("discrepancy", [], R("(E)(7)")),
    ("ed", [("emotional disability", S, AZ)], R("(E)(7)")),
    ("transition", [], R("(G)(4)")), ("postsecondary", [], R("(G)(4)")), ("course_study", [], R("(G)(4)")),
    ("age_majority", [], R("(G)(4)")),
    ("alt_assess", [], R("(G)(5)")), ("sig_cog", [], R("(G)(5)")),
    ("lre", [], R("(H)")),
    ("pwn", [], R("(I)(2)")),
    ("ferpa", [], R("(J)(1)")),
    ("delegation", [], R("(J)(3)")),
    ("part_c_transition", [], R("(K)(2)")),
    ("ppps", [], R("(L)")),
    # Traveling the Special Education Highway
    ("child_find", [], H(3)),
    ("safeguards_notice", [], H(4)),
    ("autism", [], H(7)), ("dd", [], H(7)), ("hi", [], H(7)), ("md", [], H(7)), ("oi", [], H(7)),
    ("ohi", [], H(7)), ("sld", [], H(7)), ("tbi", [], H(7)), ("vi", [], H(7)),
    ("sli", [("Speech/Language Impairment", V, AZ)], H(7)),
    # Arizona's three intellectual disability categories, filed under `id` as Nevada's are
    ("id", [("mild intellectual disability", REL, AZ), ("MIID", A, AZ), ("moderate intellectual disability", REL, AZ),
            ("severe intellectual disability", REL, AZ)], H(7)),
    ("id", [("MOID", A, AZ)], G(34)),
    ("reeval", [], H(11)),
    ("mdr", [], H(12)), ("iaes", [], H(12)),
    ("s504", [], H(13)), ("sop", [], H(13)), ("std_diploma", [], H(13)),
    ("oah", [("Arizona Office of Administrative Hearings", S, AZ)], H(14)),
    ("state_complaint", [], H(14)),
    ("pti", [], H(16)),
    # Glossary
    ("msaa", [], G(35)),
]

CONCEPTS = [
    # agencies and offices
    ("az_doe", "Arizona Department of Education", "legal_procedural", [("ADE", A, AZ)], H(16), {**AZJ, "broader": "sea"}),
    ("az_ess", "Exceptional Student Services", "legal_procedural", [("ESS", A, AZ)], H(16),
     {**AZJ, "broader": "az_doe", "note": "The Department's special education division."}),
    ("az_dru", "Dispute Resolution Unit", "legal_procedural", [], H(14),
     {**AZJ, "broader": "az_ess", "note": "Receives requests for mediation, state complaints and due process hearings."}),
    ("az_encircle", "Encircle Families", "legal_procedural", [("Raising Special Kids", L, AZ)], G(45),
     {**AZJ, "broader": "pti", "note": "Arizona's parent training and information center, formerly Raising Special Kids."}),
    ("az_dra", "Disability Rights Arizona", "legal_procedural", [], src("PSN", 1), AZJ),
    ("az_azeip", "Arizona Early Intervention Program", "early_intervention", [("AzEIP", A, AZ)], H(3),
     {**AZJ, "note": "Arizona's Part C program for infants and toddlers."}),
    ("az_ahcccs", "Arizona Health Care Cost Containment System", "legal_procedural", [("AHCCCS", A, AZ)], G(35),
     {**AZJ, "note": "Arizona's Medicaid program."}),
    # public education agencies
    ("az_accom_school", "Accommodation school", "legal_procedural", [], R("(B)(16)"),
     {**AZJ, "broader": "lea", "note": "A county-run school; one of the kinds of public education agency."}),
    ("az_boundaries", "Boundaries of responsibility", "legal_procedural", [], R("(B)(3)"),
     {**AZJ, "note": "The area or student population a public education agency is responsible for."}),
    ("az_private_sped_school", "Private special education school", "placement_setting", [], R("(B)(15)"),
     {**AZJ, "broader": "special_school"}),
    # eligibility categories
    ("az_mdssi", "Multiple disabilities with severe sensory impairment", "disability_category", [("MDSSI", A, AZ)], H(7),
     {**AZJ, "broader": "md"}),
    ("az_psd", "Preschool severe delay", "disability_category", [("PSD", A, AZ)], H(7), {**AZJ, "broader": "dd"}),
    # IEP and assessment
    ("az_grad_date", "Estimated date of graduation", "transition", [], R("(G)(4)"),
     {**AZJ, "broader": "transition", "note": "Arizona requires it in the IEP, with the course of study aligned to the transition plan."}),
    ("az_azsci", "Arizona Science Test", "iep_component", [("AzSCI", A, AZ)], G(10), AZJ),
]

JURISDICTION = "US-AZ"
LAYER_NAME = "Arizona"
RETRIEVED = "2026-10-07"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.33.0"
