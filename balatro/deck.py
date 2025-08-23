"""This module defines the BaseDeck class and its subclasses for different deck types."""

import random
from .cards import Card, Suit, Rank

class BaseDeck:
    """Represents a standard deck of playing cards."""
    def __init__(self):
        """Initializes a BaseDeck with 52 standard playing cards."""
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
        self.name = "Base Deck"
        self.description = "A standard 52-card deck."

    def __repr__(self):
        """Returns a string representation of the Deck object for debugging."""
        return f"Deck(name='{self.name}', cards={len(self.cards)})"

    def shuffle(self):
        """Shuffles the cards in the deck randomly."""
        random.shuffle(self.cards)

    def draw(self, num_cards: int = 1):
        """Draws a specified number of cards from the top of the deck."

        Args:
            num_cards (int, optional): The number of cards to draw. Defaults to 1.

        Returns:
            list[Card]: A list of drawn Card objects.
        """
        if num_cards > len(self.cards):
            # In a real game, you might handle this differently
            # (e.g., reshuffle discard pile), but for now, we'll just return what's left.
            drawn_cards = self.cards[:]
            self.cards = []
            return drawn_cards
        
        drawn_cards = [self.cards.pop() for _ in range(num_cards)]
        return drawn_cards

class RedDeck(BaseDeck):
    """Represents the Red Deck, which provides an extra discard every round."""
    def __init__(self):
        """Initializes a RedDeck."""
        super().__init__()
        self.name = "Red Deck"
        self.description = "+1 discard every round."

class GreenDeck(BaseDeck):
    """Represents the Green Deck, which provides money per remaining hand/discard but no interest."""
    def __init__(self):
        """Initializes a GreenDeck."""
        super().__init__()
        self.name = "Green Deck"
        self.description = "At end of each Round: $2 per remaining Hand, $1 per remaining Discard. Earn no Interest."

class YellowDeck(BaseDeck):
    """Represents the Yellow Deck, which provides extra starting money."""
    def __init__(self):
        """Initializes a YellowDeck."""
        super().__init__()
        self.name = "Yellow Deck"
        self.description = "Start with extra $10."