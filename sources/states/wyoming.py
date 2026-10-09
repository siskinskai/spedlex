"""
Wyoming layer for SPEDLex.

Sources reviewed 2026-10-08 (listed in sources/documents.tsv; local copies in .sources-cache/wy/):
  RULE   Wyoming Department of Education, Chapter 7: Services for Children
         with Disabilities (Wyoming Administrative Rules, reference number
         206.0002.7.03222010; effective 03/22/2010 and shown as current when
         the Secretary of State's rules portal produced it on 10/08/2026),
         cited by section, e.g. "Ch. 7, § 4(d)(i)". The portal copy
         (WY-7767.pdf, 31 pp.) is a scanned image with no text layer; the
         words were read from WY-Chapter-7-Rules.pdf (30 pp.), a copy of the
         same chapter that carries an OCR text layer. The two were not
         compared page by page. The OCR has errors (the department appears
         as "WOE"), so every quoted string was checked by eye against the
         wording around it.
  PSN    Wyoming Department of Education, Special Education Programs
         Division, Notice of Procedural Safeguards (May 2025, 36 pp.), the
         copy hosted by the Wyoming courts. Cited by PDF page, which equals
         the printed page number.

Both were read in full as text extracted with pdftotext. No main parent
guide or IEP manual was provided; the web "Parents Guide to Special
Education" was not available as a file, so none of its terms are here. The
rule is from 2010 and predates later federal changes, so newer terms the
department may use in guidance are not covered. RULE records are
'machine_validated'; PSN records are 'candidate'.

The notice is mostly the federal model notice, so most of its entries only
record that Wyoming attests an existing concept.

Left out on purpose: the Wyoming legal-aid providers and law school clinics
listed in the notice (not special-education terms), every address, phone
number and web address, individual school districts, the federal conditions
and diseases the rule lists under other health impairment beyond the four
already in SPEDLex (asthma, diabetes, heart condition, hemophilia, lead
poisoning, leukemia, nephritis, rheumatic fever), the individual speech
eligibility measures (percent and standard-deviation cut-offs), grade-span
definitions (elementary, middle and high school), funding and
enforcement terms in sections 8 and 9 (corrective action plan, compliance
agreement, high-risk grantee), and the "Parent Information Center/Parent
Education Network" name, because "Parent Information Center" already
belongs to a New Hampshire concept.
"""

RULE_URL = "https://rules.wyo.gov/"
PSN_URL = "https://www.wyocourts.gov/app/uploads/2026/02/WDE-Procedural-Safeguards-2025.pdf"


def src(doc, loc=""):
    """RULE loc is a section, e.g. '4(d)(i)'; PSN loc is a PDF page."""
    if doc == "RULE":
        return {"source_type": "state_regulation",
                "citation": f"Wyoming Department of Education Rules, Ch. 7 (206.0002.7.03222010), § {loc}",
                "doc_id": "wy-ch7ocr-2010", "url": RULE_URL}
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"Wyoming Department of Education Notice of Procedural Safeguards (May 2025), p. {loc}",
            "doc_id": "wy-psn-2025", "url": PSN_URL}


A, S, V, L, AB, P = "acronym", "synonym", "spelling_variant", "legacy", "abbreviation", "plural"
WY = ["US-WY"]
WYJ = {"jurisdiction": "US-WY"}
R = lambda loc: src("RULE", loc)
PS = lambda page: src("PSN", page)

STRINGS = [
    # Chapter 7, sections 1 to 3
    ("cwd", [], R("1(b)")), ("idea", [], R("2(a)")), ("sea", [], R("2(a)")),
    ("home_education", [("home based education", S, WY)], R("3(b)(iv)")),
    ("preschool_swd", [("preschool children with disabilities", P, None)], R("3(b)(vi)")),
    # section 4, identification, evaluation and eligibility
    ("child_find", [], R("4(a)")), ("pii", [], R("4(a)(ii)")), ("ppps", [], R("4(a)(iii)")),
    ("evaluation", [], R("4(b)(i)")), ("consent", [], R("4(b)(i)(B)")), ("pwn", [], R("4(b)(i)(D)")),
    ("eligibility", [], R("4(c)")), ("special_ed", [], R("4(c)(i)")), ("related", [], R("4(c)(i)")),
    ("autism", [], R("4(d)(i)")),
    ("id", [("Cognitive Disability", S, WY)], R("4(d)(ii)")),
    ("adaptive", [], R("4(d)(ii)(A)(III)")),
    ("deafblind", [], R("4(d)(iii)")), ("tvi", [], R("4(d)(iii)(A)")), ("audiologist", [], R("4(d)(iii)(A)")),
    ("dd", [], R("4(d)(iv)")),
    ("ed", [], R("4(d)(v)")), ("pbis", [], R("4(d)(v)(A)(I)")),
    ("hi", [], R("4(d)(vi)")), ("md", [], R("4(d)(vii)")), ("oi", [], R("4(d)(viii)")),
    ("ohi", [], R("4(d)(ix)")), ("adhd", [], R("4(d)(ix)")), ("epilepsy", [], R("4(d)(ix)")),
    ("sickle", [], R("4(d)(ix)")), ("tourette", [], R("4(d)(ix)")),
    ("sld", [], R("4(d)(x)")), ("perceptual", [], R("4(d)(x)")), ("mbd", [], R("4(d)(x)")),
    ("dyslexia", [], R("4(d)(x)")), ("aphasia", [], R("4(d)(x)")),
    ("observation", [], R("4(d)(x)(C)")),
    ("oral_expr", [], R("4(d)(x)(D)(I)")), ("listen_comp", [], R("4(d)(x)(D)(I)")),
    ("written_expr", [], R("4(d)(x)(D)(I)")), ("basic_reading", [], R("4(d)(x)(D)(I)")),
    ("fluency", [], R("4(d)(x)(D)(I)")), ("reading_comp", [], R("4(d)(x)(D)(I)")),
    ("math_calc", [], R("4(d)(x)(D)(I)")), ("math_ps", [], R("4(d)(x)(D)(I)")),
    ("discrepancy", [], R("4(d)(x)(E)(I)")), ("rti", [], R("4(d)(x)(E)(II)")),
    ("exclusionary", [], R("4(d)(x)(G)")),
    ("sli", [], R("4(d)(xi)")), ("speech_path", [], R("4(d)(xi)(A)")),
    ("artic", [], R("4(d)(xi)(A)(I)")), ("fluency_dis", [], R("4(d)(xi)(A)(II)")),
    ("lang_dis", [], R("4(d)(xi)(A)(III)")), ("voice", [], R("4(d)(xi)(A)(IV)")),
    ("tbi", [], R("4(d)(xii)")),
    ("vi", [], R("4(d)(xiii)")), ("fva", [], R("4(d)(xiii)(A)(V)")),
    # section 5, special education process
    ("fape", [], R("5(a)(i)")), ("lre", [], R("5(b)")), ("continuum", [], R("5(b)(ii)")),
    ("esy", [], R("5(c)")), ("iep", [], R("5(d)")), ("reeval", [], R("5(e)")),
    ("residential", [], R("5(h)")),
    # section 6, procedural safeguards
    ("safeguards_notice", [], R("6")), ("consent", [], R("6(b)")), ("revoke", [], R("6(b)")),
    ("iee", [], R("6(c)")), ("pwn", [], R("6(d)")), ("surrogate", [], R("6(f)")),
    ("age_majority", [], R("6(g)")), ("unilateral_pl", [], R("6(h)")),
    ("ed_records", [], R("6(i)")), ("ferpa", [], R("6(i)")),
    # section 7, dispute resolution; section 9, general supervision
    ("mediation", [], R("7(a)")), ("state_complaint", [], R("7(b)")),
    ("dp_hearing", [], R("7(c)")), ("stay_put", [], R("7(d)")),
    ("transition", [], R("9(d)(ii)")), ("resolution", [], R("9(d)(ii)")),
    # Added after the 2026-10-08 audit (existing concepts the documents use)
    ("charter_school", [], R("3(b)(ii)")), ("public_agency", [], R("4(a)")), ("adverse", [], R("4(c)(i)")),
    ("suspected", [], R("4(d)(i)(A)")), ("school_psych", [], R("4(d)(v)(A)")),
    ("srbi", [], R("4(d)(x)(D)(II)")), ("lep", [], R("4(d)(x)(G)(VI)")),
    ("norm_ref", [], R("4(d)(xi)(A)(I)")), ("iep_team", [], R("5(c)(i)(B)")), ("dp_complaint", [], R("7(c)")),
    # Notice of Procedural Safeguards
    ("safeguards_notice", [], PS(1)), ("pwn", [], PS(6)), ("consent", [], PS(7)), ("ward", [], PS(7)),
    ("revoke", [], PS(8)), ("equitable", [], PS(9)), ("iee", [], PS(9)),
    ("pii", [], PS(11)), ("ed_records", [], PS(11)), ("part_agency", [], PS(11)),
    ("ferpa", [], PS(11)), ("child_find", [], PS(11)), ("record_access", [], PS(12)),
    ("age_majority", [], PS(13)),
    ("cop", [], PS(14)), ("iaes", [], PS(14)), ("mdr", [], PS(15)), ("fba", [], PS(15)),
    ("bip", [], PS(16)), ("special_circ", [], PS(16)), ("sbi", [], PS(16)), ("weapon", [], PS(16)),
    ("controlled", [], PS(16)), ("exp_hearing", [], PS(18)), ("basis_know", [], PS(18)),
    ("state_complaint", [], PS(19)), ("homeless", [], PS(21)),
    ("mediation", [], PS(22)), ("adr", [], PS(22)), ("pti", [], PS(22)), ("cprc", [], PS(22)),
    ("stay_put", [], PS(25)), ("part_c_transition", [], PS(25)), ("resolution", [], PS(25)),
    ("dp_hearing", [], PS(27)), ("s504", [], PS(29)), ("unilateral_pl", [], PS(31)),
    ("ada", [], PS(2)), ("native_language", [], PS(2)), ("comm_mode", [], PS(2)),
    ("school_day", [], PS(14)), ("code_conduct", [], PS(14)), ("gen_curr", [], PS(15)),
]

CONCEPTS = [
    # state agencies and organizations
    ("wy_wde", "Wyoming Department of Education", "legal_procedural", [("WDE", A, WY)], R("2(a)"),
     {**WYJ, "broader": "sea", "note": "The state educational agency; the rule calls it WDE."}),
    ("wy_sepd", "Special Education Programs Division", "legal_procedural", [], PS(1),
     {**WYJ, "broader": "wy_wde", "note": "The division of the Wyoming Department of Education named on the notice's cover."}),
    ("wy_uplift", "UPLIFT", "legal_procedural", [], PS(3),
     {**WYJ, "flags": ["common_english_word"],
      "note": "A Wyoming parent advocacy organization the notice lists for help."}),
    ("wy_ddd", "Developmental Disabilities Division", "legal_procedural", [], R("9(b)"),
     {**WYJ, "broader": "wy_ieu",
      "note": "The Department of Health division the rule makes responsible for FAPE for preschool children."}),
    ("wy_ieu", "Intermediate educational unit", "legal_procedural", [], R("9(b)"),
     {**WYJ, "broader": "esa",
      "note": "The rule deems the Developmental Disabilities Division an intermediate educational unit for preschool services."}),
    ("wy_dfs", "Department of Family Services", "legal_procedural", [("DFS", A, WY)], R("5(i)(i)"),
     {**WYJ, "note": "The state agency that pays residential and treatment costs of court-ordered placements."}),
    # state concepts and placements
    ("wy_swdf", "Wyoming Severe Discrepancy Formula", "evaluation_eligibility", [], R("4(d)(x)(E)(I)"),
     {**WYJ, "broader": "discrepancy",
      "note": "The state's required formula for finding a severe discrepancy when a district chooses that model for learning disability."}),
    ("wy_dev_preschool", "Developmental preschool center", "early_intervention",
     [("developmental preschool centers", P, WY)], R("5(f)(iii)"),
     {**WYJ, "note": "A Wyoming preschool program whose children transition to a school district at age 5."}),
    ("interdistrict_placement", "Inter-district placement", "placement_setting",
     [("inter-district placements", P, WY)], R("5(g)"),
     {"note": "A district contracting with another district or agency when it cannot provide the services itself."}),
    ("court_placement", "Court-ordered placement", "placement_setting",
     [("court-ordered placements", P, WY)], R("5(i)"),
     {"note": "A placement in a private residential treatment facility or group home ordered by a court."}),
]

JURISDICTION = "US-WY"
LAYER_NAME = "Wyoming"
# Documents listed in sources/documents.tsv that no record cites, and why.
UNCITED_DOCS = {"wy-ch7portal-2010": "Scanned portal copy of the rule with no text layer; the words were read from the OCR copy, wy-ch7ocr-2010."}

RETRIEVED = "2026-10-08"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.42.0"
