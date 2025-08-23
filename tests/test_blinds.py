import pytest
from balatro.blinds import Blind, SmallBlind, BigBlind, BossBlind

def test_blind_creation():
    blind = Blind("Test Blind", 100)
    assert blind.name == "Test Blind"
    assert blind.score_required == 100

def test_blind_repr():
    blind = Blind("Test Blind", 100)
    assert repr(blind) == "Blind(name='Test Blind', score_required=100)"

def test_small_blind_creation():
    small_blind = SmallBlind()
    assert small_blind.name == "Small Blind"
    assert small_blind.score_required == 300

def test_big_blind_creation():
    big_blind = BigBlind()
    assert big_blind.name == "Big Blind"
    assert big_blind.score_required == 1000

def test_boss_blind_creation():
    boss_blind = BossBlind()
    assert boss_blind.name == "Boss Blind"
    assert boss_blind.score_required == 2000
