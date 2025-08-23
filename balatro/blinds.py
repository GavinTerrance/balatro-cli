# balatro/blinds.py

class Blind:
    """Base class for all Blinds (Small, Big, Boss)."""
    def __init__(self, name: str, score_required: int):
        self.name = name
        self.score_required = score_required

    def __repr__(self):
        return f"Blind(name='{self.name}', score_required={self.score_required})"

class SmallBlind(Blind):
    def __init__(self):
        super().__init__(
            name="Small Blind",
            score_required=300
        )

class BigBlind(Blind):
    def __init__(self):
        super().__init__(
            name="Big Blind",
            score_required=1000
        )

class BossBlind(Blind):
    def __init__(self):
        super().__init__(
            name="Boss Blind",
            score_required=2000
        )
