"""This module defines the Sticker class and its types, representing modifiers applied to Jokers and Decks."""

from enum import Enum

class StickerType(Enum):
    """Represents the different types of stickers that can be applied to Jokers or Decks."""
    ETERNAL = "Eternal"
    PERISHABLE = "Perishable"
    RENTAL = "Rental"
    WHITE_STAKE = "White Stake"
    RED_STAKE = "Red Stake"
    GREEN_STAKE = "Green Stake"
    BLACK_STAKE = "Black Stake"
    BLUE_STAKE = "Blue Stake"
    PURPLE_STAKE = "Purple Stake"
    ORANGE_STAKE = "Orange Stake"
    GOLD_STAKE = "Gold Stake"

class Sticker:
    """Represents a sticker applied to a Joker or Deck."""
    def __init__(self, sticker_type: StickerType):
        """Initializes a Sticker object."

        Args:
            sticker_type (StickerType): The type of the sticker.
        """
        self.sticker_type = sticker_type

    def __repr__(self):
        """Returns a string representation of the Sticker object for debugging."""
        return f"Sticker(type='{self.sticker_type.value}')"

    def __str__(self):
        """Returns a user-friendly string representation of the Sticker object."""
        return self.sticker_type.value

    def to_dict(self):
        """Converts the Sticker object to a dictionary for serialization."""
        return {
            "sticker_type": self.sticker_type.value
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Sticker object from a dictionary."""
        return cls(StickerType(data["sticker_type"]))
