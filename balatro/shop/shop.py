"""This module defines the Shop class where players can purchase various items."""

import random

from ..cards.jokers import Joker, load_jokers
from .stickers import Sticker, StickerType
from .vouchers import Voucher, load_vouchers
from ..cards.tarot_cards import TarotCard, load_tarot_cards
from ..cards.spectral_cards import SpectralCard, load_spectral_cards
from ..cards.planet_cards import PlanetCard, load_planet_cards
from ..utils import get_user_input

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
        available_cards = []
        if self.pack_type == "joker":
            options = random.sample(load_jokers(), 3)
        elif self.pack_type == "tarot":
            options = random.sample(load_tarot_cards(), 3)
            deck_cards = game.player.deck.cards
            available_cards = (
                random.sample(deck_cards, min(9, len(deck_cards))) if deck_cards else []
            )
        elif self.pack_type == "spectral":
            options = random.sample(load_spectral_cards(), 3)
            deck_cards = game.player.deck.cards
            available_cards = (
                random.sample(deck_cards, min(9, len(deck_cards))) if deck_cards else []
            )
        else:  # planet
            options = random.sample(load_planet_cards(), 3)

        print(f"--- {self.name} Contents ---")
        for i, opt in enumerate(options):
            desc = getattr(opt, "description", "")
            print(f"[{i}] {opt.name} - {desc}")
        if available_cards:
            print("--- 9 Card Hand ---")
            for i, c in enumerate(available_cards):
                print(f"[{i}] {c}")
            print("-------------------")
        print("---------------------------")
        choice = get_user_input("Choose an item by index or press Enter to skip: ").strip()
        if choice == "":
            return
        try:
            idx = int(choice)
            card = options[idx]
            if isinstance(card, Joker):
                game.player.jokers.append(card)
                print(f"Added {card.name} to your Jokers.")
            elif isinstance(card, PlanetCard):
                apply_now = (
                    get_user_input("Apply this card now? (y/n): ")
                    .strip()
                    .lower()
                    == "y"
                )
                if apply_now:
                    card.apply_effect(game)
                    game.last_used_card = card
                else:
                    if game.player.add_planet_card(card):
                        print(f"Added {card.name} to your Planet Cards.")
                    else:
                        card.apply_effect(game)
                        game.last_used_card = card
            elif isinstance(card, TarotCard) or isinstance(card, SpectralCard):
                if card.targets > 0 and available_cards:
                    while True:
                        print("--- 9 Card Hand ---")
                        for i, c in enumerate(available_cards):
                            print(f"[{i}] {c}")
                        print("-------------------")
                        target = get_user_input(
                            "Select target indices separated by space or press Enter to keep card: "
                        ).strip()
                        if not target:
                            break
                        try:
                            indices = [int(x) for x in target.split()][: card.targets]
                            chosen = [
                                available_cards[i]
                                for i in indices
                                if 0 <= i < len(available_cards)
                            ]
                            if len(chosen) != len(indices):
                                raise ValueError
                            card.apply_effect(game, chosen)
                            return
                        except ValueError:
                            print("Invalid card selection.")
                apply_now = False
                if card.targets == 0:
                    choice_apply = get_user_input(
                        "Apply this card now? (y/n): "
                    ).strip().lower()
                    apply_now = choice_apply == "y"
                if apply_now and card.targets == 0:
                    card.apply_effect(game, [])
                else:
                    if isinstance(card, TarotCard):
                        if game.player.add_tarot_card(card):
                            print(f"Added {card.name} to your Tarot Cards.")
                        elif card.targets == 0:
                            card.apply_effect(game, [])
                    else:
                        if game.player.add_spectral_card(card):
                            print(f"Added {card.name} to your Spectral Cards.")
                        elif card.targets == 0:
                            card.apply_effect(game, [])
        except (ValueError, IndexError):
            print("Invalid selection.")


class Shop:
    """Represents the in-game shop where players can buy items."""

    def __init__(self):
        self.items: list = []

    def generate_items(self, game):
        self.items = []
        available_vouchers = load_vouchers()

        booster_types = [
            ("Joker Pack", "joker"),
            ("Arcana Pack", "tarot"),
            ("Celestial Pack", "planet"),
            ("Spectral Pack", "spectral"),
        ]
        for _ in range(2):
            name, pack_type = random.choice(booster_types)
            self.items.append(BoosterPack(name=name, pack_type=pack_type))

        if not game.voucher_purchased and available_vouchers:
            voucher = random.choice(available_vouchers)
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
                    if item.targets > 0:
                        deck_cards = game.player.deck.cards
                        available_cards = (
                            random.sample(deck_cards, min(9, len(deck_cards))) if deck_cards else []
                        )
                        if available_cards:
                            print("--- 9 Card Hand ---")
                            for i, c in enumerate(available_cards):
                                print(f"[{i}] {c}")
                            print("-------------------")
                            target = get_user_input(
                                "Select target indices separated by space or press Enter to keep card: "
                            ).strip()
                            if target:
                                try:
                                    indices = [int(x) for x in target.split()][: item.targets]
                                    chosen = [
                                        available_cards[i]
                                        for i in indices
                                        if 0 <= i < len(available_cards)
                                    ]
                                    item.apply_effect(game, chosen)
                                    self.items.pop(item_index)
                                    return True
                                except ValueError:
                                    print("Invalid card selection.")
                    apply_now = (
                        get_user_input("Apply this card now? (y/n): ")
                        .strip()
                        .lower()
                        == "y"
                    )
                    if apply_now and item.targets == 0:
                        item.apply_effect(game, [])
                    else:
                        if not game.player.add_tarot_card(item):
                            item.apply_effect(game, [])
                        else:
                            print(f"Purchased {item.name}! Added to your Tarot Cards.")
                elif isinstance(item, SpectralCard):
                    if item.targets > 0:
                        deck_cards = game.player.deck.cards
                        available_cards = (
                            random.sample(deck_cards, min(9, len(deck_cards))) if deck_cards else []
                        )
                        if available_cards:
                            print("--- 9 Card Hand ---")
                            for i, c in enumerate(available_cards):
                                print(f"[{i}] {c}")
                            print("-------------------")
                            target = get_user_input(
                                "Select target indices separated by space or press Enter to keep card: "
                            ).strip()
                            if target:
                                try:
                                    indices = [int(x) for x in target.split()][: item.targets]
                                    chosen = [
                                        available_cards[i]
                                        for i in indices
                                        if 0 <= i < len(available_cards)
                                    ]
                                    if len(chosen) != len(indices):
                                        raise ValueError
                                    item.apply_effect(game, chosen)
                                    self.items.pop(item_index)
                                    return True
                                except ValueError:
                                    print("Invalid card selection.")
                    apply_now = False
                    if item.targets == 0:
                        apply_now = (
                            get_user_input("Apply this card now? (y/n): ")
                            .strip()
                            .lower()
                            == "y"
                        )
                    if apply_now and item.targets == 0:
                        item.apply_effect(game, [])
                    else:
                        if not game.player.add_spectral_card(item):
                            print(f"Purchased {item.name}, but no room to store it.")
                        else:
                            print(f"Purchased {item.name}! Added to your Spectral Cards.")
                elif isinstance(item, PlanetCard):
                    apply_now = (
                        get_user_input("Apply this card now? (y/n): ")
                        .strip()
                        .lower()
                        == "y"
                    )
                    if apply_now:
                        item.apply_effect(game)
                        game.last_used_card = item
                    else:
                        if not game.player.add_planet_card(item):
                            item.apply_effect(game)
                            game.last_used_card = item
                        else:
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
