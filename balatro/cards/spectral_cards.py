"""Spectral card definitions and utilities for loading from JSON."""

from __future__ import annotations

import json
import random
from pathlib import Path

from .cards import Card, Suit, Edition, Seal, Rank, Enhancement
from ..utils import get_user_input
from ..cards.jokers import load_jokers, Joker


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

        def _familiar(game, _selected, _params):
            if game.player.hand:
                game.player.hand.pop(random.randrange(len(game.player.hand)))
            for _ in range(3):
                suit = random.choice(list(Suit))
                rank = random.choice([Rank.JACK, Rank.QUEEN, Rank.KING])
                enh = random.choice([e for e in Enhancement if e != Enhancement.NONE])
                game.player.hand.append(Card(suit, rank, enh))
            print("Familiar added 3 enhanced face cards.")

        def _grim(game, _selected, _params):
            if game.player.hand:
                game.player.hand.pop(random.randrange(len(game.player.hand)))
            for _ in range(2):
                suit = random.choice(list(Suit))
                enh = random.choice([e for e in Enhancement if e != Enhancement.NONE])
                game.player.hand.append(Card(suit, Rank.ACE, enh))
            print("Grim added 2 enhanced Aces.")

        def _incantation(game, _selected, _params):
            if game.player.hand:
                game.player.hand.pop(random.randrange(len(game.player.hand)))
            numbers = [
                Rank.TWO,
                Rank.THREE,
                Rank.FOUR,
                Rank.FIVE,
                Rank.SIX,
                Rank.SEVEN,
                Rank.EIGHT,
                Rank.NINE,
                Rank.TEN,
            ]
            for _ in range(4):
                suit = random.choice(list(Suit))
                rank = random.choice(numbers)
                enh = random.choice([e for e in Enhancement if e != Enhancement.NONE])
                game.player.hand.append(Card(suit, rank, enh))
            print("Incantation added 4 enhanced numbered cards.")

        def _wraith(game, _selected, _params):
            rares = [j for j in load_jokers() if getattr(j, "rarity", "").lower() == "rare"]
            if rares:
                joker = random.choice(rares)
                game.player.jokers.append(joker)
                print(f"Gained rare Joker {joker.name}.")
            game.money = 0
            print("Money reduced to $0.")

        def _ouija(game, _selected, _params):
            rank = random.choice(list(Rank))
            for c in game.player.hand:
                c.rank = rank
            game.player.hand_size = max(0, game.player.hand_size - 1)
            print(f"All cards set to {rank.value}; hand size reduced to {game.player.hand_size}.")

        def _ectoplasm(game, _selected, _params):
            if game.player.jokers:
                joker = random.choice(game.player.jokers)
                joker.edition = Edition.NEGATIVE
                print(f"{joker.name} gained Negative edition.")
            game.player.hand_size = max(0, game.player.hand_size - (game.ectoplasm_uses + 1))
            game.ectoplasm_uses += 1
            print(f"Hand size reduced to {game.player.hand_size}.")

        def _immolate(game, _selected, _params):
            if not game.player.hand:
                print("No cards to destroy.")
                return
            count = min(5, len(game.player.hand))
            indices = random.sample(range(len(game.player.hand)), count)
            indices.sort(reverse=True)
            destroyed = [game.player.hand.pop(i) for i in indices]
            game.money += 20
            destroyed_str = ", ".join(str(c) for c in destroyed)
            print(f"Destroyed {count} cards ({destroyed_str}) and gained $20.")

        def _ankh(game, _selected, _params):
            if not game.player.jokers:
                print("No Jokers to copy.")
                return
            chosen = random.choice(game.player.jokers)
            clone = Joker.from_dict(chosen.to_dict())
            if clone.edition == Edition.NEGATIVE:
                clone.edition = Edition.NONE
            game.player.jokers = [chosen, clone]
            print(f"Ankh duplicated {chosen.name} and removed other Jokers.")

        def _hex(game, _selected, _params):
            if not game.player.jokers:
                print("No Jokers to affect.")
                return
            chosen = random.choice(game.player.jokers)
            chosen.edition = Edition.POLYCHROME
            game.player.jokers = [chosen]
            print(f"{chosen.name} became Polychrome; other Jokers destroyed.")

        def _soul(game, _selected, _params):
            legs = [j for j in load_jokers() if getattr(j, "rarity", "").lower() == "legendary"]
            if legs:
                joker = random.choice(legs)
                game.player.jokers.append(joker)
                print(f"Gained Legendary Joker {joker.name}.")

        def _black_hole(game, _selected, _params):
            from ..core.poker import PokerHand

            for hand in PokerHand:
                game.player.add_hand_bonus(hand, 10, 1)
            print("All poker hands upgraded.")

        actions = {
            "add_random_edition": _add_random_edition,
            "add_seal": _add_seal,
            "convert_all_random_suit": _convert_all_random_suit,
            "copy_card": _copy_card,
            "familiar": _familiar,
            "grim": _grim,
            "incantation": _incantation,
            "wraith": _wraith,
            "ouija": _ouija,
            "ectoplasm": _ectoplasm,
            "immolate": _immolate,
            "ankh": _ankh,
            "hex": _hex,
            "the_soul": _soul,
            "black_hole": _black_hole,
        }

        func = actions.get(self.action) or actions.get(self.name.replace(" ", "_").lower())
        if func:
            func(game, cards, self.params)
        else:
            print(f"{self.name} has no effect.")

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
