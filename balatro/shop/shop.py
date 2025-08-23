"""This module defines the Shop class where players can purchase various items."""

import random

from ..cards.jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from .stickers import Sticker, StickerType
from .vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from ..cards.tarot_cards import TarotCard, TheFool, TheMagician, TheWorld
from ..cards.planet_cards import (
    PlanetCard,
    Pluto,
    Mercury,
    Uranus,
    Venus,
    Saturn,
    Jupiter,
    Earth,
    Mars,
    Neptune,
    PlanetX,
    Ceres,
    Eris,
)

BASE_COSTS = {
    "Joker (Common)": 5,
    "Joker (Uncommon)": 8,
    "Joker (Rare)": 10,
    "Joker (Legendary)": 20,
    "Playing Card": 1,
    "Tarot Card": 3,
    "Planet Card": 3,
    "Booster Pack (Normal)": 4,
    "Voucher": 10,
}


class BoosterPack:
    """Simple representation of a booster pack."""

    def __init__(self, name: str, pack_type: str):
        self.name = name
        self.pack_type = pack_type  # joker, tarot, or planet
        self.description = f"Choose a {pack_type} card"
        self.cost = BASE_COSTS["Booster Pack (Normal)"]

    def open_pack(self, game):
        """Generate cards based on pack type and let the player pick one."""
        if self.pack_type == "joker":
            options = [random.choice([JokerOfGreed, JokerOfMadness, ChipJoker])() for _ in range(3)]
        elif self.pack_type == "tarot":
            options = [random.choice([TheFool, TheMagician, TheWorld])() for _ in range(3)]
        else:  # planet
            planet_pool = [
                Pluto,
                Mercury,
                Uranus,
                Venus,
                Saturn,
                Jupiter,
                Earth,
                Mars,
                Neptune,
                PlanetX,
                Ceres,
                Eris,
            ]
            options = [random.choice(planet_pool)() for _ in range(3)]

        print(f"--- {self.name} Contents ---")
        for i, opt in enumerate(options):
            desc = getattr(opt, "description", "")
            print(f"[{i}] {opt.name} - {desc}")
        print("---------------------------")
        choice = input("Choose an item by index or press Enter to skip: ").strip()
        if choice == "":
            return
        try:
            idx = int(choice)
            card = options[idx]
            if isinstance(card, Joker):
                game.player.jokers.append(card)
                print(f"Added {card.name} to your Jokers.")
            elif isinstance(card, TarotCard):
                game.player.tarot_cards.append(card)
                print(f"Added {card.name} to your Tarot Cards.")
            elif isinstance(card, PlanetCard):
                game.player.planet_cards.append(card)
                print(f"Added {card.name} to your Planet Cards.")
        except (ValueError, IndexError):
            print("Invalid selection.")


class Shop:
    """Represents the in-game shop where players can buy items."""

    def __init__(self):
        self.items: list = []

    def generate_items(self, game):
        self.items = []
        available_jokers = [JokerOfGreed, JokerOfMadness, ChipJoker]
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]
        available_tarot = [TheFool, TheMagician, TheWorld]
        available_planets = [
            Pluto,
            Mercury,
            Uranus,
            Venus,
            Saturn,
            Jupiter,
            Earth,
            Mars,
            Neptune,
            PlanetX,
            Ceres,
            Eris,
        ]

        booster_types = [
            ("Joker Pack", "joker"),
            ("Arcana Pack", "tarot"),
            ("Celestial Pack", "planet"),
        ]
        for _ in range(2):
            name, pack_type = random.choice(booster_types)
            self.items.append(BoosterPack(name=name, pack_type=pack_type))

        if not game.voucher_purchased:
            voucher = random.choice(available_vouchers)()
            voucher.cost = BASE_COSTS["Voucher"]
            self.items.append(voucher)

        for _ in range(2):
            choice = random.choice(["joker", "tarot", "planet"])
            if choice == "joker":
                item = random.choice(available_jokers)()
                item.cost = BASE_COSTS["Joker (Common)"]
            elif choice == "tarot":
                item = random.choice(available_tarot)()
                item.cost = BASE_COSTS["Tarot Card"]
            else:
                item = random.choice(available_planets)()
                item.cost = BASE_COSTS["Planet Card"]
            self.items.append(item)

    def display_items(self, money: int):
        print(f"--- Shop Items (Money: ${money}) ---")
        for i, item in enumerate(self.items):
            desc = getattr(item, "description", "")
            print(f"[{i}] {item.name} - Cost: ${item.cost} - {desc}")
        print("[L] Leave shop")
        print("------------------")

    def purchase_item(self, item_index: int, game) -> bool:
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if game.money >= item.cost:
                game.money -= item.cost
                if isinstance(item, Joker):
                    if game.ante >= 4 and random.random() < 0.3:
                        item.stickers.append(Sticker(StickerType.ETERNAL))
                        print(f"  {item.name} gained an Eternal Sticker!")
                    elif game.ante >= 7 and random.random() < 0.3:
                        item.stickers.append(Sticker(StickerType.PERISHABLE))
                        print(f"  {item.name} gained a Perishable Sticker!")
                    elif game.ante >= 8 and random.random() < 0.3:
                        item.stickers.append(Sticker(StickerType.RENTAL))
                        print(f"  {item.name} gained a Rental Sticker!")
                    game.player.jokers.append(item)
                    print(f"Purchased {item.name}! Added to your Jokers.")
                elif isinstance(item, Voucher):
                    game.player.vouchers.append(item)
                    game.voucher_purchased = True
                    item.apply_effect(game)
                    print(f"Purchased {item.name}! Effect applied.")
                elif isinstance(item, TarotCard):
                    game.player.tarot_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Tarot Cards.")
                elif isinstance(item, PlanetCard):
                    game.player.planet_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Planet Cards.")
                elif isinstance(item, BoosterPack):
                    item.open_pack(game)
                self.items.pop(item_index)
                return True
            else:
                print("Not enough money to purchase this item.")
        else:
            print("Invalid item index.")
        return False
