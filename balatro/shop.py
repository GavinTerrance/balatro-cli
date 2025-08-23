# balatro/shop.py

import random
from .jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from .stickers import Sticker, StickerType
from .vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from .tarot_cards import TarotCard, TheFool, TheMagician, TheWorld

class Shop:
    def __init__(self):
        self.items = []
        self.generate_items()

    def generate_items(self):
        self.items = []
        # For now, a simple random selection of Jokers and Vouchers
        available_jokers = [JokerOfGreed, JokerOfMadness, ChipJoker]
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]
        available_tarot_cards = [TheFool, TheMagician, TheWorld]

        # Add 3 random jokers
        for _ in range(3):
            self.items.append(random.choice(available_jokers)())
        
        # Add 1 random voucher
        self.items.append(random.choice(available_vouchers)())

        # Add 1 random tarot card
        self.items.append(random.choice(available_tarot_cards)())

    def display_items(self):
        print("--- Shop Items ---")
        for i, item in enumerate(self.items):
            print(f"[{i}] {item.name} - Cost: ${item.cost} - {item.description}")
        print("------------------")

    def purchase_item(self, item_index: int, game) -> bool:
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if game.money >= item.cost:
                game.money -= item.cost
                if isinstance(item, Joker):
                    # Apply stickers based on game ante (difficulty)
                    if game.ante >= 4 and random.random() < 0.3: # Black Stake and higher
                        item.stickers.append(Sticker(StickerType.ETERNAL))
                        print(f"  {item.name} gained an Eternal Sticker!")
                    elif game.ante >= 7 and random.random() < 0.3: # Orange Stake and higher
                        item.stickers.append(Sticker(StickerType.PERISHABLE))
                        print(f"  {item.name} gained a Perishable Sticker!")
                    elif game.ante >= 8 and random.random() < 0.3: # Gold Stake and higher
                        item.stickers.append(Sticker(StickerType.RENTAL))
                        print(f"  {item.name} gained a Rental Sticker!")
                    
                    game.jokers.append(item)
                    print(f"Purchased {item.name}! Added to your Jokers.")
                elif isinstance(item, Voucher):
                    game.vouchers.append(item)
                    item.apply_effect(game) # Apply effect immediately upon purchase
                    print(f"Purchased {item.name}! Effect applied.")
                elif isinstance(item, TarotCard):
                    game.tarot_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Tarot Cards.")
                self.items.pop(item_index) # Remove purchased item from shop
                return True
            else:
                print("Not enough money to purchase this item.")
        else:
            print("Invalid item index.")
        return False
