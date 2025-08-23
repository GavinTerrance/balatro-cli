import json
import re
from pathlib import Path


class PlanetCard:
    def __init__(
        self,
        name: str,
        chips_bonus: int,
        mult_bonus: int,
        poker_hand_type: str,
        cost: int = 3,
    ):
        self.name = name
        self.chips_bonus = chips_bonus
        self.mult_bonus = mult_bonus
        self.poker_hand_type = poker_hand_type
        self.cost = cost

    @property
    def description(self) -> str:
        chips = getattr(self, "chips_bonus", 0)
        mult = getattr(self, "mult_bonus", 0)
        hand = getattr(self, "poker_hand_type", "Unknown")
        return f"+{chips} Chips, +{mult} Mult for {hand}"

    def __repr__(self):
        return f"PlanetCard(name='{self.name}')"

    def apply_effect(self, game):
        # This will be implemented later when poker hand leveling is in place
        print(
            f"{self.name} used: Levels up {self.poker_hand_type} (effect not yet implemented)."
        )

    def to_dict(self):
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "chips_bonus": self.chips_bonus,
            "mult_bonus": self.mult_bonus,
            "poker_hand_type": self.poker_hand_type,
            "cost": self.cost,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["chips_bonus"],
            data["mult_bonus"],
            data["poker_hand_type"],
            data.get("cost", 3),
        )


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_planet_cards():
    """Load planet card data from JSON configuration."""
    with open(DATA_DIR / "planet_cards.json", encoding="utf-8") as f:
        raw = json.load(f)

    cards = []
    for entry in raw:
        addition = entry.get("addition", "")
        match = re.search(r"\+(\d+)\s*Mult.*\+(\d+)\s*Chips", addition)
        mult = int(match.group(1)) if match else 0
        chips = int(match.group(2)) if match else 0
        card = PlanetCard(
            name=entry["name"],
            chips_bonus=chips,
            mult_bonus=mult,
            poker_hand_type=entry.get("poker_hand", ""),
        )
        cards.append(card)

    return cards


def planet_card_from_dict(data):
    """Recreate a ``PlanetCard`` instance from serialized data."""
    return PlanetCard.from_dict(data)

