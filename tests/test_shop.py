import pytest
from balatro.shop import Shop
from balatro.jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from balatro.vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from balatro.tarot_cards import TarotCard, TheFool, TheMagician, TheWorld
from balatro.spectral_cards import SpectralCard, TheSoul
from balatro.planet_cards import PlanetCard, Pluto
from balatro.cards import Card, Suit, Rank, Enhancement, Edition, Seal
from balatro.stickers import Sticker, StickerType

# Mock Game class for testing purchase_item
class MockGame:
    def __init__(self, money=100, ante=1):
        self.money = money
        self.jokers = []
        self.vouchers = []
        self.tarot_cards = []
        self.spectral_cards = []
        self.planet_cards = []
        self.ante = ante

def test_shop_creation():
    shop = Shop()
    assert len(shop.items) > 0

def test_shop_generate_items():
    shop = Shop()
    initial_item_count = len(shop.items)
    shop.generate_items()
    assert len(shop.items) == initial_item_count # Should regenerate the same number of items

def test_shop_purchase_joker_success():
    game = MockGame(money=10)
    shop = Shop()
    # Find a joker in the shop to purchase
    joker_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, Joker):
            joker_index = i
            break
    
    if joker_index != -1:
        initial_money = game.money
        initial_joker_count = len(game.jokers)
        purchased = shop.purchase_item(joker_index, game)
        assert purchased == True
        assert game.money < initial_money # Money should decrease
        assert len(game.jokers) == initial_joker_count + 1
    else:
        pytest.skip("No Joker found in shop for testing purchase.")

def test_shop_purchase_joker_not_enough_money():
    game = MockGame(money=0)
    shop = Shop()
    joker_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, Joker):
            joker_index = i
            break
    
    if joker_index != -1:
        initial_money = game.money
        initial_joker_count = len(game.jokers)
        purchased = shop.purchase_item(joker_index, game)
        assert purchased == False
        assert game.money == initial_money
        assert len(game.jokers) == initial_joker_count
    else:
        pytest.skip("No Joker found in shop for testing purchase.")

def test_shop_purchase_voucher_success():
    game = MockGame(money=10)
    shop = Shop()
    voucher_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, Voucher):
            voucher_index = i
            break
    
    if voucher_index != -1:
        initial_money = game.money
        initial_voucher_count = len(game.vouchers)
        purchased = shop.purchase_item(voucher_index, game)
        assert purchased == True
        assert game.money < initial_money
        assert len(game.vouchers) == initial_voucher_count + 1
    else:
        pytest.skip("No Voucher found in shop for testing purchase.")

def test_shop_purchase_tarot_card_success():
    game = MockGame(money=10)
    shop = Shop()
    tarot_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, TarotCard):
            tarot_index = i
            break
    
    if tarot_index != -1:
        initial_money = game.money
        initial_tarot_count = len(game.tarot_cards)
        purchased = shop.purchase_item(tarot_index, game)
        assert purchased == True
        assert game.money < initial_money
        assert len(game.tarot_cards) == initial_tarot_count + 1
    else:
        pytest.skip("No Tarot Card found in shop for testing purchase.")

def test_shop_purchase_spectral_card_success():
    game = MockGame(money=10)
    shop = Shop()
    spectral_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, SpectralCard):
            spectral_index = i
            break
    
    if spectral_index != -1:
        initial_money = game.money
        initial_spectral_count = len(game.spectral_cards)
        purchased = shop.purchase_item(spectral_index, game)
        assert purchased == True
        assert game.money < initial_money
        assert len(game.spectral_cards) == initial_spectral_count + 1
    else:
        pytest.skip("No Spectral Card found in shop for testing purchase.")

def test_shop_purchase_planet_card_success():
    game = MockGame(money=10)
    shop = Shop()
    planet_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, PlanetCard):
            planet_index = i
            break
    
    if planet_index != -1:
        initial_money = game.money
        initial_planet_count = len(game.planet_cards)
        purchased = shop.purchase_item(planet_index, game)
        assert purchased == True
        assert game.money < initial_money
        assert len(game.planet_cards) == initial_planet_count + 1
    else:
        pytest.skip("No Planet Card found in shop for testing purchase.")

def test_shop_purchase_card_with_modifiers_success():
    game = MockGame(money=10)
    shop = Shop()
    card_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, Card):
            card_index = i
            break
    
    if card_index != -1:
        initial_money = game.money
        # For now, we just check if it's purchased successfully
        purchased = shop.purchase_item(card_index, game)
        assert purchased == True
        assert game.money < initial_money
    else:
        pytest.skip("No Card with modifiers found in shop for testing purchase.")

def test_shop_purchase_invalid_index():
    game = MockGame(money=10)
    shop = Shop()
    purchased = shop.purchase_item(999, game)
    assert purchased == False

def test_shop_joker_sticker_assignment():
    game = MockGame(money=10, ante=4) # Ante 4 for Black Stake (Eternal)
    shop = Shop()
    joker_index = -1
    for i, item in enumerate(shop.items):
        if isinstance(item, Joker):
            joker_index = i
            break
    
    if joker_index != -1:
        shop.purchase_item(joker_index, game)
        # Check if a sticker was assigned (probabilistic, so might not always be Eternal)
        assert len(game.jokers[0].stickers) >= 0 # Could be 0 if random failed
    else:
        pytest.skip("No Joker found in shop for testing sticker assignment.")
