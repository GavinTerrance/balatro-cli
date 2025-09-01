from __future__ import annotations

"""Player related state and behaviour for Balatro."""

from ..cards.cards import Card
from ..core.poker import PokerHand


class Player:
    """Represents the player and manages their cards and resources."""

    def __init__(self, deck):
        self.money = 4
        self.hands = 4
        self.discards = 3
        self.hand_size = 8
        self.score = 0
        self.sort_by = "rank"
        self.earns_interest = True

        self.deck = deck
        self.hand: list[Card] = []
        self.jokers = []
        self.vouchers = []
        self.tarot_cards = []
        self.spectral_cards = []
        self.planet_cards = []
        self.consumable_slots = 2
        self.hand_bonuses: dict[str, dict[str, int]] = {}

    # ------------------------------------------------------------------
    # Card handling
    def change_sort_type(self) -> None:
        self.sort_by = "suit" if self.sort_by == "rank" else "rank"

    def sort_hand(self) -> None:
        rank_order = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
            "9": 9, "10": 10, "Ten": 10,
            "Jack": 11, "Queen": 12, "King": 13, "Ace": 14,
        }

        def card_sort_key(card: Card):
            if self.sort_by == "rank":
                return (rank_order[card.rank.value], card.suit.value)
            return (card.suit.value, rank_order[card.rank.value])

        self.hand.sort(key=card_sort_key)

    def draw_hand(self) -> None:
        self.hand = self.deck.draw(self.hand_size)
        self.sort_hand()

    def refill_hand(self) -> None:
        need = max(0, self.hand_size - len(self.hand))
        if need:
            drawn = self.deck.draw(need)
            self.hand.extend(drawn)
            self.sort_hand()

    def discard_cards(self, card_indices: list[int]) -> list[Card]:
        if not card_indices:
            return []
        card_indices.sort(reverse=True)
        discarded = []
        for index in card_indices:
            discarded.append(self.hand.pop(index))
        self.discards -= 1
        new_cards = self.deck.draw(len(discarded))
        self.hand.extend(new_cards)
        self.sort_hand()
        return discarded

    # ------------------------------------------------------------------
    # Inventory usage helpers
    def _total_consumables(self) -> int:
        return len(self.tarot_cards) + len(self.spectral_cards) + len(self.planet_cards)

    def _has_consumable_space(self) -> bool:
        return self._total_consumables() < self.consumable_slots

    def add_tarot_card(self, card) -> bool:
        if self._has_consumable_space():
            self.tarot_cards.append(card)
            return True
        print("No room for more consumables.")
        return False

    def add_spectral_card(self, card) -> bool:
        if self._has_consumable_space():
            self.spectral_cards.append(card)
            return True
        print("No room for more consumables.")
        return False

    def add_planet_card(self, card) -> bool:
        if self._has_consumable_space():
            self.planet_cards.append(card)
            return True
        print("No room for more consumables.")
        return False

    def add_hand_bonus(self, hand: PokerHand, chips: int = 0, mult: int = 0) -> None:
        bonus = self.hand_bonuses.setdefault(hand.name, {"chips": 0, "mult": 0})
        bonus["chips"] += chips
        bonus["mult"] += mult

    def use_tarot_card(self, index: int, game) -> None:
        if 0 <= index < len(self.tarot_cards):
            tarot = self.tarot_cards.pop(index)
            tarot.apply_effect(game)
        else:
            print("Invalid Tarot card index.")

    def use_spectral_card(self, index: int, game) -> None:
        if 0 <= index < len(self.spectral_cards):
            spectral = self.spectral_cards.pop(index)
            spectral.apply_effect(game)
        else:
            print("Invalid Spectral card index.")

    def use_planet_card(self, index: int, game) -> None:
        if 0 <= index < len(self.planet_cards):
            planet = self.planet_cards.pop(index)
            planet.apply_effect(game)
            game.last_used_card = planet
        else:
            print("Invalid Planet card index.")
