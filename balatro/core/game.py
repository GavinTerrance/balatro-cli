from __future__ import annotations

"""Game engine and orchestration logic."""

import json
import random

from .deck import BaseDeck, RedDeck, GreenDeck, YellowDeck
from ..cards.cards import Card
from .poker import evaluate_hand
from .scoring import calculate_score
from ..cards.jokers import joker_from_dict, load_jokers
from ..shop.vouchers import voucher_from_dict
from .blinds import BlindManager
from ..shop.shop import Shop
from ..cards.tarot_cards import tarot_card_from_dict
from ..cards.spectral_cards import spectral_card_from_dict
from ..cards.planet_cards import planet_card_from_dict
from ..shop.stickers import StickerType
from .player import Player
from ..utils import get_user_input


class Game:
    """Represents the main game state and logic for Balatro CLI."""

    def __init__(self, deck_type: str = "Base"):
        self.round = 1
        self.ante = 1
        self.game_over = False
        self.deck_key = deck_type

        deck_cls = {"Red": RedDeck, "Green": GreenDeck, "Yellow": YellowDeck}.get(
            deck_type, BaseDeck
        )
        deck = deck_cls()
        deck.shuffle()
        self.deck = deck

        self.player = Player(deck)

        if deck_type == "Red":
            self.player.discards += 1
        elif deck_type == "Green":
            self.player.earns_interest = False
        elif deck_type == "Yellow":
            self.player.money += 10

        self.blind_manager = BlindManager()
        self.shop = Shop()
        self.round_earnings = 0
        self.voucher_purchased = False
        self.last_used_card = None
        self.ectoplasm_uses = 0
        self.activate_vouchers()

    @property
    def money(self):
        return self.player.money

    @money.setter
    def money(self, value):
        self.player.money = value

    # ------------------------------------------------------------------
    # Serialization helpers
    def to_dict(self):
        p = self.player
        return {
            "deck_type": self.deck_key,
            "player": {
                "hand": [card.to_dict() for card in p.hand],
                "jokers": [joker.to_dict() for joker in p.jokers],
                "vouchers": [voucher.to_dict() for voucher in p.vouchers],
                "tarot_cards": [t.to_dict() for t in p.tarot_cards],
                "spectral_cards": [s.to_dict() for s in p.spectral_cards],
                "planet_cards": [pc.to_dict() for pc in p.planet_cards],
                "money": p.money,
                "hands": p.hands,
                "discards": p.discards,
                "hand_size": p.hand_size,
                "score": p.score,
                "sort_by": p.sort_by,
                "consumable_slots": p.consumable_slots,
                "hand_bonuses": p.hand_bonuses,
            },
            "round": self.round,
            "ante": self.ante,
            "game_over": self.game_over,
            "current_blind_index": self.blind_manager.index,
            "ectoplasm_uses": self.ectoplasm_uses,
        }

    @classmethod
    def from_dict(cls, data):
        game = cls(deck_type=data["deck_type"])
        p_data = data["player"]
        player = game.player
        player.hand = [Card.from_dict(c) for c in p_data["hand"]]
        player.jokers = [joker_from_dict(j) for j in p_data["jokers"]]
        player.vouchers = [voucher_from_dict(v) for v in p_data["vouchers"]]
        player.tarot_cards = [tarot_card_from_dict(t) for t in p_data["tarot_cards"]]
        player.spectral_cards = [spectral_card_from_dict(s) for s in p_data["spectral_cards"]]
        player.planet_cards = [planet_card_from_dict(pc) for pc in p_data["planet_cards"]]
        player.money = p_data["money"]
        player.hands = p_data["hands"]
        player.discards = p_data["discards"]
        player.hand_size = p_data["hand_size"]
        player.score = p_data["score"]
        player.sort_by = p_data.get("sort_by", "rank")
        player.consumable_slots = p_data.get("consumable_slots", 2)
        player.hand_bonuses = p_data.get("hand_bonuses", {})
        game.round = data["round"]
        game.ante = data["ante"]
        game.game_over = data["game_over"]
        game.blind_manager.index = data["current_blind_index"]
        game.ectoplasm_uses = data.get("ectoplasm_uses", 0)
        return game

    # ------------------------------------------------------------------
    def __repr__(self):
        return (
            f"Game(Ante={self.ante}, round={self.round}, hands={self.player.hands}, "
            f"discards={self.player.discards}, score={self.player.score}, "
            f"money={self.player.money}, current_blind={self.blind_manager.current.name})"
        )

    def activate_vouchers(self):
        for voucher in self.player.vouchers:
            voucher.apply_effect(self)

    def advance_blind(self):
        cleared_ante = self.blind_manager.advance()
        self.player.score = 0
        self.player.hands = 4
        self.player.discards = 3
        if self.deck_key == "Red":
            self.player.discards += 1
        if cleared_ante:
            print("\n--- All Blinds in Ante Cleared! Advancing to next Ante! ---")
            self.ante += 1
            self.voucher_purchased = False
        print(
            f"\n--- Advancing to {self.blind_manager.current.name} (Score required: {self.blind_manager.current.score_required}) ---"
        )
        # Riff-Raff Joker effect
        for joker in self.player.jokers:
            if joker.name == "Riff-Raff":
                commons = [j for j in load_jokers() if getattr(j, "rarity", "").lower() == "common"]
                slots = max(0, 5 - len(self.player.jokers))
                to_create = min(2, slots)
                if to_create <= 0:
                    print("No room for Riff-Raff to create Jokers.")
                    break
                for _ in range(to_create):
                    self.player.jokers.append(random.choice(commons))
                plural = "s" if to_create > 1 else ""
                print(f"Riff-Raff created {to_create} Common Joker{plural}.")
                break

    def end_of_round_winnings(self) -> int:
        base = 10
        leftover = self.player.hands
        self.player.money += base + leftover

        interest = 0
        if self.player.earns_interest:
            cap = 5
            if any(v.name == "Seed Money" for v in self.player.vouchers):
                cap = 10
            if any(v.name == "Money Tree" for v in self.player.vouchers):
                cap = 20
            per5 = 1 + sum(1 for j in self.player.jokers if j.name == "To the Moon")
            interest = min(cap, (self.player.money // 5) * per5)
            self.player.money += interest

        total = base + leftover + self.round_earnings + interest
        print(
            f"End of round winnings: base ${base} + joker/gold ${self.round_earnings} + leftover hands ${leftover} + interest ${interest} = ${total}"
        )
        self.round_earnings = 0
        self.player.hands = 0
        return total

    def enter_shop(self):
        self.shop.generate_items(self)
        while True:
            self.shop.display_items(self.money)
            choice = get_user_input(
                "Select item to purchase or type 'leave' to continue: "
            ).strip().lower()
            if choice in ("", "leave", "l"):
                break
            try:
                idx = int(choice)
                self.shop.purchase_item(idx, self)
            except ValueError:
                print("Invalid selection.")

    def check_blind_cleared(self):
        if self.player.score >= self.blind_manager.current.score_required:
            total = self.end_of_round_winnings()
            print(
                f"\n--- {self.blind_manager.current.name} Cleared! You gained ${total}! ---"
            )
            self.enter_shop()
            self.advance_blind()
            self.draw_hand()
            return True
        print(
            f"\n--- Failed to clear {self.blind_manager.current.name}! Game Over! ---"
        )
        self.game_over = True
        return False

    def end_of_round_effects(self):
        for joker in self.player.jokers:
            for sticker in joker.stickers:
                if sticker.sticker_type == StickerType.PERISHABLE:
                    joker.rounds_active += 1
                    if joker.rounds_active >= 5:
                        joker.is_debuffed = True
                        print(
                            f"{joker.name} has become debuffed due to Perishable Sticker!"
                        )
                elif sticker.sticker_type == StickerType.RENTAL:
                    self.player.money -= 3
                    print(
                        f"Rental fee for {joker.name}: -$3. Current money: ${self.player.money}"
                    )

    # ------------------------------------------------------------------
    # Convenience wrappers that delegate to Player
    def change_sort_type(self):
        self.player.change_sort_type()

    def draw_hand(self):
        self.player.draw_hand()

    def refill_hand(self):
        self.player.refill_hand()

    def sort_hand(self):
        self.player.sort_hand()

    def use_tarot_card(self, index: int):
        self.player.use_tarot_card(index, self)

    def use_spectral_card(self, index: int):
        self.player.use_spectral_card(index, self)

    def use_planet_card(self, index: int):
        self.player.use_planet_card(index, self)

    def play_hand(self, cards_to_play: list[Card]):
        if len(cards_to_play) > 5: # Player can play less than 5 cards, but not more. 
            print("Error: You can't play over 5 cards.")
            return
        if not all(c in self.player.hand for c in cards_to_play):
            print("Error: One or more cards are not in the current hand.")
            return

        for card in cards_to_play:
            self.player.hand.remove(card)

        played_hand_type, hand_cards = evaluate_hand(cards_to_play)
        if played_hand_type:
            scoring_cards = (
                cards_to_play
                if any(j.name == "Splash" for j in self.player.jokers)
                else hand_cards
            )
            hand_score, chips, mult, breakdown = calculate_score(
                played_hand_type, scoring_cards, self.player.jokers, self
            )
            for line in breakdown:
                print(line)
            self.player.score += hand_score
            print(
                f"Hand played: {played_hand_type.value} for {hand_score} points!"
            )
        else:
            print("No valid poker hand was played.")

        self.player.hands -= 1
        print(
            f"Played {len(cards_to_play)} cards. {self.player.hands} hands remaining."
        )

        if self.player.score >= self.blind_manager.current.score_required:
            self.check_blind_cleared()
            return

        if self.player.hands == 0:
            self.check_blind_cleared()
            return

        self.player.refill_hand()

    def discard_cards(self, card_indices: list[int]):
        if self.player.discards <= 0:
            print("No discards remaining!")
            return
        if not card_indices:
            print("No cards selected to discard.")
            return
        if len(card_indices) > 5:
            print("Error: You can only discard up to 5 cards.")
            return
        if any(i < 0 or i >= len(self.player.hand) for i in card_indices):
            print("Error: Invalid card index for discard.")
            return
        if len(card_indices) != len(set(card_indices)):
            print("Error: Duplicate card indices for discard.")
            return

        discarded = self.player.discard_cards(card_indices)
        print(
            f"Discarded {len(discarded)} cards. {self.player.discards} discards remaining."
        )

    def show_deck(self):
        print("\n--- Remaining Deck ---")
        for i, card in enumerate(self.deck.cards):
            print(f"[{i}] {card}")
        print("--------------------")

    # ------------------------------------------------------------------
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
            repr(self),
            f"Current Ante: {self.ante}",
            f"Score needed to win blind: {self.blind_manager.current.score_required}",
        ]

        lines += render_section(
            "Your Hand", self.player.hand, lambda c, i: f"[{i}] {c}", enumerated=True
        )
        lines += render_section(
            "Your Jokers", self.player.jokers, lambda j, _: f"{j.name}: {j.description}"
        )
        lines += render_section(
            "Your Vouchers", self.player.vouchers, lambda v, _: f"{v.name}: {v.description}"
        )
        lines += render_section(
            "Your Tarot Cards",
            self.player.tarot_cards,
            lambda t, i: f"[{i}] {t.name}: {t.description}",
            enumerated=True,
        )
        lines += render_section(
            "Your Spectral Cards",
            self.player.spectral_cards,
            lambda s, i: f"[{i}] {s.name}: {s.description}",
            enumerated=True,
        )
        lines += render_section(
            "Your Planet Cards",
            self.player.planet_cards,
            lambda p, i: f"[{i}] {p.name}: {p.description}",
            enumerated=True,
        )

        return "\n".join(lines)


# ----------------------------------------------------------------------
# Persistence helpers

def save_game(game: Game, filename: str = "balatro_save.json"):
    with open(filename, "w") as f:
        json.dump(game.to_dict(), f, indent=4)
    print(f"Game saved to {filename}")


def load_game(filename: str = "balatro_save.json") -> Game | None:
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
