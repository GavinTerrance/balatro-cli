from __future__ import annotations

"""Command-line interface for the Balatro game.

This module wraps the :class:`balatro.game.Game` logic in a small
object-oriented CLI that manages user interaction.  The previous
implementation relied on a collection of loose functions; converting it
into a class keeps related behaviour together and makes it easier to
extend or test in isolation.
"""

from typing import Optional

from .core.game import Game, save_game, load_game


class BalatroCLI:
    """Simple command-line runner for Balatro."""

    def __init__(self, deck_type: str = "Base") -> None:
        self.game = Game(deck_type=deck_type)
        print(f"You have chosen the {self.game.deck.name}!")
        self.game.draw_hand()

    # ------------------------------------------------------------------
    # Helper methods
    def _print_help(self) -> None:
        """Display the available commands to the player."""
        print("\n--- Help ---")
        print("  Enter space-separated card indices (e.g., '0 2 4') to select cards.")
        print("  'p': Play selected cards")
        print("  'd': Discard selected cards")
        print("  't': Use a Tarot card from your inventory.")
        print("  's': Use a Spectral card from your inventory.")
        print("  'o': Sort your hand by rank or suit.")
        print("  'c': View the remaining deck.")
        print("  'v': Save the current game.")
        print("  'l': Load a previously saved game.")
        print("  'q': Quit the game.")
        print("--------------------")

    def _handle_action(self, action: str, cards: Optional[str]) -> bool:
        """Handle a single user action.

        Returns ``True`` to continue the game loop or ``False`` to quit.
        """
        card_indices: list[int] = []
        selected_cards = []
        if cards:
            card_indices = [int(idx) for idx in cards.split()]
            selected_cards = [
                self.game.player.hand[i]
                for i in card_indices
                if 0 <= i < len(self.game.player.hand)
            ]

        if action == "q":
            return False
        if action == "v":
            save_game(self.game)
        elif action == "l":
            loaded_game = load_game()
            if loaded_game:
                self.game = loaded_game
        elif action == "h":
            self._print_help()
        elif action == "o":
            self.game.change_sort_type()
            self.game.sort_hand()
            print("Hand sorted.")
        elif action == "p":
            if selected_cards:
                self.game.play_hand(selected_cards)
            else:
                print("Did you list the cards you want to play after 'p'?")
        elif action == "d":
            if selected_cards:
                self.game.discard_cards(card_indices)
            else:
                print("Did you list the cards you want to discard after 'd'?")
        elif action == "c":
            self.game.show_deck()
        else:
            print("Invalid action or card indices. Please try again.")
        return True

    # ------------------------------------------------------------------
    def run(self) -> Game:
        """Start the interactive command loop."""
        self._print_help()
        while True:
            while not self.game.game_over:
                print(self.game)
                user_input = input("Enter your action: ").strip().lower()
                action = user_input[:1]
                additional_input = user_input[1:]
                if not self._handle_action(action, additional_input):
                    return self.game
            again = input("Play again? (y/n): ").strip().lower()
            if again == "y":
                deck_type = self.game.deck_key
                self.game = Game(deck_type=deck_type)
                print(f"You have chosen the {self.game.deck.name}!")
                self.game.draw_hand()
                self.game.game_over = False
                self._print_help()
            else:
                break
        return self.game


__all__ = ["BalatroCLI"]
