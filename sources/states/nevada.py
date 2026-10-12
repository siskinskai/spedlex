"""
Nevada layer for SPEDLex.

Sources reviewed 2026-10-03:
  PSN  NDE, Special Education Rights of Parents and Students, June 2023 (English)
  IEP  State of Nevada Individualized Educational Program form, July 2018
  NAC  Nevada Administrative Code chapter 388, eligibility and definitions sections
  NDE  NDE special education policies page (eligibility and age-of-majority form titles)

Nevada publishes no parent guide like Texas's ARD guide; the statewide IEP
form and the per-category eligibility forms are the closest equivalents.

PSN and IEP references come from a text extraction of the PDFs, so records
that rely on them are 'candidate' until a person checks the page. NAC
citations come from the rule's section list and text: 'machine_validated'.
The IEP form is dated July 2018, so its assessment names may be out of date.
"""

PSN_URL = "https://webapp-strapi-paas-prod-nde-001.azurewebsites.net/uploads/Special_Education_Rights_Of_Parents_And_Students_English_4c259d5e86.pdf"
IEP_URL = "https://webapp-strapi-paas-prod-nde-001.azurewebsites.net/uploads/IEP_Form_1_44a0c4d762.pdf"
NDE_URL = "https://doe.nv.gov/offices/office-of-comprehensive-student-services/policies-and-procedures"
NAC_URL = "https://www.law.cornell.edu/regulations/nevada/NAC-{}"


def src(doc, loc):
    if doc == "NAC":
        return {"source_type": "state_regulation", "citation": f"NAC {loc}",
                "url": NAC_URL.format(loc.split("(")[0].replace(".", "-"))}
    return {
        "PSN": {"source_type": "procedural_safeguards_notice", "citation": f"NDE Special Education Rights of Parents and Students (June 2023), {loc}", "url": PSN_URL},
        "IEP": {"source_type": "state_guidance", "citation": f"State of Nevada IEP form (July 2018), {loc}", "url": IEP_URL},
        "NDE": {"source_type": "state_guidance", "citation": f"NDE special education policies page, {loc}", "url": NDE_URL},
    }[doc]


A, S, V, L, AB, P, REL = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural", "related"
NV = ["US-NV"]

# (existing concept key, [(text, type, regional or None)], source)
STRINGS = [
    ("iep_team", [("IEP committee", S, NV)], src("PSN", "p. 3")),
    ("iep", [("individualized educational program", V, NV)], src("IEP", "p. 1")),
    ("cwd", [("pupil with a disability", S, NV), ("pupils with disabilities", P, NV)], src("NAC", "388.093")),
    ("autism", [], src("NAC", "388.387")),
    ("deafblind", [("deaf/blind", V, NV)], src("NAC", "388.427")),
    ("hi", [("hearing impairment/deaf", V, NV)], src("NAC", "388.390")),
    ("ohi", [("health impairment", S, NV), ("health impairment other than orthopedic impairment", S, NV)], src("NAC", "388.402")),
    ("md", [("multiple impairments", S, NV), ("multiple impairment", V, NV)], src("NAC", "388.065")),
    ("sli", [("speech and language impairment", S, NV), ("speech/language impairment", V, NV)], src("NAC", "388.125")),
    ("vi", [("visual impairment/blind", V, NV)], src("NAC", "388.395")),
    ("oi", [], src("NAC", "388.400")),
    ("tbi", [], src("NAC", "388.407")),
    ("sld", [("specific learning disabilities", P, None)], src("NAC", "388.420")),
    ("id", [("mild intellectual disability", REL, NV), ("moderate intellectual disability", REL, NV),
            ("severe intellectual disability", REL, NV), ("profound intellectual disability", REL, NV)], src("NAC", "388.410")),
    ("ed", [], src("NAC", "388.415")),
    ("dd", [("developmental delays", P, None), ("developmentally delayed", V, None)], src("NAC", "388.430")),
    ("dyslexia", [], src("NAC", "388.0415")),
    ("adaptive", [], src("NAC", "388.015")),
    ("gen_curr", [], src("NAC", "388.042")),
    ("prr", [], src("NAC", "388.074")),
    ("travel_training", [], src("NAC", "388.1345")),
    ("homeless", [("homeless youth", S, None)], src("NAC", "388.049")),
    ("part_agency", [], src("NAC", "388.073")),
    ("comm_mode", [("communication mode", S, None), ("primary communication mode", S, None)], src("NAC", "388.0335")),
    ("pbis", [("positive behavioral supports", S, None), ("positive behavioral strategies, supports and interventions", S, NV)], src("NAC", "388.077")),
    ("rti", [], src("NAC", "388.102")),
    ("srbi", [("targeted scientific, research-based intervention", S, NV)], src("NAC", "388.325")),
    ("reed", [("review of evaluation data", S, NV)], src("NAC", "388.336")),
    ("reeval", [("3-year reevaluation", S, None), ("periodic reevaluation", S, NV)], src("NAC", "388.440")),
    ("fba", [("assessment of functional behavior", S, NV)], src("NAC", "388.386")),
    ("iee", [], src("NAC", "388.450")),
    ("gen_teacher", [("regular classroom teacher", S, NV)], src("NAC", "388.095")),
    ("state_complaint", [("State complaint investigation", REL, NV)], src("PSN", "pp. 9-10")),
    ("exp_hearing", [], src("PSN", "pp. 21-22")),
    ("basis_know", [], src("PSN", "pp. 22-23")),
    ("ward", [], src("PSN", "pp. 3-4")),
    ("ed_records", [], src("PSN", "p. 6")),
    ("resolution", [], src("PSN", "pp. 13-14")),
    ("lea_rep", [], src("IEP", "p. 1")),
    ("special_class", [("self-contained program", S, NV)], src("IEP", "p. 10")),
    ("resource_room", [("regular class and special education class combination", S, NV)], src("IEP", "p. 10")),
    ("removal_expl", [("justification for placement", S, NV)], src("IEP", "p. 10")),
    ("esy", [], src("IEP", "p. 10")),
    ("progress", [("method for reporting progress", S, None), ("specialized progress report", S, NV)], src("IEP", "p. 8")),
    ("postsecondary", [], src("IEP", "p. 5")),
    ("transition", [("coordinated activities", S, None)], src("IEP", "p. 6")),
    ("fve", [], src("IEP", "p. 6")),
    ("sdi", [], src("IEP", "p. 8")),
    ("program_mods", [("modification, accommodation, or support for student or personnel", REL, NV)], src("IEP", "p. 8")),
    ("amendment", [("IEP revision without a meeting", S, NV), ("revision to IEP", S, NV)], src("IEP", "p. 1")),
    ("annual_review", [("annual IEP", S, None)], src("IEP", "p. 1")),
]

# (key, preferred, category, [(text, type, regional)], source, opts)
CONCEPTS = [
    # --- Nevada agencies and legal frame ---
    ("nde", "Nevada Department of Education", "legal_procedural", [("NDE", A, NV)], src("PSN", "p. 1"),
     {"jurisdiction": "US-NV", "broader": "sea"}),
    ("ocss", "Office of Comprehensive Student Services", "legal_procedural", [("OCSS", A, NV)], src("PSN", "p. 1"),
     {"jurisdiction": "US-NV", "broader": "nde", "note": "NDE's office for special education as of the 2023 notice; NDE's site now also uses an Office of Inclusive Education. Verify the current name."}),
    ("nac", "Nevada Administrative Code", "legal_procedural", [("NAC", A, NV)], src("NAC", "388.001"), {"jurisdiction": "US-NV", "status": "machine_validated"}),

    # --- Dispute resolution: Nevada has a two-tier hearing system ---
    ("sro", "State review officer", "legal_procedural", [("state-level review", S, None), ("SRO", A, NV)], src("PSN", "pp. 16-17"),
     {"broader": "dp_hearing", "note": "Two-tier states appeal a hearing decision to a state review officer before court (34 CFR 300.514(b)). 'SRO' also means 'school resource officer' in discipline records, so the acronym is ambiguous."}),

    # --- Eligibility and evaluation (NAC 388) ---
    ("statement_elig", "Statement of eligibility", "evaluation_eligibility", [("eligibility statement", S, NV)], src("NDE", "eligibility forms"),
     {"jurisdiction": "US-NV", "note": "Nevada's per-category eligibility form, e.g. 'Statement of Eligibility - Specific Learning Disabilities'."}),
    ("gifted", "Gifted and talented", "evaluation_eligibility", [("gifted and talented pupil", S, NV)], src("NAC", "388.435"),
     {"status": "machine_validated", "note": "Not an IDEA category, but Nevada determines it under the same chapter, so it appears in the same paperwork."}),
    ("cog", "Cognitive abilities", "evaluation_eligibility", [("assessment of cognitive abilities", REL, NV)], src("NAC", "388.031"), {"status": "machine_validated"}),
    ("socemo", "Social and emotional condition", "evaluation_eligibility", [("assessment of social and emotional condition", REL, NV)], src("NAC", "388.111"), {"status": "machine_validated"}),
    ("devfx", "Developmental functioning", "evaluation_eligibility", [], src("NAC", "388.041"), {"status": "machine_validated"}),
    ("cba", "Classroom-based assessment", "evaluation_eligibility", [("classroom-based assessments", P, None)], src("NAC", "388.029"), {"status": "machine_validated"}),
    ("pces", "Performance in the current educational setting", "evaluation_eligibility", [("assessment of performance in current educational setting", REL, NV)], src("NAC", "388.075"), {"status": "machine_validated"}),
    ("eoi", "Evidence of intervention", "evaluation_eligibility", [("assessment of evidence of intervention", REL, NV)], src("NAC", "388.385"), {"status": "machine_validated"}),
    ("consult", "Collaborative or consulting services", "related_service", [("consultative services", S, None), ("direct services", S, None)], src("NAC", "388.033"),
     {"status": "machine_validated", "note": "The IEP form codes service type as A (assessment), C (consultative) or D (direct). Single letters are never safelisted."}),

    # --- IEP form structure ---
    ("interim_iep", "Interim IEP", "iep_component", [("interim individualized educational program", S, NV)], src("IEP", "p. 1"),
     {"note": "National usage, e.g. for transfer students (34 CFR 300.323(e))."}),
    ("fed_place_code", "Federal placement code", "placement_setting", [("educational environment code", S, None)], src("IEP", "p. 1"), {}),
    ("pct_regular", "Percentage of time in regular education environment", "placement_setting", [("percent of time in general education", S, None)], src("IEP", "p. 10"),
     {"broader": "lre"}),
    ("strengths", "Statement of student strengths", "iep_component", [("student strengths", AB, None)], src("IEP", "p. 3"), {}),
    ("parent_concerns", "Parent educational concerns", "iep_component", [("statement of parent educational concerns", S, NV), ("parent concerns", AB, None)], src("IEP", "p. 3"),
     {"note": "Federal requirement to consider the parents' concerns (34 CFR 300.324(a)(1)(ii))."}),
    ("prefs", "Student preferences and interests", "transition", [("statement of student's preferences and interests", S, NV)], src("IEP", "p. 3"), {}),
    ("vision_future", "Student's vision for the future", "transition", [("vision statement", S, None)], src("IEP", "p. 5"), {}),
    ("comm_exp", "Community experiences", "transition", [], src("IEP", "p. 6"), {"broader": "transition", "note": "Transition-services component under 34 CFR 300.43(a)(2)."}),
    ("post_school", "Employment and other post-school adult living objectives", "transition", [("post-school adult living objectives", AB, None)], src("IEP", "p. 6"), {"broader": "transition"}),
    ("daily_living", "Acquisition of daily living skills", "functional_skill", [("daily living skills", AB, None), ("activities of daily living", S, None)], src("IEP", "p. 6"), {"broader": "transition"}),
    ("comm_access", "Communication access", "accommodation_modification", [("equal opportunity for communication access", S, NV)], src("IEP", "p. 4"),
     {"broader": "comm_mode", "note": "From the special factors Nevada adds for students who are deaf or hard of hearing."}),

    # --- Dyslexia instructional approaches (IEP form special factor 7) ---
    ("explicit", "Explicit, direct instruction", "academic_skill", [("explicit instruction", AB, None), ("systematic, sequential and cumulative instruction", S, None)], src("IEP", "p. 4"), {"broader": "dyslexia"}),
    ("alpha_principle", "Alphabetic principle", "academic_skill", [], src("IEP", "p. 4"), {"broader": "dyslexia"}),
    ("multisensory", "Multisensory instruction", "academic_skill", [("multi-sensory instruction", V, None), ("structured literacy", S, None)], src("IEP", "p. 4"),
     {"broader": "dyslexia", "note": "'Structured literacy' is practitioner usage, not from the form."}),
    ("meaning_based", "Meaning-based instruction", "academic_skill", [], src("IEP", "p. 4"), {"broader": "dyslexia"}),

    # --- Assessments and diplomas ---
    ("naa", "Nevada Alternate Assessment", "iep_component", [("NAA", A, NV)], src("IEP", "p. 5"), {"jurisdiction": "US-NV", "broader": "alt_assess"}),
    ("crt", "State criterion-referenced test", "iep_component", [("criterion-referenced test", AB, None), ("CRT", A, NV)], src("IEP", "p. 9"),
     {"jurisdiction": "US-NV", "note": "Name from the 2018 form; Nevada's current assessment names may differ."}),
    ("ccra", "College and Career Readiness Assessment", "iep_component", [], src("IEP", "p. 9"), {"jurisdiction": "US-NV", "note": "Name from the 2018 form."}),
    ("nvpep", "Nevada Proficiency Examination Program", "iep_component", [], src("IEP", "p. 9"), {"jurisdiction": "US-NV", "note": "Name from the 2018 form."}),
    ("std_diploma", "Standard high school diploma", "transition", [("advanced high school diploma", REL, NV)], src("IEP", "p. 5"), {}),
    ("adj_diploma", "Adjusted high school diploma", "transition", [("adjusted diploma", AB, NV)], src("IEP", "p. 5"), {"jurisdiction": "US-NV", "note": "Earned by completing IEP requirements."}),
    ("alt_diploma", "Alternative high school diploma", "transition", [("alternative diploma", AB, None)], src("IEP", "p. 5"),
     {"note": "Federal concept (ESSA) for students assessed on the alternate assessment."}),
    ("aom_rep", "Application to represent the educational interests of a student at the age of majority", "transition", [], src("NDE", "age-of-majority form"),
     {"jurisdiction": "US-NV", "broader": "age_majority"}),
]

JURISDICTION = "US-NV"
LAYER_NAME = "Nevada"
RETRIEVED = "2026-10-03"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.3.0"
