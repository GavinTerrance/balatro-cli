import pytest
from balatro.poker import evaluate_hand, PokerHand, get_rank_value
from balatro.cards import Card, Suit, Rank

def test_get_rank_value():
    assert get_rank_value(Rank.TWO) == 2
    assert get_rank_value(Rank.TEN) == 10
    assert get_rank_value(Rank.ACE) == 14

def test_evaluate_hand_high_card():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.FOUR),
        Card(Suit.CLUBS, Rank.SIX),
        Card(Suit.DIAMONDS, Rank.EIGHT),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.HIGH_CARD

def test_evaluate_hand_pair():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.SIX),
        Card(Suit.DIAMONDS, Rank.EIGHT),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.PAIR

def test_evaluate_hand_two_pair():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.SIX),
        Card(Suit.DIAMONDS, Rank.SIX),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.TWO_PAIR

def test_evaluate_hand_three_of_a_kind():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.EIGHT),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.THREE_OF_A_KIND

def test_evaluate_hand_straight():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.THREE),
        Card(Suit.CLUBS, Rank.FOUR),
        Card(Suit.DIAMONDS, Rank.FIVE),
        Card(Suit.SPADES, Rank.SIX)
    ]
    assert evaluate_hand(hand) == PokerHand.STRAIGHT

def test_evaluate_hand_straight_ace_high():
    hand = [
        Card(Suit.SPADES, Rank.TEN),
        Card(Suit.HEARTS, Rank.JACK),
        Card(Suit.CLUBS, Rank.QUEEN),
        Card(Suit.DIAMONDS, Rank.KING),
        Card(Suit.SPADES, Rank.ACE)
    ]
    assert evaluate_hand(hand) == PokerHand.STRAIGHT

def test_evaluate_hand_straight_ace_low():
    hand = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.THREE),
        Card(Suit.DIAMONDS, Rank.FOUR),
        Card(Suit.SPADES, Rank.FIVE)
    ]
    assert evaluate_hand(hand) == PokerHand.STRAIGHT

def test_evaluate_hand_flush():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.SPADES, Rank.FOUR),
        Card(Suit.SPADES, Rank.SIX),
        Card(Suit.SPADES, Rank.EIGHT),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.FLUSH

def test_evaluate_hand_full_house():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.SIX),
        Card(Suit.SPADES, Rank.SIX)
    ]
    assert evaluate_hand(hand) == PokerHand.FULL_HOUSE

def test_evaluate_hand_four_of_a_kind():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.TWO),
        Card(Suit.SPADES, Rank.TEN)
    ]
    assert evaluate_hand(hand) == PokerHand.FOUR_OF_A_KIND

def test_evaluate_hand_straight_flush():
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.SPADES, Rank.THREE),
        Card(Suit.SPADES, Rank.FOUR),
        Card(Suit.SPADES, Rank.FIVE),
        Card(Suit.SPADES, Rank.SIX)
    ]
    assert evaluate_hand(hand) == PokerHand.STRAIGHT_FLUSH

def test_evaluate_hand_five_of_a_kind():
    # This would typically require a Joker or special card
    # For testing, we'll simulate it with 5 cards of the same rank
    hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.TWO),
        Card(Suit.SPADES, Rank.TWO) # This is a placeholder for a 5th card of same rank
    ]
    assert evaluate_hand(hand) == PokerHand.FIVE_OF_A_KIND
