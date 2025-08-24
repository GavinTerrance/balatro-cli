"""Joker card definitions and loader."""

from __future__ import annotations

import json
from pathlib import Path

from ..shop.stickers import Sticker
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - type hints only
    from ..core.poker import PokerHand


class Joker:
    """Base class for all Joker cards loaded from JSON."""

    def __init__(
        self,
        name: str,
        description: str,
        chip_bonus: int = 0,
        mult_bonus: int = 0,
        mult_multiplier: float = 1.0,
        trigger_hand: "PokerHand" | None = None,
        retrigger: int = 0,
    ) -> None:
        self.name = name
        self.description = description
        self.chip_bonus = chip_bonus
        self.mult_bonus = mult_bonus
        self.mult_multiplier = mult_multiplier
        self.trigger_hand = trigger_hand
        self.retrigger = retrigger
        self.stickers: list[Sticker] = []
        self.rounds_active = 0
        self.is_debuffed = False

    def applies_to(self, hand: "PokerHand") -> bool:
        """Return True if this Joker should apply to the given hand type."""

        return self.trigger_hand is None or self.trigger_hand == hand

    def apply_chips(self, chips: int) -> int:
        """Apply chip modifications from this Joker."""

        if self.is_debuffed:
            return 0
        return chips + self.chip_bonus

    def apply_mult(self, mult: int) -> int:
        """Apply multiplier modifications from this Joker."""

        if self.is_debuffed:
            return 0
        new_mult = mult + self.mult_bonus
        return new_mult * self.mult_multiplier

    def to_dict(self) -> dict:
        """Serialize this Joker to a dict."""

        return {
            "name": self.name,
            "description": self.description,
            "chips": self.chip_bonus,
            "mult": self.mult_bonus,
            "mult_multiplier": self.mult_multiplier,
            "hand": self.trigger_hand.name if self.trigger_hand else None,
            "retrigger": self.retrigger,
            "stickers": [s.to_dict() for s in self.stickers],
            "rounds_active": self.rounds_active,
            "is_debuffed": self.is_debuffed,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Joker":
        """Create a Joker from a serialized dict."""

        from ..core.poker import PokerHand

        hand_str = data.get("hand")
        hand = PokerHand[hand_str] if hand_str else None
        joker = cls(
            data["name"],
            data.get("description", ""),
            chip_bonus=data.get("chips", 0),
            mult_bonus=data.get("mult", 0),
            mult_multiplier=data.get("mult_multiplier", 1.0),
            trigger_hand=hand,
            retrigger=data.get("retrigger", 0),
        )
        joker.stickers = [Sticker.from_dict(s) for s in data.get("stickers", [])]
        joker.rounds_active = data.get("rounds_active", 0)
        joker.is_debuffed = data.get("is_debuffed", False)
        return joker


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_jokers() -> list[Joker]:
    """Load Joker data from JSON configuration."""

    from ..core.poker import PokerHand

    with open(DATA_DIR / "jokers.json", encoding="utf-8") as f:
        raw = json.load(f)

    jokers: list[Joker] = []
    for entry in raw:
        name = entry.get("name", "")
        description = entry.get("effect", "")
        chips = int(entry.get("chips", 0))
        mult = int(entry.get("mult", 0))
        mult_mult = float(entry.get("mult_multiplier", 1))
        hand_str = entry.get("hand")
        trigger_hand = PokerHand[hand_str] if hand_str else None
        retrigger = int(entry.get("retrigger", 0))

        joker = Joker(
            name,
            description,
            chip_bonus=chips,
            mult_bonus=mult,
            mult_multiplier=mult_mult,
            trigger_hand=trigger_hand,
            retrigger=retrigger,
        )

        # Parse cost like "$5" -> 5
        cost_str = str(entry.get("cost", "")).strip()
        if cost_str.startswith("$"):
            cost_str = cost_str[1:]
        try:
            joker.cost = int(cost_str)
        except (ValueError, TypeError):
            joker.cost = 0
        joker.rarity = entry.get("rarity")
        jokers.append(joker)

    return jokers


def joker_from_dict(data: dict) -> Joker:
    """Recreate a ``Joker`` instance from serialized data."""

    return Joker.from_dict(data)

