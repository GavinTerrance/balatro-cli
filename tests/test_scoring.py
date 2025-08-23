import pytest
from balatro.scoring import calculate_score, HAND_SCORES
from balatro.poker import PokerHand
from balatro.jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from balatro.cards import Card, Suit, Rank, Enhancement, Edition, Seal

# Mock Game class for testing scoring with game state interaction
class MockGame:
    def __init__(self):
        self.money = 0

def test_calculate_score_high_card_no_jokers():
    game = MockGame()
    score = calculate_score(PokerHand.HIGH_CARD, [], [], game)
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * HAND_SCORES[PokerHand.HIGH_CARD]["mult"]

def test_calculate_score_pair_with_joker_of_madness():
    game = MockGame()
    joker = JokerOfMadness()
    score = calculate_score(PokerHand.PAIR, [], [joker], game)
    expected_mult = HAND_SCORES[PokerHand.PAIR]["mult"] + 10
    assert score == HAND_SCORES[PokerHand.PAIR]["chips"] * expected_mult

def test_calculate_score_three_of_a_kind_with_chip_joker():
    game = MockGame()
    joker = ChipJoker()
    score = calculate_score(PokerHand.THREE_OF_A_KIND, [], [joker], game)
    expected_chips = HAND_SCORES[PokerHand.THREE_OF_A_KIND]["chips"] + 100
    assert score == expected_chips * HAND_SCORES[PokerHand.THREE_OF_A_KIND]["mult"]

def test_calculate_score_with_glass_enhancement():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.GLASS)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_mult = HAND_SCORES[PokerHand.HIGH_CARD]["mult"] + 2
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * expected_mult

def test_calculate_score_with_steel_enhancement():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.STEEL)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_mult = HAND_SCORES[PokerHand.HIGH_CARD]["mult"] * 1.5
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * expected_mult

def test_calculate_score_with_gold_enhancement():
    game = MockGame()
    initial_money = game.money
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.GOLD)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    assert game.money == initial_money + 3

def test_calculate_score_with_lucky_enhancement():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.LUCKY)
    # This test is probabilistic, so we'll just check if it doesn't crash
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    assert isinstance(score, (int, float))

def test_calculate_score_with_mult_enhancement():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.MULT)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_mult = HAND_SCORES[PokerHand.HIGH_CARD]["mult"] + 4
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * expected_mult

def test_calculate_score_with_chip_enhancement():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, enhancement=Enhancement.CHIP)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_chips = HAND_SCORES[PokerHand.HIGH_CARD]["chips"] + 10
    assert score == expected_chips * HAND_SCORES[PokerHand.HIGH_CARD]["mult"]

def test_calculate_score_with_foil_edition():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, edition=Edition.FOIL)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_chips = HAND_SCORES[PokerHand.HIGH_CARD]["chips"] + 50
    assert score == expected_chips * HAND_SCORES[PokerHand.HIGH_CARD]["mult"]

def test_calculate_score_with_holographic_edition():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, edition=Edition.HOLOGRAPHIC)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_mult = HAND_SCORES[PokerHand.HIGH_CARD]["mult"] + 10
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * expected_mult

def test_calculate_score_with_polychrome_edition():
    game = MockGame()
    card = Card(Suit.SPADES, Rank.ACE, edition=Edition.POLYCHROME)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    expected_mult = HAND_SCORES[PokerHand.HIGH_CARD]["mult"] * 1.5
    assert score == HAND_SCORES[PokerHand.HIGH_CARD]["chips"] * expected_mult

def test_calculate_score_with_gold_seal():
    game = MockGame()
    initial_money = game.money
    card = Card(Suit.SPADES, Rank.ACE, seal=Seal.GOLD)
    score = calculate_score(PokerHand.HIGH_CARD, [card], [], game)
    assert game.money == initial_money + 3
