import pytest
from balatro.jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker, joker_from_dict
from balatro.stickers import Sticker, StickerType

def test_joker_creation():
    joker = Joker("Test Joker", "A simple test joker.")
    assert joker.name == "Test Joker"
    assert joker.description == "A simple test joker."
    assert joker.stickers == []
    assert joker.rounds_active == 0
    assert joker.is_debuffed == False

def test_joker_apply_chips_mult():
    joker = Joker("Test Joker", "A simple test joker.")
    assert joker.apply_chips(100) == 100
    assert joker.apply_mult(5) == 5

def test_joker_debuffed_effects():
    joker = Joker("Test Joker", "A simple test joker.")
    joker.is_debuffed = True
    assert joker.apply_chips(100) == 0
    assert joker.apply_mult(5) == 0

def test_joker_of_greed():
    joker = JokerOfGreed()
    assert joker.name == "Joker of Greed"
    assert joker.description == "Adds +4 Mult for every hand played."
    joker.hands_played = 2
    assert joker.apply_mult(10) == 18 # 10 + (4 * 2)

def test_joker_of_madness():
    joker = JokerOfMadness()
    assert joker.name == "Joker of Madness"
    assert joker.description == "Adds a flat +10 Mult."
    assert joker.apply_mult(5) == 15 # 5 + 10

def test_chip_joker():
    joker = ChipJoker()
    assert joker.name == "Chip Joker"
    assert joker.description == "Adds +100 Chips."
    assert joker.apply_chips(50) == 150 # 50 + 100

def test_joker_to_dict():
    joker = JokerOfGreed()
    joker.hands_played = 3
    joker.stickers.append(Sticker(StickerType.PERISHABLE))
    joker.rounds_active = 1
    joker.is_debuffed = False
    joker_dict = joker.to_dict()
    assert joker_dict["_class"] == "JokerOfGreed"
    assert joker_dict["name"] == "Joker of Greed"
    assert joker_dict["description"] == "Adds +4 Mult for every hand played."
    assert len(joker_dict["stickers"]) == 1
    assert joker_dict["stickers"][0]["sticker_type"] == "Perishable"
    assert joker_dict["rounds_active"] == 1
    assert joker_dict["is_debuffed"] == False
    assert joker_dict["hands_played"] == 3

def test_joker_from_dict():
    joker_dict = {
        "_class": "JokerOfGreed",
        "name": "Joker of Greed",
        "description": "Adds +4 Mult for every hand played.",
        "stickers": [{"sticker_type": "Eternal"}],
        "rounds_active": 2,
        "is_debuffed": True,
        "hands_played": 5
    }
    joker = joker_from_dict(joker_dict)
    assert isinstance(joker, JokerOfGreed)
    assert joker.name == "Joker of Greed"
    assert joker.description == "Adds +4 Mult for every hand played."
    assert len(joker.stickers) == 1
    assert joker.stickers[0].sticker_type == StickerType.ETERNAL
    assert joker.rounds_active == 2
    assert joker.is_debuffed == True
    assert joker.hands_played == 5

def test_joker_from_dict_base_joker():
    joker_dict = {
        "_class": "Joker",
        "name": "Base Joker",
        "description": "A base joker.",
        "stickers": [],
        "rounds_active": 0,
        "is_debuffed": False
    }
    joker = joker_from_dict(joker_dict)
    assert isinstance(joker, Joker)
    assert joker.name == "Base Joker"
    assert joker.description == "A base joker."
    assert joker.stickers == []
    assert joker.rounds_active == 0
    assert joker.is_debuffed == False
