"""Tarot card definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
import random
from pathlib import Path

from .cards import Card, Suit, Rank, Enhancement, Edition
from ..cards.jokers import load_jokers
from ..cards.planet_cards import load_planet_cards
from ..utils import get_user_input


class TarotCard:
    """Simple representation of a Tarot card."""

    def __init__(
        self,
        name: str,
        description: str,
        cost: int = 0,
        targets: int = 0,
        action: str | None = None,
        params: dict | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.cost = cost
        self.targets = targets
        self.action = action
        self.params = params or {}

    def __repr__(self) -> str:  # pragma: no cover - simple repr
        return f"TarotCard(name='{self.name}')"

    def apply_effect(self, game, chosen: list[Card] | None = None) -> None:
        """Apply the tarot card's effect."""

        player = game.player
        cards = chosen or []
        if not cards and self.targets > 0:
            print("--- Available Cards for Application ---")
            for i, c in enumerate(player.hand):
                print(f"[{i}] {c}")
            print("---------------------------")
            selection = get_user_input(
                "Select target indices separated by space: "
            ).strip()
            if selection:
                indices = [int(s) for s in selection.split()][: self.targets]
                cards = [player.hand[i] for i in indices if 0 <= i < len(player.hand)]

        def _apply_enhancement(_game, selected, params):
            enh = Enhancement[params.get("enhancement", "LUCKY")]
            for c in selected:
                c.enhancement = enh
            print(f"Applied {enh.value} to {len(selected)} card(s).")

        def _convert_suit(_game, selected, params):
            suit = Suit[params.get("suit", "HEARTS")]
            for c in selected:
                c.suit = suit
            print(f"Converted {len(selected)} card(s) to {suit.value}.")

        def _increase_rank(_game, selected, params):
            order = [
                Rank.TWO,
                Rank.THREE,
                Rank.FOUR,
                Rank.FIVE,
                Rank.SIX,
                Rank.SEVEN,
                Rank.EIGHT,
                Rank.NINE,
                Rank.TEN,
                Rank.JACK,
                Rank.QUEEN,
                Rank.KING,
                Rank.ACE,
            ]
            for c in selected:
                idx = order.index(c.rank)
                c.rank = order[(idx + 1) % len(order)]
            print(f"Increased rank of {len(selected)} card(s).")

        def _destroy(game, selected, _params):
            for c in selected:
                if c in game.player.hand:
                    game.player.hand.remove(c)
            print(f"Destroyed {len(selected)} card(s).")

        def _transform(game, selected, _params):
            if len(selected) >= 2:
                src, dst = selected[0], selected[1]
                dst.suit = src.suit
                dst.rank = src.rank
                dst.enhancement = src.enhancement
                dst.edition = src.edition
                dst.seal = src.seal
                if src in game.player.hand:
                    game.player.hand.remove(src)
                print("Converted second card into first card and destroyed the original.")

        def _double_money(game, _selected, _params):
            game.player.money = min(game.player.money * 2, 20)
            print(f"Money is now ${game.player.money}.")

        def _add_planet_cards(game, _selected, params):
            count = int(params.get("count", 2))
            new_cards = random.sample(load_planet_cards(), k=count)
            game.player.planet_cards.extend(new_cards)
            print(f"Gained {count} Planet card(s).")

        def _add_tarot_cards(game, _selected, params):
            count = int(params.get("count", 2))
            new_cards = random.sample(load_tarot_cards(), k=count)
            game.player.tarot_cards.extend(new_cards)
            print(f"Gained {count} Tarot card(s).")

        def _wheel_of_fortune(game, _selected, params):
            chance = float(params.get("chance", 0.25))
            if game.player.jokers and random.random() < chance:
                joker = random.choice(game.player.jokers)
                joker.edition = random.choice(
                    [Edition.FOIL, Edition.HOLOGRAPHIC, Edition.POLYCHROME]
                )
                print(f"{joker.name} gained {joker.edition.value} edition.")
            else:
                print("Wheel of Fortune had no effect.")

        def _add_random_joker(game, _selected, _params):
            joker = random.choice(load_jokers())
            game.player.jokers.append(joker)
            print(f"Gained Joker {joker.name}.")

        actions = {
            "apply_enhancement": _apply_enhancement,
            "convert_suit": _convert_suit,
            "increase_rank": _increase_rank,
            "destroy": _destroy,
            "transform": _transform,
            "double_money": _double_money,
            "add_planet_cards": _add_planet_cards,
            "add_tarot_cards": _add_tarot_cards,
            "wheel_of_fortune": _wheel_of_fortune,
            "add_random_joker": _add_random_joker,
        }

        func = actions.get(self.action)
        if func:
            func(game, cards, self.params)
        else:
            print(f"{self.name} used: {self.description} (effect not yet implemented).")

        game.last_used_card = self

    def to_dict(self) -> dict:
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost,
            "targets": self.targets,
            "action": self.action,
            "params": self.params,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TarotCard":
        return cls(
            data["name"],
            data["description"],
            data.get("cost", 0),
            data.get("targets", 0),
            data.get("action"),
            data.get("params"),
        )


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_tarot_cards() -> list[TarotCard]:
    """Load tarot cards from the JSON data file."""

    with open(DATA_DIR / "tarot_cards.json", encoding="utf-8") as f:
        raw = json.load(f)

    cards = []
    for entry in raw:
        params = {
            k: v
            for k, v in entry.items()
            if k not in {"name", "description", "targets", "action"}
        }
        card = TarotCard(
            name=entry.get("name", ""),
            description=entry.get("description", ""),
            cost=3,
            targets=int(entry.get("targets", 0)),
            action=entry.get("action"),
            params=params,
        )
        cards.append(card)

    return cards


def tarot_card_from_dict(data: dict) -> TarotCard:
    """Recreate a ``TarotCard`` instance from serialized data."""

    return TarotCard.from_dict(data)

