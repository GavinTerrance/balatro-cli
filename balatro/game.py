# balatro/game.py

from .deck import Deck
from .cards import Card
from .poker import evaluate_hand
from .scoring import calculate_score
from .jokers import JokerOfMadness # Example Joker
from .vouchers import Voucher, TarotMerchant # Example Voucher
from .blinds import SmallBlind, BigBlind, BossBlind
from .shop import Shop
from .tarot_cards import TarotCard # Import TarotCard base class
from .stickers import StickerType # Import StickerType enum

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = []
        self.jokers = [] # No longer hardcoded
        self.vouchers = [] # No longer hardcoded
        self.tarot_cards = [] # New list for tarot cards
        self.spectral_cards = [] # New list for spectral cards
        self.planet_cards = [] # New list for planet cards
        self.activate_vouchers()

        self.blinds = [SmallBlind(), BigBlind(), BossBlind()]
        self.current_blind_index = 0
        self.current_blind = self.blinds[self.current_blind_index]
        
        self.shop = Shop() # Initialize the shop

        # Game state variables
        self.money = 4
        self.round = 1
        self.hands = 4
        self.discards = 3
        self.score = 0
        self.ante = 1 # Starting ante
        self.game_over = False # New attribute for game over state

    def __repr__(self):
        return (
            f"Game(Ante={self.ante}, round={self.round}, hands={self.hands}, "
            f"discards={self.discards}, score={self.score}, money={self.money}, "
            f"current_blind={self.current_blind.name})"
        )

    def activate_vouchers(self):
        for voucher in self.vouchers:
            voucher.apply_effect(self)

    def advance_blind(self):
        self.current_blind_index += 1
        if self.current_blind_index < len(self.blinds):
            self.current_blind = self.blinds[self.current_blind_index]
            print(f"\n--- Advancing to {self.current_blind.name} (Score required: {self.current_blind.score_required}) ---")
        else:
            print("\n--- All Blinds in Ante Cleared! Advancing to next Ante! ---")
            self.ante += 1
            self.current_blind_index = 0 # Reset blind index for new ante
            self.current_blind = self.blinds[self.current_blind_index]
            self.score = 0 # Reset score for new ante
            print(f"\n--- Now in Ante {self.ante}, starting with {self.current_blind.name} (Score required: {self.current_blind.score_required}) ---")

    def check_blind_cleared(self):
        if self.score >= self.current_blind.score_required:
            print(f"\n--- {self.current_blind.name} Cleared! You gained 10 money! ---")
            self.money += 10
            self.advance_blind()
            return True
        else:
            print(f"\n--- Failed to clear {self.current_blind.name}! Game Over! ---")
            self.game_over = True
            return False

    def end_of_round_effects(self):
        # Handle Perishable and Rental stickers
        for joker in self.jokers:
            for sticker in joker.stickers:
                if sticker.sticker_type == StickerType.PERISHABLE:
                    joker.rounds_active += 1
                    if joker.rounds_active >= 5:
                        joker.is_debuffed = True
                        print(f"{joker.name} has become debuffed due to Perishable Sticker!")
                elif sticker.sticker_type == StickerType.RENTAL:
                    self.money -= 3
                    print(f"Rental fee for {joker.name}: -$3. Current money: ${self.money}")

    def draw_hand(self, hand_size: int = 8):
        # Discard current hand if any, and draw a new one.
        self.hand = self.deck.draw(hand_size)
        self.sort_hand(sort_by='rank') # Sort the hand after drawing

    def use_tarot_card(self, tarot_card_index: int):
        if 0 <= tarot_card_index < len(self.tarot_cards):
            tarot_card = self.tarot_cards.pop(tarot_card_index)
            print(f"Using {tarot_card.name}...")
            tarot_card.apply_effect(self)
        else:
            print("Invalid Tarot card index.")

    def use_spectral_card(self, spectral_card_index: int):
        if 0 <= spectral_card_index < len(self.spectral_cards):
            spectral_card = self.spectral_cards.pop(spectral_card_index)
            print(f"Using {spectral_card.name}...")
            spectral_card.apply_effect(self)
        else:
            print("Invalid Spectral card index.")

    def use_planet_card(self, planet_card_index: int):
        if 0 <= planet_card_index < len(self.planet_cards):
            planet_card = self.planet_cards.pop(planet_card_index)
            print(f"Using {planet_card.name}...")
            planet_card.apply_effect(self)
        else:
            print("Invalid Planet card index.")

    def play_hand(self, cards_to_play: list[Card]):
        if not all(c in self.hand for c in cards_to_play):
            print("Error: One or more cards are not in the current hand.")
            return

        for card in cards_to_play:
            self.hand.remove(card)
        self.sort_hand(sort_by='rank') # Sort the hand after playing cards
        
        played_hand_type = evaluate_hand(cards_to_play)
        if played_hand_type:
            hand_score = calculate_score(played_hand_type, cards_to_play, self.jokers)
            self.score += hand_score
            print(f"Hand played: {played_hand_type.value} for {hand_score} points!")
        else:
            print("No valid poker hand was played.")

        self.hands -= 1
        print(f"Played {len(cards_to_play)} cards. {self.hands} hands remaining.")

        if self.hands == 0: # End of round, check if blind is cleared
            self.check_blind_cleared()

    def discard_cards(self, card_indices: list[int]):
        if self.discards <= 0:
            print("No discards remaining!")
            return

        if not card_indices:
            print("No cards selected to discard.")
            return

        if len(card_indices) > 5:
            print("Error: You can only discard up to 5 cards.")
            return

        # Ensure all indices are valid and unique
        if any(i < 0 or i >= len(self.hand) for i in card_indices):
            print("Error: Invalid card index for discard.")
            return
        if len(card_indices) != len(set(card_indices)):
            print("Error: Duplicate card indices for discard.")
            return

        # Sort indices in descending order to avoid issues when removing
        card_indices.sort(reverse=True)
        discarded_cards = []
        for index in card_indices:
            discarded_cards.append(self.hand.pop(index))
        
        # Draw new cards to replace discarded ones
        new_cards = self.deck.draw(len(discarded_cards))
        self.hand.extend(new_cards)
        self.sort_hand(sort_by='rank') # Sort the hand after discarding
        
        self.discards -= 1
        print(f"Discarded {len(discarded_cards)} cards. {self.discards} discards remaining.")
        self.hands -= 1 # Discarding also counts as a hand played
        print(f"Discarding counts as a hand. {self.hands} hands remaining.")

    def sort_hand(self, sort_by: str = 'rank'):
        # Define a custom sorting key for cards
        def card_sort_key(card):
            rank_order = {
                '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Ten': 10, 
                'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
            }
            if sort_by == 'rank':
                return (rank_order[card.rank.value], card.suit.value)
            elif sort_by == 'suit':
                return (card.suit.value, rank_order[card.rank.value])
            else:
                return (rank_order[card.rank.value], card.suit.value) # Default to rank sort
        self.hand.sort(key=card_sort_key)
