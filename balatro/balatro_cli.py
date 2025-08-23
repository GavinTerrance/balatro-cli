# main.py

"""This module contains the main command-line interface for the Balatro game."""

from balatro.game import Game, save_game, load_game
from balatro.deck import BaseDeck, RedDeck, GreenDeck, YellowDeck

def main(commands: list = None):
    """Main function to run the Balatro CLI game."""

    game = Game(deck_type="Base")
    print(f"You have chosen the {game.deck.name}!")
    game.draw_hand()

    command_index = 0

    # Main game loop
    while True:
        if game.game_over:
            break
        print("\n--------------------")
        print(game)
        print(f"Current Ante: {game.ante}")
        print("\n--- Your Hand ---")
        for i, card in enumerate(game.hand):
            print(f"[{i}] {card}")
        print("--------------------")

        # Display Jokers
        if game.jokers:
            print("\n--- Your Jokers ---")
            for joker in game.jokers:
                print(f"{joker.name}: {joker.description}")
            print("--------------------")

        # Display Vouchers
        if game.vouchers:
            print("\n--- Your Vouchers ---")
            for voucher in game.vouchers:
                print(f"{voucher.name}: {voucher.description}")
            print("--------------------")

        # Display Tarot Cards
        if game.tarot_cards:
            print("\n--- Your Tarot Cards ---")
            for i, tarot_card in enumerate(game.tarot_cards):
                print(f"[{i}] {tarot_card.name}: {tarot_card.description}")
            print("--------------------")

        # Display Spectral Cards
        if game.spectral_cards:
            print("\n--- Your Spectral Cards ---")
            for i, spectral_card in enumerate(game.spectral_cards):
                print(f"[{i}] {spectral_card.name}: {spectral_card.description}")
            print("--------------------")

        # Display Planet Cards
        if game.planet_cards:
            print("\n--- Your Planet Cards ---")
            for i, planet_card in enumerate(game.planet_cards):
                print(f"[{i}] {planet_card.name}: {planet_card.description}")
            print("--------------------")

        # Get action from commands list or default to 'q' if no commands left
        if commands and command_index < len(commands):
            action = commands[command_index].lower()
            command_index += 1
            print(f"Executing command: {action}") # Echo the command being executed
        else:
            action = 'q' # Default to quit if no more commands

        if action == 'q':
            break
        elif action == 'v':
            save_game(game)
            continue
        elif action == 'l':
            loaded_game = load_game()
            if loaded_game:
                game = loaded_game
            continue
        elif action == 'h':
            print("\n--- Help ---")
            print("  Enter space-separated card indices (e.g., '0 2 4') to play a hand.")
            print("  'd': Discard selected cards and draw new ones. Costs a hand.")
            print("  't': Use a Tarot card from your inventory.")
            print("  's': Use a Spectral card from your inventory.")
            print("  'p': Use a Planet card from your inventory.")
            print("  'o': Sort your hand by rank or suit.")
            print("  'v': Save the current game.")
            print("  'l': Load a previously saved game.")
            print("  'q': Quit the game.")
            print("--------------------")
            continue

            


            
