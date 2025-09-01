"""This module defines poker hand types and functions for evaluating poker hands."""

from enum import Enum
from collections import Counter
from ..cards.cards import Card, Rank


class PokerHand(Enum):
    """Represents different types of poker hands."""

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
def get_rank_value(rank: Rank) -> int:
    """Returns the numerical value of a card rank."""

    # This mapping is simplified. In a real game, Ace can be high or low.
    rank_order = {r: i for i, r in enumerate(Rank, 2)}
    return rank_order[rank]


def evaluate_hand(cards: list[Card]) -> tuple[PokerHand | None, list[Card]]:
    """Evaluate cards and return the best hand type and cards used.

    Returning the specific cards that form the hand allows callers to only
    score those cards, matching Balatro's rule that only hand cards are
    counted unless modified by an effect.
    """

    if not cards:
        return None, []

    ranks = [c.rank for c in cards]
    suits = [c.suit for c in cards]
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # --- Check for hands ---
    is_flush = len(suit_counts) == 1

    # Check for straight
    unique_rank_values = sorted([get_rank_value(r) for r in set(ranks)])
    is_straight = (
        len(unique_rank_values) == 5
        and (unique_rank_values[-1] - unique_rank_values[0] == 4)
    )
    # Ace-low straight (A, 2, 3, 4, 5)
    if not is_straight and set(unique_rank_values) == {14, 2, 3, 4, 5}:
        is_straight = True

    # Check for kinds
    counts = sorted(rank_counts.values(), reverse=True)
    is_five_of_a_kind = counts[0] == 5
    is_four_of_a_kind = counts[0] == 4
    is_full_house = counts == [3, 2]
    is_three_of_a_kind = counts[0] == 3
    is_two_pair = list(rank_counts.values()).count(2) == 2
    is_pair = counts[0] == 2

    # --- Determine the hand based on checks and extract used cards ---
    if is_straight and is_flush:
        return PokerHand.STRAIGHT_FLUSH, cards
    if is_five_of_a_kind:
        rank = rank_counts.most_common(1)[0][0]
        used = [c for c in cards if c.rank == rank][:5]
        return PokerHand.FIVE_OF_A_KIND, used
    if is_four_of_a_kind:
        rank = rank_counts.most_common(1)[0][0]
        used = [c for c in cards if c.rank == rank][:4]
        return PokerHand.FOUR_OF_A_KIND, used
    if is_full_house:
        three_rank = [r for r, c in rank_counts.items() if c == 3][0]
        pair_rank = [r for r, c in rank_counts.items() if c == 2][0]
        used = [c for c in cards if c.rank == three_rank][:3]
        used += [c for c in cards if c.rank == pair_rank][:2]
        return PokerHand.FULL_HOUSE, used
    if is_flush:
        return PokerHand.FLUSH, cards
    if is_straight:
        return PokerHand.STRAIGHT, cards
    if is_three_of_a_kind:
        rank = [r for r, c in rank_counts.items() if c == 3][0]
        used = [c for c in cards if c.rank == rank][:3]
        return PokerHand.THREE_OF_A_KIND, used
    if is_two_pair:
        pair_ranks = [r for r, c in rank_counts.items() if c == 2][:2]
        used: list[Card] = []
        for r in pair_ranks:
            used.extend([c for c in cards if c.rank == r][:2])
        return PokerHand.TWO_PAIR, used
    if is_pair:
        rank = rank_counts.most_common(1)[0][0]
        used = [c for c in cards if c.rank == rank][:2]
        return PokerHand.PAIR, used

    highest = max(cards, key=lambda c: get_rank_value(c.rank))
    return PokerHand.HIGH_CARD, [highest]

