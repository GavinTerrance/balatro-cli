# balatro/poker.py

from enum import Enum
from collections import Counter
from .cards import Card, Rank

class PokerHand(Enum):
    HIGH_CARD = "High Card"
    PAIR = "Pair"
    TWO_PAIR = "Two Pair"
    THREE_OF_A_KIND = "Three of a Kind"
    STRAIGHT = "Straight"
    FLUSH = "Flush"
    FULL_HOUSE = "Full House"
    FOUR_OF_A_KIND = "Four of a Kind"
    STRAIGHT_FLUSH = "Straight Flush"
    FIVE_OF_A_KIND = "Five of a Kind"

# Helper function to get rank values for sorting and comparison
def get_rank_value(rank: Rank):
    # This mapping is simplified. In a real game, Ace can be high or low.
    rank_order = {r: i for i, r in enumerate(Rank, 2)}
    return rank_order[rank]

def evaluate_hand(cards: list[Card]):
    """Evaluates a list of cards and returns the best poker hand."""
    if not cards:
        return None

    ranks = [c.rank for c in cards]
    suits = [c.suit for c in cards]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # --- Check for hands ---
    is_flush = len(suit_counts) == 1
    
    # Check for straight
    unique_rank_values = sorted([get_rank_value(r) for r in set(ranks)])
    is_straight = (len(unique_rank_values) == 5 and 
                   (unique_rank_values[-1] - unique_rank_values[0] == 4))
    # Ace-low straight (A, 2, 3, 4, 5)
    if not is_straight and set(unique_rank_values) == {14, 2, 3, 4, 5}:
        is_straight = True

    # Check for kinds
    counts = sorted(rank_counts.values(), reverse=True)
    is_five_of_a_kind = counts[0] == 5
    is_four_of_a_kind = counts[0] == 4
    is_full_house = counts == [3, 2]
    is_three_of_a_kind = counts[0] == 3
    is_two_pair = counts == [2, 2, 1]
    is_pair = counts[0] == 2

    # --- Determine the hand based on checks ---
    if is_straight and is_flush:
        return PokerHand.STRAIGHT_FLUSH
    if is_five_of_a_kind:
        return PokerHand.FIVE_OF_A_KIND
    if is_four_of_a_kind:
        return PokerHand.FOUR_OF_A_KIND
    if is_full_house:
        return PokerHand.FULL_HOUSE
    if is_flush:
        return PokerHand.FLUSH
    if is_straight:
        return PokerHand.STRAIGHT
    if is_three_of_a_kind:
        return PokerHand.THREE_OF_A_KIND
    if is_two_pair:
        return PokerHand.TWO_PAIR
    if is_pair:
        return PokerHand.PAIR
    
    return PokerHand.HIGH_CARD
