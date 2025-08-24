"""Spectral card definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
from pathlib import Path


class SpectralCard:
    """Simple representation of a Spectral card."""

    def __init__(self, name: str, description: str, cost: int = 4) -> None:
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self) -> str:  # pragma: no cover - simple repr
        return f"SpectralCard(name='{self.name}')"

    def apply_effect(self, game) -> None:  # pragma: no cover - placeholder
        """Apply the spectral card's effect.

        The project does not yet model individual spectral card effects. This
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
    def from_dict(cls, data: dict) -> "SpectralCard":
        return cls(data["name"], data["description"], data.get("cost", 4))


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_spectral_cards() -> list[SpectralCard]:
    """Load spectral cards from the JSON data file."""

    with open(DATA_DIR / "spectral_cards.json", encoding="utf-8") as f:
        raw = json.load(f)

    cards = []
    for entry in raw:
        card = SpectralCard(
            name=entry.get("name", ""),
            description=entry.get("effect", ""),
            cost=4,
        )
        cards.append(card)

    return cards


def spectral_card_from_dict(data: dict) -> SpectralCard:
    """Recreate a ``SpectralCard`` instance from serialized data."""

    return SpectralCard.from_dict(data)
