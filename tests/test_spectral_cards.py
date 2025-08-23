import pytest
from balatro.spectral_cards import SpectralCard, SpectralCardType, spectral_card_from_dict

# Mock Game class for testing apply_effect methods
class MockGame:
    def __init__(self):
        pass

def test_spectral_card_creation():
    spectral = SpectralCard("Test Spectral", "A simple test spectral.", 5)
    assert spectral.name == "Test Spectral"
    assert spectral.description == "A simple test spectral."
    assert spectral.cost == 5

def test_spectral_card_repr():
    spectral = SpectralCard("Test Spectral", "A simple test spectral.", 5)
    assert repr(spectral) == "SpectralCard(name='Test Spectral')"

def test_spectral_card_to_dict():
    spectral = SpectralCard("Test Spectral", "A simple test spectral.", 5)
    spectral_dict = spectral.to_dict()
    assert spectral_dict["_class"] == "SpectralCard"
    assert spectral_dict["name"] == "Test Spectral"
    assert spectral_dict["description"] == "A simple test spectral."
    assert spectral_dict["cost"] == 5

def test_spectral_card_from_dict():
    spectral_dict = {
        "_class": "TheSoul",
        "name": "The Soul",
        "description": "Creates a random Rare Joker.",
        "cost": 0
    }
    spectral = spectral_card_from_dict(spectral_dict)
    assert isinstance(spectral, spectral_card_from_dict(spectral_dict).__class__)
    assert spectral.name == "The Soul"
    assert spectral.description == "Creates a random Rare Joker."
    assert spectral.cost == 0
