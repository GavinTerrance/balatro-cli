# balatro/jokers.py

class Joker:
    """Base class for all Joker cards."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Joker(name='{self.name}')"

    def apply_chips(self, chips: int) -> int:
        """Apply any chip modifications. Overridden by specific jokers."""
        return chips

    def apply_mult(self, mult: int) -> int:
        """Apply any multiplier modifications. Overridden by specific jokers."""
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
