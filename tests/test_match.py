"""The safety property and the matching rules of the reference matcher."""

import pytest

from spedlex import Safelist
from spedlex.risk import FIRST_NAMES, PLACE_NAMES, POSTAL_CODES, SURNAMES, assess_risk

ALL = Safelist.from_default(statuses={"candidate", "machine_validated", "expert_accepted", "illustrative"})


def protected(sl, text):
    return [m.text for m in sl.find(text)]


def test_never_shelters_a_capitalized_name():
    """No first name or surname, written as a name, is ever protected."""
    sheltered = [n for n in sorted(FIRST_NAMES | SURNAMES)
                 if ALL.find(f"Today {n.capitalize()} came.")]
    assert sheltered == []


def test_all_caps_name_collisions_are_only_known_acronyms():
    """All-caps forms like LEA or ED are protected on purpose: they are
    matched case-sensitively, so the names Lea and Ed are not. Any new entry
    here needs a reviewer's eye."""
    known = {"ADA", "ADD", "ALTA", "ASHA", "ED", "ELL", "IDA", "LEA", "REED", "SOL", "TEA"}
    hits = {n.upper() for n in FIRST_NAMES | SURNAMES if ALL.find(f"Today {n.upper()} came.")}
    assert hits <= known, f"new all-caps collisions to review: {sorted(hits - known)}"


def test_never_shelters_a_bare_place_name():
    """No state or territory name is ever protected on its own."""
    sheltered = [p for p in sorted(PLACE_NAMES)
                 if any(m.text.lower() == p.lower() for m in ALL.find(f"The family moved to {p} last year."))]
    assert sheltered == []


def test_bare_postal_codes_are_only_known_acronyms():
    """Some postal codes are also special-education acronyms (ID is
    intellectual disability, VI visual impairment). Any new one here needs a
    reviewer's eye."""
    known = {"HI", "ID", "MD", "PR", "VI"}
    hits = {c for c in POSTAL_CODES if any(m.text == c for m in ALL.find(f"The family moved to {c} last year."))}
    assert hits <= known, f"new postal-code collisions to review: {sorted(hits - known)}"


def test_place_names_make_a_concept_high_risk():
    class NoScrubber:
        NAME_DICT_PREFIX = "NAME"

        def collisions(self, text):
            return []

    def grade(*texts):
        strings = [{"text": t, "match": "phrase_ci"} for t in texts]
        return assess_risk(strings, [], NoScrubber())

    for text in ("Georgia Milestones", "Strong Start DC", "D.C. Language Access Act of 2004", "WA-AIM",
                 "Hawai\u02bbi State Department of Education", "Hawai'i State Department of Education"):
        r = grade(text)
        assert r["level"] == "high" and "place_name" in r["reasons"], text
    # One-word acronyms that match postal codes are not places, nor are reviewed exceptions.
    for text in ("ID", "MD", "HI", "CT services"):
        assert "place_name" not in grade(text)["reasons"], text


def test_acronyms_are_case_sensitive():
    assert protected(ALL, "ED is met; Ed attends.") == ["ED"]


def test_eponym_alone_is_not_protected_but_full_title_is():
    text = "Kaufman scored the Kaufman Assessment Battery for Children, Second Edition."
    assert protected(ALL, text) == ["Kaufman Assessment Battery for Children, Second Edition"]


def test_longest_match_wins():
    assert protected(ALL, "We held an ARD committee meeting.") == ["ARD committee meeting"]
    assert protected(ALL, "The ARD committee met.") == ["ARD committee"]


def test_class_ratio_does_not_match_inside_a_time():
    assert protected(ALL, "a 12:1+1 class at 12:15") == ["12:1+1"]


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December", "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep",
          "Sept", "Oct", "Nov", "Dec"]
DATE_FORMATS = ["DOB: {m} 14, 2015", "DOB: 14 {m} 2015", "DOB: 14-{m}-15", "born {m} 2015",
                "DOB {m}. 3, 2016", "{m}/14/2015", "born on the 3rd {m} 2016", "DOB:{m}14,2015"]


def test_never_shelters_a_month_inside_a_date():
    """A month name or abbreviation next to a number is part of a date, which
    may be a date of birth, so it is never protected, even when the same
    letters are an acronym ("APR", Annual Performance Report)."""
    sheltered = [(fmt, form) for m in MONTHS for form in {m, m.upper(), m.lower()} for fmt in DATE_FORMATS
                 if any(x.text.rstrip(".").lower() == m.lower() for x in ALL.find(fmt.format(m=form)))]
    assert sheltered == []


def test_month_shaped_acronym_is_protected_away_from_dates():
    assert protected(ALL, "The state submitted its APR to OSEP.") == ["APR", "OSEP"]
    assert protected(ALL, "Annual Performance Report (APR) for FFY 2022") == ["Annual Performance Report", "APR"]


def test_household_names_override_the_safelist():
    sl = Safelist.from_default(household_names={"Rosa"})
    assert protected(sl, "Rosa's Law applies.") == []
    assert protected(Safelist.from_default(), "Rosa's Law applies.") == ["Rosa's Law"]


def test_jurisdiction_filter_keeps_federal_and_named_states():
    tx = Safelist.from_default(jurisdictions={"US-TX"})
    assert "ARD committee" in protected(tx, "the ARD committee")
    assert protected(tx, "Georgia Milestones") == []


def test_illustrative_placeholders_are_excluded_by_default():
    assert protected(Safelist.from_default(), "the WISC-V") == []
    assert protected(ALL, "the WISC-V") == ["WISC-V"]


def test_protect_and_restore_round_trip():
    sl = Safelist.from_default()
    text = "Rosa's Law and FAPE; call Rosa at 555-123-4567."
    masked, restore = sl.protect(text)
    assert "Rosa's Law" not in masked and "FAPE" not in masked
    scrubbed = masked.replace("Rosa", "[NAME]").replace("555-123-4567", "[PHONE]")
    assert restore(scrubbed) == "Rosa's Law and FAPE; call [NAME] at [PHONE]."


@pytest.mark.parametrize("state", ["Virginia", "Florida", "Georgia", "Carolina"])
def test_bare_state_names_are_not_protected(state):
    assert protected(ALL, f"{state} came to the meeting.") == []


def test_possessive_eponym_alone_is_not_protected():
    assert protected(ALL, "Met with Tourette's today.") == []
    assert protected(ALL, "Diagnosed with Tourette syndrome.") == ["Tourette syndrome"]
