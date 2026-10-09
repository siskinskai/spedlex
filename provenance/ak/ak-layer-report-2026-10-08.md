# Alaska layer (v0.35.0): contributor report

Drafted 2026-10-08 with Claude Opus 5.5 (`claude-opus-5-5`) following `prompts/add-state.md`. A person must review this before it is submitted, and `prompts/audit-layer.md` should be run on it in a fresh conversation, ideally with a different model.

## 1. Documents read
- **RULE**: 4 AAC 52, Article 2, 4 AAC 52.100 to 52.790, printed from the Alaska Legislature's Administrative Code site to `.sources-cache/ak/4 AAC 52.100.pdf` (16 pp.). Read in full. The printout starts at 52.100, so **52.090 (district responsibility) is missing**. It also has no history notes. A Cornell LII copy shows 52.130 was last amended 9/9/2016 (Register 219), but that copy was only consulted, not saved.
- **PSN**: DEED, Notice of Procedural Safeguards: Parental Rights for Special Education (37 pp.). Read in full. **No date is printed on it**; the PDF file's creation date is March 19, 2024, and the citation says so.
- **GUIDE**: Alaska Special Education Parents' Guide, by LINKS Mat-Su Parent Resource Center for DEED (June 2017, 12 pp.). Read in full. The pages are two-column, so extracted lines interleave; quotes below were read column by column.
- **ALT**: DEED's Dynamic Learning Maps (DLM) Alternate Assessment page, printed to PDF 2026-10-08 (3 pp.). Read in full. It was saved in the repository root and has been moved into `.sources-cache/ak/`.
- **Missing**: DEED's Special Education Handbook (no DEED-hosted copy found) and any diploma or graduation guidance.
- All text came from `pdftotext`. Every new string and every attestation was checked automatically against its cited section or page; 17 attestations with no literal hit were checked by hand and are wording variants (for example "preferences and interests" for `prefs`, "Homebound, or hospital, instruction" for `home_instr`).

## 2. New concepts
| Key | Preferred term | Where it appears (15 words or fewer) | Citation |
|---|---|---|---|
| `ak_deed` | Alaska Department of Education and Early Development | "Alaska Department of Education and Early Development PO Box 110500 Juneau, AK" | PSN p. 1 |
| `ak_tls` | Division of Teaching and Learning Support | "It must be sent to the department, division of teaching and learning support" | 4 AAC 52.500(b) |
| `ak_abdhh` | Advisory Board for the Deaf and Hard of Hearing | "Board of Education and Early Development's Advisory Board for the Deaf and Hard of Hearing" | 4 AAC 52.255 |
| `ak_dfcs` | Department of Family and Community Services | "committed to the custody of the Department of Family and Community Services" | 4 AAC 52.590(b)(4) |
| `ak_ilp` | Alaska Infant Learning Program | "Alaska Infant Learning Program ... Part C Coordinator" (contact name omitted) | GUIDE p. 8 |
| `ak_sems` | Alaska Special Education Mediation Services | "Alaska Special Education Mediation Services has qualified mediators who know the laws" | PSN p. 13 |
| `ak_sesa` | Special Education Service Agency | "Special Education Service Agency ... Executive Director" (contact name omitted) | GUIDE p. 8 |
| `ak_ssg` | Stone Soup Group | "Stone Soup Group (Statewide)" | PSN p. 33 |
| `ak_dlc` | Disability Law Center of Alaska | "Disability Law Center of Alaska" | GUIDE p. 8 |
| `ak_links` | LINKS Mat-Su Parent Resource Center | "Developed by LINKS Mat-Su Parent Resource Center for the Department of Education" | GUIDE p. 2 |
| `ak_admin_complaint_form` | Notice of Administrative Complaint | "NOTICE OF ADMINISTRATIVE COMPLAINT The use of this form is optional" | PSN p. 34 |
| `ak_dp_request_form` | Notice of Request for Due Process Hearing | "NOTICE OF REQUEST FOR DUE PROCESS HEARING The use of this form is optional" | PSN p. 36 |
| `ak_aa_checklist` | Alternate Assessment Participation Checklist | "Alternate Assessment Participation Checklist" | ALT |
| `fasd` | Fetal alcohol spectrum disorder | "leukemia, fetal alcohol spectrum disorder, diabetes, or a heightened alertness" | 4 AAC 52.130(k)(1) |
| `unilateral_pl` | Unilateral placement | "4 AAC 52.155. Unilateral placement by parents or other custodians." | 4 AAC 52.155 |
| `pullout` | Pull-out | "some of their services provided in a "pull-out" environment" | GUIDE p. 6 |
| `gross_motor` | Gross motor | "Gross Motor: Movement that involves balance, coordination and large muscle activity" | GUIDE p. 10 |
| `iq` | Intelligence quotient | "Intelligence Quotient (IQ): A way of expressing the score results" | GUIDE p. 10 |
| `norm_ref` | Norm-referenced test | "Norm-referenced Test: Test which compares a learner's performance to an average." | GUIDE p. 10 |

The last six have no `jurisdiction`: they are national ideas that Alaska's documents happen to be the first to attest.

New strings on existing concepts: "cognitive impairment" and "cognitively impaired" (`id`), "deaf and blind" (`deafblind`), "early childhood developmental delay" and the rule's "early childhood development delay" (`dd`), "speech impairment" (`sli`), "teacher of children with visual impairment" (`tvi`), "administrative complaint" (`state_complaint`), "complaint for a due process hearing" (`dp_complaint`), "state special education advisory panel" (`state_panel`), "alternative intervention strategies" (all tagged US-AK); and, untagged, "emotionally disturbed", "orthopedically impaired", "other health impairments", "learning disabilities", "special education aide(s)", "teacher's aide", "compensatory education", "IEP facilitator", "regular classroom teacher", "separate day school", "institutional services", "secondary transition plan", "adaptive physical education", "pre-referral strategies", "DLM Essential Elements" and "present level of academic achievement and functional performance".

## 3. Unsure
- **Cognitive impairment is Alaska's name for intellectual disability.** 4 AAC 52.130(b) and .790(3) never say "intellectual disability". Mapped to `id`, as Michigan's is.
- **"Early childhood development delay"** (.790(3)) looks like a drafting slip for .130(n)'s "early childhood developmental delay". It is current rule text, so it was kept as a spelling variant.
- **Alternative intervention / pre-referral strategies** went on `gen_ed_int` (general education intervention procedures). The glossary describes classroom changes made before a referral, which matches.
- **"Separate day school"** went on `special_school`, and **"institutional services"** on `hospital_instr`.
- **Stone Soup Group** is Alaska's Parent Training and Information Center according to DEED's special education web page, but none of the saved documents say so, so it has no `broader: pti`. If you save that page, add the link.
- **The PSN date.** If DEED confirms a revision date, update the citation.
- **The guide is from 2017** and names contacts who may have changed; only organizations were taken from it.

## 4. Risky
- **Place names (graded high automatically):** `ak_deed`, `ak_ilp`, `ak_sems`, `ak_dlc` ("Alaska") and `ak_links` ("Mat-Su", flagged `place_name` by hand). All are protected only as full phrases.
- **Name-list hits:** "Early" (first name and surname) in the DEED name, "Infant" in the infant learning program, "Stone" in Stone Soup Group, "Law" in the Disability Law Center, "Mat" and "Parent" in the LINKS center, and "Gross" in "Gross motor". "Stone Soup Group" and "Gross motor" are graded low. None collides with the reference scrubber.
- **IQ** is a new two-letter acronym, matched case-sensitively. It is not on the name lists.
- **"Disability Law Center"** is Utah's `dlc_ut`. Alaska's notice uses the same short name, so Alaska's record uses only the full "Disability Law Center of Alaska".

## 5. Left out
- Every person named in the documents (mediation, DEED, parent-center and DLM contacts), plus all addresses, phone numbers and emails.
- The intensive-student funding terms (4 AAC 52.700(c), 52.790(20)-(25): "intensive services", "basic adaptive skills", "individual care", "rudimentary facility"), because the prompt excludes funding formulas. A reviewer might still want "intensive services", since IEPs are written to meet it.
- Nine health problems in 52.130(k)(1) that the federal seed doesn't carry (heart condition, tuberculosis, rheumatic fever, nephritis, asthma, hemophilia, lead poisoning, leukemia, diabetes). Only FASD, which the federal list lacks, was added.
- "Special Education Dispute Resolution" (the PSN's mailing unit), "Alaska Family Directory" (a website), "statewide correspondence study program" (general education), the "National Registry of Interpreters for the Deaf" (national), and general glossary words ("aptitude test", "readiness test", "auditory perception", "multi-sensory").
- "Mat-Su LINKS Parent Resource Center" (GUIDE p. 8), a second spelling of `ak_links`; it can be added with a p. 8 citation.
