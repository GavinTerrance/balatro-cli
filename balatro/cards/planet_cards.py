from enum import Enum
from ..core.poker import PokerHand  # Import PokerHand for type hinting

class PlanetCardType(Enum):
    PLUTO = "Pluto"
    MERCURY = "Mercury"
    URANUS = "Uranus"
    VENUS = "Venus"
    SATURN = "Saturn"
    JUPITER = "Jupiter"
    EARTH = "Earth"
    MARS = "Mars"
    NEPTUNE = "Neptune"
    PLANET_X = "Planet X"
    CERES = "Ceres"
    ERIS = "Eris"

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
        """Human-readable summary used by the CLI when listing cards.

        Defining ``description`` as a property guarantees the attribute is
        available even if a ``PlanetCard`` is instantiated in an unexpected way
        (e.g. through deserialisation that bypasses ``__init__``).
        """
        chips = getattr(self, "chips_bonus", 0)
        mult = getattr(self, "mult_bonus", 0)
        hand = getattr(self, "poker_hand_type", "Unknown")
        return f"+{chips} Chips, +{mult} Mult for {hand}"

    def __repr__(self):
        return f"PlanetCard(name='{self.name}')"

    def apply_effect(self, game):
        # This will be implemented later when poker hand leveling is in place
        print(f"{self.name} used: Levels up {self.poker_hand_type} (effect not yet implemented).")

    def to_dict(self):
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "chips_bonus": self.chips_bonus,
            "mult_bonus": self.mult_bonus,
            "poker_hand_type": self.poker_hand_type,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        # This will be a generic from_dict for the base PlanetCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base PlanetCard attributes
        return cls(data["name"], data["chips_bonus"], data["mult_bonus"], data["poker_hand_type"], data["cost"])

# --- Implementations for each Planet Card ---

class Pluto(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.PLUTO.value,
            chips_bonus=10,
            mult_bonus=1,
            poker_hand_type="High Card"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Mercury(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.MERCURY.value,
            chips_bonus=15,
            mult_bonus=1,
            poker_hand_type="Pair"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Uranus(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.URANUS.value,
            chips_bonus=20,
            mult_bonus=1,
            poker_hand_type="Two Pair"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Venus(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.VENUS.value,
            chips_bonus=20,
            mult_bonus=2,
            poker_hand_type="Three of a Kind"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Saturn(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.SATURN.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Straight"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Jupiter(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.JUPITER.value,
            chips_bonus=15,
            mult_bonus=2,
            poker_hand_type="Flush"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Earth(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.EARTH.value,
            chips_bonus=25,
            mult_bonus=2,
            poker_hand_type="Full House"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Mars(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.MARS.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Four of a Kind"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Neptune(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.NEPTUNE.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Straight Flush"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class PlanetX(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.PLANET_X.value,
            chips_bonus=35,
            mult_bonus=3,
            poker_hand_type="Five of a Kind"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Ceres(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.CERES.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Flush House"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Eris(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.ERIS.value,
            chips_bonus=50,
            mult_bonus=3,
            poker_hand_type="Flush Five"
        )

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

PLANET_CARD_CLASSES = {
    "PlanetCard": PlanetCard,
    "Pluto": Pluto,
    "Mercury": Mercury,
    "Uranus": Uranus,
    "Venus": Venus,
    "Saturn": Saturn,
    "Jupiter": Jupiter,
    "Earth": Earth,
    "Mars": Mars,
    "Neptune": Neptune,
    "PlanetX": PlanetX,
    "Ceres": Ceres,
    "Eris": Eris
}
def planet_card_from_dict(data):
    """Factory function to create a PlanetCard object from a dictionary."""
    planet_card_class = PLANET_CARD_CLASSES[data["_class"]]
    return planet_card_class(data["name"], data["chips_bonus"], data["mult_bonus"], data["poker_hand_type"], data["cost"])

