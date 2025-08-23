import pytest
from balatro.tarot_cards import TarotCard, TheFool, TheMagician, TheWorld, tarot_card_from_dict
from balatro.jokers import JokerOfGreed, JokerOfMadness, ChipJoker
from balatro.vouchers import TarotMerchant, CardSharp, Honeypot
from balatro.cards import Card, Suit, Rank

# Mock Game class for testing apply_effect methods
class MockGame:
    def __init__(self):
        self.jokers = []
        self.vouchers = []
        self.hand = [Card(Suit.SPADES, Rank.TWO), Card(Suit.CLUBS, Rank.THREE)]

def test_tarot_card_creation():
    tarot = TarotCard("Test Tarot", "A simple test tarot.", 3)
    assert tarot.name == "Test Tarot"
    assert tarot.description == "A simple test tarot."
    assert tarot.cost == 3

def test_tarot_card_repr():
    tarot = TarotCard("Test Tarot", "A simple test tarot.", 3)
    assert repr(tarot) == "TarotCard(name='Test Tarot')"

def test_the_fool_creation():
    fool = TheFool()
    assert fool.name == "The Fool"
    assert fool.description == "Generates a random Joker."
    assert fool.cost == 4

def test_the_fool_apply_effect():
    game = MockGame()
    fool = TheFool()
    initial_joker_count = len(game.jokers)
    fool.apply_effect(game)
    assert len(game.jokers) == initial_joker_count + 1
    assert isinstance(game.jokers[0], (JokerOfGreed, JokerOfMadness, ChipJoker))

def test_the_magician_creation():
    magician = TheMagician()
    assert magician.name == "The Magician"
    assert magician.description == "Upgrades a selected card to a higher rank."
    assert magician.cost == 4

# Test for TheMagician.apply_effect is difficult without mocking user input
# and will be skipped for now.

def test_the_world_creation():
    world = TheWorld()
    assert world.name == "The World"
    assert world.description == "Generates a random Voucher."
    assert world.cost == 4

def test_the_world_apply_effect():
    game = MockGame()
    world = TheWorld()
    initial_voucher_count = len(game.vouchers)
    world.apply_effect(game)
    assert len(game.vouchers) == initial_voucher_count + 1
    assert isinstance(game.vouchers[0], (TarotMerchant, CardSharp, Honeypot))

def test_tarot_card_to_dict():
    tarot = TheFool()
    tarot_dict = tarot.to_dict()
    assert tarot_dict["_class"] == "TheFool"
    assert tarot_dict["name"] == "The Fool"
    assert tarot_dict["description"] == "Generates a random Joker."
    assert tarot_dict["cost"] == 4

def test_tarot_card_from_dict():
    tarot_dict = {
        "_class": "TheMagician",
        "name": "The Magician",
        "description": "Upgrades a selected card to a higher rank.",
        "cost": 4
    }
    tarot = tarot_card_from_dict(tarot_dict)
    assert isinstance(tarot, TheMagician)
    assert tarot.name == "The Magician"
    assert tarot.description == "Upgrades a selected card to a higher rank."
    assert tarot.cost == 4
