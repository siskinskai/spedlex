"""
Alaska layer for SPEDLex.

Sources reviewed 2026-10-08 (published by the State of Alaska unless noted):
  RULE   4 AAC 52, Article 2 (Program Administration: Children with
         Disabilities), 4 AAC 52.100 - 52.790, from the Alaska Legislature's
         Alaska Administrative Code (akleg.gov), printed to PDF on
         2026-10-08 (16 pp.), cited by section and subsection, e.g.
         "4 AAC 52.130(b)"
  PSN    Alaska Department of Education & Early Development (DEED), Notice of
         Procedural Safeguards: Parental Rights for Special Education (no date
         printed; the PDF file is dated March 2024; 37 pp.), cited by page
  GUIDE  Alaska Special Education Parents' Guide, developed by LINKS Mat-Su
         Parent Resource Center for DEED (June 2017, 12 pp.), cited by page
  ALT    DEED web page "Dynamic Learning Maps (DLM) Alternate Assessment",
         education.alaska.gov/sped/alternate, printed to PDF on 2026-10-08

All four were read in full as text extracted from the PDFs with pdftotext.
The RULE printout starts at 4 AAC 52.100, so 4 AAC 52.090 (district
responsibility) was not read. The printout carries no history notes; another
copy shows 4 AAC 52.130 was last amended 9/9/2016 (Register 219). DEED's
Special Education Handbook has no DEED-hosted copy and was not used. RULE
records are 'machine_validated'; the others are 'candidate'.

Left out on purpose: every person named in PSN pp. 14 and GUIDE p. 8 (DEED,
mediation and parent-center contacts) and on the ALT page; addresses, phone
numbers and email addresses; "Disability Law Center" on its own (PSN p. 33),
because Utah's layer already uses that exact name; the intensive-student
funding terms in 4 AAC 52.700 and 52.790(20)-(25); the nine health problems
in 4 AAC 52.130(k)(1) that the federal list doesn't seed (heart condition,
tuberculosis and so on); and general glossary words in GUIDE pp. 9-11
("aptitude test", "readiness test", "auditory perception").
"""

RULE_URL = "https://www.akleg.gov/basis/aac.asp#4.52"
PSN_URL = "https://education.alaska.gov/tls/sped/docs/Procedural%20Safeguards.pdf"
GUIDE_URL = "https://education.alaska.gov/tls/SPED/docs/ParentResourceGuide%20ADA.pdf"
ALT_URL = "https://education.alaska.gov/sped/alternate"


def src(doc, loc=""):
    """RULE loc is a section and subsection, e.g. '.130(b)'; PSN and GUIDE loc is a page number."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"4 AAC 52{loc}", "doc_id": "ak-4aac52-2026", "url": RULE_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"Alaska Special Education Parents' Guide (LINKS for DEED, June 2017), p. {loc}",
                "doc_id": "ak-parentguide-2017", "url": GUIDE_URL}
    if doc == "ALT":
        return {"source_type": "state_guidance",
                "citation": "DEED, Dynamic Learning Maps (DLM) Alternate Assessment web page (printed 2026-10-08)",
                "doc_id": "ak-dlmpage-2026", "url": ALT_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"DEED Notice of Procedural Safeguards: Parental Rights for Special Education (undated; file dated Mar. 2024), p. {loc}",
            "doc_id": "ak-psn-2024", "url": PSN_URL}


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
AK = ["US-AK"]
AKJ = {"jurisdiction": "US-AK"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)
ALT = src("ALT")

STRINGS = [
    # 4 AAC 52.100 - 52.180: child find, evaluation, eligibility, IEP
    ("child_find", [], R(".100")),
    ("referral", [], R(".100(a)(3)")),
    ("evaluation", [], R(".120")),
    ("eligibility", [], R(".125(a)")),
    ("adaptive", [], R(".125(a)(1)")),
    ("eval_report", [], R(".125(b)")),
    # 4 AAC 52.130: eligibility categories
    ("id", [("cognitive impairment", S, AK), ("cognitively impaired", S, AK)], R(".130(b)")),
    ("sld", [], R(".130(c)")),
    ("ed", [], R(".130(d)")),
    ("deafness", [], R(".130(e)")),
    ("hi", [], R(".130(f)")),
    ("deafblind", [("deaf and blind", S, AK)], R(".130(g)")),
    ("oi", [("orthopedically impaired", S, None)], R(".130(h)")),
    ("vi", [], R(".130(i)")),
    ("tvi", [("teacher of children with visual impairment", S, AK)], R(".130(i)(2)")),
    ("sli", [], R(".130(j)")),
    ("ohi", [("other health impairments", P, None)], R(".130(k)")),
    ("adhd", [], R(".130(k)(1)")), ("sickle", [], R(".130(k)(1)")), ("epilepsy", [], R(".130(k)(1)")),
    ("md", [], R(".130(l)")),
    ("dd", [("early childhood developmental delay", S, AK)], R(".130(n)")),
    ("autism", [], R(".130(o)")),
    ("tbi", [], R(".130(p)")),
    ("iep", [], R(".140(a)")), ("iep_team", [], R(".140(a)")),
    ("annual_goals", [], R(".140(g)")), ("sto", [], R(".140(g)")),
    ("ifsp", [], R(".142(a)")),
    ("esy", [], R(".144(a)")),
    ("transition", [], R(".145(a)")),
    ("prefs", [], R(".145(b)")), ("comm_exp", [], R(".145(b)")), ("post_school", [], R(".145(b)")),
    ("daily_living", [], R(".145(b)")), ("fve", [], R(".145(b)")),
    ("part_agency", [], R(".145(h)")),
    ("at_device", [], R(".148")), ("at_service", [], R(".148")),
    ("lre", [], R(".170(a)")),
    ("nonacademic_settings", [], R(".170(b)")),
    ("implant", [], R(".170(d)")),
    ("reeval", [], R(".180(a)")),
    ("plaafp", [], R(".180(b)(2)(B)")),
    ("gen_curr", [], R(".180(b)(2)(D)")),
    # 4 AAC 52.190 - 52.260: notice, consent, staffing
    ("pwn", [], R(".190")),
    ("consent", [], R(".200")),
    ("para", [("special education aide", S, None), ("special education aides", P, None)], R(".250(a)")),
    ("interpreting", [], R(".255")),
    # 4 AAC 52.480 - 52.630: safeguards and dispute resolution
    ("safeguards_notice", [], R(".480")),
    ("mediation", [], R(".490")),
    ("state_complaint", [("administrative complaint", S, AK)], R(".500(a)")),
    ("homeless", [], R(".500(b)(6)(A)")),
    ("comp_services", [("compensatory education", S, None)], R(".500(e)(5)")),
    ("iee", [], R(".540(a)")),
    ("dp_hearing", [], R(".550(a)")),
    ("dp_complaint", [("complaint for a due process hearing", S, AK)], R(".550(a)")),
    ("prehearing", [], R(".550(g)")),
    ("exp_hearing", [], R(".550(l)")),
    ("state_panel", [], R(".550(m)")),
    ("resolution", [], R(".555(a)")),
    ("stay_put", [], R(".580(a)")),
    ("iaes", [], R(".580(c)")), ("mdr", [], R(".580(c)")),
    ("surrogate", [], R(".590(a)")),
    ("foster", [], R(".600(d)")),
    ("age_majority", [], R(".620")),
    ("pii", [], R(".765(a)")),
    # 4 AAC 52.790: definitions
    ("at_device", [], R(".790(1)")), ("at_service", [], R(".790(2)")),
    ("cwd", [], R(".790(3)")),
    ("sld", [("learning disabilities", P, None)], R(".790(3)")),
    ("sli", [("speech impairment", REL, AK)], R(".790(3)")),
    ("dd", [("early childhood development delay", V, AK)], R(".790(3)")),
    ("adverse", [], R(".790(4)")),
    ("ed", [("emotionally disturbed", S, None)], R(".790(5)")),
    ("fape", [], R(".790(7)")),
    ("iaes", [], R(".790(12)")),
    ("related", [], R(".790(15)")),
    ("special_ed", [], R(".790(17)")),
    ("sdi", [], R(".790(18)")),
    ("saas", [], R(".790(19)")),
    # Procedural Safeguards Notice
    ("idea", [], PS(1)),
    ("pwn", [], PS(3)), ("native_language", [], PS(3)),
    ("consent", [], PS(4)), ("revoke", [], PS(4)), ("braille", [], PS(4)),
    ("ward", [], PS(5)),
    ("equitable", [], PS(7)), ("iee", [], PS(7)),
    ("age_majority", [], PS(8)),
    ("ed_records", [], PS(9)), ("pii", [], PS(9)), ("part_agency", [], PS(9)), ("ferpa", [], PS(9)),
    ("child_find", [], PS(9)),
    ("iep_facil", [("IEP facilitator", S, None)], PS(14)),
    ("state_complaint", [], PS(15)), ("pti", [], PS(15)),
    ("dp_complaint", [], PS(17)),
    ("resolution", [], PS(21)), ("dp_hearing", [], PS(22)),
    ("state_panel", [("state special education advisory panel", S, AK)], PS(24)),
    ("code_conduct", [], PS(26)), ("iaes", [], PS(26)),
    ("fba", [], PS(27)),
    ("mdr", [], PS(28)), ("bip", [], PS(28)), ("special_circ", [], PS(28)), ("controlled", [], PS(28)),
    ("illegal_drug", [], PS(29)), ("sbi", [], PS(29)), ("weapon", [], PS(29)), ("cop", [], PS(29)),
    ("exp_hearing", [], PS(30)),
    ("basis_know", [], PS(31)),
    ("ppps", [], PS(7)),
    # Parents' Guide
    ("child_find", [], G(4)), ("referral", [], G(4)), ("pwn", [], G(4)), ("iee", [], G(4)),
    ("iep", [], G(5)), ("iep_team", [], G(5)),
    ("plaafp", [], G(5)), ("annual_goals", [], G(5)), ("sto", [], G(5)),
    ("gen_teacher", [("regular classroom teacher", S, None)], G(5)),
    ("sped_teacher", [], G(5)), ("lea_rep", [], G(5)), ("eval_interp", [], G(5)), ("progress", [], G(5)),
    ("regular_class", [], G(6)), ("itinerant", [], G(6)), ("special_class", [], G(6)),
    ("special_school", [("separate day school", S, None)], G(6)),
    ("home_instr", [], G(6)),
    ("hospital_instr", [("institutional services", S, None)], G(6)),
    ("transition", [("secondary transition plan", S, None)], G(6)),
    ("age_majority", [], G(6)),
    ("related", [], G(6)), ("transport", [], G(6)), ("slp", [], G(6)), ("psych", [], G(6)), ("pt", [], G(6)),
    ("ot", [], G(6)), ("recreation", [], G(6)), ("nursing", [], G(6)), ("social_work", [], G(6)),
    ("counseling", [], G(6)), ("audiology", [], G(6)), ("om", [], G(6)), ("parent_training", [], G(6)),
    ("rehab", [], G(6)),
    ("pe", [("adaptive physical education", V, None)], G(6)),
    ("mediation", [], G(7)), ("state_complaint", [], G(7)), ("dp_hearing", [], G(7)),
    ("comp_services", [], G(8)),
    ("gen_ed_int", [("alternative intervention strategies", REL, AK), ("pre-referral strategies", S, None)], G(9)),
    ("adaptive", [], G(9)), ("artic", [], G(9)), ("autism", [], G(9)), ("cop", [], G(9)),
    ("id", [], G(9)), ("deafness", [], G(9)), ("deafblind", [], G(9)), ("dyslexia", [], G(9)),
    ("dd", [], G(10)), ("ed", [], G(10)), ("evaluation", [], G(10)), ("ferpa", [], G(10)),
    ("fine_motor", [], G(10)), ("fba", [], G(10)), ("hi", [], G(10)), ("inclusive", [], G(10)),
    ("idea", [], G(10)), ("lang_dis", [], G(10)), ("lre", [], G(10)), ("md", [], G(10)),
    ("oi", [], G(11)), ("ohi", [], G(11)), ("para", [("teacher's aide", V, None)], G(11)),
    ("plaafp", [("present level of academic achievement and functional performance", V, None)], G(11)), ("safeguards_notice", [], G(11)), ("reeval", [], G(11)), ("special_ed", [], G(11)),
    ("sld", [], G(11)), ("tbi", [], G(11)), ("vi", [], G(11)),
    # DLM alternate assessment page
    ("alt_assess", [], ALT), ("dlm", [], ALT), ("sig_cog", [], ALT), ("adaptive", [], ALT),
    ("ess_elements", [("DLM Essential Elements", S, None)], ALT),
]

CONCEPTS = [
    # agencies, offices and state resources
    ("ak_deed", "Alaska Department of Education and Early Development", "legal_procedural",
     [("Alaska Department of Education & Early Development", V, AK),
      ("Department of Education and Early Development", S, AK),
      ("Department of Education & Early Development", V, AK)], PS(1),
     {**AKJ, "broader": "sea"}),
    ("ak_tls", "Division of Teaching and Learning Support", "legal_procedural", [], R(".500(b)"),
     {**AKJ, "broader": "ak_deed", "note": "The DEED division that receives special education administrative complaints."}),
    ("ak_abdhh", "Advisory Board for the Deaf and Hard of Hearing", "legal_procedural", [], R(".255"),
     {**AKJ, "note": "A board under the state Board of Education whose standards apply to interpreters for deaf students."}),
    ("ak_dfcs", "Department of Family and Community Services", "legal_procedural", [], R(".590(b)(4)"),
     {**AKJ, "note": "A child committed to this department's custody is entitled to a surrogate parent."}),
    ("ak_ilp", "Alaska Infant Learning Program", "early_intervention", [("infant learning program", S, AK)], G(8),
     {**AKJ, "note": "Alaska's Part C early intervention program; children it serves need an IEP by age 3 if eligible."}),
    ("ak_sems", "Alaska Special Education Mediation Services", "legal_procedural", [], PS(13),
     {**AKJ, "broader": "mediation", "note": "The service that provides special education mediators and IEP facilitators."}),
    ("ak_sesa", "Special Education Service Agency", "legal_procedural", [], G(8),
     {**AKJ, "note": "A statewide special education agency listed among the parents' guide resources."}),
    ("ak_ssg", "Stone Soup Group", "legal_procedural", [], PS(33),
     {**AKJ, "note": "A statewide family organization listed among the safeguards notice resources."}),
    ("ak_dlc", "Disability Law Center of Alaska", "legal_procedural", [], G(8),
     {**AKJ, "note": "Statewide disability legal services; the safeguards notice calls it the Disability Law Center."}),
    ("ak_links", "LINKS Mat-Su Parent Resource Center", "legal_procedural", [], G(2),
     {**AKJ, "flags": ["place_name"], "note": "The parent resource center that wrote the 2017 parents' guide for DEED."}),
    # forms
    ("ak_admin_complaint_form", "Notice of Administrative Complaint", "legal_procedural", [], PS(34),
     {**AKJ, "broader": "state_complaint", "note": "DEED's optional form for filing an administrative complaint."}),
    ("ak_dp_request_form", "Notice of Request for Due Process Hearing", "legal_procedural", [], PS(36),
     {**AKJ, "broader": "dp_complaint", "note": "DEED's optional form for requesting a due process hearing."}),
    # assessment
    ("ak_aa_checklist", "Alternate Assessment Participation Checklist", "iep_component", [], ALT,
     {**AKJ, "broader": "alt_assess",
      "note": "Three criteria the IEP team documents to decide that a student takes the alternate assessment."}),
    # national concepts first attested by Alaska's documents
    ("fasd", "Fetal alcohol spectrum disorder", "health_condition", [], R(".130(k)(1)"),
     {"broader": "ohi", "note": "Alaska names it among the health problems that can qualify a child as other health impaired."}),
    ("unilateral_pl", "Unilateral placement", "legal_procedural", [("unilateral placement by parents", S, None)], R(".155"),
     {"note": "A parent's own placement of a child in a private school; reimbursement follows 34 CFR 300.148."}),
    ("pullout", "Pull-out", "placement_setting", [], G(6),
     {"note": "Services given outside the regular class for part of the day."}),
    ("gross_motor", "Gross motor", "functional_skill", [], G(10),
     {"note": "Movement that uses balance, coordination and the large muscles."}),
    ("iq", "Intelligence quotient", "score_metric", [("IQ", A, None)], G(10), {}),
    ("norm_ref", "Norm-referenced test", "evaluation_eligibility", [], G(10), {}),
]

JURISDICTION = "US-AK"
LAYER_NAME = "Alaska"
RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.35.0"
