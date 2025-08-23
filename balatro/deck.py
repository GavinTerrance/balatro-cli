# balatro/deck.py

import random
from .cards import Card, Suit, Rank

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def __repr__(self):
        return f"Deck(cards={len(self.cards)})"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards: int = 1):
        if num_cards > len(self.cards):
            # In a real game, you might handle this differently
            # (e.g., reshuffle discard pile), but for now, we'll just return what's left.
            drawn_cards = self.cards[:]
            self.cards = []
            return drawn_cards
        
        drawn_cards = [self.cards.pop() for _ in range(num_cards)]
        return drawn_cards
