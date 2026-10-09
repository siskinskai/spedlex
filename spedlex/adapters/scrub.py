"""Collision adapter for SCRUB, an offline de-identification tool for
special-education documents and the first tool to use SPEDLex. It is the
build's default reference scrubber.

This is a copy of SCRUB's redaction patterns and its first-name dictionary
(SCRUB's lowest-confidence redaction tier) (scrub_first_names.txt, from the dominictarr/random-name word
list, with common English words and U.S. state names removed exactly as
SCRUB removes them). Docstrings and unrelated methods are trimmed. If
SCRUB's patterns change, update this file and rebuild.

Adapter contract (see adapters/__init__.py): NAME, NAME_DICT_PREFIX, and
collisions(text) -> list of hit labels.
"""

import re
from pathlib import Path
from typing import Optional, Iterable

NAME = "scrub"
NAME_DICT_PREFIX = "NAME_COMMON_DICT"

_STATE_NAME_COLLISIONS = {
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Tennessee", "Texas", "Utah",
    "Vermont", "Virginia", "Washington", "Wisconsin", "Wyoming",
    # parts of multi-word names: New Hampshire, New Jersey, New Mexico,
    # New York, North/South Carolina, North/South Dakota, Rhode Island,
    # District of Columbia, Puerto Rico
    "Hampshire", "Jersey", "Mexico", "York", "Carolina", "Dakota",
    "Rhode", "Island", "Columbia", "Puerto", "Rico", "Guam", "Samoa",
}

_COMMON_WORD_NAME_COLLISIONS = {
    "Hope", "Grace", "Faith", "Dawn", "Summer", "June", "May", "April",
    "Will", "Mark", "Rose", "Lily", "Ivy", "Joy", "Patience", "Charity",
    "Sky", "Star", "Honor", "Promise", "Genesis", "Trinity",
}


def _load_common_first_names(source_path: Optional[Path] = None) -> frozenset:
    if source_path is None:
        source_path = Path(__file__).parent / "scrub_first_names.txt"
    try:
        raw_names = source_path.read_text(encoding="utf-8").splitlines()
    except (FileNotFoundError, OSError):
        return frozenset()
    names = {n.strip() for n in raw_names if n.strip()}
    names -= _COMMON_WORD_NAME_COLLISIONS
    names -= _STATE_NAME_COLLISIONS
    return frozenset(names)


_COMMON_FIRST_NAMES = _load_common_first_names()


def _build_common_name_pattern(names: Iterable[str]) -> Optional[re.Pattern]:
    names = sorted(names, key=len, reverse=True)
    if not names:
        return None
    return re.compile(r"\b(?:" + "|".join(re.escape(n) for n in names) + r")\b")


_COMMON_NAME_PATTERN = _build_common_name_pattern(_COMMON_FIRST_NAMES)

PII_PATTERNS: dict[str, re.Pattern] = {
    "PHONE": re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"),
    "SSN": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "EMAIL": re.compile(r"\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", re.IGNORECASE),
    "NAME_TITLE": re.compile(r"\b(?:Dr|Mr|Mrs|Ms|Mx)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\b"),
    "NAME_KINSHIP": re.compile(
        r"\b(?i:grandma|grandpa|grandmother|grandfather|mom|mother|dad|"
        r"father|son|daughter|caregiver|aunt|uncle|sister|brother)\s+"
        r"([A-Z][a-z]+)\b",
    ),
    "ADDRESS_STREET": re.compile(
        r"\b\d{1,5}\s+[A-Z][a-zA-Z]*(?:\s[A-Z][a-zA-Z]*)*\s"
        r"(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|"
        r"Blvd|Court|Ct|Way|Place|Pl)\b\.?",
    ),
    "ADDRESS_ZIP": re.compile(r"\b\d{5}(?:-\d{4})?\b"),
    "PHI_RECORD_ID": re.compile(
        r"\b(?:Patient\s?ID|MRN|Medical\s+Record\s+Number|Record\s?ID)"
        r"[:\s]*[#-]?\s*(?:MRN[-\s]?)?\d{4,10}\b",
        re.IGNORECASE,
    ),
    "PHI_MEDICATION_DOSE": re.compile(r"\b\d+\s?(?:mg|mcg|ml|milligrams?|micrograms?)\b", re.IGNORECASE),
}


def collisions(text: str) -> list[str]:
    """Return the scrubber tiers/patterns that would redact any part of text."""
    hits = [name for name, p in PII_PATTERNS.items() if p.search(text)]
    if _COMMON_NAME_PATTERN is not None:
        for m in _COMMON_NAME_PATTERN.finditer(text):
            hits.append(f"NAME_COMMON_DICT:{m.group()}")
    return hits
