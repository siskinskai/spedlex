"""Adapter that reports no collisions: risk grades then rest on the
reference name lists alone."""

NAME = "none"
NAME_DICT_PREFIX = "NAME_DICT"


def collisions(text: str) -> list[str]:
    return []
