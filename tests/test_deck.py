import pytest
from balatro.deck import BaseDeck, RedDeck, GreenDeck, YellowDeck
from balatro.cards import Card, Suit, Rank

def test_base_deck_creation():
    deck = BaseDeck()
    assert len(deck.cards) == 52
    # Check for unique cards (no duplicates)
    assert len(set(str(card) for card in deck.cards)) == 52

def test_base_deck_shuffle():
    deck = BaseDeck()
    original_order = list(deck.cards) # Create a copy
    deck.shuffle()
    assert len(deck.cards) == 52
    assert set(str(card) for card in deck.cards) == set(str(card) for card in original_order) # Same cards, different order
    # High probability that the order is different after shuffle
    assert deck.cards != original_order

def test_base_deck_draw_single_card():
    deck = BaseDeck()
    initial_len = len(deck.cards)
    card = deck.draw()
    assert len(card) == 1
    assert isinstance(card[0], Card)
    assert len(deck.cards) == initial_len - 1

def test_base_deck_draw_multiple_cards():
    deck = BaseDeck()
    initial_len = len(deck.cards)
    drawn_cards = deck.draw(5)
    assert len(drawn_cards) == 5
    assert all(isinstance(card, Card) for card in drawn_cards)
    assert len(deck.cards) == initial_len - 5

def test_base_deck_draw_more_cards_than_available():
    deck = BaseDeck()
    all_cards = deck.draw(52)
    assert len(all_cards) == 52
    assert len(deck.cards) == 0

def test_red_deck_creation():
    red_deck = RedDeck()
    assert red_deck.name == "Red Deck"
    assert red_deck.description == "+1 discard every round."
    assert len(red_deck.cards) == 52

def test_green_deck_creation():
    green_deck = GreenDeck()
    assert green_deck.name == "Green Deck"
    assert green_deck.description == "At end of each Round: $2 per remaining Hand, $1 per remaining Discard. Earn no Interest."
    assert len(green_deck.cards) == 52

def test_yellow_deck_creation():
    yellow_deck = YellowDeck()
    assert yellow_deck.name == "Yellow Deck"
    assert yellow_deck.description == "Start with extra $10."
    assert len(yellow_deck.cards) == 52
