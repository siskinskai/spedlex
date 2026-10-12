"""
District of Columbia layer for SPEDLex.

Sources reviewed 2026-10-04 (all published by the Office of the State
Superintendent of Education, OSSE, the District's state education agency):
  RULE  5-A DCMR Chapter 30, Special Education (OSSE full-text compilation,
        dated 7/1/2022): disability categories (3011), related services
        (3012), placement (3002, 3024, 3025), definitions (3099) and the rest
        of the chapter
  PSN   District of Columbia IDEA Part B Notice of Procedural Safeguards:
        Rights of Parents of Students with Disabilities (revised Aug. 2018,
        the edition OSSE still posts)
  HB    OSSE Special Education Process Handbook, 2026-27 school year
        (posted Aug. 26, 2026), the District's IEP process manual
  BRO   OSSE Special Education Parent Information Brochure (2026)
  ALT   OSSE Alternate Assessments web page

All five were read in full as text extracted from the official files.
HB pages are the printed page numbers (PDF page minus 2); PSN and BRO
printed pages match the PDF pages. The RULE compilation is OSSE's copy,
not the official D.C. Register; amendments after 7/1/2022 were not checked.
The PSN still cites the chapter by its former subtitle (5-E DCMR).
RULE records are 'machine_validated'; the others are 'candidate'.

District of Columbia Public Schools (DCPS) is left out on purpose: it is
a local education agency (a district name), even though the documents
name it often. The build grades concepts whose strings contain DC, D.C. or
District of Columbia as high risk (place_name) automatically. 5-A DCMR
Chapter 30 carries a manual place_name flag, because DCMR abbreviates
District of Columbia Municipal Regulations.
"""

RULE_URL = "https://osse.dc.gov/sites/default/files/dc/sites/osse/service_content/attachments/5-A%20DCMR%20Chapter%2030_Full%20Text.pdf"
PSN_URL = "https://osse.dc.gov/sites/default/files/dc/sites/osse/publication/attachments/Part%20B%20Procedural%20Safeguards%20Update_%20August%202018-ENG.pdf"
HB_URL = "https://osse.dc.gov/sites/default/files/dc/sites/osse/publication/attachments/SY26-27%20OSSE%20Special%20Education%20Process%20Handbook.pdf"
BRO_URL = "https://osse.dc.gov/sites/default/files/dc/sites/osse/service_content/attachments/Special%20Education%20Parent%20Information%20Brochure%20%282026%29.pdf"
ALT_URL = "https://osse.dc.gov/service/alternate-assessments"


def src(doc, loc=""):
    """Build a source dict. RULE loc is a section, e.g. '3011.5'; other loc is a page, e.g. 'p. 14'."""
    tail = f", {loc}" if loc else ""
    if doc == "RULE":
        return {"source_type": "state_regulation", "citation": f"5-A DCMR § {loc}" if loc else "5-A DCMR Chapter 30",
                "doc_id": "dc-dcmr5a30-2022", "url": RULE_URL}
    if doc == "HB":
        return {"source_type": "state_guidance", "citation": f"OSSE Special Education Process Handbook (SY2026-27){tail}",
                "doc_id": "dc-handbook-2026", "url": HB_URL}
    if doc == "BRO":
        return {"source_type": "state_guidance", "citation": f"OSSE Special Education Parent Information Brochure (2026){tail}",
                "doc_id": "dc-brochure-2026", "url": BRO_URL}
    if doc == "ALT":
        return {"source_type": "state_guidance", "citation": "OSSE Alternate Assessments page", "url": ALT_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"OSSE IDEA Part B Notice of Procedural Safeguards (rev. Aug. 2018){tail}", "doc_id": "dc-psn-2018", "url": PSN_URL}


# string types
A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
DC = ["US-DC"]                    # regional tag for strings only used in the District
DCJ = {"jurisdiction": "US-DC"}   # opts for concepts that only exist in the District
R = lambda loc: src("RULE", loc)
H = lambda page: src("HB", f"p. {page}")
N = lambda page: src("PSN", f"p. {page}")

STRINGS = [
    # 5-A DCMR 3011: the District's fourteen disability categories
    ("autism", [], R("3011.1")),
    ("deafblind", [], R("3011.2")),
    ("deafness", [], R("3011.3")),
    ("dd", [], R("3011.4")),
    ("ed", [("emotional disability", S, DC)], R("3011.5")),
    ("hi", [], R("3011.6")),
    ("id", [], R("3011.7")),
    ("md", [], R("3011.8")),
    ("oi", [], R("3011.9")),
    ("ohi", [], R("3011.10")),
    ("adhd", [], R("3011.10")), ("epilepsy", [], R("3011.10")), ("sickle", [], R("3011.10")), ("tourette", [], R("3011.10")),
    ("sld", [], R("3011.11")),
    ("dyslexia", [], R("3011.11")), ("perceptual", [], R("3011.11")), ("mbd", [], R("3011.11")), ("aphasia", [], R("3011.11")),
    ("oral_expr", [], R("3011.11")), ("listen_comp", [], R("3011.11")), ("written_expr", [], R("3011.11")),
    ("basic_reading", [], R("3011.11")), ("fluency", [], R("3011.11")), ("reading_comp", [], R("3011.11")),
    ("math_calc", [], R("3011.11")), ("math_ps", [], R("3011.11")),
    ("rti", [("Response-to-Intervention model", V, None)], R("3011.11")),
    ("srbi", [], R("3011.11")),
    ("psw", [], R("3011.11")),
    ("discrepancy", [("discrepancy model", S, None)], R("3011.11")),
    ("sli", [], R("3011.12")),
    ("artic", [("articulation impairment", S, None)], R("3011.12")), ("lang_dis", [], R("3011.12")),
    ("tbi", [], R("3011.13")),
    ("vi", [], R("3011.14")),
    ("adaptive", [], R("3011.7")),
    ("cwd", [], R("3099.1")),
    # eligibility and evaluation
    ("eligibility", [], R("3010")),
    ("exclusionary", [("determinant factor", S, None)], R("3010.2")),
    ("s504", [], R("3010.7")),
    ("child_find", [], R("3003")),
    ("screening", [], R("3006.13")),
    ("evaluation", [], R("3005")),
    ("eval_report", [], R("3006.11")),
    ("observation", [], R("3006.10")),
    ("reeval", [("triennial evaluation", S, None)], R("3007.5")),
    ("medical", [], R("3012.7")),
    ("iee", [], R("3038")),
    # IEP team and IEP content
    ("iep", [], R("3099.1")),
    ("iep_team", [], R("3008")),
    ("gen_teacher", [], R("3008.1")), ("sped_teacher", [], R("3008.1")), ("lea_rep", [], R("3008.1")),
    ("eval_interp", [], R("3008.1")),
    ("plaafp", [], R("3017.8")), ("annual_goals", [], R("3017.8")), ("progress", [], R("3017.8")),
    ("sto", [], R("3017.8")), ("saas", [], R("3017.8")), ("program_mods", [], R("3017.8")),
    ("removal_expl", [], R("3017.8")), ("test_accom", [], R("3017.8")), ("alt_assess", [], R("3017.8")),
    ("fld", [], R("3017.8")),
    ("comm_mode", [], R("3017.9")),
    ("pbis", [], R("3017.10")), ("fba", [], R("3017.10")), ("bip", [], R("3017.10")),
    ("braille", [], R("3017.12")),
    ("lep", [], R("3099.1")),
    ("annual_review", [], R("3018.1")),
    ("amendment", [], R("3019")),
    ("comparable", [], R("3020.5")),
    ("gen_curr", [], R("3099.1")),
    ("sdi", [], R("3099.1")),
    ("special_ed", [], R("3099.1")),
    ("travel_training", [], R("3099.1")),
    ("voc_ed", [], R("3099.1")),
    ("para", [], R("3099.1")),
    # related services, AT, PE, ESY
    ("related", [], R("3012")),
    ("audiology", [], R("3012.3")), ("counseling", [], R("3012.4")), ("early_id", [], R("3012.5")),
    ("interpreting", [], R("3012.6")),
    ("cart", [("communication access real-time translation", V, None)], R("3012.6")),
    ("ot", [], R("3012.8")), ("om", [], R("3012.9")), ("parent_training", [], R("3012.10")),
    ("pt", [], R("3012.11")), ("psych", [], R("3012.12")), ("recreation", [], R("3012.13")),
    ("rehab", [], R("3012.14")), ("nursing", [], R("3012.15")), ("social_work", [], R("3012.16")),
    ("slp", [], R("3012.17")), ("transport", [], R("3012.18")),
    ("at_device", [], R("3099.1")), ("at_service", [], R("3099.1")),
    ("pe", [], R("3014")),
    ("esy", [], R("3015")),
    ("regression", [], R("3015.2")),
    # placement
    ("continuum", [], R("3002")),
    ("regular_class", [("regular education classroom", S, None)], R("3002.3")),
    ("special_class", [("special education classroom", S, None)], R("3002.3")),
    ("special_school", [("special education day program", REL, DC)], R("3002.3")),
    ("residential", [("special education residential program", S, DC)], R("3002.3")),
    ("residential", [("residential treatment facility", S, None)], R("3025.13")),
    ("home_instr", [], R("3024")),
    ("hospital_instr", [], R("3024")),
    ("lre", [], R("3021")),
    ("nonacademic", [], R("3021.3")),
    ("aversive", [], R("3025.9")),
    # transition and exit
    ("transition", [], R("3026")),
    ("postsecondary", [], R("3026.1")), ("trans_assess", [], R("3026.1")), ("interagency", [], R("3026.1")),
    ("course_study", [], R("3026.5")),
    ("std_diploma", [], R("3026.6")),
    ("exit_sped", [("exit from special education", S, None)], R("3028")),
    ("sop", [], R("3028.5")),
    ("fve", [], R("3099.1")),
    ("age_majority", [], R("3035")),
    ("sdm", [], R("3035")),
    # rights, records, parents, private schools
    ("fape", [], R("3001.1")),
    ("lea", [], R("3001.1")),
    ("sea", [], R("3099.1")),
    ("homeless", [], R("3001.1")), ("ward", [], R("3001.1")),
    ("part_c_transition", [], R("3001.11")),
    ("ifsp", [], R("3099.1")), ("itd", [], R("3099.1")),
    ("native_language", [], R("3099.1")),
    ("ed_records", [], R("3030")), ("ferpa", [], R("3030.1")), ("pii", [], R("3031.1")),
    ("consent", [], R("3031")), ("revoke", [], R("3016.6")),
    ("pwn", [], R("3032")),
    ("safeguards_notice", [("IDEA Part B Notice of Procedural Safeguards", S, DC),
                           ("Rights of Parents of Students with Disabilities", S, DC)], N(1)),
    ("surrogate", [("educational surrogate", AB, DC)], N(9)),
    ("foster", [], N(9)),
    ("gal", [], R("3034.5")),
    ("uhy", [], R("3034.1")),
    ("ppps", [], R("3040")), ("equitable", [], R("3040")), ("services_plan", [], R("3099.1")),
    ("hqt", [], R("3040.10")),
    ("part_agency", [], N(14)),
    ("pti", [], N(7)),
    ("idea", [], N(2)),
    ("ada", [], N(29)),
    # dispute resolution
    ("mediation", [], R("3047")),
    ("state_complaint", [], R("3048")),
    ("dp_complaint", [], R("3049")), ("dp_hearing", [], R("3049")),
    ("stay_put", [], R("3050")),
    ("resolution", [], R("3052")),
    ("state_panel", [("State Education Agency Advisory Panel", S, DC)], R("3053.8")),
    ("exp_hearing", [], N(36)),
    # discipline, restraint
    ("code_conduct", [], R("3043.1")), ("iaes", [], R("3043.2")), ("cop", [], R("3043.3")),
    ("special_circ", [], R("3043.9")), ("weapon", [], R("3043.9")), ("illegal_drug", [], R("3043.9")),
    ("controlled", [], R("3043.9")), ("sbi", [], R("3043.9")),
    ("mdr", [], R("3043.11")),
    ("basis_know", [], N(37)),
    ("restraint", [], R("3044.4")),
    ("mech_restraint", [("mechanical restraint", V, None)], R("3044.1")),
    # OSSE handbook names for existing concepts
    ("reed", [("analysis of existing data", S, DC)], H(5)),
    ("eval_report", [("evaluation summary report", S, DC)], H(10)),
    ("two_prong", [("two-pronged test", V, None)], H(10)),
    ("social_hist", [("social history assessment", S, None)], H(7)),
    ("audiological_assess", [("audiological evaluation", S, None)], H(7)),
    ("voc_eval", [], H(7)),
    ("consult", [("consultation services", S, None)], H(24)),
    ("comparable", [("comparable services plan", REL, DC)], H(27)),
    ("coteach", [], H(26)),
    ("dys_screen", [], H(4)),
    ("ext_time", [], H(17)), ("large_print", [], H(17)), ("asl", [], H(17)),
    ("word_pred", [], H(17)),
    ("small_group", [("small group testing", S, DC)], H(17)),
    ("indiv_admin", [("individual testing", S, DC)], H(17)),
    ("msaa", [], src("ALT")),
    ("dlm", [("DLM Science Alternate Assessment", REL, DC)], src("ALT")),
    ("ess_elements", [("EEs", A, None)], src("ALT")),
    ("sig_cog", [], src("ALT")),
]

CONCEPTS = [
    # agencies and offices
    ("dc_osse", "Office of the State Superintendent of Education", "legal_procedural", [("OSSE", A, DC)], R("3099.1"),
     {**DCJ, "broader": "sea", "note": "The District's state education agency."}),
    ("dc_sco", "State Complaint Office", "legal_procedural", [("SCO", A, DC)], R("3048.1"),
     {**DCJ, "broader": "dc_osse", "note": "OSSE office that investigates special education state complaints."}),
    ("dc_odr", "Office of Dispute Resolution", "legal_procedural", [("ODR", A, DC)], H(35),
     {**DCJ, "broader": "dc_osse",
      "note": "OSSE's due process hearing office. Its acronym ODR is shared with Pennsylvania's Office for Dispute Resolution."}),
    ("dc_osse_dot", "Division of Transportation", "related_service", [("OSSE-DOT", A, DC)], H(19),
     {**DCJ, "broader": "dc_osse", "note": "OSSE division that provides special education transportation."}),
    ("dc_pcsb", "District of Columbia Public Charter School Board", "legal_procedural", [("PCSB", A, DC)], R("3001.9"),
     {**DCJ, "note": "Contains a place name, so only the full phrase is protected."}),
    ("dc_cfsa", "Child and Family Services Agency", "legal_procedural", [("CFSA", A, DC)], R("3001.7"),
     {**DCJ, "note": "Children in its custody may need an educational surrogate parent."}),
    ("dc_dyrs", "Department of Youth Rehabilitation Services", "legal_procedural", [("DYRS", A, DC)], R("3001.6"),
     {**DCJ, "note": "Must make FAPE available to committed youth in its secure facilities."}),
    ("dc_dhcf", "Department of Health Care Finance", "legal_procedural", [("DHCF", A, DC)], R("3025.14"),
     {**DCJ, "note": "The District's Medicaid agency."}),
    ("dc_dbh", "Department of Behavioral Health", "legal_procedural", [("DBH", A, DC)], R("3025.16"), DCJ),
    ("dc_dds", "Department on Disability Services", "transition", [("DDS", A, DC)], H(13),
     {**DCJ, "note": "Invited to IEP meetings as a participating agency for transition services."}),
    ("dc_rsa", "Rehabilitation Services Administration", "transition", [("RSA", A, DC)], H(13),
     {**DCJ, "note": "Invited to IEP meetings as a participating agency for transition services."}),
    ("dc_ombuds", "Office of the Ombudsman for Public Education", "legal_procedural", [], R("3032.2"),
     {**DCJ, "note": "Listed in every prior written notice as a source of help."}),
    ("dc_sped_hub", "DC Special Education Hub", "legal_procedural", [("Special Education Hub", AB, DC)], H(14),
     {**DCJ, "broader": "dc_ombuds"}),
    ("dc_osa", "Office of the Student Advocate", "legal_procedural", [], R("3032.2"), DCJ),
    ("dc_aje", "Advocates for Justice and Education", "legal_procedural", [("AJE", A, DC)], H(14),
     {**DCJ, "broader": "pti", "note": "The District's federally funded parent training and information center."}),
    ("dc_strong_start", "Strong Start DC Early Intervention Program", "early_intervention", [("Strong Start DC", AB, DC)],
     src("BRO", "p. 2"), {**DCJ, "note": "OSSE's early intervention program for infants and toddlers."}),
    ("dc_special_programs", "Special Programs", "legal_procedural", [], H(4),
     {**DCJ, "flags": ["common_english_word"], "note": "OSSE's state-level special education database, where IEPs are written."}),
    # law and regulation
    ("dc_ch30", "5-A DCMR Chapter 30", "legal_procedural", [], src("RULE"),
     {**DCJ, "flags": ["place_name"],
      "note": "The District's special education regulations. Older documents cite it as 5-E DCMR. DCMR stands for District of Columbia Municipal Regulations."}),
    ("dc_language_access", "D.C. Language Access Act of 2004", "legal_procedural", [("Language Access Act", AB, DC)],
     R("3009.8"), {**DCJ, "note": "Can extend the deadline for giving parents a translated IEP."}),
    ("dc_sfasa", "Student Fair Access to School Act of 2018", "discipline", [], H(32),
     {**DCJ, "note": "District law limiting suspension and expulsion."}),
    ("dc_hhi_act", "Students' Right to Home and Hospital Instruction Act of 2020", "placement_setting", [], H(26),
     {**DCJ, "broader": "home_instr"}),
    ("dc_dyslexia_act", "Addressing Dyslexia and Other Reading Difficulties Amendment Act of 2020", "evaluation_eligibility",
     [], H(4), {**DCJ, "broader": "dys_screen", "note": "Requires universal reading screening in kindergarten through grade 2."}),
    # LEAs and enrollment
    ("dc_pcs_lea", "Public charter school LEA", "legal_procedural", [("public charter school LEAs", P, DC)], R("3003.3"),
     {**DCJ, "broader": ["lea", "charter_school"], "note": "A charter school that has elected to be its own LEA for IDEA."}),
    ("dc_lea_right", "LEA-of-right", "legal_procedural", [("geographical LEA-of-right", S, DC)], H(3),
     {**DCJ, "broader": "lea", "note": "The District's geographic LEA, responsible for residents not enrolled in a charter LEA."}),
    ("dc_stage5", "Stage 5 enrollment", "legal_procedural", [], H(27),
     {**DCJ, "note": "The enrollment stage at which a child is attending school."}),
    # evaluation and eligibility
    ("primary_disability", "Primary disability", "evaluation_eligibility", [], R("3010.4"), {"broader": "eligibility"}),
    ("secondary_disability", "Secondary disability", "evaluation_eligibility", [("secondary disabilities", P, None)],
     R("3010.4"), {"broader": "eligibility"}),
    ("cbm", "Curriculum-based measurement", "evaluation_eligibility", [("CBM", A, None)], H(8), {}),
    ("fva", "Functional vision assessment", "evaluation_eligibility", [], H(7), {}),
    ("lma", "Learning media assessment", "evaluation_eligibility", [], H(7), {}),
    # IEP and services
    ("dc_dwa", "Documented written agreement", "iep_component", [], R("3019.1"),
     {**DCJ, "broader": "amendment", "note": "Amending an IEP by written agreement instead of an IEP team meeting."}),
    ("dc_speech_only", "Speech-only IEP", "iep_component", [("Speech Only IEPs", P, DC)], H(21),
     {**DCJ, "broader": "slp", "note": "The District lets speech-language pathology count as special education."}),
    ("dedicated_aide", "Dedicated aide", "personnel_role", [], H(16), {"broader": "para"}),
    ("comp_services", "Compensatory services", "legal_procedural", [], H(24), {}),
    ("critical_skill", "Critical skill", "iep_component", [], R("3015.3"), {"broader": "esy"}),
    ("dc_mfs", "Medically Fragile Students", "related_service", [("MFS", A, DC)], H(19),
     {**DCJ, "broader": "transport", "note": "Transportation eligibility category."}),
    ("dc_sts", "Structured Transportation Supports", "related_service", [("STS", A, DC)], H(19),
     {**DCJ, "broader": "transport", "note": "Transportation eligibility category."}),
    ("dc_asp", "Accessing Special Programs", "related_service", [("ASP", A, DC)], H(19),
     {**DCJ, "broader": "transport", "note": "Transportation eligibility category."}),
    # placement
    ("dc_service_location", "Service location", "placement_setting", [], R("3099.1"),
     {**DCJ, "note": "The physical address where services are delivered, distinct from placement."}),
    ("dc_outside_lea", "Placement outside of the LEA", "placement_setting", [], R("3025"),
     {**DCJ, "broader": "continuum", "note": "OSSE reviews the LEA's request and issues a service location."}),
    ("dc_nonpublic", "Nonpublic special education school or program", "placement_setting",
     [("nonpublic special education school", AB, DC)], R("3099.1"), {**DCJ, "broader": "special_school"}),
    ("dc_coa", "Certificate of approval", "legal_procedural", [], R("3025.8"),
     {**DCJ, "broader": "dc_nonpublic", "note": "OSSE approval a nonpublic school needs to serve District students."}),
    ("prtf", "Psychiatric residential treatment facility", "placement_setting", [("PRTF", A, None)], R("3025.14"),
     {"broader": "residential"}),
    # transition and exit
    ("dc_iep_coc", "IEP Certificate of Completion", "transition", [], R("3027"),
     {**DCJ, "broader": "cert_completion", "note": "A credential other than a diploma; FAPE continues until age 22."}),
    ("dc_diploma_notice", "Notice of Change in Diploma Type", "transition", [], H(31), DCJ),
    ("graduation_plan", "Graduation plan", "transition", [], R("3026.5"), {"broader": "course_study"}),
    ("dc_educ_rep", "Educational representative", "transition", [], R("3099.1"),
     {"broader": "age_majority",
      "note": "An adult appointed to make education decisions for a student 18 or older (by OSSE in DC). General concept: Indiana uses the term too; the key keeps its dc_ prefix."}),
    # rights and dispute resolution
    ("dc_parent_obs", "Parent observation", "legal_procedural", [], R("3041"),
     {**DCJ, "note": "Parents and their designees may observe a child's current or proposed program."}),
    ("dc_hod", "Hearing Officer Determination", "legal_procedural", [("HOD", A, DC)], R("3053.5"),
     {**DCJ, "broader": "dp_hearing"}),
    # behavior, restraint, discipline
    ("seclusion", "Seclusion", "discipline", [], R("3045"), {}),
    ("prone_restraint", "Prone restraint", "discipline", [], R("3099.1"), {"broader": "restraint"}),
    ("chem_restraint", "Chemical restraint", "discipline", [], R("3044.3"), {"broader": "restraint"}),
    ("fade_plan", "BIP fade plan", "discipline", [("fade plan", AB, None)], H(32), {"broader": "bip"}),
    ("informal_removal", "Informal removal", "discipline", [("informal removals", P, None)], H(33), {}),
    # assessment and standards
    ("dc_cape", "DC CAPE Next", "iep_component", [], src("ALT"),
     {**DCJ, "note": "The District's general statewide assessment; MSAA and DLM are its alternates."}),
    ("ccss", "Common Core State Standards", "academic_skill", [("CCSS", A, None)], H(15), {}),
    ("ngss", "Next Generation Science Standards", "academic_skill", [("NGSS", A, None)], H(17), {}),
    ("essa", "Every Student Succeeds Act", "legal_procedural", [], src("ALT"),
     {"note": "Caps alternate assessment participation at 1 percent of students."}),
]

JURISDICTION = "US-DC"
LAYER_NAME = "District of Columbia"
RETRIEVED = "2026-10-04"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.24.0"
