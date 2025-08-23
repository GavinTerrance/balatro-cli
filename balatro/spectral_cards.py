from .cards import Card, Suit, Rank
from enum import Enum
import random
from .jokers import joker_from_dict
from .vouchers import voucher_from_dict
from .tarot_cards import tarot_card_from_dict

class SpectralCardType(Enum):
    # Add all spectral card types from the wiki
    THE_SOUL = "The Soul"
    BLACK_HOLE = "Black Hole"
    OMEN = "Omen"
    FLAT_EARTH = "Flat Earth"
    SEANCE = "Séance"
    IMMOLATE = "Immolate"
    OBSERVATORY = "Observatory"
    NEBULA = "Nebula"
    VOID = "Void"
    ECHO = "Echo"
    GRIM = "Grim"
    SIGIL = "Sigil"
    WHEEL_OF_FORTUNE = "Wheel of Fortune"
    DEATH = "Death"
    JUDGEMENT = "Judgement"
    HANGED_MAN = "Hanged Man"
    STRENGTH = "Strength"
    HERMIT = "Hermit"

class SpectralCard:
    def __init__(self, name: str, description: str, cost: int = 4):
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self):
        return f"SpectralCard(name='{self.name}')"

    def apply_effect(self, game):
        raise NotImplementedError("Subclasses must implement apply_effect")

    def to_dict(self):
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        # This will be a generic from_dict for the base SpectralCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base SpectralCard attributes
        return cls(data["name"], data["description"], data["cost"])

# --- Implementations for each Spectral Card ---

"""This module defines the SpectralCard class and its subclasses, representing different Spectral cards in the game."""

from .cards import Card, Suit, Rank
from enum import Enum
import random
from .jokers import joker_from_dict
from .vouchers import voucher_from_dict
from .tarot_cards import tarot_card_from_dict

class SpectralCardType(Enum):
    """Represents the type of Spectral card."""
    # Add all spectral card types from the wiki
    THE_SOUL = "The Soul"
    BLACK_HOLE = "Black Hole"
    OMEN = "Omen"
    FLAT_EARTH = "Flat Earth"
    SEANCE = "Séance"
    IMMOLATE = "Immolate"
    OBSERVATORY = "Observatory"
    NEBULA = "Nebula"
    VOID = "Void"
    ECHO = "Echo"
    GRIM = "Grim"
    SIGIL = "Sigil"
    WHEEL_OF_FORTUNE = "Wheel of Fortune"
    DEATH = "Death"
    JUDGEMENT = "Judgement"
    HANGED_MAN = "Hanged Man"
    STRENGTH = "Strength"
    HERMIT = "Hermit"

class SpectralCard:
    """Base class for all Spectral cards."""
    def __init__(self, name: str, description: str, cost: int = 4):
        """Initializes a SpectralCard object."

        Args:
            name (str): The name of the Spectral card.
            description (str): A brief description of the Spectral card's effect.
            cost (int, optional): The cost of the card in the shop. Defaults to 4.
        """
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self):
        """Returns a string representation of the SpectralCard object for debugging."""
        return f"SpectralCard(name='{self.name}')"

    def apply_effect(self, game):
        """Applies the Spectral card's effect to the game state."""
        raise NotImplementedError("Subclasses must implement apply_effect")

    def to_dict(self):
        """Converts the SpectralCard object to a dictionary for serialization."""
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a SpectralCard object from a dictionary. This is a factory method for subclasses."""
        # This will be a generic from_dict for the base SpectralCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base SpectralCard attributes
        return cls(data["name"], data["description"], data["cost"])

# --- Implementations for each Spectral Card ---

class TheSoul(SpectralCard):
    """Represents The Soul Spectral card."""
    def __init__(self):
        """Initializes The Soul SpectralCard."""
        super().__init__(
            name=SpectralCardType.THE_SOUL.value,
            description="Creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker rarity is defined
        print(f"{self.name} used: Creates a random Rare Joker (effect not yet implemented).")

    def to_dict(self):
        """Converts The Soul SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates The Soul SpectralCard object from a dictionary."""
        return cls()

class BlackHole(SpectralCard):
    """Represents the Black Hole Spectral card."""
    def __init__(self):
        """Initializes a BlackHole SpectralCard."""
        super().__init__(
            name=SpectralCardType.BLACK_HOLE.value,
            description="Destroys a selected Joker and levels up all Poker Hands."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and hand leveling are defined
        print(f"{self.name} used: Destroys a selected Joker and levels up all Poker Hands (effect not yet implemented).")

    def to_dict(self):
        """Converts the BlackHole SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a BlackHole SpectralCard object from a dictionary."""
        return cls()

class Omen(SpectralCard):
    """Represents the Omen Spectral card."""
    def __init__(self):
        """Initializes an Omen SpectralCard."""
        super().__init__(
            name=SpectralCardType.OMEN.value,
            description="Creates a random Negative Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Jokers are defined
        print(f"{self.name} used: Creates a random Negative Joker (effect not yet implemented).")

    def to_dict(self):
        """Converts the Omen SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Omen SpectralCard object from a dictionary."""
        return cls()

class FlatEarth(SpectralCard):
    """Represents the Flat Earth Spectral card."""
    def __init__(self):
        """Initializes a FlatEarth SpectralCard."""
        super().__init__(
            name=SpectralCardType.FLAT_EARTH.value,
            description="All Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: All Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

    def to_dict(self):
        """Converts the FlatEarth SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a FlatEarth SpectralCard object from a dictionary."""
        return cls()

class Seance(SpectralCard):
    """Represents the Séance Spectral card."""
    def __init__(self):
        """Initializes a Seance SpectralCard."""
        super().__init__(
            name=SpectralCardType.SEANCE.value,
            description="Creates a random Spectral Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Spectral card generation is defined
        print(f"{self.name} used: Creates a random Spectral Card (effect not yet implemented).")

    def to_dict(self):
        """Converts the Seance SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Seance SpectralCard object from a dictionary."""
        return cls()

class Immolate(SpectralCard):
    """Represents the Immolate Spectral card."""
    def __init__(self):
        """Initializes an Immolate SpectralCard."""
        super().__init__(
            name=SpectralCardType.IMMOLATE.value,
            description="Destroys all Jokers and creates a random Legendary Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and Legendary Jokers are defined
        print(f"{self.name} used: Destroys all Jokers and creates a random Legendary Joker (effect not yet implemented).")

    def to_dict(self):
        """Converts the Immolate SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Immolate SpectralCard object from a dictionary."""
        return cls()

class Observatory(SpectralCard):
    """Represents the Observatory Spectral card."""
    def __init__(self):
        """Initializes an Observatory SpectralCard."""
        super().__init__(
            name=SpectralCardType.OBSERVATORY.value,
            description="Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

    def to_dict(self):
        """Converts the Observatory SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Observatory SpectralCard object from a dictionary."""
        return cls()

class Nebula(SpectralCard):
    """Represents the Nebula Spectral card."""
    def __init__(self):
        """Initializes a Nebula SpectralCard."""
        super().__init__(
            name=SpectralCardType.NEBULA.value,
            description="Creates a random Planet Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card generation is defined
        print(f"{self.name} used: Creates a random Planet Card (effect not yet implemented).")

    def to_dict(self):
        """Converts the Nebula SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Nebula SpectralCard object from a dictionary."""
        return cls()

class Void(SpectralCard):
    """Represents the Void Spectral card."""
    def __init__(self):
        """Initializes a Void SpectralCard."""
        super().__init__(
            name=SpectralCardType.VOID.value,
            description="Destroys all Vouchers and creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Voucher destruction and Joker rarity are defined
        print(f"{self.name} used: Destroys all Vouchers and creates a random Rare Joker (effect not yet implemented).")

    def to_dict(self):
        """Converts the Void SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Void SpectralCard object from a dictionary."""
        return cls()

class Echo(SpectralCard):
    """Represents the Echo Spectral card."""
    def __init__(self):
        """Initializes an Echo SpectralCard."""
        super().__init__(
            name=SpectralCardType.ECHO.value,
            description="Creates a random Tarot Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Tarot card generation is defined
        print(f"{self.name} used: Creates a random Tarot Card (effect not yet implemented).")

    def to_dict(self):
        """Converts the Echo SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates an Echo SpectralCard object from a dictionary."""
        return cls()

class Grim(SpectralCard):
    """Represents the Grim Spectral card."""
    def __init__(self):
        """Initializes a Grim SpectralCard."""
        super().__init__(
            name=SpectralCardType.GRIM.value,
            description="Creates a random Playing Card with a Negative Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Negative Edition (effect not yet implemented).")

    def to_dict(self):
        """Converts the Grim SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Grim SpectralCard object from a dictionary."""
        return cls()

class Sigil(SpectralCard):
    """Represents the Sigil Spectral card."""
    def __init__(self):
        """Initializes a Sigil SpectralCard."""
        super().__init__(
            name=SpectralCardType.SIGIL.value,
            description="Creates a random Playing Card with a Polychrome Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Polychrome Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Polychrome Edition (effect not yet implemented).")

    def to_dict(self):
        """Converts the Sigil SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Sigil SpectralCard object from a dictionary."""
        return cls()

class WheelOfFortune(SpectralCard):
    """Represents the Wheel of Fortune Spectral card."""
    def __init__(self):
        """Initializes a WheelOfFortune SpectralCard."""
        super().__init__(
            name=SpectralCardType.WHEEL_OF_FORTUNE.value,
            description="Creates a random Playing Card with a Holographic Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Holographic Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Holographic Edition (effect not yet implemented).")

    def to_dict(self):
        """Converts the WheelOfFortune SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a WheelOfFortune SpectralCard object from a dictionary."""
        return cls()

class Death(SpectralCard):
    """Represents the Death Spectral card."""
    def __init__(self):
        """Initializes a Death SpectralCard."""
        super().__init__(
            name=SpectralCardType.DEATH.value,
            description="Creates a random Playing Card with a Foil Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Foil Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Foil Edition (effect not yet implemented).")

    def to_dict(self):
        """Converts the Death SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Death SpectralCard object from a dictionary."""
        return cls()

class Judgement(SpectralCard):
    """Represents the Judgement Spectral card."""
    def __init__(self):
        """Initializes a Judgement SpectralCard."""
        super().__init__(
            name=SpectralCardType.JUDGEMENT.value,
            description="Creates a random Playing Card with a Gold Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Gold Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Gold Seal (effect not yet implemented).")

    def to_dict(self):
        """Converts the Judgement SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Judgement SpectralCard object from a dictionary."""
        return cls()

class HangedMan(SpectralCard):
    """Represents the Hanged Man Spectral card."""
    def __init__(self):
        """Initializes a HangedMan SpectralCard."""
        super().__init__(
            name=SpectralCardType.HANGED_MAN.value,
            description="Creates a random Playing Card with a Red Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Red Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Red Seal (effect not yet implemented).")

    def to_dict(self):
        """Converts the HangedMan SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a HangedMan SpectralCard object from a dictionary."""
        return cls()

class Strength(SpectralCard):
    """Represents the Strength Spectral card."""
    def __init__(self):
        """Initializes a Strength SpectralCard."""
        super().__init__(
            name=SpectralCardType.STRENGTH.value,
            description="Creates a random Playing Card with a Blue Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Blue Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Blue Seal (effect not yet implemented).")

    def to_dict(self):
        """Converts the Strength SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Strength SpectralCard object from a dictionary."""
        return cls()

class Hermit(SpectralCard):
    """Represents the Hermit Spectral card."""
    def __init__(self):
        """Initializes a Hermit SpectralCard."""
        super().__init__(
            name=SpectralCardType.HERMIT.value,
            description="Creates a random Playing Card with a Purple Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Purple Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Purple Seal (effect not yet implemented).")

    def to_dict(self):
        """Converts the Hermit SpectralCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates a Hermit SpectralCard object from a dictionary."""
        return cls()

SPECTRAL_CARD_CLASSES = {
    "SpectralCard": SpectralCard,
    "TheSoul": TheSoul,
    "BlackHole": BlackHole,
    "Omen": Omen,
    "FlatEarth": FlatEarth,
    "Seance": Seance,
    "Immolate": Immolate,
    "Observatory": Observatory,
    "Nebula": Nebula,
    "Void": Void,
    "Echo": Echo,
    "Grim": Grim,
    "Sigil": Sigil,
    "WheelOfFortune": WheelOfFortune,
    "Death": Death,
    "Judgement": Judgement,
    "HangedMan": HangedMan,
    "Strength": Strength,
    "Hermit": Hermit
}

def spectral_card_from_dict(data):
    """Factory function to create a SpectralCard object from a dictionary."""
    spectral_card_class = SPECTRAL_CARD_CLASSES[data["_class"]]
    return spectral_card_class(data["name"], data["description"], data["cost"])

class BlackHole(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.BLACK_HOLE.value,
            description="Destroys a selected Joker and levels up all Poker Hands."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and hand leveling are defined
        print(f"{self.name} used: Destroys a selected Joker and levels up all Poker Hands (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Omen(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.OMEN.value,
            description="Creates a random Negative Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Jokers are defined
        print(f"{self.name} used: Creates a random Negative Joker (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class FlatEarth(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.FLAT_EARTH.value,
            description="All Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: All Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Seance(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.SEANCE.value,
            description="Creates a random Spectral Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Spectral card generation is defined
        print(f"{self.name} used: Creates a random Spectral Card (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Immolate(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.IMMOLATE.value,
            description="Destroys all Jokers and creates a random Legendary Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and Legendary Jokers are defined
        print(f"{self.name} used: Destroys all Jokers and creates a random Legendary Joker (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Observatory(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.OBSERVATORY.value,
            description="Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Nebula(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.NEBULA.value,
            description="Creates a random Planet Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card generation is defined
        print(f"{self.name} used: Creates a random Planet Card (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Void(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.VOID.value,
            description="Destroys all Vouchers and creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Voucher destruction and Joker rarity are defined
        print(f"{self.name} used: Destroys all Vouchers and creates a random Rare Joker (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Echo(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.ECHO.value,
            description="Creates a random Tarot Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Tarot card generation is defined
        print(f"{self.name} used: Creates a random Tarot Card (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Grim(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.GRIM.value,
            description="Creates a random Playing Card with a Negative Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Negative Edition (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Sigil(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.SIGIL.value,
            description="Creates a random Playing Card with a Polychrome Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Polychrome Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Polychrome Edition (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class WheelOfFortune(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.WHEEL_OF_FORTUNE.value,
            description="Creates a random Playing Card with a Holographic Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Holographic Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Holographic Edition (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Death(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.DEATH.value,
            description="Creates a random Playing Card with a Foil Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Foil Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Foil Edition (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Judgement(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.JUDGEMENT.value,
            description="Creates a random Playing Card with a Gold Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Gold Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Gold Seal (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class HangedMan(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.HANGED_MAN.value,
            description="Creates a random Playing Card with a Red Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Red Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Red Seal (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Strength(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.STRENGTH.value,
            description="Creates a random Playing Card with a Blue Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Blue Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Blue Seal (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

class Hermit(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.HERMIT.value,
            description="Creates a random Playing Card with a Purple Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Purple Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Purple Seal (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

SPECTRAL_CARD_CLASSES = {
    "SpectralCard": SpectralCard,
    "TheSoul": TheSoul,
    "BlackHole": BlackHole,
    "Omen": Omen,
    "FlatEarth": FlatEarth,
    "Seance": Seance,
    "Immolate": Immolate,
    "Observatory": Observatory,
    "Nebula": Nebula,
    "Void": Void,
    "Echo": Echo,
    "Grim": Grim,
    "Sigil": Sigil,
    "WheelOfFortune": WheelOfFortune,
    "Death": Death,
    "Judgement": Judgement,
    "HangedMan": HangedMan,
    "Strength": Strength,
    "Hermit": Hermit
}

def spectral_card_from_dict(data):
    spectral_card_class = SPECTRAL_CARD_CLASSES[data["_class"]]
    return spectral_card_class(data["name"], data["description"], data["cost"])

class TheSoul(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.THE_SOUL.value,
            description="Creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker rarity is defined
        print(f"{self.name} used: Creates a random Rare Joker (effect not yet implemented).")

class BlackHole(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.BLACK_HOLE.value,
            description="Destroys a selected Joker and levels up all Poker Hands."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and hand leveling are defined
        print(f"{self.name} used: Destroys a selected Joker and levels up all Poker Hands (effect not yet implemented).")

class Omen(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.OMEN.value,
            description="Creates a random Negative Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Jokers are defined
        print(f"{self.name} used: Creates a random Negative Joker (effect not yet implemented).")

class FlatEarth(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.FLAT_EARTH.value,
            description="All Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: All Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

class Seance(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.SEANCE.value,
            description="Creates a random Spectral Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Spectral card generation is defined
        print(f"{self.name} used: Creates a random Spectral Card (effect not yet implemented).")

class Immolate(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.IMMOLATE.value,
            description="Destroys all Jokers and creates a random Legendary Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker destruction and Legendary Jokers are defined
        print(f"{self.name} used: Destroys all Jokers and creates a random Legendary Joker (effect not yet implemented).")

class Observatory(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.OBSERVATORY.value,
            description="Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card effects are defined
        print(f"{self.name} used: Makes Planet cards in your consumable area give X1.5 Mult for their specified poker hand (effect not yet implemented).")

class Nebula(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.NEBULA.value,
            description="Creates a random Planet Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Planet card generation is defined
        print(f"{self.name} used: Creates a random Planet Card (effect not yet implemented).")

class Void(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.VOID.value,
            description="Destroys all Vouchers and creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Voucher destruction and Joker rarity are defined
        print(f"{self.name} used: Destroys all Vouchers and creates a random Rare Joker (effect not yet implemented).")

class Echo(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.ECHO.value,
            description="Creates a random Tarot Card."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Tarot card generation is defined
        print(f"{self.name} used: Creates a random Tarot Card (effect not yet implemented).")

class Grim(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.GRIM.value,
            description="Creates a random Playing Card with a Negative Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Negative Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Negative Edition (effect not yet implemented).")

class Sigil(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.SIGIL.value,
            description="Creates a random Playing Card with a Polychrome Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Polychrome Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Polychrome Edition (effect not yet implemented).")

class WheelOfFortune(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.WHEEL_OF_FORTUNE.value,
            description="Creates a random Playing Card with a Holographic Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Holographic Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Holographic Edition (effect not yet implemented).")

class Death(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.DEATH.value,
            description="Creates a random Playing Card with a Foil Edition."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Foil Edition cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Foil Edition (effect not yet implemented).")

class Judgement(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.JUDGEMENT.value,
            description="Creates a random Playing Card with a Gold Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Gold Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Gold Seal (effect not yet implemented).")

class HangedMan(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.HANGED_MAN.value,
            description="Creates a random Playing Card with a Red Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Red Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Red Seal (effect not yet implemented).")

class Strength(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.STRENGTH.value,
            description="Creates a random Playing Card with a Blue Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Blue Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Blue Seal (effect not yet implemented).")

class Hermit(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.HERMIT.value,
            description="Creates a random Playing Card with a Purple Seal."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Purple Seal cards are defined
        print(f"{self.name} used: Creates a random Playing Card with a Purple Seal (effect not yet implemented).")
