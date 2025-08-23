# balatro/tarot_cards.py

from .cards import Card, Suit, Rank
from .jokers import Joker, JokerOfGreed, JokerOfMadness, ChipJoker
from .vouchers import Voucher, TarotMerchant, CardSharp, Honeypot
import random

class TarotCard:
    """Base class for all Tarot cards."""
    def __init__(self, name: str, description: str, cost: int = 0):
        self.name = name
        self.description = description
        self.cost = cost # Tarot cards usually have a cost in shop

    def __repr__(self):
        return f"TarotCard(name='{self.name}')"

    def apply_effect(self, game):
        """Applies the Tarot card's effect to the game state."""
        raise NotImplementedError("Subclasses must implement apply_effect")

# --- Example Tarot Card Implementations ---

class TheFool(TarotCard):
    def __init__(self):
        super().__init__(
            name="The Fool",
            description="Generates a random Joker.",
            cost=4
        )

    def apply_effect(self, game):
        available_jokers = [JokerOfGreed, JokerOfMadness, ChipJoker]
        new_joker = random.choice(available_jokers)()
        game.jokers.append(new_joker)
        print(f"The Fool generated: {new_joker.name}!")

class TheMagician(TarotCard):
    def __init__(self):
        super().__init__(
            name="The Magician",
            description="Upgrades a selected card to a higher rank.",
            cost=4
        )

    def apply_effect(self, game):
        if not game.hand:
            print("No cards in hand to upgrade.")
            return
        
        print("Select a card to upgrade:")
        for i, card in enumerate(game.hand):
            print(f"[{i}] {card}")
        
        try:
            choice = int(input("Enter index of card to upgrade: "))
            if 0 <= choice < len(game.hand):
                card_to_upgrade = game.hand[choice]
                # Simple upgrade logic: find next rank. Needs more robust handling for Ace.
                current_rank_index = list(Rank).index(card_to_upgrade.rank)
                if current_rank_index < len(list(Rank)) - 1:
                    new_rank = list(Rank)[current_rank_index + 1]
                    game.hand[choice] = Card(card_to_upgrade.suit, new_rank)
                    print(f"Upgraded {card_to_upgrade} to {game.hand[choice]}!")
                else:
                    print(f"{card_to_upgrade.rank.value} is already the highest rank.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input.")

class TheWorld(TarotCard):
    def __init__(self):
        super().__init__(
            name="The World",
            description="Generates a random Voucher.",
            cost=4
        )

    def apply_effect(self, game):
        available_vouchers = [TarotMerchant, CardSharp, Honeypot]
        new_voucher = random.choice(available_vouchers)()
        game.vouchers.append(new_voucher)
        new_voucher.apply_effect(game) # Apply effect immediately
        print(f"The World generated: {new_voucher.name}!")
