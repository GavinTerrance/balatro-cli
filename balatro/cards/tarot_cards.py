"""This module defines the TarotCard class and its subclasses, representing different Tarot cards in the game."""

from .cards import Card, Suit, Rank
from .jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker, joker_from_dict # Import joker_from_dict
from ..shop.vouchers import (
    Voucher,
    TarotMerchant,
    CardSharp,
    Honeypot,
    voucher_from_dict,
)  # Import voucher_from_dict
import random

class TarotCard:
    """Base class for all Tarot cards."""
    def __init__(self, name: str, description: str, cost: int = 0):
        """Initializes a TarotCard object."

        Args:
            name (str): The name of the Tarot card.
            description (str): A brief description of the Tarot card's effect.
            cost (int, optional): The cost of the card in the shop. Defaults to 0.
        """
        self.name = name
        self.description = description
        self.cost = cost # Tarot cards usually have a cost in shop

    def __repr__(self):
        """Returns a string representation of the TarotCard object for debugging."""
        return f"TarotCard(name='{self.name}')"

    def apply_effect(self, game):
        """Applies the Tarot card's effect to the game state."""
        raise NotImplementedError("Subclasses must implement apply_effect")

    def to_dict(self):
        """Converts the TarotCard object to a dictionary for serialization."""
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a TarotCard object from a dictionary. This is a factory method for subclasses."""
        # This will be a generic from_dict for the base TarotCard class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base TarotCard attributes
        return cls(data["name"], data["description"], data["cost"])

# --- Example Tarot Card Implementations ---

class TheFool(TarotCard):
    """Represents The Fool Tarot card, which generates a random Joker."""
    def __init__(self):
        """Initializes The Fool TarotCard."""
        super().__init__(
            name="The Fool",
            description="Generates a random Joker.",
            cost=3
        )

    def apply_effect(self, game):
        """Applies the effect of The Fool: generates a random Joker."""
        available_jokers = [JokerOfGreed, JokerOfMadness, ChipJoker]
        new_joker = random.choice(available_jokers)()
        game.jokers.append(new_joker)
        print(f"The Fool generated: {new_joker.name}!")

    def to_dict(self):
        """Converts The Fool TarotCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates The Fool TarotCard object from a dictionary."""
        return cls()

class TheMagician(TarotCard):
    """Represents The Magician Tarot card, which upgrades a selected card."""
    def __init__(self):
        """Initializes The Magician TarotCard."""
        super().__init__(
            name="The Magician",
            description="Upgrades a selected card to a higher rank.",
            cost=3
        )

    def apply_effect(self, game):
        """Applies the effect of The Magician: upgrades a selected card to a higher rank."""
        if not game.hand:
            print("No cards in hand to upgrade.")
            return
        
        print("Select a card to upgrade:")
        for i, card in enumerate(game.hand):
            print(f"[{i}] {card}")
        
        try:
            choice = int(input("Enter index of card to upgrade: "))
            if 0 <= choice < len(game.hand):
                card_to_upgrade = game.hand[choice]
                # Simple upgrade logic: find next rank. Needs more robust handling for Ace.
                current_rank_index = list(Rank).index(card_to_upgrade.rank)
                if current_rank_index < len(list(Rank)) - 1:
                    new_rank = list(Rank)[current_rank_index + 1]
                    game.hand[choice] = Card(card_to_upgrade.suit, new_rank)
                    print(f"Upgraded {card_to_upgrade} to {game.hand[choice]}!")
                else:
                    print(f"{card_to_upgrade.rank.value} is already the highest rank.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input.")

    def to_dict(self):
        """Converts The Magician TarotCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates The Magician TarotCard object from a dictionary."""
        return cls()

class TheWorld(TarotCard):
    """Represents The World Tarot card, which generates a random Voucher."""
    def __init__(self):
        """Initializes The World TarotCard."""
        super().__init__(
            name="The World",
            description="Generates a random Voucher.",
            cost=3
        )

    def apply_effect(self, game):
        """Applies the effect of The World: generates a random Voucher."""
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]
        new_voucher = random.choice(available_vouchers)()
        game.vouchers.append(new_voucher)
        new_voucher.apply_effect(game) # Apply effect immediately
        print(f"The World generated: {new_voucher.name}!")

    def to_dict(self):
        """Converts The World TarotCard object to a dictionary for serialization."""
        return super().to_dict()

    @classmethod
    def from_dict(cls, data):
        """Creates The World TarotCard object from a dictionary."""
        return cls()

TAROT_CARD_CLASSES = {
    "TarotCard": TarotCard,
    "TheFool": TheFool,
    "TheMagician": TheMagician,
    "TheWorld": TheWorld
}

def tarot_card_from_dict(data):
    """Factory function to create a TarotCard object from a dictionary."""
    tarot_card_class = TAROT_CARD_CLASSES[data["_class"]]
    return tarot_card_class(data["name"], data["description"], data["cost"])
