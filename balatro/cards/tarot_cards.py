"""Tarot card definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
from pathlib import Path


class TarotCard:
    """Simple representation of a Tarot card."""

    def __init__(self, name: str, description: str, cost: int = 0) -> None:
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self) -> str:  # pragma: no cover - simple repr
        return f"TarotCard(name='{self.name}')"

    def apply_effect(self, game) -> None:  # pragma: no cover - placeholder
        """Apply the tarot card's effect.

        The project does not yet model individual tarot card effects. This
        placeholder prevents runtime errors when a card is used.
        """

        print(f"{self.name} used: {self.description} (effect not yet implemented).")

    def to_dict(self) -> dict:
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TarotCard":
        return cls(data["name"], data["description"], data.get("cost", 0))


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_tarot_cards() -> list[TarotCard]:
    """Load tarot cards from the JSON data file."""

    with open(DATA_DIR / "tarot_cards.json", encoding="utf-8") as f:
        raw = json.load(f)

    cards = []
    for entry in raw:
        card = TarotCard(
            name=entry.get("name", ""),
            description=entry.get("description", ""),
            cost=3,
        )
        cards.append(card)

    return cards


def tarot_card_from_dict(data: dict) -> TarotCard:
    """Recreate a ``TarotCard`` instance from serialized data."""

    return TarotCard.from_dict(data)

