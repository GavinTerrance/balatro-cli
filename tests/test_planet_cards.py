import pytest
from balatro.planet_cards import PlanetCard, PlanetCardType, planet_card_from_dict

# Mock Game class for testing apply_effect methods
class MockGame:
    def __init__(self):
        pass

def test_planet_card_creation():
    planet = PlanetCard("Test Planet", 10, 2, "High Card", 3)
    assert planet.name == "Test Planet"
    assert planet.chips_bonus == 10
    assert planet.mult_bonus == 2
    assert planet.poker_hand_type == "High Card"
    assert planet.cost == 3

def test_planet_card_repr():
    planet = PlanetCard("Test Planet", 10, 2, "High Card", 3)
    assert repr(planet) == "PlanetCard(name='Test Planet')"

def test_planet_card_to_dict():
    planet = Pluto()
    planet_dict = planet.to_dict()
    assert planet_dict["_class"] == "Pluto"
    assert planet_dict["name"] == "Pluto"
    assert planet_dict["chips_bonus"] == 10
    assert planet_dict["mult_bonus"] == 1
    assert planet_dict["poker_hand_type"] == "High Card"
    assert planet_dict["cost"] == 0

def test_planet_card_from_dict():
    planet_dict = {
        "_class": "Mercury",
        "name": "Mercury",
        "chips_bonus": 15,
        "mult_bonus": 1,
        "poker_hand_type": "Pair",
        "cost": 0
    }
    planet = planet_card_from_dict(planet_dict)
    assert isinstance(planet, planet_card_from_dict(planet_dict).__class__)
    assert planet.name == "Mercury"
    assert planet.chips_bonus == 15
    assert planet.mult_bonus == 1
    assert planet.poker_hand_type == "Pair"
    assert planet.cost == 0
