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

class TheSoul(SpectralCard):
    def __init__(self):
        super().__init__(
            name=SpectralCardType.THE_SOUL.value,
            description="Creates a random Rare Joker."
        )

    def apply_effect(self, game):
        # This needs to be implemented once Joker rarity is defined
        print(f"{self.name} used: Creates a random Rare Joker (effect not yet implemented).")

    def to_dict(self):
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        return cls()

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
