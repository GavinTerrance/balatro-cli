"""This module handles the scoring logic for poker hands in Balatro."""

from .poker import PokerHand, get_rank_value
from ..cards.jokers import Joker
from ..cards.cards import Card, Enhancement, Edition, Seal
import random  # Import random for Lucky Card

# Base chips and multiplier for each hand type
# Values taken from Balatro wiki
HAND_SCORES = {
    PokerHand.HIGH_CARD: {"chips": 5, "mult": 1},
    PokerHand.PAIR: {"chips": 10, "mult": 2},
    PokerHand.TWO_PAIR: {"chips": 20, "mult": 2},
    PokerHand.THREE_OF_A_KIND: {"chips": 30, "mult": 3},
    PokerHand.STRAIGHT: {"chips": 30, "mult": 4},
    PokerHand.FLUSH: {"chips": 35, "mult": 4},
    PokerHand.FULL_HOUSE: {"chips": 40, "mult": 4},
    PokerHand.FOUR_OF_A_KIND: {"chips": 60, "mult": 7},
    PokerHand.STRAIGHT_FLUSH: {"chips": 100, "mult": 8},
    PokerHand.FIVE_OF_A_KIND: {"chips": 120, "mult": 12},  # Assuming a generic five of a kind
}

def calculate_score(
    hand_type: PokerHand, cards: list[Card], jokers: list[Joker], game
) -> tuple[float, float, float, list[str]]:
    """Calculate score and provide chip/mult breakdown."""

    base_score = HAND_SCORES.get(hand_type, {"chips": 0, "mult": 0})
    chips = base_score["chips"]
    mult = base_score["mult"]
    messages: list[str] = [f"Base hand ({hand_type.value}): {chips} chips, {mult} mult"]

    for card in cards:
        rank_value = get_rank_value(card.rank)
        chips += rank_value
        messages.append(f"{card} adds +{rank_value} chips (card value)")

        if card.enhancement == Enhancement.GLASS:
            mult += 2
            messages.append(f"{card} Glass bonus: +2 mult")
        elif card.enhancement == Enhancement.STEEL:
            mult *= 1.5
            messages.append(f"{card} Steel bonus: x1.5 mult")
        elif card.enhancement == Enhancement.GOLD:
            game.money += 3
            print(f"Gold Card played: +$3. Current money: ${game.money}")
        elif card.enhancement == Enhancement.LUCKY:
            if random.random() < 0.25:
                mult += 20
                messages.append(f"{card} Lucky bonus: +20 mult")
        elif card.enhancement == Enhancement.MULT:
            mult += 4
            messages.append(f"{card} Mult bonus: +4 mult")
        elif card.enhancement == Enhancement.CHIP:
            chips += 10
            messages.append(f"{card} Chip bonus: +10 chips")

        if card.edition == Edition.FOIL:
            chips += 50
            messages.append(f"{card} Foil edition: +50 chips")
        elif card.edition == Edition.HOLOGRAPHIC:
            mult += 10
            messages.append(f"{card} Holographic edition: +10 mult")
        elif card.edition == Edition.POLYCHROME:
            mult *= 1.5
            messages.append(f"{card} Polychrome edition: x1.5 mult")

        if card.seal == Seal.GOLD:
            game.money += 3
            print(f"Gold Seal card played: +$3. Current money: ${game.money}")

    for joker in jokers:
        new_chips = joker.apply_chips(chips)
        if new_chips != chips:
            messages.append(f"{joker.name} changes chips {chips} -> {new_chips}")
        chips = new_chips
        new_mult = joker.apply_mult(mult)
        if new_mult != mult:
            messages.append(f"{joker.name} changes mult {mult} -> {new_mult}")
        mult = new_mult

    final_score = chips * mult
    messages.append(f"Final: {chips} chips x {mult} mult = {final_score}")
    return final_score, chips, mult, messages
