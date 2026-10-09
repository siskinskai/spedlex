"""
Colorado layer for SPEDLex.

Sources reviewed 2026-10-08 (all published by the Colorado Department of
Education (CDE), Exceptional Student Services Unit (ESSU), or the State
Board of Education through the Secretary of State's Code of Colorado
Regulations):
  RULE   1 CCR 301-8, Rules for the Administration of the Exceptional
         Children's Educational Act (ECEA), the Code of Colorado Regulations
         PDF (126 pp.) linked from CDE's Special Education Rules and
         Regulations page (ruleVersionId=11935); its Editor's Notes list
         amendments through May 15, 2025. Cited by rule number, e.g.
         "1 CCR 301-8, Rule 2.09(3)"
  PSN    CDE, "A Guide to Parent Rights in Special Education: Special
         Education Procedural Safeguards Notice" (English, April 2024
         edition, 51 pp.; the file's appendix D footers read April 2025),
         cited by PDF page (printed page number + 4 for the body, e.g.
         PDF p. 5 is printed p. 1)
  GUIDE  CDE ESSU, "IEP Procedural Guidance: Exceptional Student Services
         Unit Technical Assistance" (revised July 2017, 158 pp.), cited by
         page (printed page numbers equal PDF page numbers). It is a
         practitioner manual for administrative units, not a parent guide;
         CDE's parent-facing pages are web pages, which were not used.

All three were read as text extracted with pdftotext. The rules were read in
the definitions (Rules 2.00-2.54), child find and evaluation (Rule 4.02),
IEP (Rule 4.03) and gifted-education definitions (Rule 12.01) sections, and
searched for Colorado terms elsewhere; the funding, tuition-contract and
administrative-unit-reorganization rules (Rules 3.01-3.03, 7.03, 9.03-9.07)
were not read line by line. The GUIDE's Pages 12-39 and the model forms
(Pages 83-147) were searched, not read in full. The 2017 guidance predates
the 2024 abbreviated-school-day law and the 2025 rule amendments. RULE
records for new concepts are 'machine_validated'; the others are 'candidate'.
Rule 2.20's Editor's Notes say it was repealed effective 06/30/2022, but the
rule text still carries 2.20 and 2.20(1); the text is what is cited. In the
rules PDF "Colorado State Board of Education" appears in full only in the
running page header; Rule 2.47 says "State Board".

Left out on purpose: every person named in the documents (task-force
members, CDE staff, their e-mail addresses and phone numbers) and the
districts, BOCES and schools they work for (the one exception is the
state-run Colorado School for the Deaf and the Blind, which Rule 2.50(1)
names as a State-Operated Program); "SASID" (the label for a
student's state identification number, left out because it names an
identifier); ICAP, UIP and per-pupil revenue (general-education planning and
funding terms); tuition, contract-element and funding-formula terms; the
YODeL training library and the "Quality Tips" worksheets; commercial
reading screeners named in the guidance; "Show and Tell" on its own (a
common phrase); "PEAK" on its own (a common word); the CDE staff job
titles other than the dispute-resolution roles; and the long
eligibility-criteria wording of each disability category.
"""

RULE_URL = "https://www.sos.state.co.us/CCR/GenerateRulePdf.do?ruleVersionId=11935&fileName=1%20CCR%20301-8"
PSN_URL = "https://ed.cde.state.co.us/fs/resource-manager/view/c8fc104d-1433-48fb-b803-f7d0ec9545bb"
GUIDE_URL = "https://ed.cde.state.co.us/fs/resource-manager/view/00bbb119-c6d9-4331-b661-70b3b3989ffa"


def src(doc, loc=""):
    """RULE loc is a rule number, e.g. '2.09(3)'; PSN loc is a PDF page; GUIDE loc is a page."""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"1 CCR 301-8, Rule {loc}", "doc_id": "co-ecea-2025", "url": RULE_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"CDE IEP Procedural Guidance (rev. July 2017), p. {loc}", "doc_id": "co-iepguidance-2017", "url": GUIDE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"CDE Procedural Safeguards Notice (Apr. 2024), PDF p. {loc}", "doc_id": "co-psn-2024", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
CO = ["US-CO"]
COJ = {"jurisdiction": "US-CO"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)

STRINGS = [
    # ECEA rules: definitions (Rule 2.00)
    ("at_device", [], R("2.04")), ("at_service", [], R("2.05")), ("charter_school", [], R("2.07")),
    ("child_find", [], R("2.08")), ("cwd", [], R("2.09")),
    ("autism", [], R("2.09(1)")),
    ("hi", [("Hearing Impairment, Including Deafness", S, CO)], R("2.09(2)")),
    ("ed", [("Serious Emotional Disability", S, CO)], R("2.09(3)")),
    ("id", [], R("2.09(4)")), ("md", [], R("2.09(5)")), ("oi", [], R("2.09(6)")),
    ("ohi", [("Other Health Impaired", V, None)], R("2.09(7)")),
    ("adhd", [], R("2.09(7)")), ("epilepsy", [], R("2.09(7)")), ("sickle", [], R("2.09(7)")),
    ("tourette", [], R("2.09(7)")),
    ("sld", [], R("2.09(8)")), ("dyslexia", [], R("2.09(8)(a)")), ("perceptual", [], R("2.09(8)(a)")),
    ("mbd", [], R("2.09(8)(a)")), ("aphasia", [], R("2.09(8)(a)")),
    ("sli", [], R("2.09(9)")), ("tbi", [], R("2.09(10)")),
    ("vi", [("Visual Impairment, Including Blindness", V, CO)], R("2.09(11)")),
    ("deafblind", [], R("2.09(12)")), ("dd", [], R("2.09(13)")), ("itd", [], R("2.09(14)")),
    ("comm_mode", [("Communication Mode or Language", S, CO)], R("2.10")),
    ("asl", [], R("2.10(1)")), ("consent", [], R("2.11")), ("school_day", [], R("2.12")),
    ("surrogate", [("educational surrogate parent", S, CO)], R("2.15")),
    ("evaluation", [], R("2.18")), ("excess_costs", [], R("2.19")), ("fape", [], R("2.21")),
    ("homeless", [], R("2.22")), ("idea", [], R("2.23")), ("iep", [], R("2.25")),
    ("iep_team", [], R("2.26")), ("ifsp", [], R("2.27")), ("lre", [], R("2.29")),
    ("lep", [], R("2.30")), ("braille", [], R("2.31(2)")), ("lea", [], R("2.32")),
    ("native_language", [], R("2.33")), ("foster", [], R("2.34(1)(b)")), ("pii", [], R("2.35")),
    ("public_agency", [], R("2.36")), ("related", [], R("2.38")), ("implant", [], R("2.38(2)")),
    ("audiology", [], R("2.38(3)(a)")), ("counseling", [], R("2.38(3)(b)")),
    ("early_id", [], R("2.38(3)(c)")), ("interpreting", [], R("2.38(3)(d)")),
    ("cart", [], R("2.38(3)(d)(i)")), ("medical", [], R("2.38(3)(e)")), ("ot", [], R("2.38(3)(f)")),
    ("om", [], R("2.38(3)(g)")), ("parent_training", [], R("2.38(3)(h)")), ("pt", [], R("2.38(3)(i)")),
    ("psych", [], R("2.38(3)(j)")), ("recreation", [], R("2.38(3)(k)")),
    ("rehab", [], R("2.38(3)(l)")), ("nursing", [], R("2.38(3)(m)")),
    ("social_work", [], R("2.38(3)(n)")), ("transport", [], R("2.38(3)(o)")),
    ("sbr", [], R("2.39")), ("services_plan", [], R("2.42")), ("special_ed", [], R("2.44")),
    ("slp", [], R("2.44(1)(b)(i)")), ("pe", [], R("2.44(2)(b)")), ("sdi", [], R("2.44(2)(c)")),
    ("travel_training", [], R("2.44(2)(d)")), ("voc_ed", [], R("2.44(2)(e)")),
    ("sea", [], R("2.49")), ("state_ops", [("State Operated Program", V, CO)], R("2.50, 3.02(2)")),
    ("saas", [], R("2.51")), ("transition", [], R("2.52")), ("universal_design", [], R("2.53")),
    ("ward", [], R("2.54")),
    # child find, evaluation and IEP rules (Rules 4.02-4.03)
    ("referral", [("special education referral", S, CO)], R("4.02(3)")),
    ("rti", [], R("4.02(2)(c)(v)")), ("screening", [], R("4.02(4)(b)")),
    ("reeval", [], R("4.02(5)")), ("eligibility", [], R("4.02(6)")),
    ("mdt", [], R("4.02(6)(b)(i)")), ("sop", [], R("4.02(6)(c)(ii)")),
    ("amendment", [], R("4.03(2)(f)")), ("annual_review", [], R("4.03(3)")),
    ("postsecondary", [], R("4.03(6)(d)(ii)")), ("trans_assess", [], R("4.03(6)(d)(ii)")),
    ("course_study", [], R("4.03(6)(d)(iii)")), ("age_majority", [], R("4.03(6)(e)")),
    ("sto", [], R("4.03(6)(f)")), ("alt_assess", [], R("4.03(6)(f)(i)")),
    ("sped_admin", [("Special Education Director", S, CO)], R("4.02(6)(b)(ii)")),
    # personnel, funding conditions, procedural safeguards, complaints
    ("edu_interpreter", [], R("3.04(1)(f)")),
    ("state_panel", [("Colorado Special Education Advisory Committee", S, CO)], R("5.01(18)")),
    ("nimas", [], R("5.01(21)")), ("nimac", [], R("5.01(21)(b)")), ("disprop", [], R("5.01(22)")),
    ("dp_complaint", [], R("6.02(7.5)(a)")), ("dp_hearing", [], R("6.02(7.5)(c)")),
    ("resolution", [], R("6.02(7.5)(d)")), ("exp_hearing", [], R("6.02(7.5)(i)")),
    ("stay_put", [], R("6.02(7.5)(l)")), ("mdr", [], R("6.02(10)(f)")),
    ("state_complaint", [], R("7.06")),
    ("pwn", [], R("4.02(3)(b)(i)")), ("safeguards_notice", [], R("4.02(3)(b)(i)")),
    # gifted education (Rule 12.00)
    ("gifted", [("gifted children", S, CO)], R("12.01(16)")), ("twice_ex", [], R("12.01(16)")),
    # Procedural Safeguards Notice (April 2024)
    ("iep", [], PS(3)), ("fape", [], PS(6)), ("lre", [], PS(42)), ("consent", [], PS(5)),
    ("pwn", [], PS(6)), ("iee", [], PS(9)), ("mediation", [], PS(16)), ("state_complaint", [], PS(18)),
    ("dp_complaint", [], PS(22)), ("dp_hearing", [], PS(22)), ("resolution", [], PS(25)),
    ("stay_put", [], PS(28)), ("ferpa", [], PS(13)), ("ed_records", [], PS(13)), ("pii", [], PS(13)),
    ("surrogate", [], PS(9)), ("ward", [], PS(9)), ("native_language", [], PS(7)),
    ("safeguards_notice", [], PS(3)), ("s504", [], PS(3)), ("ada", [], PS(7)), ("idea", [], PS(3)),
    ("lea", [], PS(3)), ("sea", [], PS(48)), ("public_agency", [], PS(3)), ("special_ed", [], PS(3)),
    ("related", [], PS(49)), ("pti", [], PS(15)), ("iaes", [], PS(33)), ("mdr", [], PS(32)),
    ("fba", [], PS(6)), ("bip", [], PS(32)), ("code_conduct", [], PS(32)), ("cop", [], PS(32)),
    ("exp_hearing", [], PS(33)), ("foster", [], PS(3)), ("homeless", [], PS(9)), ("uhy", [], PS(9)),
    ("gal", [], PS(9)), ("evaluation", [], PS(7)), ("reeval", [], PS(6)), ("iep_team", [], PS(6)),
    ("cwd", [], PS(3)), ("sbi", [], PS(33)), ("controlled", [], PS(33)),
    ("iep_facil", [("Special Education Facilitation", S, CO)], PS(50)),
    ("sped_admin", [], PS(3)),
    ("lep", [("multilingual learner", S, None)], PS(7)),
    ("autism", [], PS(8)), ("hi", [], PS(8)), ("ed", [], PS(8)), ("id", [], PS(8)), ("md", [], PS(8)),
    ("oi", [], PS(8)), ("ohi", [], PS(8)), ("sld", [], PS(8)), ("sli", [], PS(8)), ("tbi", [], PS(8)),
    ("vi", [], PS(8)), ("deafblind", [], PS(8)), ("dd", [], PS(8)),
    # IEP Procedural Guidance (rev. July 2017)
    ("iep", [], G(10)), ("mdt", [], G(10)), ("referral", [], G(11)), ("evaluation", [], G(16)),
    ("pwn", [], G(17)), ("consent", [], G(17)), ("eligibility", [], G(23)), ("eval_report", [], G(22)),
    ("iep_team", [], G(26)), ("transition", [], G(40)), ("postsecondary", [], G(40)),
    ("course_study", [], G(40)), ("trans_assess", [], G(40)), ("sop", [("Summary of Performance", S, None)], G(41)),
    ("sto", [], G(44)), ("alt_assess", [], G(44)), ("self_det", [], G(44)),
    ("annual_review", [], G(51)), ("progress", [], G(51)), ("amendment", [], G(52)),
    ("part_c_transition", [], G(52)), ("esy", [], G(55)), ("residential", [], G(57)),
    ("services_plan", [], G(56)), ("head_start", [], G(49)), ("braille", [], G(39)),
    ("fba", [], G(65)), ("comm_mode", [], G(65)), ("lep", [], G(66)), ("at_device", [], G(66)),
    ("at_service", [], G(66)), ("cert_completion", [], G(68)), ("std_diploma", [], G(42)),
    ("ecse", [], G(149)), ("child_find", [], G(153)),
    ("continuum", [], G(153)), ("home_instr", [], G(153)), ("hospital_instr", [], G(153)),
    ("dp_hearing", [], G(153)), ("surrogate", [], G(154)),
    ("lre", [], G(154)), ("coteach", [], G(154)), ("plaafp", [], G(156)), ("annual_goals", [], G(152)),
    ("test_accom", [], G(152)), ("bip", [], G(152)), ("mdr", [], G(155)), ("mediation", [], G(155)),
    ("program_mods", [], G(155)), ("pbis", [], G(156)), ("resource_room", [], G(157)),
    ("sdi", [], G(157)), ("sped_admin", [], G(157)), ("saas", [], G(158)), ("state_complaint", [], G(158)),
]

CONCEPTS = [
    # state agencies, offices and the administrative-unit family
    ("co_cde", "Colorado Department of Education", "legal_procedural", [("CDE", A, CO)], R("2.49, 2.20(1)"),
     {**COJ, "broader": "sea", "note": "The state educational agency; the rules also call it the Department."}),
    ("co_essu", "Exceptional Student Services Unit", "legal_procedural", [("ESSU", A, CO)], PS(5),
     {**COJ, "broader": "co_cde", "note": "The CDE office that oversees special education and handles disputes."}),
    ("co_board", "Colorado State Board of Education", "legal_procedural", [], R("2.47"),
     {**COJ, "note": "The elected board that adopts the ECEA rules; the rules call it the State Board."}),
    ("co_ofs", "Office of Facility Schools", "legal_procedural", [], R("2.20(1)"),
     {**COJ, "broader": "co_cde", "note": "The CDE office that authorizes approved facility schools."}),
    ("co_ecea", "Exceptional Children's Educational Act", "legal_procedural", [("ECEA", A, CO)], R("1.00"),
     {**COJ, "note": "Colorado's special education statute, implemented by 1 CCR 301-8."}),
    ("co_cdec", "Department of Early Childhood", "legal_procedural",
     [("CDEC", A, CO)], R("2.14(1)"),
     {**COJ, "note": "The state department that runs the universal preschool program."}),
    ("co_lco", "Local Coordinating Organization", "legal_procedural", [("LCO", A, CO)], R("2.14(2)"), COJ),
    ("co_upk", "Universal Preschool Program", "early_intervention", [], R("2.14(4)"),
     {**COJ, "note": "The state preschool program whose providers must follow child find and special education rules."}),
    ("co_au", "Administrative unit", "legal_procedural", [("AU", A, CO)], R("2.03"),
     {**COJ, "broader": "lea",
      "note": "The Colorado entity responsible for local special education: a district, BOCES or similar."}),
    ("co_aur", "Administrative unit of residence", "legal_procedural", [("AUR", A, CO)], R("2.03(1)"),
     {**COJ, "broader": "co_au"}),
    ("co_aua", "Administrative unit of attendance", "legal_procedural", [("AUA", A, CO)], R("2.03(2)"),
     {**COJ, "broader": "co_au"}),
    ("co_alt_au", "Alternative administrative unit", "legal_procedural", [], R("2.03(3)"),
     {**COJ, "broader": "co_au"}),
    ("co_multi_au", "Multi-district administrative unit", "legal_procedural", [], R("2.03(4)"),
     {**COJ, "broader": "co_au"}),
    ("co_boces", "Board of Cooperative Services", "legal_procedural",
     [("BOCES", A, CO)], R("2.06, 3.01(3)(a)(ii)"),
     {**COJ, "broader": "co_au", "note": "A regional unit that provides special education for several small districts."}),
    ("co_csi", "State Charter School Institute", "legal_procedural",
     [("Charter School Institute", S, CO)], R("2.48"),
     {**COJ, "broader": "co_au", "note": "A state charter authorizer that can act as an administrative unit."}),
    ("co_charter_network", "Charter school network", "placement_setting", [], R("2.07(5)"),
     {**COJ, "broader": "charter_school"}),
    ("co_charter_collab", "Charter school collaborative", "placement_setting", [], R("2.07(4)"),
     {**COJ, "broader": "charter_school"}),
    ("co_approved_facility", "Approved facility school", "placement_setting",
     [("Approved Facility Schools", P, CO)], R("2.20(1), 3.02(1)"),
     {**COJ, "note": "A school program in a day treatment center, hospital or similar facility that the state has approved."}),
    ("co_online_school", "Multidistrict online school", "placement_setting", [], R("9.01(4)"), COJ),
    ("co_sop_csdb", "Colorado School for the Deaf and the Blind", "placement_setting", [], R("2.50(1)"),
     {**COJ, "broader": "state_ops", "note": "A state-operated program supervised by CDE."}),
    # dispute resolution and advocacy
    ("co_sco", "State Complaints Officer", "personnel_role", [("SCO", A, CO)], PS(17),
     {**COJ, "note": "The CDE staff member who investigates and decides state complaints."}),
    ("co_oac", "Office of Administrative Courts", "legal_procedural", [("OAC", A, CO)], PS(22),
     {**COJ, "note": "Assigns the administrative law judge for a due process complaint."}),
    ("co_dpar", "Dispute Prevention and Assisted Resolution Supervisor", "personnel_role", [], PS(51),
     {**COJ, "note": "The CDE contact for mediation and IEP facilitation."}),
    ("co_ppra", "Protection of Persons from Restraint Act", "legal_procedural",
     [("PPRA", A, CO), ("Protection of Individuals from Restraint and Seclusion Act", S, CO)], PS(18),
     {**COJ, "note": "The state law on restraint and seclusion that CDE can investigate through a state complaint."}),
    ("co_tjp", "Transformative Justice Project", "legal_procedural", [], PS(22),
     {**COJ, "note": "Provides an attorney to a parent in some due process hearings."}),
    ("co_peak", "PEAK Parent Center", "legal_procedural", [], PS(15),
     {**COJ, "broader": "pti", "note": "One of Colorado's federally funded parent training and information centers."}),
    ("co_show_tell", "Show and Tell Corporation", "legal_procedural", [], PS(15),
     {**COJ, "broader": "pti", "note": "A parent-led Colorado parent training and information center."}),
    ("co_thrive", "THRIVE Center", "legal_procedural", [("Denver Metro Community Parent Resource Center", L, CO)], PS(15),
     {**COJ, "broader": "pti", "flags": ["place_name"], "note": "The center's former name includes a city."}),
    ("co_dlc", "Disability Law Colorado", "legal_procedural", [], PS(15),
     {**COJ, "note": "Colorado's designated protection and advocacy system."}),
    ("co_arc", "The Arc of Colorado", "legal_procedural", [], PS(37), COJ),
    ("ocr", "Office for Civil Rights", "legal_procedural", [("OCR", A, None)], PS(37),
     {"note": "The U.S. Department of Education office that handles Section 504 complaints."}),
    ("s504_coord", "504 Coordinator", "section_504", [], PS(3),
     {"broader": "s504"}),
    ("counsel_youth", "Counsel for Youth", "personnel_role", [], PS(9),
     {"note": "A person a court may appoint to make a child's educational decisions."}),
    # IEP content, forms and procedures
    ("co_comm_plan", "Communication Plan", "iep_component", [], R("4.03(6)(a)"),
     {**COJ, "note": "A plan the IEP must include for a child with a hearing disability."}),
    ("co_lmp", "Learning Media Plan", "iep_component", [], R("4.03(6)(b)"),
     {**COJ, "note": "A plan the IEP must include for a child with a vision disability."}),
    ("co_literacy_mode", "Literacy mode", "iep_component", [], R("2.31"),
     {**COJ, "note": "One of four ways a child who is blind achieves literacy: auditory, Braille, print enlargement or regular print."}),
    ("co_abbrev_day", "Abbreviated school day", "legal_procedural", [("Abbreviated School Days", P, CO)], R("2.01"),
     {**COJ, "note": "A school day with fewer instructional hours than most same-grade peers."}),
    ("co_abbrev_sched", "Abbreviated school day schedule", "iep_component", [],
     R("2.01(1)"), {**COJ, "broader": "co_abbrev_day"}),
    ("co_child_find_coord", "Child find coordinator", "personnel_role", [], R("4.02(2)(b)"),
     {**COJ, "note": "The person each administrative unit designates to run child identification."}),
    ("co_building_referral", "Building level referral", "evaluation_eligibility", [], R("4.02(3)"),
     {**COJ, "note": "A general education referral that is distinct from a special education referral."}),
    ("co_nonsig_change", "Nonsignificant change in program/services", "iep_component", [], R("4.03(8)(b)(i)"),
     {**COJ, "note": "A change such as the amount of a service; it needs prior written notice but not consent."}),
    ("co_sig_change", "Significant change in placement", "iep_component", [], R("4.03(8)(b)(ii)"),
     {**COJ, "note": "A change that requires reevaluation, such as adding or ending a service."}),
    ("co_comp_plan", "Comprehensive Plan", "legal_procedural", [], R("8.01(1)(a)"),
     {**COJ, "note": "The plan each administrative unit adopts for its special education program."}),
    ("co_seta", "Special Education Temporary Authorization", "personnel_role",
     [("SETA", A, CO), ("Temporary Educator Eligibility", L, CO), ("TEE", L, CO)], R("3.04(3)"),
     {**COJ, "note": "A temporary authorization for staff who provide special education."}),
    ("co_eipa", "Educational Interpreter Performance Assessment", "instrument", [("EIPA", A, None)], R("3.04(1)(f)"),
     {"note": "The assessment Colorado requires of educational interpreters."}),
    ("co_state_iep", "State Recommended IEP", "iep_component", [], G(4),
     {**COJ, "broader": "model_iep", "note": "The model IEP forms CDE recommends."}),
    ("co_service_delivery", "Service Delivery Statement", "iep_component", [], G(75),
     {**COJ, "note": "The IEP section that explains the services table to parents."}),
    ("co_rec_placement", "Recommended Placement in the Least Restrictive Environment", "iep_component", [], G(76), COJ),
    ("co_special_factors", "Consideration of Special Factors", "iep_component", [], G(65), COJ),
    ("co_ps_plan", "Postsecondary Transition Plan", "transition", [], G(68), {**COJ, "broader": "transition"}),
    ("co_invite_agencies", "Consent to Invite Agencies Related to Transition", "transition",
     [], G(41),
     {**COJ, "note": "The form a parent signs before an adult agency is invited to an IEP meeting."}),
    ("notice_meeting", "Notice of Meeting", "legal_procedural", [], G(11), {}),
    ("co_eeo", "Extended Evidence Outcomes", "academic_skill", [("EEOs", P, CO), ("EEO", A, CO)], G(44),
     {**COJ, "broader": "alt_assess", "note": "Alternate achievement standards for students with significant cognitive disabilities."}),
    ("co_cas", "Colorado Academic Standards", "academic_skill", [], G(43), COJ),
    ("co_eic", "Early Intervention Colorado", "early_intervention", [], G(52),
     {**COJ, "broader": "part_c_transition", "note": "Colorado's Part C early intervention program."}),
    ("co_eldg", "Early Learning and Development Guidelines", "early_intervention", [("ELDGs", A, CO)], G(150), COJ),
    ("co_insurance_model", "Insurance model", "legal_procedural", [], G(56),
     {**COJ, "note": "A charter school pays the administrative unit to provide all special education."}),
    ("co_contracted_model", "Contracted model", "legal_procedural", [], G(56),
     {**COJ, "note": "A charter school receives its funding share and contracts for its own services."}),
    ("co_combo_model", "Combination/modified insurance model", "legal_procedural", [], G(56), COJ),
    # gifted education (Rule 12.00)
    ("co_alp", "Advanced Learning Plan", "iep_component", [("ALP", A, CO), ("ALPs", P, CO)], R("12.01(2)"),
     {**COJ, "note": "The written plan for a gifted student."}),
    ("co_early_access", "Early Access", "legal_procedural", [], R("12.01(12)"),
     {**COJ, "flags": ["common_english_word"], "note": "Early entrance to kindergarten or first grade for a highly advanced gifted child."}),
]

JURISDICTION = "US-CO"
LAYER_NAME = "Colorado"
# Documents listed in sources/documents.tsv that no record cites, and why.
UNCITED_DOCS = {"co-parentfaq-2026": "Saved web page of links; read for orientation, cites nothing."}

RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.39.0"  # tools/add_state.py sets this
