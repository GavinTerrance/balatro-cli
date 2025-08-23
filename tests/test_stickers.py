import pytest
from balatro.stickers import Sticker, StickerType

def test_sticker_type_enum():
    assert StickerType.ETERNAL.value == "Eternal"
    assert StickerType.GOLD_STAKE.value == "Gold Stake"

def test_sticker_creation():
    sticker = Sticker(StickerType.ETERNAL)
    assert sticker.sticker_type == StickerType.ETERNAL

def test_sticker_repr():
    sticker = Sticker(StickerType.PERISHABLE)
    assert repr(sticker) == "Sticker(type='Perishable')"

def test_sticker_str():
    sticker = Sticker(StickerType.RENTAL)
    assert str(sticker) == "Rental"

def test_sticker_to_dict():
    sticker = Sticker(StickerType.WHITE_STAKE)
    sticker_dict = sticker.to_dict()
    assert sticker_dict["sticker_type"] == "White Stake"

def test_sticker_from_dict():
    sticker_dict = {"sticker_type": "Red Stake"}
    sticker = Sticker.from_dict(sticker_dict)
    assert sticker.sticker_type == StickerType.RED_STAKE
