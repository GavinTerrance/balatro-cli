# balatro/game.py

from .deck import Deck
from .cards import Card
from .poker import evaluate_hand
from .scoring import calculate_score
from .jokers import JokerOfMadness # Example Joker

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = []
        self.jokers = [JokerOfMadness()] # Start with a joker for testing
        
        # Game state variables
        self.money = 4
        self.round = 1
        self.hands = 4
        self.discards = 3
        self.score = 0

    def __repr__(self):
        return (
            f"Game(round={self.round}, hands={self.hands}, "
            f"discards={self.discards}, score={self.score}, money={self.money})"
        )

    def draw_hand(self, hand_size: int = 8):
        # Discard current hand if any, and draw a new one.
        self.hand = self.deck.draw(hand_size)

    def play_hand(self, cards_to_play: list[Card]):
        if not all(c in self.hand for c in cards_to_play):
            print("Error: One or more cards are not in the current hand.")
            return

        for card in cards_to_play:
            self.hand.remove(card)
        
        played_hand_type = evaluate_hand(cards_to_play)
        if played_hand_type:
            hand_score = calculate_score(played_hand_type, cards_to_play, self.jokers)
            self.score += hand_score
            print(f"Hand played: {played_hand_type.value} for {hand_score} points!")
        else:
            print("No valid poker hand was played.")

        self.hands -= 1
        print(f"Played {len(cards_to_play)} cards. {self.hands} hands remaining.")

