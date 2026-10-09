"""
New Mexico layer for SPEDLex.

Sources reviewed 2026-10-09 (listed in sources/documents.tsv; local copies in .sources-cache/nm/):
  RULE   6.31.2 NMAC, Children with Disabilities (Public Education
         Department; effective 7/14/2020, amended 7/31/2023), the State
         Records Center and Archives PDF (40 pp.). Cited by section and
         paragraph plus page, e.g. "6.31.2.7(B)(18) NMAC, p. 3".
  PSN    New Mexico Public Education Department, Special Education Division,
         Special Education Procedural Safeguards for Students with
         Disabilities and Their Families Required Under IDEA Part B (revised
         December 2020, 35 pp.), listed by the PED as "Parent and Child
         Rights Procedural Safeguard Notice - December 2020". Cited by PDF
         page; the printed page number is one lower (the cover is unnumbered).
  GUIDE  NMPED Special Education Bureau, Developing Quality IEPs (revised
         October 2011, 127 pp.), the department's IEP technical assistance
         manual. Cited by PDF page; the printed "Page N" is five lower.
  GRAD   NMPED, High School Graduation Requirements Guidance (April 2025,
         47 pp.; posted 08/2026). Optional diploma document. Cited by PDF page.

All four were read as text extracted with pdftotext. GUIDE PDF pages 2-3
and 72-83 have no text layer (blank or image-only form pages) and were not
read. GRAD's course-catalog appendices (PDF pages 27-47) were searched for
special-education wording rather than read line by line. The NM TEAM manual
(NM-TEAM-2026.pdf, 496 pp.) was downloaded but not read, so none of its
terms are here. The PDFs were saved through the browser from the PED and
State Records Center sites; no document was summarized by a fetch tool.
RULE records are 'machine_validated'; PSN, GUIDE and GRAD records are
'candidate'.

GUIDE dates from 2011. It still uses the former Special Education Bureau
name, the three graduation options (Standard, Career Readiness, Ability),
the New Mexico Alternate Assessment and the New Mexico Graduation Exam.
They are kept because they appear in older family records.

Left out on purpose: the Puente para los ninos fund and other funding terms
(qualified student, school-age person, program units, annual determinations,
needs intervention); the New Mexico Legal Aid Society and Pegasus Legal
Services for Children (legal aid providers, as in other layers); the
Children's Court; course codes and course names in GRAD's appendices; the
SAT School Day, PSAT, WorkKeys and other College Board or ACT products;
"consent override"; the GUIDE profile domains (Recreation & Leisure,
Community Participation, Jobs & Job Training); the teacher notice and
contact-log forms; "FVE/LMA", whose expansion the documents do not give;
"IFSP-IEP"; "Office of Special Education" (the current name of the PED
division in GRAD), because that string already belongs to a New York
concept; and "Special Education Division" alone, which belongs to a
California concept (New Mexico's division is recorded under its fuller name).
"""

RULE_URL = "https://www.srca.nm.gov/parts/title06/06.031.0002.pdf"
PSN_URL = "https://web.ped.nm.gov/wp-content/uploads/2025/01/Eng-Procedural-Safeguards-12-23-2020.pdf"
GUIDE_URL = "https://web.ped.nm.gov/wp-content/uploads/2025/01/Developing-Quality-IEPs.pdf"
GRAD_URL = "https://web.ped.nm.gov/wp-content/uploads/2026/08/High-School-Graduation-Requirements-Guidance.pdf"


def src(doc, loc, page=None):
    """RULE loc is a section and paragraph with its page; other loc is a PDF page."""
    if doc == "RULE":
        return {"source_type": "state_regulation",
                "citation": f"6.31.2 NMAC, Children with Disabilities (as amended 7/31/2023), {loc}, p. {page}",
                "doc_id": "nm-nmac6312-2023", "url": RULE_URL}
    if doc == "PSN":
        return {"source_type": "procedural_safeguards_notice",
                "citation": f"NMPED Special Education Procedural Safeguards Notice (rev. December 2020), PDF p. {loc}",
                "doc_id": "nm-psn-2020", "url": PSN_URL}
    if doc == "GUIDE":
        return {"source_type": "state_guidance",
                "citation": f"NMPED, Developing Quality IEPs (rev. October 2011), PDF p. {loc}",
                "doc_id": "nm-iepguide-2011", "url": GUIDE_URL}
    return {"source_type": "state_guidance",
            "citation": f"NMPED, High School Graduation Requirements Guidance (April 2025), PDF p. {loc}",
            "doc_id": "nm-grad-2025", "url": GRAD_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
NM = ["US-NM"]
NMJ = {"jurisdiction": "US-NM"}
R = lambda loc, page: src("RULE", loc, page)
PS = lambda page: src("PSN", page)
G = lambda page: src("GUIDE", page)
GR = lambda page: src("GRAD", page)

STRINGS = [
    # 6.31.2.7 definitions
    ("cwd", [], R("6.31.2.7(B)(2)", 1)), ("dd", [], R("6.31.2.7(B)(3)", 2)),
    ("psw", [], R("6.31.2.7(B)(4)(b)", 2)), ("dyslexia", [], R("6.31.2.7(B)(5)", 2)),
    ("fape", [], R("6.31.2.7(B)(7)", 2)), ("gen_curr", [], R("6.31.2.7(B)(8)", 2)),
    ("lea", [], R("6.31.2.7(B)(9)", 2)), ("iep", [], R("6.31.2.7(B)(10)", 2)),
    ("iep_team", [], R("6.31.2.7(B)(11)", 2)), ("gen_teacher", [], R("6.31.2.7(B)(11)(b)", 2)),
    ("sped_teacher", [], R("6.31.2.7(B)(11)(c)", 2)), ("lea_rep", [], R("6.31.2.7(B)(11)(d)", 3)),
    ("eval_interp", [], R("6.31.2.7(B)(11)(e)", 3)), ("idea", [], R("6.31.2.7(B)(12)", 3)),
    ("foster", [], R("6.31.2.7(B)(15)", 3)), ("surrogate", [], R("6.31.2.7(B)(15)", 3)),
    ("public_agency", [], R("6.31.2.7(B)(16)", 3)), ("esa", [], R("6.31.2.7(B)(16)", 3)),
    ("charter_school", [], R("6.31.2.7(B)(16)", 3)),
    ("sst", [("SAT", A, NM)], R("6.31.2.7(B)(18)", 3)),
    ("special_ed", [], R("6.31.2.7(B)(20)", 3)), ("slp", [], R("6.31.2.7(B)(20)(a)", 3)),
    ("screening", [], R("6.31.2.7(B)(20)(b)(i)", 3)), ("fluency_dis", [], R("6.31.2.7(B)(20)(b)(ii)", 3)),
    ("lang_dis", [], R("6.31.2.7(B)(20)(b)(ii)", 3)), ("adverse", [], R("6.31.2.7(B)(20)(b)(ii)", 3)),
    ("iep_facil", [("FIEP meeting", V, NM)], R("6.31.2.7(C)(1)", 4)),
    ("mediation", [], R("6.31.2.7(C)(2)", 4)), ("exp_hearing", [], R("6.31.2.7(D)(1)", 4)),
    # 6.31.2.9 public agency responsibilities
    ("child_count", [], R("6.31.2.9(B)(2)", 5)), ("residential", [], R("6.31.2.9(B)(3)", 5)),
    ("resident_dist", [], R("6.31.2.9(B)(3)(a)", 5)), ("public_benefits_consent", [], R("6.31.2.9(B)(6)", 6)),
    ("para", [], R("6.31.2.9(B)(9)(a)", 7)), ("ceis", [], R("6.31.2.9(D)", 8)),
    ("disprop", [], R("6.31.2.9(E)", 8)), ("cceis", [], R("6.31.2.9(E)(3)(b)", 8)),
    ("spp", [], R("6.31.2.9(F)", 9)),
    # 6.31.2.10 identification, evaluation and eligibility
    ("child_find", [], R("6.31.2.10(A)", 9)),
    ("mtss", [("multi-layered system of supports", S, NM)], R("6.31.2.10(B)", 9)),
    ("evaluation", [], R("6.31.2.10(B)(2)", 10)), ("suspected", [], R("6.31.2.10(B)(3)", 10)),
    ("referral", [], R("6.31.2.10(B)(3)", 10)), ("reeval", [], R("6.31.2.10(C)(2)", 10)),
    ("sop", [], R("6.31.2.10(C)(3)(b)", 10)), ("std_diploma", [], R("6.31.2.10(C)(3)(b)", 10)),
    ("pwn", [], R("6.31.2.10(D)(4)(a)", 11)), ("safeguards_notice", [], R("6.31.2.10(D)(4)(a)", 11)),
    ("state_complaint", [], R("6.31.2.10(D)(6)", 11)), ("dp_hearing", [], R("6.31.2.10(D)(6)", 11)),
    ("consent", [], R("6.31.2.10(E)(2)", 11)), ("eval_report", [], R("6.31.2.10(F)(2)", 11)),
    ("al_edt", [], R("6.31.2.10(F)(1)", 11)),
    ("native_language", [], R("6.31.2.10(H)(1)", 12)), ("asl", [], R("6.31.2.10(H)(1)", 12)),
    ("lep", [], R("6.31.2.10(H)(2)", 12)), ("exclusionary", [], R("6.31.2.10(H)(2)", 12)),
    ("iee", [], R("6.31.2.10(I)", 12)), ("dp_complaint", [], R("6.31.2.10(I)(2)(a)", 12)),
    ("sld", [], R("6.31.2.10(K)", 13)), ("data_doc", [], R("6.31.2.10(K)(1)(b)(ii)", 13)),
    ("rti", [], R("6.31.2.10(K)(1)(c)(iv)", 13)), ("srbi", [], R("6.31.2.10(K)(1)(c)(iv)", 13)),
    # 6.31.2.11 educational services
    ("preschool_swd", [], R("6.31.2.11(A)(1)", 14)),
    ("ifsp", [("individual family services plan", V, NM)], R("6.31.2.11(A)(1)", 14)),
    ("part_c_transition", [], R("6.31.2.11(A)(3)", 14)), ("reed", [], R("6.31.2.11(A)(3)(c)", 14)),
    ("service_coord", [], R("6.31.2.11(A)(5)(g)(i)", 15)),
    ("annual_review", [], R("6.31.2.11(B)(3)", 16)), ("amendment", [], R("6.31.2.11(B)(4)", 16)),
    ("autism", [], R("6.31.2.11(B)(5)", 16)), ("ext_ed_prog", [], R("6.31.2.11(B)(5)(a)", 16)),
    ("esy", [], R("6.31.2.11(B)(5)(a)", 16)), ("daily_sched", [], R("6.31.2.11(B)(5)(b)", 16)),
    ("in_home_cbt", [], R("6.31.2.11(B)(5)(c)", 16)), ("bip", [], R("6.31.2.11(B)(5)(d)(ii)", 16)),
    ("fba", [], R("6.31.2.11(B)(5)(d)(ii)", 16)), ("futures", [], R("6.31.2.11(B)(5)(e)", 16)),
    ("staff_ratio", [("staff-to-student ratio", V, NM)], R("6.31.2.11(B)(5)(g)", 16)),
    ("adaptive", [], R("6.31.2.11(B)(5)(g)(i)", 16)), ("social_skills", [], R("6.31.2.11(B)(5)(i)", 16)),
    ("aba", [], R("6.31.2.11(B)(5)(k)", 17)),
    ("lre", [], R("6.31.2.11(C)", 17)), ("continuum", [], R("6.31.2.11(C)(2)(b)", 17)),
    ("saas", [], R("6.31.2.11(C)(2)(e)", 17)), ("program_mods", [], R("6.31.2.11(C)(2)(e)", 17)),
    ("prr", [], R("6.31.2.11(C)(2)(e)", 17)), ("removal_expl", [], R("6.31.2.11(C)(2)(g)", 17)),
    ("sig_cog", [], R("6.31.2.11(D)(2)", 18)),
    ("ccss", [("Common Core Standards", V, NM)], R("6.31.2.11(D)(2)(a)", 18)),
    ("statewide_assess", [], R("6.31.2.11(E)", 18)), ("test_accom", [], R("6.31.2.11(E)(2)", 18)),
    ("alt_assess", [], R("6.31.2.11(E)(3)", 18)), ("pbis", [], R("6.31.2.11(F)(1)", 18)),
    ("cop", [], R("6.31.2.11(F)(2)", 18)), ("expulsion", [], R("6.31.2.11(F)(2)", 18)),
    ("graduation_plan", [], R("6.31.2.11(G)(1)", 19)), ("course_study", [], R("6.31.2.11(G)(1)(a)", 19)),
    ("transition", [], R("6.31.2.11(G)(2)", 19)), ("voc_ed", [], R("6.31.2.11(G)(2)(b)", 19)),
    ("supported_employment", [], R("6.31.2.11(G)(2)(b)", 19)), ("prefs", [], R("6.31.2.11(G)(2)(c)", 19)),
    ("comm_exp", [], R("6.31.2.11(G)(2)(c)(iii)", 19)), ("post_school", [], R("6.31.2.11(G)(2)(c)(iv)", 19)),
    ("daily_living", [], R("6.31.2.11(G)(2)(c)(v)", 19)), ("fve", [], R("6.31.2.11(G)(2)(c)(v)", 19)),
    ("postsecondary", [], R("6.31.2.11(G)(3)(a)", 19)), ("trans_assess", [], R("6.31.2.11(G)(3)(a)", 19)),
    ("age_majority", [], R("6.31.2.11(G)(3)(c)", 19)), ("comparable", [], R("6.31.2.11(H)(1)", 20)),
    ("special_school", [], R("6.31.2.11(K)(1)", 21)), ("audiological_assess", [], R("6.31.2.11(K)(2)", 21)),
    ("regular_class", [], R("6.31.2.11(K)(4)(c)", 22)), ("special_class", [], R("6.31.2.11(K)(4)(c)", 22)),
    ("home_instr", [], R("6.31.2.11(K)(4)(c)", 22)), ("hospital_instr", [], R("6.31.2.11(K)(4)(c)", 22)),
    ("resource_room", [], R("6.31.2.11(K)(4)(c)", 22)), ("itinerant", [], R("6.31.2.11(K)(4)(c)", 22)),
    ("ecc", [], R("6.31.2.11(L)(1)", 22)), ("ward", [], R("6.31.2.11(M)(7)", 24)),
    ("ppps", [], R("6.31.2.11(N)(1)(a)", 24)), ("services_plan", [], R("6.31.2.11(N)(1)(d)", 24)),
    ("unilateral_pl", [], R("6.31.2.11(N)(5)", 25)),
    # 6.31.2.13 additional rights
    ("ed_records", [], R("6.31.2.13(B)", 25)), ("notice_meeting", [], R("6.31.2.13(D)(1)", 26)),
    ("revoke", [], R("6.31.2.13(F)(6)", 27)),
    ("state_complaint", [("state-level complaint", S, NM)], R("6.31.2.13(G)(2)(c)(i)", 27)),
    ("resolution", [], R("6.31.2.13(G)(2)(c)(ii)", 27)), ("adr", [], R("6.31.2.13(H)(3)(a)", 28)),
    ("mdr", [], R("6.31.2.13(I)(3)(a)", 30)),
    ("state_panel", [("state IDEA advisory panel", S, NM)], R("6.31.2.13(I)(6)(f)", 32)),
    ("civil_action", [], R("6.31.2.13(I)(23)", 36)), ("attorneys_fees", [], R("6.31.2.13(I)(24)", 36)),
    ("stay_put", [], R("6.31.2.13(I)(25)", 36)), ("ferpa", [], R("6.31.2.13(L)(1)", 37)),
    ("pii", [], R("6.31.2.13(L)(1)", 37)), ("destruction_pii", [], R("6.31.2.13(L)(5)", 38)),
    ("progress", [], R("6.31.2.13(L)(6)(b)(ii)", 39)),

    # Procedural safeguards notice
    ("safeguards_notice", [], PS(1)), ("al_edt", [], PS(2)), ("s504", [], PS(2)), ("ada", [], PS(2)),
    ("s504_coord", [("Section 504 coordinator", V, None)], PS(2)),
    ("pwn", [], PS(3)), ("consent", [], PS(3)), ("revoke", [], PS(3)), ("iee", [], PS(3)),
    ("code_conduct", [], PS(4)), ("mdr", [], PS(4)), ("sped_admin", [], PS(4)), ("ed_records", [], PS(4)),
    ("native_language", [], PS(6)), ("comm_mode", [], PS(6)), ("lep", [], PS(6)), ("braille", [], PS(6)),
    ("ward", [], PS(7)), ("foster", [], PS(7)), ("surrogate", [], PS(7)), ("homeless", [], PS(7)),
    ("public_benefits_consent", [], PS(9)),
    ("equitable", [], PS(10)), ("ppps", [], PS(10)), ("age_majority", [], PS(10)),
    ("emancipated", [], PS(10)), ("sdm", [], PS(10)),
    ("rti", [], PS(11)), ("mtss", [("MLSS", A, NM)], PS(11)), ("sst", [], PS(11)),
    ("iep_team", [], PS(13)), ("annual_goals", [], PS(13)), ("gen_teacher", [], PS(13)),
    ("sped_teacher", [], PS(13)), ("para", [], PS(13)),
    ("postsecondary", [], PS(14)), ("transition", [], PS(14)), ("case_by_case", [], PS(14)),
    ("iaes", [], PS(14)), ("gen_curr", [], PS(15)), ("fba", [], PS(15)),
    ("bip", [], PS(16)), ("special_circ", [], PS(16)), ("weapon", [], PS(16)), ("controlled", [], PS(16)),
    ("illegal_drug", [], PS(16)), ("sbi", [], PS(16)), ("cop", [], PS(16)),
    ("exp_hearing", [], PS(17)), ("resolution", [], PS(17)), ("dp_complaint", [], PS(17)),
    ("dp_hearing", [], PS(17)), ("basis_know", [], PS(18)), ("unilateral_pl", [], PS(19)),
    ("ferpa", [], PS(19)), ("iep_facil", [], PS(20)), ("mediation", [], PS(20)),
    ("state_complaint", [], PS(20)), ("adr", [], PS(21)), ("pti", [], PS(23)), ("cil", [], PS(23)),
    ("stay_put", [], PS(26)), ("agreement_review_period", [], PS(27)),
    ("state_panel", [("New Mexico IDEA Advisory Panel", S, NM)], PS(29)), ("civil_action", [], PS(29)),
    ("attorneys_fees", [], PS(30)), ("destruction_pii", [], PS(31)), ("part_agency", [], PS(31)),
    ("pii", [], PS(31)), ("child_find", [], PS(32)), ("record_access", [], PS(33)),
    ("state_panel", [("New Mexico Individuals with Disabilities Education Act Advisory Panel", S, NM),
                     ("IDEA Panel", AB, NM)], PS(35)),

    # Developing Quality IEPs
    ("tier1", [("Tier I", V, None), ("Tier II", V, None)], G(10)), ("gifted", [], G(10)),
    ("id", [], G(11)), ("dd", [], G(11)), ("comm_mode", [], G(11)),
    ("sto", [], G(12)), ("plaafp", [], G(12)), ("progress", [], G(13)), ("reed", [], G(13)),
    ("cba", [], G(13)), ("self_det", [], G(15)), ("lea_rep", [], G(18)),
    ("safeguards_notice", [("Parent and Child Rights in Special Education", S, NM)], G(23)),
    ("vision_future", [], G(24)), ("pwn", [("Prior Written Notice of Proposed Actions", S, NM)], G(25)),
    ("primary_disability", [], G(34)), ("secondary_disability", [], G(34)),
    ("vision_future", [("Student/Family Vision", S, NM)], G(34)),
    ("co_special_factors", [], G(37)), ("at_device", [], G(38)), ("at_service", [], G(38)),
    ("osep", [], G(40)), ("course_study", [], G(44)), ("std_diploma", [], G(44)),
    ("fine_motor", [], G(48)), ("gross_motor", [], G(48)),
    ("ihp", [], G(52)), ("nursing", [], G(52)), ("pe", [], G(53)), ("transport", [], G(53)),
    ("regression", [], G(53)), ("continuum", [], G(54)), ("ar_sched_services", [], G(55)),
    ("ot", [], G(55)), ("pt", [], G(55)), ("psych", [], G(55)), ("social_work", [], G(55)),
    ("parent_training", [], G(55)), ("iq", [], G(67)), ("observation", [], G(68)),
    ("voc_eval", [], G(68)), ("init_place", [], G(84)), ("exit_sped", [], G(84)),

    # High School Graduation Requirements Guidance
    ("dlm", [], GR(17)), ("access_ell", [], GR(17)), ("ess_elements", [], GR(22)),
    ("alt_diploma", [], GR(23)),
    ("ccss", [("New Mexico Common Core State Standards", S, NM), ("NMCCSS", A, NM)], GR(28)),
]

CONCEPTS = [
    # state agencies, offices and laws
    ("nm_ped", "New Mexico Public Education Department", "legal_procedural",
     [("Public Education Department", S, NM), ("PED", A, NM), ("NMPED", A, NM)], PS(2),
     {**NMJ, "broader": "sea", "note": "The state educational agency. NMPED is the form used in Developing Quality IEPs (PDF p. 7)."}),
    ("nm_sed", "PED Special Education Division", "legal_procedural",
     [("SED", A, NM), ("Special Education Bureau", L, NM)], PS(20),
     {**NMJ, "broader": "nm_ped",
      "note": "The PED division that handles mediation, complaints and hearings. The rule calls it SED (6.31.2.7(B)(19)); the 2011 IEP manual calls it the Special Education Bureau."}),
    ("nm_cyfd", "Children, Youth and Families Department", "legal_procedural", [("CYFD", A, NM)], PS(7),
     {**NMJ, "note": "The state agency whose custody makes a child a ward of the state for IDEA purposes."}),
    ("nm_nmac", "New Mexico Administrative Code", "legal_procedural", [("NMAC", A, NM)], R("6.31.2.7(B)(13)", 3),
     {**NMJ, "note": "The compilation of New Mexico agency rules, including the special education rule."}),
    ("nm_6312", "6.31.2 NMAC", "legal_procedural", [], R("6.31.2.1", 1),
     {**NMJ, "broader": "nm_nmac", "note": "New Mexico's special education rule, Children with Disabilities."}),
    ("nm_dhh_bor", "NM Deaf/Hard of Hearing Education Bill of Rights", "legal_procedural", [], G(93),
     {**NMJ, "note": "The state law that the deaf or hard of hearing IEP addendum helps carry out."}),
    ("nm_stars", "STARS", "legal_procedural", [], G(93),
     {**NMJ, "flags": ["common_english_word"],
      "note": "The state student data reporting system named on the IEP addendum; the documents do not expand it."}),
    ("nm_dvr", "New Mexico Division of Vocational Rehabilitation", "transition", [("DVR", A, NM)], PS(31),
     {**NMJ, "broader": "vr_services",
      "note": "The state agency that may provide transition services; DVR is the form in Developing Quality IEPs (PDF p. 46)."}),
    # parent centres and advocacy organizations
    ("nm_pro", "Parents Reaching Out", "legal_procedural", [("PRO", A, NM)], PS(35),
     {**NMJ, "note": "A New Mexico parent advocacy and support group listed in the safeguards notice."}),
    ("nm_epics", "Education for Parents of Indian Children with Special Needs", "legal_procedural",
     [("EPICS", A, NM)], PS(35),
     {**NMJ, "note": "A New Mexico parent support group for families of Native American children with disabilities."}),
    ("nm_families_asap", "Families ASAP", "legal_procedural", [], PS(35),
     {**NMJ, "note": "A New Mexico parent advocacy and support group listed in the safeguards notice."}),
    ("nm_drnm", "Disability Rights New Mexico", "legal_procedural", [("DRNM", A, NM)], PS(35),
     {**NMJ, "note": "A free or low-cost legal service listed in the safeguards notice."}),
    ("nm_nadlc", "Native American Disability Law Center", "legal_procedural", [("NADLC", A, NM)], PS(35),
     {**NMJ, "note": "A free or low-cost legal service listed in the safeguards notice."}),
    ("educational_decision_maker", "Educational decision-maker", "legal_procedural",
     [("educational decision-makers", P, None), ("educational decision maker", V, None)], PS(7),
     {"broader": "surrogate",
      "note": "A person who makes IDEA decisions for a child when no parent can, such as one a court appoints for a ward of the state."}),
    # state rule concepts
    ("nm_ed_jurisdiction", "Educational jurisdiction", "legal_procedural", [], R("6.31.2.7(B)(6)", 2),
     {**NMJ, "note": "The area, ages and facilities for which a public agency must provide special education under state rules or agreements."}),
    ("nm_ssep", "State-supported educational program", "placement_setting",
     [("state-supported educational programs", P, NM)], R("6.31.2.7(B)(21)", 4),
     {**NMJ, "broader": "state_ops",
      "note": "A program run by or for a state school, institution, hospital or agency that serves children with disabilities."}),
    ("nm_nmsd", "New Mexico School for the Deaf", "placement_setting", [("NMSD", A, NM)], R("6.31.2.11(K)", 21),
     {**NMJ, "broader": "special_school", "note": "The state school for students who are deaf or hard of hearing."}),
    ("nm_nmsbvi", "New Mexico School for the Blind and Visually Impaired", "placement_setting",
     [("NMSBVI", A, NM)], R("6.31.2.11(L)", 22),
     {**NMJ, "broader": "special_school", "note": "The state school for students who are blind or visually impaired."}),
    ("dual_discrepancy", "Dual discrepancy", "evaluation_eligibility",
     [("dual discrepancy model", S, None)], R("6.31.2.7(B)(4)", 2),
     {"broader": "sld",
      "note": "Low achievement plus either too little progress or a pattern of strengths and weaknesses; New Mexico requires it for identifying learning disabilities."}),
    ("nm_team", "New Mexico Technical Evaluation and Assessment Manual", "evaluation_eligibility",
     [("New Mexico T.E.A.M.", V, NM), ("NM TEAM", AB, NM)], R("6.31.2.10(G)(1)", 11),
     {**NMJ, "note": "The state manual that sets evaluation and eligibility standards for each disability category."}),
    ("nm_sfe", "New Mexico Standards for Excellence", "academic_skill",
     [("New Mexico Standards of Excellence", V, NM)], R("6.31.2.7(B)(4)", 2),
     {**NMJ, "note": "The state's content standards and graduation requirements in Chapter 29 of Title 6 NMAC."}),
    ("nm_eps", "Expanded performance standards", "academic_skill", [], R("6.31.2.11(D)(2)", 18),
     {**NMJ, "note": "The standards that IEP academic goals align to for students with significant cognitive disabilities."}),
    # IEP components and forms
    ("nm_student_profile", "Student profile", "iep_component", [], G(34),
     {**NMJ, "note": "The opening section of the state-recommended IEP that summarizes strengths, needs and concerns."}),
    ("nm_level_service", "Level of service", "iep_component", [], G(58),
     {**NMJ, "note": "The IEP entry recording the hours of special education a student receives, used for state funding."}),
    ("nm_continuing_iep", "Continuing or transition IEP", "iep_component",
     [("continuing or transitioning IEP", V, NM)], G(45),
     {**NMJ, "note": "The IEP a student keeps after the conditional certificate of transition, until a diploma or age 22."}),
    ("nm_comm_considerations", "Addendum for Students who are Deaf or Hard of Hearing", "iep_component",
     [("Communication Considerations Form", S, NM), ("Communication Considerations", AB, NM)], G(93),
     {**NMJ, "broader": "comm_mode",
      "note": "A required IEP addendum on language and communication needs for any student who is deaf or hard of hearing."}),
    ("nm_esy_addendum", "Addendum for Determining Eligibility for Extended School Year Services", "iep_component",
     [], G(53), {**NMJ, "broader": "esy", "note": "The IEP addendum that documents the team's extended school year decision."}),
    ("nm_nmaa", "New Mexico Alternate Assessment", "iep_component", [], G(54),
     {**NMJ, "broader": "alt_assess",
      "note": "The state alternate assessment named in the 2011 manual; the 2025 guidance names Dynamic Learning Maps instead."}),
    ("nm_aa_addendum", "Addendum for Determining Eligibility for the New Mexico Alternate Assessment", "iep_component",
     [("Alternate Assessment Addendum", S, NM)], G(54),
     {**NMJ, "broader": "nm_nmaa",
      "note": "The IEP addendum used to decide whether a student takes the alternate assessment. The 2025 graduation guidance calls it the Alternate Assessment Addendum (PDF p. 21)."}),
    ("nm_prq", "Parent Report Questionnaire", "iep_component", [], G(24),
     {**NMJ, "note": "An optional state form for parents' input before an IEP meeting."}),
    ("nm_consent_form", "Parent Consent Form for Educational Evaluation", "legal_procedural",
     [("Parent Consent for Educational Evaluation", V, NM)], G(20),
     {**NMJ, "broader": "consent", "note": "The state-recommended form for parental consent to an evaluation."}),
    ("nm_pwn_meeting", "Prior Written Notice of IEP Meeting", "legal_procedural",
     [("Prior Written Notice of Meeting", V, NM)], G(23),
     {**NMJ, "broader": "notice_meeting", "note": "The state-recommended form that invites parents to an IEP meeting."}),
    ("nm_elig_form", "Determination of Eligibility for Special Education Services", "evaluation_eligibility", [], G(21),
     {**NMJ, "broader": "eligibility", "note": "The state-recommended form that records the team's eligibility decision."}),
    ("nm_sld_form", "Determining the Existence of a Specific Learning Disability", "evaluation_eligibility", [], G(21),
     {**NMJ, "broader": "sld", "note": "The state-recommended form completed when a student is found eligible with a learning disability."}),
    ("nm_student_bor", "Student Bill of Rights", "transition", [], G(125),
     {**NMJ, "note": "A state handout listing the rights and responsibilities of high school students in special education."}),
    # transition and graduation
    ("nm_lifespan", "Life Span Transition Planning", "transition", [], G(47),
     {**NMJ, "note": "New Mexico's transition planning for preschool and elementary students."}),
    ("nm_nsp", "Next-Step Plan", "transition", [("Next-Step Plans", P, NM), ("NSP", A, NM)], GR(14),
     {**NMJ, "note": "The yearly post-high-school plan every New Mexico high school student completes; an IEP can satisfy it."}),
    ("nm_diploma", "New Mexico Diploma of Excellence", "transition", [("Diploma of Excellence", S, NM)], GR(6),
     {**NMJ, "broader": "std_diploma", "note": "New Mexico's high school diploma."}),
    ("nm_std_pos", "Standard program of study", "transition",
     [("Standard Graduation Option", L, NM)], R("6.31.2.11(G)(1)(d)", 19),
     {**NMJ, "note": "The graduation path for students with disabilities that meets all state requirements; the 2011 manual calls it the Standard Graduation Option."}),
    ("nm_ability_pos", "Ability program of study", "transition",
     [("Ability Alternative Graduation Option", L, NM)], GR(19),
     {**NMJ, "note": "The graduation path for students with the most significant cognitive disabilities; its diploma does not end the right to FAPE."}),
    ("nm_modified_pos", "Modified program of study", "transition", [], R("6.31.2.11(G)(1)(c)", 19),
     {**NMJ, "note": "A graduation path the rule names alongside the ability program of study; its diploma does not end the right to FAPE."}),
    ("nm_career_pos", "Career Readiness Alternative Graduation Option", "transition", [], G(45),
     {**NMJ, "note": "A former graduation option based on employability and career education standards."}),
    ("nm_cct", "Conditional certificate of transition", "transition", [], R("6.31.2.11(G)(1)(d)", 19),
     {**NMJ, "note": "A certificate that lets a student join graduation with peers without ending special education services."}),
    ("nm_doc", "Demonstration of competency", "transition", [("demonstrations of competency", P, NM)], GR(6),
     {**NMJ, "note": "A former state graduation requirement in five core subjects, removed in 2024."}),
    ("nm_nmge", "New Mexico Graduation Exam", "iep_component", [], G(45),
     {**NMJ, "broader": "statewide_assess", "note": "A former state high school exam named in the 2011 manual."}),
    ("nm_sba", "Standards-Based Assessment", "iep_component", [("SBA", A, NM)], GR(17),
     {**NMJ, "broader": "statewide_assess", "note": "A state assessment; English learners may take its Spanish Reading test in grade 11."}),
    ("nm_asr", "New Mexico Assessment of Science Readiness", "iep_component", [("NM-ASR", A, NM)], GR(17),
     {**NMJ, "broader": "statewide_assess", "note": "The state grade 11 science assessment."}),
]

JURISDICTION = "US-NM"
LAYER_NAME = "New Mexico"
# Documents listed in sources/documents.tsv that no record cites, and why.
UNCITED_DOCS = {"nm-team-2026": "Downloaded but not read (496 pp.); reserved for a later supplement layer."}

RETRIEVED = "2026-10-09"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.44.0"
