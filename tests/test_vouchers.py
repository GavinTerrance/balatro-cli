import pytest
from balatro.vouchers import Voucher, TarotMerchant, CardSharp, Honeypot, voucher_from_dict

def test_voucher_creation():
    voucher = Voucher("Test Voucher", "A simple test voucher.", 5)
    assert voucher.name == "Test Voucher"
    assert voucher.description == "A simple test voucher."
    assert voucher.cost == 5

def test_voucher_repr():
    voucher = Voucher("Test Voucher", "A simple test voucher.", 5)
    assert repr(voucher) == "Voucher(name='Test Voucher', cost=5)"

def test_tarot_merchant_creation():
    tm = TarotMerchant()
    assert tm.name == "Tarot Merchant"
    assert tm.description == "Tarot cards appear in the shop."
    assert tm.cost == 4

def test_card_sharp_creation():
    cs = CardSharp()
    assert cs.name == "Card Sharp"
    assert cs.description == "First hand of each round gets +2 Mult."
    assert cs.cost == 4

def test_honeypot_creation():
    hp = Honeypot()
    assert hp.name == "Honeypot"
    assert hp.description == "Gain $10 when you sell a Joker."
    assert hp.cost == 4

def test_voucher_to_dict():
    voucher = TarotMerchant()
    voucher_dict = voucher.to_dict()
    assert voucher_dict["_class"] == "TarotMerchant"
    assert voucher_dict["name"] == "Tarot Merchant"
    assert voucher_dict["description"] == "Tarot cards appear in the shop."
    assert voucher_dict["cost"] == 4

def test_voucher_from_dict():
    voucher_dict = {
        "_class": "CardSharp",
        "name": "Card Sharp",
        "description": "First hand of each round gets +2 Mult.",
        "cost": 4
    }
    voucher = voucher_from_dict(voucher_dict)
    assert isinstance(voucher, CardSharp)
    assert voucher.name == "Card Sharp"
    assert voucher.description == "First hand of each round gets +2 Mult."
    assert voucher.cost == 4
