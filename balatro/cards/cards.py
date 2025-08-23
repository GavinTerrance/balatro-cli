# balatro/cards.py

"""This module defines the Card class and related enums for suits, ranks, enhancements, editions, and seals."""

from enum import Enum

class Suit(Enum):
    """Represents the suit of a playing card."""
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    """Represents the rank of a playing card."""
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"

class Enhancement(Enum):
    """Represents an enhancement applied to a playing card."""
    NONE = "None"
    GLASS = "Glass"
    STEEL = "Steel"
    GOLD = "Gold"
    LUCKY = "Lucky"
    MULT = "Mult"
    CHIP = "Chip"

class Edition(Enum):
    """Represents an edition applied to a playing card."""
    NONE = "None"
    FOIL = "Foil"
    HOLOGRAPHIC = "Holographic"
    POLYCHROME = "Polychrome"
    NEGATIVE = "Negative"

class Seal(Enum):
    """Represents a seal applied to a playing card."""
    NONE = "None"
    GOLD = "Gold"
    RED = "Red"
    BLUE = "Blue"
    PURPLE = "Purple"

class Card:
    """Represents a playing card with suit, rank, and optional modifiers."""
    def __init__(self, suit: Suit, rank: Rank, enhancement: Enhancement = Enhancement.NONE, edition: Edition = Edition.NONE, seal: Seal = Seal.NONE):
        """Initializes a Card object."

        Args:
            suit (Suit): The suit of the card.
            rank (Rank): The rank of the card.
            enhancement (Enhancement, optional): The enhancement applied to the card. Defaults to Enhancement.NONE.
            edition (Edition, optional): The edition applied to the card. Defaults to Edition.NONE.
            seal (Seal, optional): The seal applied to the card. Defaults to Seal.NONE.
        """
        self.suit = suit
        self.rank = rank
        self.enhancement = enhancement
        self.edition = edition
        self.seal = seal

    def __repr__(self):
        """Returns a string representation of the Card object for debugging."""
        return f"Card('{self.rank.value}', '{self.suit.value}', Enhancement.{self.enhancement.name}, Edition.{self.edition.name}, Seal.{self.seal.name})"

    def __str__(self):
        """Returns a user-friendly string representation of the Card object."""
        modifiers = []
        if self.enhancement != Enhancement.NONE:
            modifiers.append(self.enhancement.value)
        if self.edition != Edition.NONE:
            modifiers.append(self.edition.value)
        if self.seal != Seal.NONE:
            modifiers.append(self.seal.value)
        
        if modifiers:
            return f"{self.rank.value} of {self.suit.value} ({', '.join(modifiers)})"
        else:
            return f"{self.rank.value} of {self.suit.value}"

    def to_dict(self):
        """Converts the Card object to a dictionary for serialization."""
        return {
            "suit": self.suit.value,
            "rank": self.rank.value,
            "enhancement": self.enhancement.value,
            "edition": self.edition.value,
            "seal": self.seal.value
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Card object from a dictionary."""
        suit = Suit(data["suit"])
        rank = Rank(data["rank"])
        enhancement = Enhancement(data["enhancement"])
        edition = Edition(data["edition"])
        seal = Seal(data["seal"])
        return cls(suit, rank, enhancement, edition, seal)
