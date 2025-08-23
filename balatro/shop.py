"""This module defines the Shop class where players can purchase various items."""

import random
from .jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from .stickers import Sticker, StickerType
from .vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
from .tarot_cards import TarotCard, TheFool, TheMagician, TheWorld
from .spectral_cards import SpectralCard, TheSoul, BlackHole, Omen, FlatEarth, Seance, Immolate, Observatory, Nebula, Void, Echo, Grim, Sigil, WheelOfFortune, Death, Judgement, HangedMan, Strength, Hermit
from .planet_cards import PlanetCard, Pluto, Mercury, Uranus, Venus, Saturn, Jupiter, Earth, Mars, Neptune, PlanetX, Ceres, Eris
from .cards import Card, Suit, Rank, Enhancement, Edition, Seal

# Base costs for items (from wiki)
BASE_COSTS = {
    "Joker (Common)": 5, # Placeholder, need to define rarity for Jokers
    "Joker (Uncommon)": 8,
    "Joker (Rare)": 10,
    "Joker (Legendary)": 20,
    "Playing Card": 1,
    "Tarot Card": 3,
    "Planet Card": 3,
    "Spectral Card": 4,
    "Booster Pack (Normal)": 4,
    "Booster Pack (Jumbo)": 6,
    "Booster Pack (Mega)": 8,
    "Voucher": 10
}

class Shop:
    """Represents the in-game shop where players can buy items."""
    def __init__(self):
        """Initializes the Shop and generates its initial items."""
        self.items = []
        self.generate_items()

    def generate_items(self):
        """Generates a new set of random items for the shop."""
        self.items = []
        # For now, a simple random selection of Jokers and Vouchers
        available_jokers = [JokerOfGreed, JokerOfMadness, ChipJoker]
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]
        available_tarot_cards = [TheFool, TheMagician, TheWorld]
        available_spectral_cards = [TheSoul, BlackHole, Omen, FlatEarth, Seance, Immolate, Observatory, Nebula, Void, Echo, Grim, Sigil, WheelOfFortune, Death, Judgement, HangedMan, Strength, Hermit]
        available_planet_cards = [Pluto, Mercury, Uranus, Venus, Saturn, Jupiter, Earth, Mars, Neptune, PlanetX, Ceres, Eris]

        # Add 3 random jokers
        for _ in range(3):
            joker = random.choice(available_jokers)()
            joker.cost = BASE_COSTS["Joker (Common)"] # Assign a default common joker cost
            self.items.append(joker)
        
        # Add 1 random voucher
        voucher = random.choice(available_vouchers)()
        voucher.cost = BASE_COSTS["Voucher"]
        self.items.append(voucher)

        # Add 1 random tarot card
        tarot_card = random.choice(available_tarot_cards)()
        tarot_card.cost = BASE_COSTS["Tarot Card"]
        self.items.append(tarot_card)

        # Add 1 random spectral card
        spectral_card = random.choice(available_spectral_cards)()
        spectral_card.cost = BASE_COSTS["Spectral Card"]
        self.items.append(spectral_card)

        # Add 1 random planet card
        planet_card = random.choice(available_planet_cards)()
        planet_card.cost = BASE_COSTS["Planet Card"]
        self.items.append(planet_card)

        # Add 3 random standard playing cards with potential modifiers
        for _ in range(3):
            suit = random.choice(list(Suit))
            rank = random.choice(list(Rank))
            
            enhancement = Enhancement.NONE
            if random.random() < 0.1: # 10% chance for enhancement
                enhancement = random.choice([e for e in list(Enhancement) if e != Enhancement.NONE])
            
            edition = Edition.NONE
            if random.random() < 0.05: # 5% chance for edition
                edition = random.choice([e for e in list(Edition) if e != Edition.NONE])

            seal = Seal.NONE
            if random.random() < 0.05: # 5% chance for seal
                seal = random.choice([s for s in list(Seal) if s != Seal.NONE])

            card = Card(suit, rank, enhancement, edition, seal)
            card.cost = BASE_COSTS["Playing Card"]
            self.items.append(card)

    def display_items(self):
        """Prints the current items available in the shop."""
        print("--- Shop Items ---")
        for i, item in enumerate(self.items):
            print(f"[{i}] {item.name} - Cost: ${item.cost} - {item.description}")
        print("------------------")

    def purchase_item(self, item_index: int, game) -> bool:
        """Attempts to purchase an item from the shop."

        Args:
            item_index (int): The index of the item to purchase.
            game: The current Game object.

        Returns:
            bool: True if the purchase was successful, False otherwise.
        """
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
                elif isinstance(item, SpectralCard):
                    game.spectral_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Spectral Cards.")
                elif isinstance(item, PlanetCard):
                    game.planet_cards.append(item)
                    print(f"Purchased {item.name}! Added to your Planet Cards.")
                self.items.pop(item_index) # Remove purchased item from shop
                return True
            else:
                print("Not enough money to purchase this item.")
        else:
            print("Invalid item index.")
        return False
