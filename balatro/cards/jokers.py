# balatro/jokers.py

"""This module defines the Joker class and its subclasses, representing different Joker cards in the game."""

import json
from pathlib import Path

from ..shop.stickers import Sticker, StickerType  # Import Sticker class and StickerType

class Joker:
    """Base class for all Joker cards."""
    def __init__(self, name: str, description: str):
        """Initializes a Joker object."

        Args:
            name (str): The name of the Joker.
            description (str): A brief description of the Joker's effect.
        """
        self.name = name
        self.description = description
        self.stickers = [] # New attribute to hold Sticker objects
        self.rounds_active = 0 # For Perishable sticker
        self.is_debuffed = False # For Perishable sticker

    def __repr__(self):
        """Returns a string representation of the Joker object for debugging."""
        return f"Joker(name='{self.name}')"

    def apply_chips(self, chips: int) -> int:
        """Applies any chip modifications from this Joker. Overridden by specific jokers."

        Args:
            chips (int): The current chips value.

        Returns:
            int: The modified chips value.
        """
        if self.is_debuffed:
            return 0 # Debuffed jokers provide no chips
        return chips

    def apply_mult(self, mult: int) -> int:
        """Applies any multiplier modifications from this Joker. Overridden by specific jokers."

        Args:
            mult (int): The current multiplier value.

        Returns:
            int: The modified multiplier value.
        """
        if self.is_debuffed:
            return 0 # Debuffed jokers provide no multiplier
        return mult

    def to_dict(self):
        """Converts the Joker object to a dictionary for serialization."""
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "stickers": [sticker.to_dict() for sticker in self.stickers],
            "rounds_active": self.rounds_active,
            "is_debuffed": self.is_debuffed
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Joker object from a dictionary. This is a factory method for subclasses."""
        # This will be a generic from_dict for the base Joker class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base Joker attributes
        return cls(data["name"], data["description"])

# --- Example Joker Implementations ---

class JokerOfGreed(Joker):
    """A Joker that adds +4 Mult for every hand played."""
    def __init__(self):
        """Initializes a JokerOfGreed object."""
        super().__init__(
            name="Joker of Greed",
            description="Adds +4 Mult for every hand played."
        )
        self.hands_played = 0

    def apply_mult(self, mult: int) -> int:
        """Applies the multiplier bonus based on hands played."""
        return mult + (4 * self.hands_played)

    def to_dict(self):
        """Converts the JokerOfGreed object to a dictionary for serialization."""
        data = super().to_dict()
        data["hands_played"] = self.hands_played
        return data

    @classmethod
    def from_dict(cls, data):
        """Creates a JokerOfGreed object from a dictionary."""
        instance = cls()
        instance.name = data["name"]
        instance.description = data["description"]
        instance.stickers = [Sticker.from_dict(s_data) for s_data in data["stickers"]]
        instance.rounds_active = data["rounds_active"]
        instance.is_debuffed = data["is_debuffed"]
        instance.hands_played = data["hands_played"]
        return instance

class JokerOfMadness(Joker):
    """A Joker that adds a flat +10 Mult."""
    def __init__(self):
        """Initializes a JokerOfMadness object."""
        super().__init__(
            name="Joker of Madness",
            description="Adds a flat +10 Mult."
        )

    def apply_mult(self, mult: int) -> int:
        """Applies the flat multiplier bonus."""
        return mult + 10

    def to_dict(self):
        """Converts the JokerOfMadness object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a JokerOfMadness object from a dictionary."""
        instance = cls()
        instance.name = data["name"]
        instance.description = data["description"]
        instance.stickers = [Sticker.from_dict(s_data) for s_data in data["stickers"]]
        instance.rounds_active = data["rounds_active"]
        instance.is_debuffed = data["is_debuffed"]
        return instance

class ChipJoker(Joker):
    """A Joker that adds +100 Chips."""
    def __init__(self):
        """Initializes a ChipJoker object."""
        super().__init__(
            name="Chip Joker",
            description="Adds +100 Chips."
        )

    def apply_chips(self, chips: int) -> int:
        """Applies the flat chips bonus."""
        return chips + 100

    def to_dict(self):
        """Converts the ChipJoker object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a ChipJoker object from a dictionary."""
        instance = cls()
        instance.name = data["name"]
        instance.description = data["description"]
        instance.stickers = [Sticker.from_dict(s_data) for s_data in data["stickers"]]
        instance.rounds_active = data["rounds_active"]
        instance.is_debuffed = data["is_debuffed"]
        return instance

JOKER_CLASSES = {
    "Joker": Joker,
    "JokerOfGreed": JokerOfGreed,
    "JokerOfMadness": JokerOfMadness,
    "ChipJoker": ChipJoker
}

def joker_from_dict(data):
    """Factory function to create a Joker object from a dictionary."""
    joker_class = JOKER_CLASSES[data["_class"]]
    return joker_class.from_dict(data)


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_jokers():
    """Load joker data from JSON configuration."""
    with open(DATA_DIR / "jokers.json", encoding="utf-8") as f:
        raw = json.load(f)

    jokers = []
    for entry in raw:
        name = entry.get("name", "")
        description = entry.get("effect", "")
        joker = Joker(name, description)
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
