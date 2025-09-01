"""Spectral card definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
import random
from pathlib import Path

from .cards import Card, Suit, Edition, Seal
from ..utils import get_user_input


class SpectralCard:
    """Simple representation of a Spectral card."""

    def __init__(
        self,
        name: str,
        description: str,
        cost: int = 4,
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
        return f"SpectralCard(name='{self.name}')"

    def apply_effect(self, game, chosen: list[Card] | None = None) -> None:
        """Apply the spectral card's effect."""

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

        def _add_random_edition(_, selected, __):
            if selected:
                card = selected[0]
                card.edition = random.choice(
                    [Edition.FOIL, Edition.HOLOGRAPHIC, Edition.POLYCHROME]
                )
                print(f"{card} gained {card.edition.value} edition.")

        def _add_seal(_, selected, params):
            if selected:
                card = selected[0]
                seal = Seal[params.get("seal", "GOLD")]
                card.seal = seal
                print(f"{card} gained a {seal.value} Seal.")

        def _convert_all_random_suit(game, _selected, __):
            suit = random.choice(list(Suit))
            for c in game.player.hand:
                c.suit = suit
            print(f"All cards converted to {suit.value}.")

        def _copy_card(game, selected, params):
            if selected:
                card = selected[0]
                copies = int(params.get("copies", 1))
                for _ in range(copies):
                    game.player.hand.append(
                        Card(card.suit, card.rank, card.enhancement, card.edition, card.seal)
                    )
                print(f"Created {copies} copies of selected card.")

        actions = {
            "add_random_edition": _add_random_edition,
            "add_seal": _add_seal,
            "convert_all_random_suit": _convert_all_random_suit,
            "copy_card": _copy_card,
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
    def from_dict(cls, data: dict) -> "SpectralCard":
        return cls(
            data["name"],
            data["description"],
            data.get("cost", 4),
            data.get("targets", 0),
            data.get("action"),
            data.get("params"),
        )


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_spectral_cards() -> list[SpectralCard]:
    """Load spectral cards from the JSON data file."""

    with open(DATA_DIR / "spectral_cards.json", encoding="utf-8") as f:
        raw = json.load(f)

    cards = []
    for entry in raw:
        params = {
            k: v
            for k, v in entry.items()
            if k not in {"name", "effect", "targets", "action"}
        }
        card = SpectralCard(
            name=entry.get("name", ""),
            description=entry.get("effect", ""),
            cost=4,
            targets=int(entry.get("targets", 0)),
            action=entry.get("action"),
            params=params,
        )
        cards.append(card)

    return cards


def spectral_card_from_dict(data: dict) -> SpectralCard:
    """Recreate a ``SpectralCard`` instance from serialized data."""

    return SpectralCard.from_dict(data)
