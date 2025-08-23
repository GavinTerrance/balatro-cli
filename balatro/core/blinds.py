# balatro/blinds.py

class Blind:
    """Base class for all Blinds (Small, Big, Boss)."""
    def __init__(self, name: str, score_required: int):
        self.name = name
        self.score_required = score_required

    def __repr__(self):
        return f"Blind(name='{self.name}', score_required={self.score_required})"

class SmallBlind(Blind):
    """Represents the Small Blind in the game."""
    def __init__(self):
        super().__init__(
            name="Small Blind",
            score_required=300
        )

class BigBlind(Blind):
    """Represents the Big Blind in the game."""
    def __init__(self):
        super().__init__(
            name="Big Blind",
            score_required=1000
        )

class BossBlind(Blind):
    """Represents a Boss Blind in the game."""
    def __init__(self):
        super().__init__(
            name="Boss Blind",
            score_required=2000
        )


class BlindManager:
    """Keeps track of the current blind and handles advancement."""

    def __init__(self):
        self.blinds = [SmallBlind(), BigBlind(), BossBlind()]
        self.index = 0

    @property
    def current(self) -> Blind:
        return self.blinds[self.index]

    def advance(self) -> bool:
        """Advance to the next blind.

        Returns ``True`` when all blinds have been cleared, signalling that
        the ante should increase.
        """

        self.index += 1
        if self.index >= len(self.blinds):
            self.index = 0
            return True
        return False
