"""This module handles the scoring logic for poker hands in Balatro."""

from .poker import PokerHand
from ..cards.jokers import Joker
from ..cards.cards import Card, Enhancement, Edition, Seal
import random # Import random for Lucky Card

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
    PokerHand.FIVE_OF_A_KIND: {"chips": 120, "mult": 12}, # Assuming a generic five of a kind
}

def calculate_score(hand_type: PokerHand, cards: list[Card], jokers: list[Joker], game) -> float:
    """Calculates the score for a given hand type, applying joker bonuses and card modifiers."

    Args:
        hand_type (PokerHand): The type of poker hand played.
        cards (list[Card]): The list of cards that formed the hand.
        jokers (list[Joker]): The list of active Joker cards.
        game: The current Game object (for accessing money, etc.).

    Returns:
        float: The calculated score for the hand.
    """
    base_score = HAND_SCORES.get(hand_type, {"chips": 0, "mult": 0})
    
    chips = base_score["chips"]
    mult = base_score["mult"]

    # Apply card enhancement and edition bonuses
    for card in cards:
        if card.enhancement == Enhancement.GLASS:
            mult += 2
        elif card.enhancement == Enhancement.STEEL:
            mult *= 1.5
        elif card.enhancement == Enhancement.GOLD:
            game.money += 3
            print(f"Gold Card played: +$3. Current money: ${game.money}")
        elif card.enhancement == Enhancement.LUCKY:
            if random.random() < 0.25:
                mult += 20
                print(f"Lucky Card activated: +20 Mult!")
        elif card.enhancement == Enhancement.MULT:
            mult += 4
        elif card.enhancement == Enhancement.CHIP:
            chips += 10

        if card.edition == Edition.FOIL:
            chips += 50
        elif card.edition == Edition.HOLOGRAPHIC:
            mult += 10
        elif card.edition == Edition.POLYCHROME:
            mult *= 1.5

        if card.seal == Seal.GOLD:
            game.money += 3
            print(f"Gold Seal card played: +$3. Current money: ${game.money}")

    # Apply joker bonuses
    for joker in jokers:
        chips = joker.apply_chips(chips)
        mult = joker.apply_mult(mult)
    
    return chips * mult
