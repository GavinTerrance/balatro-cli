import random
from .cards import Card, Suit, Rank

class BaseDeck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
        self.name = "Base Deck"
        self.description = "A standard 52-card deck."

    def __repr__(self):
        return f"Deck(name='{self.name}', cards={len(self.cards)})"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, num_cards: int = 1):
        if num_cards > len(self.cards):
            drawn_cards = self.cards[:]
            self.cards = []
            return drawn_cards
        
        drawn_cards = [self.cards.pop() for _ in range(num_cards)]
        return drawn_cards

class RedDeck(BaseDeck):
    def __init__(self):
        super().__init__()
        self.name = "Red Deck"
        self.description = "+1 discard every round."

class GreenDeck(BaseDeck):
    def __init__(self):
        super().__init__()
        self.name = "Green Deck"
        self.description = "At end of each Round: $2 per remaining Hand, $1 per remaining Discard. Earn no Interest."

class YellowDeck(BaseDeck):
    def __init__(self):
        super().__init__()
        self.name = "Yellow Deck"
        self.description = "Start with extra $10."