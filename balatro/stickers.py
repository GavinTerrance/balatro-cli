from enum import Enum

class StickerType(Enum):
    ETERNAL = "Eternal"
    PERISHABLE = "Perishable"
    RENTAL = "Rental"
    WHITE_STAKE = "White Stake"
    RED_STAKE = "Red Stake"
    GREEN_STAKE = "Green Stake"
    BLACK_STAKE = "Black Stake"
    BLUE_STAKE = "Blue Stake"
    PURPLE_STAKE = "Purple Stake"
    ORANGE_STAKE = "Orange Stake"
    GOLD_STAKE = "Gold Stake"

class Sticker:
    def __init__(self, sticker_type: StickerType):
        self.sticker_type = sticker_type

    def __repr__(self):
        return f"Sticker(type='{self.sticker_type.value}')"

    def __str__(self):
        return self.sticker_type.value

    def to_dict(self):
        return {
            "sticker_type": self.sticker_type.value
        }

    @classmethod
    def from_dict(cls, data):
        return cls(StickerType(data["sticker_type"]))
