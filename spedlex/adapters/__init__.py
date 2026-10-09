"""Scrubber collision adapters.

The build asks one adapter which of its redaction patterns would fire on
each safelist string. The answers are stored in pii_risk.scrubber_collisions
so integrators can see, before deploying, which protected terms their
scrubber would otherwise destroy.

An adapter is a module with:
    NAME              short identifier, e.g. "scrub"
    NAME_DICT_PREFIX  hits starting with this come from a first-name
                      dictionary; they make a concept high risk
    collisions(text)  list of hit labels for every pattern that matches
                      any part of text, e.g. ["PHONE", "NAME_COMMON_DICT:Rosa"]

To test SPEDLex against your own scrubber, copy scrub.py, replace its
patterns, register it in ADAPTERS below, and run
    python -m spedlex.build --adapter yourname --out /tmp/report
The published data is always built with the default adapter.
"""

from importlib import import_module

ADAPTERS = {"scrub": "spedlex.adapters.scrub", "none": "spedlex.adapters.none"}
DEFAULT = "scrub"


def get_adapter(name: str = DEFAULT):
    if name not in ADAPTERS:
        raise SystemExit(f"unknown adapter {name!r}; choose from {sorted(ADAPTERS)}")
    return import_module(ADAPTERS[name])
