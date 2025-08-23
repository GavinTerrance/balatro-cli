# main.py

"""This module contains the main command-line interface for the Balatro game."""

from balatro.game import Game, save_game, load_game
from balatro.deck import BaseDeck, RedDeck, GreenDeck, YellowDeck

def main():
    """Main function to run the Balatro CLI game."""

    # Allow user to choose a starting deck
    print("Available Decks:")
    print("  1. Base Deck (Standard 52-card deck)")
    print("  2. Red Deck (+1 discard every round)")
    print("  3. Green Deck (End of Round: $2 per remaining Hand, $1 per remaining Discard. No Interest)")
    print("  4. Yellow Deck (Start with extra $10)")

    game = None
    # Loop to allow user to start a new game or load an existing one
    while game is None:
        start_option = input("Start a [N]ew game or [L]oad game? ").lower()
        if start_option == 'n':
            deck_choice = input("Choose your starting deck (1-4): ")
            selected_deck_type = "Base"
            if deck_choice == "2":
                selected_deck_type = "Red"
            elif deck_choice == "3":
                selected_deck_type = "Green"
            elif deck_choice == "4":
                selected_deck_type = "Yellow"
            
            game = Game(deck_type=selected_deck_type)
            print(f"You have chosen the {game.deck.name}!")
            game.draw_hand()
        elif start_option == 'l':
            game = load_game()
            if game is None:
                print("Could not load game. Starting a new game.")
                # Fallback to new game if load fails
                print("Available Decks:")
                print("  1. Base Deck (Standard 52-card deck)")
                print("  2. Red Deck (+1 discard every round)")
                print("  3. Green Deck (End of Round: $2 per remaining Hand, $1 per remaining Discard. No Interest)")
                print("  4. Yellow Deck (Start with extra $10)")

                deck_choice = input("Choose your starting deck (1-4): ")
                selected_deck_type = "Base"
                if deck_choice == "2":
                    selected_deck_type = "Red"
                elif deck_choice == "3":
                    selected_deck_type = "Green"
                elif deck_choice == "4":
                    selected_deck_type = "Yellow"
                
                game = Game(deck_type=selected_deck_type)
                print(f"You have chosen the {game.deck.name}!")
                game.draw_hand()
        else:
            print("Invalid option. Please enter 'N' or 'L'.")

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

        action = input("Enter card indices to play (e.g., '0 2 4'), 'd' to discard, 't' to use Tarot card, 's' to use Spectral card, 'p' to use Planet card, 'v' to save, 'l' to load, 'h' for help, or 'q' to quit: ").lower()

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

            


            
