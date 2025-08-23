# balatro/scoring.py

from .poker import PokerHand

# Base chips and multiplier for each hand type
# Values taken from Balatro wiki
HAND_SCORES = {
    PokerHand.HIGH_CARD: {"chips": 5, "mult": 1},
    PokerHand.PAIR: {"chips": 10, "mult": 2},
    PokerHand.TWO_PAIR: {"chips": 20, "mult": 2},
    PokerHand.THREE_OF_A_KIND: {"chips": 30, "mult": 3},
    PokerHand.STRAIGHT: {"chips": 30, "mult": 4},
    PokerHand.FLUSH: {"chips": 35, "mult": 4},
    PokerHand.FULL_HOUSE: {"chips": 40, "mult": 4},
    PokerHand.FOUR_OF_A_KIND: {"chips": 60, "mult": 7},
    PokerHand.STRAIGHT_FLUSH: {"chips": 100, "mult": 8},
    PokerHand.FIVE_OF_A_KIND: {"chips": 120, "mult": 12}, # Assuming a generic five of a kind
}

def calculate_score(hand_type: PokerHand, cards: list):
    """Calculates the score for a given hand type and the cards in it."""
    base_score = HAND_SCORES.get(hand_type, {"chips": 0, "mult": 0})
    
    # For now, card-specific bonuses are not implemented.
    # This is a simplified calculation.
    chips = base_score["chips"]
    mult = base_score["mult"]
    
    return chips * mult
