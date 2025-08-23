# balatro/jokers.py

from .stickers import Sticker # Import Sticker class

class Joker:
    """Base class for all Joker cards."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.stickers = [] # New attribute to hold Sticker objects

    def __repr__(self):
        return f"Joker(name='{self.name}')"

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

class JokerOfMadness(Joker):
    def __init__(self):
        super().__init__(
            name="Joker of Madness",
            description="Adds a flat +10 Mult."
        )

    def apply_mult(self, mult: int) -> int:
        return mult + 10

class ChipJoker(Joker):
    def __init__(self):
        super().__init__(
            name="Chip Joker",
            description="Adds +100 Chips."
        )

    def apply_chips(self, chips: int) -> int:
        return chips + 100
