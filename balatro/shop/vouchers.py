"""Voucher definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
from pathlib import Path


class Voucher:
    """Simple representation of a shop voucher."""

    def __init__(self, name: str, description: str, cost: int = 0) -> None:
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self) -> str:  # pragma: no cover - simple repr
        return f"Voucher(name='{self.name}', cost={self.cost})"

    def apply_effect(self, game) -> None:  # pragma: no cover - simple effects
        """Apply this voucher's effect."""

        effects = {
            "Crystal Ball": lambda g: setattr(g.player, "consumable_slots", g.player.consumable_slots + 1),
            "Grabber": lambda g: setattr(g.player, "hands", g.player.hands + 1),
            "Wasteful": lambda g: setattr(g.player, "discards", g.player.discards + 1),
        }

        func = effects.get(self.name)
        if func:
            func(game)
        print(f"{self.name} activated: {self.description}")

    def to_dict(self) -> dict:
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Voucher":
        return cls(data["name"], data.get("description", ""), data.get("cost", 0))


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_vouchers() -> list[Voucher]:
    """Load voucher definitions from the JSON data file."""

    with open(DATA_DIR / "vouchers.json", encoding="utf-8") as f:
        raw = json.load(f)

    vouchers: list[Voucher] = []
    for entry in raw:
        voucher = Voucher(
            name=entry.get("base_name", ""),
            description=entry.get("base_effect", ""),
            cost=10,  # default shop price; Shop may override
        )
        vouchers.append(voucher)

    return vouchers


def voucher_from_dict(data: dict) -> Voucher:
    """Recreate a :class:`Voucher` instance from serialized data."""

    return Voucher.from_dict(data)
