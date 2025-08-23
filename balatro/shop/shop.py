"""This module defines the Shop class where players can purchase various items."""

import random

from ..cards.jokers import Joker, load_jokers
from .stickers import Sticker, StickerType
from .vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from ..cards.tarot_cards import TarotCard, load_tarot_cards
from ..cards.spectral_cards import SpectralCard, TheSoul, BlackHole, Omen
from ..cards.planet_cards import PlanetCard, load_planet_cards

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
        # pack_type can be joker, tarot, planet or spectral
        self.pack_type = pack_type
        self.description = f"Choose a {pack_type} card"
        self.cost = BASE_COSTS["Booster Pack (Normal)"]

    def open_pack(self, game):
        """Generate cards based on pack type and let the player pick one."""
        if self.pack_type == "joker":
            options = random.sample(load_jokers(), 3)
        elif self.pack_type == "tarot":
            options = random.sample(load_tarot_cards(), 3)
        elif self.pack_type == "spectral":
            options = [random.choice([TheSoul, BlackHole, Omen])() for _ in range(3)]
        else:  # planet
            options = random.sample(load_planet_cards(), 3)

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
            elif isinstance(card, PlanetCard):
                game.player.planet_cards.append(card)
                print(f"Added {card.name} to your Planet Cards.")
            elif isinstance(card, TarotCard) or isinstance(card, SpectralCard):
                # Display sample playing cards and current jokers for potential application
                sample_cards = game.deck.cards[:8]
                print("--- Available Cards for Application ---")
                for i, c in enumerate(sample_cards):
                    print(f"[{i}] {c}")
                for j, joker in enumerate(game.player.jokers):
                    print(f"[J{j}] {joker.name}")
                print("---------------------------")
                target = input("Select target index (number or J#) or press Enter to keep card: ").strip()
                if target:
                    if target.upper().startswith("J"):
                        try:
                            j_idx = int(target[1:])
                            joker = game.player.jokers[j_idx]
                            print(
                                f"Applied {card.name} to {joker.name} (effect not yet implemented)."
                            )
                        except (ValueError, IndexError):
                            print("Invalid joker selection.")
                    else:
                        try:
                            c_idx = int(target)
                            chosen_card = sample_cards[c_idx]
                            print(
                                f"Applied {card.name} to {chosen_card} (effect not yet implemented)."
                            )
                        except (ValueError, IndexError):
                            print("Invalid card selection.")
                else:
                    if isinstance(card, TarotCard):
                        game.player.tarot_cards.append(card)
                        print(f"Added {card.name} to your Tarot Cards.")
                    else:
                        game.player.spectral_cards.append(card)
                        print(f"Added {card.name} to your Spectral Cards.")
        except (ValueError, IndexError):
            print("Invalid selection.")


class Shop:
    """Represents the in-game shop where players can buy items."""

    def __init__(self):
        self.items: list = []

    def generate_items(self, game):
        self.items = []
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]

        booster_types = [
            ("Joker Pack", "joker"),
            ("Arcana Pack", "tarot"),
            ("Celestial Pack", "planet"),
            ("Spectral Pack", "spectral"),
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
                item = random.choice(load_jokers())
            elif choice == "tarot":
                item = random.choice(load_tarot_cards())
                item.cost = BASE_COSTS["Tarot Card"]
            else:
                item = random.choice(load_planet_cards())
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
                elif isinstance(item, SpectralCard):
                    game.player.spectral_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Spectral Cards.")
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
