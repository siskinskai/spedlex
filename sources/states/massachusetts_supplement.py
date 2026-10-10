"""
Massachusetts layer, consistency additions.

A second reading of the Massachusetts layer's parent guide for agencies,
organizations and terms the first pass left out.
Read 2026-10-10 by text extraction through a web fetch, not from a saved,
hashed copy, so the sources are cited by URL like the rest of this early layer
and every record is a 'candidate'. See provenance/early-layers-reread-2026-10-10.md.

Sources reviewed 2026-10-10:
  PG  FCSN/Massachusetts DOE, A Parent's Guide to Special Education, cited by page

Left out on purpose: the Massachusetts Department of Mental Retardation
(p. 36), an older agency name containing a disfavored term; the maintainer
can decide whether to record it as legacy. "PAL" (Parent Professional Advocacy
League) is recorded only in full.
"""

from .massachusetts import src, A, S, V, L, AB, P, MA, MAJ

STRINGS = [
    ("ch766", [("MGL c. 71B", AB, MA)], src("PG", "p. 8")),
]

CONCEPTS = [
    ("masspac", "Massachusetts Association of Special Education Parent Advisory Councils", "legal_procedural",
     [("MASSPAC", A, MA)], src("PG", "p. 35"), MAJ),
    ("ma_pal", "Parent Professional Advocacy League", "legal_procedural", [], src("PG", "p. 35"), MAJ),
    ("ma_mcb", "Massachusetts Commission for the Blind", "legal_procedural", [], src("PG", "p. 36"), MAJ),
    ("ma_mcdhh", "Massachusetts Commission for the Deaf and Hard of Hearing", "legal_procedural",
     [("Massachusetts Commission for Deaf and Hard of Hearing", V, MA)], src("PG", "p. 36"), MAJ),
    ("ma_mrc", "Massachusetts Rehabilitation Commission", "legal_procedural", [], src("PG", "p. 36"), MAJ),
    ("ma_dmh", "Massachusetts Department of Mental Health", "legal_procedural", [], src("PG", "p. 36"), MAJ),
    ("ma_dph", "Massachusetts Department of Public Health", "legal_procedural", [], src("PG", "p. 36"), MAJ),
    ("ma_dss", "Massachusetts Department of Social Services", "legal_procedural", [], src("PG", "p. 36"),
     {**MAJ, "note": "An older agency name (now the Department of Children and Families)."}),
    ("ma_eohhs", "Executive Office of Health and Human Services", "legal_procedural", [], src("PG", "p. 36"), MAJ),
    ("ma_btp", "Bureau of Transitional Planning", "transition", [], src("PG", "p. 36"), MAJ),
    ("ma_sliding_fee", "Sliding fee scale", "legal_procedural", [], src("PG", "p. 17"),
     {**MAJ, "note": "Cost sharing for an independent educational evaluation, by family income."}),
    ("instructional_supports", "Instructional supports", "accommodation_modification", [], src("PG", "p. 11"), {}),
    ("ma_student_vision", "Student vision", "iep_component", [], src("PG", "p. 20"), MAJ),
    ("ma_era", "Massachusetts Education Reform Act", "legal_procedural", [], src("PG", "p. 23"), MAJ),
]

# Read through a web fetch, not from a hashed copy: keep every new record a candidate.
CONCEPTS = [(*c[:5], {**c[5], "status": "candidate"}) for c in CONCEPTS]

JURISDICTION = "US-MA"
LAYER_NAME = "Massachusetts (consistency additions)"
RETRIEVED = "2026-10-10"
ASSISTED_BY = "claude-opus-5-5"
VERSION_ADDED = "0.51.0"
