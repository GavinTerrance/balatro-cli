import pytest
from balatro.cards import Card, Suit, Rank, Enhancement, Edition, Seal

def test_card_creation():
    card = Card(Suit.SPADES, Rank.ACE)
    assert card.suit == Suit.SPADES
    assert card.rank == Rank.ACE
    assert card.enhancement == Enhancement.NONE
    assert card.edition == Edition.NONE
    assert card.seal == Seal.NONE

def test_card_creation_with_modifiers():
    card = Card(Suit.HEARTS, Rank.TEN, Enhancement.GOLD, Edition.FOIL, Seal.RED)
    assert card.suit == Suit.HEARTS
    assert card.rank == Rank.TEN
    assert card.enhancement == Enhancement.GOLD
    assert card.edition == Edition.FOIL
    assert card.seal == Seal.RED

def test_card_repr():
    card = Card(Suit.CLUBS, Rank.KING)
    assert repr(card) == "Card('King', 'Clubs', Enhancement.NONE, Edition.NONE, Seal.NONE)"

def test_card_str():
    card = Card(Suit.DIAMONDS, Rank.QUEEN)
    assert str(card) == "Queen of Diamonds"

    card_with_enhancement = Card(Suit.SPADES, Rank.TWO, enhancement=Enhancement.MULT)
    assert str(card_with_enhancement) == "2 of Spades (Mult)"

    card_with_edition = Card(Suit.HEARTS, Rank.THREE, edition=Edition.HOLOGRAPHIC)
    assert str(card_with_edition) == "3 of Hearts (Holographic)"

    card_with_seal = Card(Suit.CLUBS, Rank.FOUR, seal=Seal.GOLD)
    assert str(card_with_seal) == "4 of Clubs (Gold)"

    card_with_all = Card(Suit.DIAMONDS, Rank.FIVE, Enhancement.CHIP, Edition.POLYCHROME, Seal.BLUE)
    assert str(card_with_all) == "5 of Diamonds (Chip, Polychrome, Blue)"

def test_card_to_dict():
    card = Card(Suit.SPADES, Rank.ACE, Enhancement.GLASS, Edition.FOIL, Seal.PURPLE)
    card_dict = card.to_dict()
    expected_dict = {
        "suit": "Spades",
        "rank": "Ace",
        "enhancement": "Glass",
        "edition": "Foil",
        "seal": "Purple"
    }
    assert card_dict == expected_dict

def test_card_from_dict():
    card_dict = {
        "suit": "Diamonds",
        "rank": "King",
        "enhancement": "Gold",
        "edition": "Holographic",
        "seal": "Red"
    }
    card = Card.from_dict(card_dict)
    assert card.suit == Suit.DIAMONDS
    assert card.rank == Rank.KING
    assert card.enhancement == Enhancement.GOLD
    assert card.edition == Edition.HOLOGRAPHIC
    assert card.seal == Seal.RED

def test_card_from_dict_no_modifiers():
    card_dict = {
        "suit": "Clubs",
        "rank": "Two",
        "enhancement": "None",
        "edition": "None",
        "seal": "None"
    }
    card = Card.from_dict(card_dict)
    assert card.suit == Suit.CLUBS
    assert card.rank == Rank.TWO
    assert card.enhancement == Enhancement.NONE
    assert card.edition == Edition.NONE
    assert card.seal == Seal.NONE
