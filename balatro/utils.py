from __future__ import annotations

"""Utility helpers for the Balatro CLI project."""

import math

from .cards.cards import Edition


def get_user_input(prompt: str) -> str:
    """Prompt the user for input and allow exiting the game.

    If the user enters ``exit``, ``quit`` or ``q`` (case-insensitive),
    a :class:`SystemExit` is raised so that the program terminates
    gracefully.  Otherwise the raw input string is returned.
    """
    response = input(prompt)
    if response.strip().lower() in {"exit", "quit", "q"}:
        print("Exiting game.")
        raise SystemExit
    return response


def calculate_sell_value(item) -> int:
    """Return the sell value for a Joker or consumable item."""

    base = getattr(item, "sell_value", None)
    if base is None:
        cost = getattr(item, "cost", 0)
        base = math.floor(cost / 2)
    base = max(1, int(base))
    edition = getattr(item, "edition", Edition.NONE)
    bonus_map = {
        Edition.FOIL: 2,
        Edition.HOLOGRAPHIC: 3,
        Edition.POLYCHROME: 5,
        Edition.NEGATIVE: 5,
    }
    return base + bonus_map.get(edition, 0)
