import pytest
from balatro.game import Game, save_game, load_game
from balatro.deck import BaseDeck, RedDeck, GreenDeck, YellowDeck
from balatro.cards import Card, Suit, Rank, Enhancement, Edition, Seal
from balatro.jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from balatro.vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from balatro.tarot_cards import TarotCard, TheFool, TheMagician, TheWorld
from balatro.spectral_cards import SpectralCard, TheSoul
from balatro.planet_cards import PlanetCard, Pluto
from balatro.blinds import SmallBlind, BigBlind, BossBlind
import os

# Helper function to create a dummy game state for testing
def create_dummy_game():
    game = Game()
    game.money = 100
    game.round = 5
    game.hands = 2
    game.discards = 1
    game.score = 5000
    game.ante = 3
    game.game_over = False
    game.jokers = [JokerOfGreed(), JokerOfMadness()]
    game.vouchers = [TarotMerchant()]
    game.tarot_cards = [TheFool()]
    game.spectral_cards = [TheSoul()]
    game.planet_cards = [Pluto()]
    game.hand = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.KING),
        Card(Suit.CLUBS, Rank.QUEEN),
        Card(Suit.DIAMONDS, Rank.JACK),
        Card(Suit.SPADES, Rank.TEN, enhancement=Enhancement.GOLD)
    ]
    game.current_blind_index = 1 # Big Blind
    game.current_blind = game.blinds[game.current_blind_index]
    return game

def test_game_initialization_base_deck():
    game = Game()
    assert isinstance(game.deck, BaseDeck)
    assert len(game.deck.cards) == 52
    assert game.money == 4
    assert game.round == 1
    assert game.hands == 4
    assert game.discards == 3
    assert game.score == 0
    assert game.ante == 1
    assert game.game_over == False
    assert isinstance(game.current_blind, SmallBlind)

def test_game_initialization_red_deck():
    game = Game(deck_type="Red")
    assert isinstance(game.deck, RedDeck)
    assert game.discards == 4 # +1 discard from Red Deck

def test_game_initialization_green_deck():
    game = Game(deck_type="Green")
    assert isinstance(game.deck, GreenDeck)
    assert game.earns_interest == False # Green Deck effect

def test_game_initialization_yellow_deck():
    game = Game(deck_type="Yellow")
    assert isinstance(game.deck, YellowDeck)
    assert game.money == 14 # +10 money from Yellow Deck

def test_draw_hand():
    game = Game()
    game.draw_hand()
    assert len(game.hand) == 8
    assert len(game.deck.cards) == 52 - 8

def test_sort_hand():
    game = Game()
    game.hand = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.KING)
    ]
    game.sort_hand(sort_by='rank')
    assert game.hand[0].rank == Rank.TWO
    assert game.hand[1].rank == Rank.KING
    assert game.hand[2].rank == Rank.ACE

def test_play_hand_valid():
    game = Game()
    game.hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.CLUBS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.EIGHT),
        Card(Suit.SPADES, Rank.TEN)
    ]
    initial_hands = game.hands
    initial_score = game.score
    game.play_hand([game.hand[0], game.hand[1], game.hand[2]]) # Play a Three of a Kind
    assert game.hands == initial_hands - 1
    assert game.score > initial_score

def test_discard_cards_valid():
    game = Game()
    game.hand = [
        Card(Suit.SPADES, Rank.TWO),
        Card(Suit.HEARTS, Rank.THREE),
        Card(Suit.CLUBS, Rank.FOUR),
        Card(Suit.DIAMONDS, Rank.FIVE),
        Card(Suit.SPADES, Rank.SIX)
    ]
    initial_discards = game.discards
    initial_hands = game.hands
    game.discard_cards([0, 1])
    assert game.discards == initial_discards - 1
    assert game.hands == initial_hands - 1
    assert len(game.hand) == 8 # Hand size should remain 8 after drawing new cards

def test_advance_blind():
    game = Game()
    initial_ante = game.ante
    initial_blind_index = game.current_blind_index
    game.advance_blind()
    assert game.current_blind_index == initial_blind_index + 1
    assert game.ante == initial_ante

def test_advance_blind_to_next_ante():
    game = Game()
    game.current_blind_index = 2 # Boss Blind
    game.advance_blind()
    assert game.ante == 2
    assert game.current_blind_index == 0
    assert game.score == 0

def test_check_blind_cleared_success():
    game = Game()
    game.score = game.current_blind.score_required + 100
    assert game.check_blind_cleared() == True
    assert game.money == 14 # Initial 4 + 10

def test_check_blind_cleared_failure():
    game = Game()
    game.score = game.current_blind.score_required - 100
    assert game.check_blind_cleared() == False
    assert game.game_over == True

def test_end_of_round_effects_perishable_sticker():
    game = Game()
    joker = JokerOfGreed()
    joker.stickers.append(Sticker(StickerType.PERISHABLE))
    game.jokers.append(joker)

    # Simulate 4 rounds
    for _ in range(4):
        game.end_of_round_effects()
        assert joker.is_debuffed == False

    # Simulate 5th round
    game.end_of_round_effects()
    assert joker.is_debuffed == True

def test_end_of_round_effects_rental_sticker():
    game = Game()
    joker = JokerOfMadness()
    joker.stickers.append(Sticker(StickerType.RENTAL))
    game.jokers.append(joker)
    initial_money = game.money
    game.end_of_round_effects()
    assert game.money == initial_money - 3

def test_save_load_game():
    game = create_dummy_game()
    save_game(game, "test_save.json")
    loaded_game = load_game("test_save.json")

    assert loaded_game is not None
    assert loaded_game.money == game.money
    assert loaded_game.round == game.round
    assert loaded_game.hands == game.hands
    assert loaded_game.discards == game.discards
    assert loaded_game.score == game.score
    assert loaded_game.ante == game.ante
    assert loaded_game.game_over == game.game_over
    assert loaded_game.current_blind_index == game.current_blind_index
    assert loaded_game.current_blind.name == game.current_blind.name

    # Compare hand cards
    assert len(loaded_game.hand) == len(game.hand)
    for i in range(len(game.hand)):
        assert loaded_game.hand[i].suit == game.hand[i].suit
        assert loaded_game.hand[i].rank == game.hand[i].rank
        assert loaded_game.hand[i].enhancement == game.hand[i].enhancement
        assert loaded_game.hand[i].edition == game.hand[i].edition
        assert loaded_game.hand[i].seal == game.hand[i].seal

    # Compare jokers
    assert len(loaded_game.jokers) == len(game.jokers)
    for i in range(len(game.jokers)):
        assert loaded_game.jokers[i].name == game.jokers[i].name
        assert loaded_game.jokers[i].description == game.jokers[i].description
        assert len(loaded_game.jokers[i].stickers) == len(game.jokers[i].stickers)
        assert loaded_game.jokers[i].rounds_active == game.jokers[i].rounds_active
        assert loaded_game.jokers[i].is_debuffed == game.jokers[i].is_debuffed

    # Compare vouchers
    assert len(loaded_game.vouchers) == len(game.vouchers)
    for i in range(len(game.vouchers)):
        assert loaded_game.vouchers[i].name == game.vouchers[i].name

    # Compare tarot cards
    assert len(loaded_game.tarot_cards) == len(game.tarot_cards)
    for i in range(len(game.tarot_cards)):
        assert loaded_game.tarot_cards[i].name == game.tarot_cards[i].name

    # Compare spectral cards
    assert len(loaded_game.spectral_cards) == len(game.spectral_cards)
    for i in range(len(game.spectral_cards)):
        assert loaded_game.spectral_cards[i].name == game.spectral_cards[i].name

    # Compare planet cards
    assert len(loaded_game.planet_cards) == len(game.planet_cards)
    for i in range(len(game.planet_cards)):
        assert loaded_game.planet_cards[i].name == game.planet_cards[i].name

    # Clean up the test save file
    os.remove("test_save.json")

def test_load_game_no_file():
    if os.path.exists("non_existent_save.json"):
        os.remove("non_existent_save.json")
    loaded_game = load_game("non_existent_save.json")
    assert loaded_game is None
