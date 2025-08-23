# balatro/jokers.py

from .stickers import Sticker, StickerType # Import Sticker class and StickerType

class Joker:
    """Base class for all Joker cards."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.stickers = [] # New attribute to hold Sticker objects

    def __repr__(self):
        return f"Joker(name='{self.name}')"

    class Joker:
    """Base class for all Joker cards."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.stickers = [] # New attribute to hold Sticker objects
        self.rounds_active = 0 # For Perishable sticker
        self.is_debuffed = False # For Perishable sticker

    def apply_chips(self, chips: int) -> int:
        """Apply any chip modifications. Overridden by specific jokers."""
        if self.is_debuffed:
            return 0 # Debuffed jokers provide no chips
        return chips

    def apply_mult(self, mult: int) -> int:
        """Apply any multiplier modifications. Overridden by specific jokers."""
        if self.is_debuffed:
            return 0 # Debuffed jokers provide no multiplier
        return mult

    def to_dict(self):
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
        # This will be a generic from_dict for the base Joker class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base Joker attributes
        return cls(data["name"], data["description"])

# --- Example Joker Implementations ---

class JokerOfGreed(Joker):
    def __init__(self):
        super().__init__(
            name="Joker of Greed",
            description="Adds +4 Mult for every hand played."
        )
        self.hands_played = 0

    def apply_mult(self, mult: int) -> int:
        return mult + (4 * self.hands_played)

    def to_dict(self):
        data = super().to_dict()
        data["hands_played"] = self.hands_played
        return data

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.name = data["name"]
        instance.description = data["description"]
        instance.stickers = [Sticker.from_dict(s_data) for s_data in data["stickers"]]
        instance.rounds_active = data["rounds_active"]
        instance.is_debuffed = data["is_debuffed"]
        instance.hands_played = data["hands_played"]
        return instance

class JokerOfMadness(Joker):
    def __init__(self):
        super().__init__(
            name="Joker of Madness",
            description="Adds a flat +10 Mult."
        )

    def apply_mult(self, mult: int) -> int:
        return mult + 10

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.name = data["name"]
        instance.description = data["description"]
        instance.stickers = [Sticker.from_dict(s_data) for s_data in data["stickers"]]
        instance.rounds_active = data["rounds_active"]
        instance.is_debuffed = data["is_debuffed"]
        return instance

class ChipJoker(Joker):
    def __init__(self):
        super().__init__(
            name="Chip Joker",
            description="Adds +100 Chips."
        )

    def apply_chips(self, chips: int) -> int:
        return chips + 100

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
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
    joker_class = JOKER_CLASSES[data["_class"]]
    return joker_class.from_dict(data)
