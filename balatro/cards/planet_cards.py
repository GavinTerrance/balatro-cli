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
    def __init__(self, name: str, chips_bonus: int, mult_bonus: int, poker_hand_type: str, cost: int = 3):
        self.name = name
        self.chips_bonus = chips_bonus
        self.mult_bonus = mult_bonus
        self.poker_hand_type = poker_hand_type
        self.cost = cost

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

"""This module defines the PlanetCard class and its subclasses, representing different Planet cards in the game."""

from enum import Enum
from .poker import PokerHand # Import PokerHand for type hinting

class PlanetCardType(Enum):
    """Represents the type of Planet card."""
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
    """Base class for all Planet cards."""
    def __init__(self, name: str, chips_bonus: int, mult_bonus: int, poker_hand_type: str, cost: int = 3):
        """Initializes a PlanetCard object."

        Args:
            name (str): The name of the Planet card.
            chips_bonus (int): The chips bonus provided by the card.
            mult_bonus (int): The multiplier bonus provided by the card.
            poker_hand_type (str): The poker hand type associated with this card.
            cost (int, optional): The cost of the card in the shop. Defaults to 3.
        """
        self.name = name
        self.chips_bonus = chips_bonus
        self.mult_bonus = mult_bonus
        self.poker_hand_type = poker_hand_type
        self.cost = cost

    def __repr__(self):
        """Returns a string representation of the PlanetCard object for debugging."""
        return f"PlanetCard(name='{self.name}')"

    def apply_effect(self, game):
        """Applies the Planet card's effect to the game state."""
        # This will be implemented later when poker hand leveling is in place
        print(f"{self.name} used: Levels up {self.poker_hand_type} (effect not yet implemented).")

    def to_dict(self):
        """Converts the PlanetCard object to a dictionary for serialization."""
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
        """Creates a PlanetCard object from a dictionary. This is a factory method for subclasses."""
        # This will be a generic from_dict for the base PlanetCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base PlanetCard attributes
        return cls(data["name"], data["chips_bonus"], data["mult_bonus"], data["poker_hand_type"], data["cost"])

# --- Implementations for each Planet Card ---

class Pluto(PlanetCard):
    """Represents the Pluto Planet card, associated with High Card."""
    def __init__(self):
        """Initializes a Pluto PlanetCard."""
        super().__init__(
            name=PlanetCardType.PLUTO.value,
            chips_bonus=10,
            mult_bonus=1,
            poker_hand_type="High Card"
        )

    def to_dict(self):
        """Converts the Pluto PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Pluto PlanetCard object from a dictionary."""
        return cls()

class Mercury(PlanetCard):
    """Represents the Mercury Planet card, associated with Pair."""
    def __init__(self):
        """Initializes a Mercury PlanetCard."""
        super().__init__(
            name=PlanetCardType.MERCURY.value,
            chips_bonus=15,
            mult_bonus=1,
            poker_hand_type="Pair"
        )

    def to_dict(self):
        """Converts the Mercury PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Mercury PlanetCard object from a dictionary."""
        return cls()

class Uranus(PlanetCard):
    """Represents the Uranus Planet card, associated with Two Pair."""
    def __init__(self):
        """Initializes a Uranus PlanetCard."""
        super().__init__(
            name=PlanetCardType.URANUS.value,
            chips_bonus=20,
            mult_bonus=1,
            poker_hand_type="Two Pair"
        )

    def to_dict(self):
        """Converts the Uranus PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Uranus PlanetCard object from a dictionary."""
        return cls()

class Venus(PlanetCard):
    """Represents the Venus Planet card, associated with Three of a Kind."""
    def __init__(self):
        """Initializes a Venus PlanetCard."""
        super().__init__(
            name=PlanetCardType.VENUS.value,
            chips_bonus=20,
            mult_bonus=2,
            poker_hand_type="Three of a Kind"
        )

    def to_dict(self):
        """Converts the Venus PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Venus PlanetCard object from a dictionary."""
        return cls()

class Saturn(PlanetCard):
    """Represents the Saturn Planet card, associated with Straight."""
    def __init__(self):
        """Initializes a Saturn PlanetCard."""
        super().__init__(
            name=PlanetCardType.SATURN.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Straight"
        )

    def to_dict(self):
        """Converts the Saturn PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Saturn PlanetCard object from a dictionary."""
        return cls()

class Jupiter(PlanetCard):
    """Represents the Jupiter Planet card, associated with Flush."""
    def __init__(self):
        """Initializes a Jupiter PlanetCard."""
        super().__init__(
            name=PlanetCardType.JUPITER.value,
            chips_bonus=15,
            mult_bonus=2,
            poker_hand_type="Flush"
        )

    def to_dict(self):
        """Converts the Jupiter PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Jupiter PlanetCard object from a dictionary."""
        return cls()

class Earth(PlanetCard):
    """Represents the Earth Planet card, associated with Full House."""
    def __init__(self):
        """Initializes an Earth PlanetCard."""
        super().__init__(
            name=PlanetCardType.EARTH.value,
            chips_bonus=25,
            mult_bonus=2,
            poker_hand_type="Full House"
        )

    def to_dict(self):
        """Converts the Earth PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Earth PlanetCard object from a dictionary."""
        return cls()

class Mars(PlanetCard):
    """Represents the Mars Planet card, associated with Four of a Kind."""
    def __init__(self):
        """Initializes a Mars PlanetCard."""
        super().__init__(
            name=PlanetCardType.MARS.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Four of a Kind"
        )

    def to_dict(self):
        """Converts the Mars PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Mars PlanetCard object from a dictionary."""
        return cls()

class Neptune(PlanetCard):
    """Represents the Neptune Planet card, associated with Straight Flush."""
    def __init__(self):
        """Initializes a Neptune PlanetCard."""
        super().__init__(
            name=PlanetCardType.NEPTUNE.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Straight Flush"
        )

    def to_dict(self):
        """Converts the Neptune PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Neptune PlanetCard object from a dictionary."""
        return cls()

class PlanetX(PlanetCard):
    """Represents the Planet X card, associated with Five of a Kind."""
    def __init__(self):
        """Initializes a PlanetX PlanetCard."""
        super().__init__(
            name=PlanetCardType.PLANET_X.value,
            chips_bonus=35,
            mult_bonus=3,
            poker_hand_type="Five of a Kind"
        )

    def to_dict(self):
        """Converts the PlanetX PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a PlanetX PlanetCard object from a dictionary."""
        return cls()

class Ceres(PlanetCard):
    """Represents the Ceres Planet card, associated with Flush House."""
    def __init__(self):
        """Initializes a Ceres PlanetCard."""
        super().__init__(
            name=PlanetCardType.CERES.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Flush House"
        )

    def to_dict(self):
        """Converts the Ceres PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Ceres PlanetCard object from a dictionary."""
        return cls()

class Eris(PlanetCard):
    """Represents the Eris Planet card, associated with Flush Five."""
    def __init__(self):
        """Initializes an Eris PlanetCard."""
        super().__init__(
            name=PlanetCardType.ERIS.value,
            chips_bonus=50,
            mult_bonus=3,
            poker_hand_type="Flush Five"
        )

    def to_dict(self):
        """Converts the Eris PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Eris PlanetCard object from a dictionary."""
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

"""This module defines the PlanetCard class and its subclasses, representing different Planet cards in the game."""

from enum import Enum
from .poker import PokerHand # Import PokerHand for type hinting

class PlanetCardType(Enum):
    """Represents the type of Planet card."""
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
    """Base class for all Planet cards."""
    def __init__(self, name: str, chips_bonus: int, mult_bonus: int, poker_hand_type: str, cost: int = 3):
        """Initializes a PlanetCard object."

        Args:
            name (str): The name of the Planet card.
            chips_bonus (int): The chips bonus provided by the card.
            mult_bonus (int): The multiplier bonus provided by the card.
            poker_hand_type (str): The poker hand type associated with this card.
            cost (int, optional): The cost of the card in the shop. Defaults to 3.
        """
        self.name = name
        self.chips_bonus = chips_bonus
        self.mult_bonus = mult_bonus
        self.poker_hand_type = poker_hand_type
        self.cost = cost

    def __repr__(self):
        """Returns a string representation of the PlanetCard object for debugging."""
        return f"PlanetCard(name='{self.name}')"

    def apply_effect(self, game):
        """Applies the Planet card's effect to the game state."""
        # This will be implemented later when poker hand leveling is in place
        print(f"{self.name} used: Levels up {self.poker_hand_type} (effect not yet implemented).")

    def to_dict(self):
        """Converts the PlanetCard object to a dictionary for serialization."""
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
        """Creates a PlanetCard object from a dictionary. This is a factory method for subclasses."""
        # This will be a generic from_dict for the base PlanetCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base PlanetCard attributes
        return cls(data["name"], data["chips_bonus"], data["mult_bonus"], data["poker_hand_type"], data["cost"])

# --- Implementations for each Planet Card ---

class Pluto(PlanetCard):
    """Represents the Pluto Planet card, associated with High Card."""
    def __init__(self):
        """Initializes a Pluto PlanetCard."""
        super().__init__(
            name=PlanetCardType.PLUTO.value,
            chips_bonus=10,
            mult_bonus=1,
            poker_hand_type="High Card"
        )

    def to_dict(self):
        """Converts the Pluto PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Pluto PlanetCard object from a dictionary."""
        return cls()

class Mercury(PlanetCard):
    """Represents the Mercury Planet card, associated with Pair."""
    def __init__(self):
        """Initializes a Mercury PlanetCard."""
        super().__init__(
            name=PlanetCardType.MERCURY.value,
            chips_bonus=15,
            mult_bonus=1,
            poker_hand_type="Pair"
        )

    def to_dict(self):
        """Converts the Mercury PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Mercury PlanetCard object from a dictionary."""
        return cls()

class Uranus(PlanetCard):
    """Represents the Uranus Planet card, associated with Two Pair."""
    def __init__(self):
        """Initializes a Uranus PlanetCard."""
        super().__init__(
            name=PlanetCardType.URANUS.value,
            chips_bonus=20,
            mult_bonus=1,
            poker_hand_type="Two Pair"
        )

    def to_dict(self):
        """Converts the Uranus PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Uranus PlanetCard object from a dictionary."""
        return cls()

class Venus(PlanetCard):
    """Represents the Venus Planet card, associated with Three of a Kind."""
    def __init__(self):
        """Initializes a Venus PlanetCard."""
        super().__init__(
            name=PlanetCardType.VENUS.value,
            chips_bonus=20,
            mult_bonus=2,
            poker_hand_type="Three of a Kind"
        )

    def to_dict(self):
        """Converts the Venus PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Venus PlanetCard object from a dictionary."""
        return cls()

class Saturn(PlanetCard):
    """Represents the Saturn Planet card, associated with Straight."""
    def __init__(self):
        """Initializes a Saturn PlanetCard."""
        super().__init__(
            name=PlanetCardType.SATURN.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Straight"
        )

    def to_dict(self):
        """Converts the Saturn PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Saturn PlanetCard object from a dictionary."""
        return cls()

class Jupiter(PlanetCard):
    """Represents the Jupiter Planet card, associated with Flush."""
    def __init__(self):
        """Initializes a Jupiter PlanetCard."""
        super().__init__(
            name=PlanetCardType.JUPITER.value,
            chips_bonus=15,
            mult_bonus=2,
            poker_hand_type="Flush"
        )

    def to_dict(self):
        """Converts the Jupiter PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Jupiter PlanetCard object from a dictionary."""
        return cls()

class Earth(PlanetCard):
    """Represents the Earth Planet card, associated with Full House."""
    def __init__(self):
        """Initializes an Earth PlanetCard."""
        super().__init__(
            name=PlanetCardType.EARTH.value,
            chips_bonus=25,
            mult_bonus=2,
            poker_hand_type="Full House"
        )

    def to_dict(self):
        """Converts the Earth PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Earth PlanetCard object from a dictionary."""
        return cls()

class Mars(PlanetCard):
    """Represents the Mars Planet card, associated with Four of a Kind."""
    def __init__(self):
        """Initializes a Mars PlanetCard."""
        super().__init__(
            name=PlanetCardType.MARS.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Four of a Kind"
        )

    def to_dict(self):
        """Converts the Mars PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Mars PlanetCard object from a dictionary."""
        return cls()

class Neptune(PlanetCard):
    """Represents the Neptune Planet card, associated with Straight Flush."""
    def __init__(self):
        """Initializes a Neptune PlanetCard."""
        super().__init__(
            name=PlanetCardType.NEPTUNE.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Straight Flush"
        )

    def to_dict(self):
        """Converts the Neptune PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Neptune PlanetCard object from a dictionary."""
        return cls()

class PlanetX(PlanetCard):
    """Represents the Planet X card, associated with Five of a Kind."""
    def __init__(self):
        """Initializes a PlanetX PlanetCard."""
        super().__init__(
            name=PlanetCardType.PLANET_X.value,
            chips_bonus=35,
            mult_bonus=3,
            poker_hand_type="Five of a Kind"
        )

    def to_dict(self):
        """Converts the PlanetX PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a PlanetX PlanetCard object from a dictionary."""
        return cls()

class Ceres(PlanetCard):
    """Represents the Ceres Planet card, associated with Flush House."""
    def __init__(self):
        """Initializes a Ceres PlanetCard."""
        super().__init__(
            name=PlanetCardType.CERES.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Flush House"
        )

    def to_dict(self):
        """Converts the Ceres PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Ceres PlanetCard object from a dictionary."""
        return cls()

class Eris(PlanetCard):
    """Represents the Eris Planet card, associated with Flush Five."""
    def __init__(self):
        """Initializes an Eris PlanetCard."""
        super().__init__(
            name=PlanetCardType.ERIS.value,
            chips_bonus=50,
            mult_bonus=3,
            poker_hand_type="Flush Five"
        )

    def to_dict(self):
        """Converts the Eris PlanetCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Eris PlanetCard object from a dictionary."""
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
