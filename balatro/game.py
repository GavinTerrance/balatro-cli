"""This module defines the main Game class and its core functionalities."""

from .deck import BaseDeck, RedDeck, GreenDeck, YellowDeck
from .cards import Card, Suit, Rank, Enhancement, Edition, Seal
from .poker import evaluate_hand
from .scoring import calculate_score
from .jokers import Joker, joker_from_dict # Import Joker and joker_from_dict
from .vouchers import Voucher, voucher_from_dict # Import Voucher and voucher_from_dict
from .blinds import SmallBlind, BigBlind, BossBlind
from .shop import Shop
from .tarot_cards import TarotCard, tarot_card_from_dict # Import TarotCard and tarot_card_from_dict
from .spectral_cards import SpectralCard, spectral_card_from_dict # Import SpectralCard and spectral_card_from_dict
from .planet_cards import PlanetCard, planet_card_from_dict # Import PlanetCard and planet_card_from_dict
from .stickers import StickerType # Import StickerType enum
import json

class Game:
    """Represents the main game state and logic for Balatro CLI."""
    def __init__(self, deck_type: str = "Base"):
        """Initializes a new game instance.

        Args:
            deck_type (str, optional): The type of starting deck. Defaults to "Base".
        """
        self.money = 4
        self.round = 1
        self.hands = 4
        self.discards = 3
        self.hand_size = 8
        self.score = 0
        self.ante = 1
        self.game_over = False
        self.earns_interest = True  # default; Green turns this off
        self.sort_by = 'rank'

        # Collections
        self.hand = []
        self.jokers = []
        self.vouchers = []
        self.tarot_cards = []
        self.spectral_cards = []
        self.planet_cards = []

        # Deck (use a canonical key)
        self.deck_key = deck_type  # "Base" | "Red" | "Green" | "Yellow"
        deck_cls = {"Red": RedDeck, "Green": GreenDeck, "Yellow": YellowDeck}.get(self.deck_key, BaseDeck)
        self.deck = deck_cls()
        self.deck.shuffle()

        # Apply deck effects AFTER defaults exist
        if self.deck_key == "Red":
            self.discards += 1
        elif self.deck_key == "Green":
            self.earns_interest = False
        elif self.deck_key == "Yellow":
            self.money += 10

        # Blinds
        self.blinds = [SmallBlind(), BigBlind(), BossBlind()]
        self.current_blind_index = 0
        self.current_blind = self.blinds[0]

        # Shop
        self.shop = Shop()

        # Activate vouchers last so effects read correct baselines
        self.activate_vouchers()

    def to_dict(self):
        """Converts the Game object to a dictionary for serialization."""
        return {
            "deck_type": self.deck_key,
            "hand": [card.to_dict() for card in self.hand],
            "jokers": [joker.to_dict() for joker in self.jokers],
            "vouchers": [voucher.to_dict() for voucher in self.vouchers],
            "tarot_cards": [tarot_card.to_dict() for tarot_card in self.tarot_cards],
            "spectral_cards": [spectral_card.to_dict() for spectral_card in self.spectral_cards],
            "planet_cards": [planet_card.to_dict() for planet_card in self.planet_cards],
            "money": self.money,
            "round": self.round,
            "hands": self.hands,
            "discards": self.discards,
            "score": self.score,
            "ante": self.ante,
            "game_over": self.game_over,
            "current_blind_index": self.current_blind_index
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Game object from a dictionary for deserialization."""
        game = cls(deck_type=data["deck_type"]) # Initialize with deck type
        game.hand = [Card.from_dict(c_data) for c_data in data["hand"]]
        game.jokers = [joker_from_dict(j_data) for j_data in data["jokers"]]
        game.vouchers = [voucher_from_dict(v_data) for v_data in data["vouchers"]]
        game.tarot_cards = [tarot_card_from_dict(t_data) for t_data in data["tarot_cards"]]
        game.spectral_cards = [spectral_card_from_dict(s_data) for s_data in data["spectral_cards"]]
        game.planet_cards = [planet_card_from_dict(p_data) for p_data in data["planet_cards"]]
        game.money = data["money"]
        game.round = data["round"]
        game.hands = data["hands"]
        game.hand_size = data["hand_size"]
        game.discards = data["discards"]
        game.score = data["score"]
        game.ante = data["ante"]
        game.game_over = data["game_over"]
        game.current_blind_index = data["current_blind_index"]
        game.current_blind = game.blinds[game.current_blind_index]
        return game

    def __repr__(self):
        """Returns a string representation of the Game object for debugging."""
        return (
            f"Game(Ante={self.ante}, round={self.round}, hands={self.hands}, "
            f"discards={self.discards}, score={self.score}, money={self.money}, "
            f"current_blind={self.current_blind.name})"
        )

    def activate_vouchers(self):
        """Activates the effects of all owned vouchers."""
        for voucher in self.vouchers:
            voucher.apply_effect(self)

    def advance_blind(self):
        """Advances the game to the next blind or ante."""
        self.current_blind_index += 1
        if self.current_blind_index < len(self.blinds):
            self.current_blind = self.blinds[self.current_blind_index]
            print(f"\n--- Advancing to {self.current_blind.name} (Score required: {self.current_blind.score_required}) ---")
        else:
            print(f"\n--- All Blinds in Ante Cleared! Advancing to next Ante! ---")
            self.ante += 1
            self.current_blind_index = 0 # Reset blind index for new ante
            self.current_blind = self.blinds[self.current_blind_index]
            self.score = 0 # Reset score for new ante
            print(f"\n--- Now in Ante {self.ante}, starting with {self.current_blind.name} (Score required: {self.current_blind.score_required}) ---")

    def check_blind_cleared(self):
        """Checks if the current blind has been cleared and updates game state accordingly."""
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
        """Applies end-of-round effects, such as Perishable and Rental sticker effects."""
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
    
    def change_sort_type(self):
        if self.sort_by == 'rank':
            self.sort_by = 'suit'
        else: 
            self.sort_by = 'rank'

    def draw_hand(self):
        """Draws a new hand of cards from the deck."""
        # Discard current hand if any, and draw a new one.
        self.hand = self.deck.draw(self.hand_size)
        self.sort_hand() # Sort the hand after drawing

    def refill_hand(self):
        """Draw up to hand_size to refill the current hand."""
        need = max(0, self.hand_size - len(self.hand))
        if need:
            drawn = self.deck.draw(need)   # if deck is low, this may return fewer than `need`
            self.hand.extend(drawn)
            self.sort_hand()

    def use_tarot_card(self, tarot_card_index: int):
        """Uses a Tarot card from the player's inventory."""
        if 0 <= tarot_card_index < len(self.tarot_cards):
            tarot_card = self.tarot_cards.pop(tarot_card_index)
            print(f"Using {tarot_card.name}...")
            tarot_card.apply_effect(self)
        else:
            print("Invalid Tarot card index.")

    def use_spectral_card(self, spectral_card_index: int):
        """Uses a Spectral card from the player's inventory."""
        if 0 <= spectral_card_index < len(self.spectral_cards):
            spectral_card = self.spectral_cards.pop(spectral_card_index)
            print(f"Using {spectral_card.name}...")
            spectral_card.apply_effect(self)
        else:
            print("Invalid Spectral card index.")

    def use_planet_card(self, planet_card_index: int):
        """Uses a Planet card from the player's inventory."""
        if 0 <= planet_card_index < len(self.planet_cards):
            planet_card = self.planet_cards.pop(planet_card_index)
            print(f"Using {planet_card.name}...")
            planet_card.apply_effect(self)
        else:
            print("Invalid Planet card index.")

    def play_hand(self, cards_to_play: list[Card]):
        """Plays a selected hand of cards, calculates score, and updates game state."""
        if not all(c in self.hand for c in cards_to_play):
            print("Error: One or more cards are not in the current hand.")
            return

        for card in cards_to_play:
            self.hand.remove(card)
        

        
        played_hand_type = evaluate_hand(cards_to_play)
        if played_hand_type:
            hand_score = calculate_score(played_hand_type, cards_to_play, self.jokers, self)
            self.score += hand_score
            print(f"Hand played: {played_hand_type.value} for {hand_score} points!")
        else:
            print("No valid poker hand was played.")

        self.hands -= 1
        print(f"Played {len(cards_to_play)} cards. {self.hands} hands remaining.")

        if self.hands == 0: # End of round, check if blind is cleared
            self.check_blind_cleared()
            return
        
        self.refill_hand()
        self.sort_hand() # Sort the hand after playing cards

    def discard_cards(self, card_indices: list[int]):
        """Discards selected cards and draws new ones."""
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
        self.sort_hand() # Sort the hand after discarding
        
        self.discards -= 1
        print(f"Discarded {len(discarded_cards)} cards. {self.discards} discards remaining.")

    def sort_hand(self):
        """Sorts the player's hand by rank or suit."""
        # Define a custom sorting key for cards
        def card_sort_key(card):
            rank_order = {
                '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Ten': 10, 
                'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
            }
            if self.sort_by == 'rank':
                return (rank_order[card.rank.value], card.suit.value)
            elif self.sort_by == 'suit':
                return (card.suit.value, rank_order[card.rank.value])
            else:
                return (rank_order[card.rank.value], card.suit.value) # Default to rank sort
        self.hand.sort(key=card_sort_key)

    def __str__(self) -> str:
        def render_section(title, seq, line_fn, enumerated=False):
            if not seq:
                return []
            out = ["", f"--- {title} ---"]
            if enumerated:
                for i, item in enumerate(seq):
                    out.append(line_fn(item, i))
            else:
                for item in seq:
                    out.append(line_fn(item, None))
            out.append("--------------------")
            return out

        lines = [
            "",
            "--------------------",
            repr(self),  # avoids recursion; shows <Game object at 0x...>
            f"Current Ante: {self.ante}",
        ]

        # Hand
        lines += render_section("Your Hand", self.hand, lambda c, i: f"[{i}] {c}", enumerated=True)

        # Jokers & Vouchers (no index)
        lines += render_section("Your Jokers", getattr(self, "jokers", None),
                                lambda j, _: f"{j.name}: {j.description}")
        lines += render_section("Your Vouchers", getattr(self, "vouchers", None),
                                lambda v, _: f"{v.name}: {v.description}")

        # Enumerated card groups
        lines += render_section("Your Tarot Cards", getattr(self, "tarot_cards", None),
                                lambda t, i: f"[{i}] {t.name}: {t.description}", enumerated=True)
        lines += render_section("Your Spectral Cards", getattr(self, "spectral_cards", None),
                                lambda s, i: f"[{i}] {s.name}: {s.description}", enumerated=True)
        lines += render_section("Your Planet Cards", getattr(self, "planet_cards", None),
                                lambda p, i: f"[{i}] {p.name}: {p.description}", enumerated=True)

        return "\n".join(lines)

def save_game(game, filename="balatro_save.json"):
    """Saves the current game state to a JSON file."""
    with open(filename, "w") as f:
        json.dump(game.to_dict(), f, indent=4)
    print(f"Game saved to {filename}")

def load_game(filename="balatro_save.json"):
    """Loads a game state from a JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        game = Game.from_dict(data)
        print(f"Game loaded from {filename}")
        return game
    except FileNotFoundError:
        print(f"No save file found at {filename}")
        return None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None

