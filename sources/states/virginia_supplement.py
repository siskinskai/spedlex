"""
Virginia layer, 2024 procedural safeguards notice.

The first Virginia pass read the 2013 Regulatory Town Hall copy of the notice
because VDOE's own copy of the September 2024 edition could not be opened. This
supplement reads the September 2024 edition itself.

Sources reviewed 2026-10-12 (local copy in .sources-cache/va/, git-ignored):
  PSN24  VDOE, Your Family's Special Education Rights: Virginia Procedural
         Safeguards Notice, "Revised September 2024", form SS/SE-4 (1/25), 47
         PDF pages (VA-PSN-2024-SS-SE-4.pdf). The contributor supplied the file.
         It was read in full as extracted text (pdftotext). Cited by the page
         number printed in the footer. The cover and the four contents pages
         (i-iv) come first; the first body page (the "General Information"
         page) has no printed number and is cited as p. 1, so the printed page
         number is the PDF page minus five.

What this adds: most of the notice is the federal model notice, so most entries
only record that Virginia's notice attests an existing concept (a federal term
the 2013-copy pass had not yet attested for Virginia). Three Virginia terms
and one Virginia regulation title are new concepts. The notice also re-attests
seven concepts the first pass cited to the 2013 copy or the family guide (the
Department, the Virginia Regulations, the Office of Dispute Resolution and
Administrative Services, PEATC, the Parent Ombudsman, the State Special
Education Advisory Committee and the Advanced Studies Diploma). The notice
names the standard diploma only in the words "standard or advanced studies
diploma", so the Standard high school diploma is not attested from it.

Records read from this PDF by text extraction are 'candidate'.

Cited by URL, not by doc_id, like the rest of this early layer: none of the
Virginia documents the first pass read was saved with a hash, and
tests/test_manifest.py requires every source of a state with a manifest row to
carry a doc_id. The file's details are in provenance/va/va-psn-2024-sources-2026-10-12.md
(SHA-256 18f41bb4449cb09d8a6e6dafc0d368826cc7bfbbd46cdc8ac5a1c339a2f597e7,
1,541,001 bytes, 47 pages). When the other Virginia documents are saved and
hashed, add manifest rows for all of them and move this layer to doc_id.

Left out on purpose: phone numbers, email and web addresses; the Code of
Virginia section on non-attorney representation; the VDOE webpage titles
("Special Education Due Process Hearings", "Resolving Disputes", "Student
Records") and the Library of Virginia records schedule (names of pages and
schedules, not special-education terms); the Commonwealth security standard
SEC530; the federal Controlled Substances Act citation. Concepts that other
states define (a Connecticut board of education, an Illinois school code, a
DC Office of Dispute Resolution, an Alaska or Illinois test name) were not
attested for Virginia where the notice's words only coincide with theirs.
"Qualified examiner" (a New Hampshire-tagged concept) is attested because the
notice uses it for independent evaluations; the maintainers may drop the
single-state tag, since the idea is general.
"""

from .virginia import A, S, V, L, AB, P, VA, VAJ

PSN24_URL = "https://www.doe.virginia.gov/home/showpublisheddocument/922"


def psn(loc=""):
    tail = f", {loc}" if loc else ""
    return {"source_type": "procedural_safeguards_notice",
            "citation": f"VDOE Virginia Procedural Safeguards Notice (rev. Sept. 2024){tail}",
            "url": PSN24_URL}


STRINGS = [
    # Concepts the first pass cited to the 2013 copy, re-attested by the 2024 edition
    ("vdoe", [], psn("cover")),
    ("va_regs", [], psn("cover")),
    ("va_odr", [], psn("cover")),
    ("peatc", [], psn("p. 1")),
    ("ombud", [], psn("p. 1")),
    ("state_panel", [], psn("p. 29")),
    ("adv_studies", [], psn("p. 7")),
    # Concepts that exist in other layers, now attested for Virginia
    ("annual_goals", [], psn("p. 1")),
    ("cwd", [], psn("p. 1")),
    ("fape", [], psn("p. 1")),
    ("func_perf", [], psn("p. 1")),
    ("idea", [], psn("p. 1")),
    ("iep", [], psn("p. 1")),
    ("lre", [], psn("p. 1")),
    ("plaafp", [], psn("p. 1")),
    ("progress", [], psn("p. 1")),
    ("related", [], psn("p. 1")),
    ("safeguards_notice", [], psn("p. 1")),
    ("special_ed", [], psn("p. 1")),
    ("test_accom", [], psn("p. 1")),
    ("comm_mode", [], psn("p. 2")),
    ("evaluation", [], psn("p. 2")),
    ("native_language", [], psn("p. 2")),
    ("pwn", [], psn("p. 2")),
    ("referral", [], psn("p. 2")),
    ("dp_complaint", [("request for due process", S, VA)], psn("p. 3")),
    ("lep", [], psn("p. 3")),
    ("revoke", [], psn("p. 4")),
    ("mediation", [], psn("p. 5")),
    ("ward", [("wards of the State", P, VA)], psn("p. 5")),
    ("equitable", [], psn("p. 8")),
    ("home_education", [], psn("p. 8")),
    ("ppps", [], psn("p. 8")),
    ("iee", [], psn("p. 9")),
    ("interim_iep", [], psn("p. 9")),
    ("parent_initiated_eval", [], psn("p. 10")),
    ("ed_records", [("scholastic records", S, VA), ("scholastic record", S, VA)], psn("pp. 11-12")),
    ("ferpa", [], psn("p. 11")),
    ("pii", [], psn("p. 11")),
    ("child_find", [], psn("p. 13")),
    ("part_agency", [], psn("p. 13")),
    ("record_access", [], psn("p. 13")),
    ("resolution", [], psn("p. 13")),
    ("destruction_pii", [], psn("p. 16")),
    ("adr", [], psn("p. 17")),
    ("cprc", [], psn("p. 17")),
    ("pti", [], psn("p. 17")),
    ("public_agency", [], psn("p. 18")),
    ("state_complaint", [], psn("p. 18")),
    ("prot_advocacy", [], psn("p. 19")),
    ("homeless", [], psn("p. 21")),
    ("stay_put", [], psn("p. 24")),
    ("agreement_review_period", [], psn("p. 27")),
    ("civil_action", [], psn("p. 30")),
    ("ada", [], psn("p. 31")),
    ("attorneys_fees", [], psn("p. 31")),
    ("rehab_act", [], psn("p. 31")),
    ("case_by_case", [], psn("p. 33")),
    ("code_conduct", [], psn("p. 33")),
    ("school_day", [], psn("p. 33")),
    ("gen_curr", [], psn("p. 34")),
    ("controlled", [], psn("p. 35")),
    ("sbi", [], psn("p. 35")),
    ("special_circ", [], psn("p. 35")),
    ("weapon", [], psn("p. 35")),
    ("illegal_drug", [], psn("p. 36")),
    ("exp_hearing", [], psn("p. 37")),
    ("basis_know", [], psn("p. 38")),
    ("expulsion", [], psn("p. 39")),
    ("unilateral_pl", [], psn("p. 39")),
    ("public_benefits_consent", [], psn("p. 41")),
]

CONCEPTS = [
    ("va_complaint_appeal_reviewer", "Complaint Appeal Reviewer", "personnel_role", [], psn("p. 21"),
     {**VAJ, "broader": "state_complaint",
      "note": "The person whose decision is final when a party appeals VDOE's decision on a state complaint."}),
    ("va_iep_coordinator", "IEP Coordinator", "personnel_role", [], psn("p. 7"),
     {**VAJ, "note": "Named, with the local director of special education and the principal, as a person to whom a parent sends a written revocation of consent."}),
    ("va_prc", "Parent Resource Center", "legal_procedural", [], psn("cover, p. 1"),
     {**VAJ, "note": "Named as a place to ask questions about special education; the cover calls it the local school division's. Compare Community Parent Resource Center."}),
    ("va_scholastic_regs", "Management of the Student's Scholastic Record in the Public Schools of Virginia", "legal_procedural",
     [("Management of Student Scholastic Records", S, VA)], psn("pp. 11-12"),
     {**VAJ, "note": "The Board of Education regulation (8 VAC 20-150-10) the notice cites for how school divisions keep student records."}),
]

JURISDICTION = "US-VA"
LAYER_NAME = "Virginia (2024 procedural safeguards notice)"
RETRIEVED = "2026-10-12"
ASSISTED_BY = "claude-sonnet-5-5"
VERSION_ADDED = "0.52.0"  # tools/add_state.py sets this
