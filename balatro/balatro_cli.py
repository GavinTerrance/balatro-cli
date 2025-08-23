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
        elif action == 'o':
            sort_option = input("Sort hand by 'rank' or 'suit'? ").lower()
            if sort_option in ['rank', 'suit']:
                game.sort_hand(sort_by=sort_option)
                print(f"Hand sorted by {sort_option}.")
            else:
                print("Invalid sort option.")
            continue
        elif action == 't':
            if not game.tarot_cards:
                print("You have no Tarot cards to use.")
                continue
            print("\n--- Your Tarot Cards ---")
            for i, tarot_card in enumerate(game.tarot_cards):
                print(f"[{i}] {tarot_card.name}: {tarot_card.description}")
            print("--------------------")
            try:
                tarot_index = int(input("Enter the index of the Tarot card to use: "))
                game.use_tarot_card(tarot_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 's':
            if not game.spectral_cards:
                print("You have no Spectral cards to use.")
                continue
            print("\n--- Your Spectral Cards ---")
            for i, spectral_card in enumerate(game.spectral_cards):
                print(f"[{i}] {spectral_card.name}: {spectral_card.description}")
            print("--------------------")
            try:
                spectral_index = int(input("Enter the index of the Spectral card to use: "))
                game.use_spectral_card(spectral_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 'p':
            if not game.planet_cards:
                print("You have no Planet cards to use.")
                continue
            print("\n--- Your Planet Cards ---")
            for i, planet_card in enumerate(game.planet_cards):
                print(f"[{i}] {planet_card.name}: {planet_card.description}")
            print("--------------------")
            try:
                planet_index = int(input("Enter the index of the Planet card to use: "))
                game.use_planet_card(planet_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 'd':
            if game.discards <= 0:
                print("No discards remaining!")
                continue
            
            discard_input = input("Enter card indices to discard (e.g., '0 2 4'): ").lower()
            try:
                indices_to_discard = [int(i) for i in discard_input.split()]
                game.discard_cards(indices_to_discard)

                if game.hands == 0:
                    print("\n--- End of Round ---")
                    game.check_blind_cleared()
                    game.end_of_round_effects() # Apply end of round effects
                    shop_phase(game) # Call shop phase
                    game.hands = 4 # Reset for next round
                    game.draw_hand() # Draw new hand for next round
            except ValueError:
                print("Invalid input. Please enter space-separated numbers.")
            continue

        try:
            indices = [int(i) for i in action.split()]
            
            if any(i >= len(game.hand) for i in indices):
                print("Error: Invalid index. Please choose cards from your hand.")
                continue

            cards_to_play = [game.hand[i] for i in indices]
            game.play_hand(cards_to_play)

            if game.hands == 0:
                print("\n--- End of Round ---")
                game.check_blind_cleared()
                game.end_of_round_effects() # Apply end of round effects
                shop_phase(game) # Call shop phase
                game.hands = 4 # Reset for next round
                game.draw_hand() # Draw new hand for next round

        except ValueError:
            print("Invalid input. Please enter space-separated numbers.")

def shop_phase(game):
    """Handles the shop phase of the game."""
    while True:
        print("\n--- Shop ---")
        game.shop.display_items()
        shop_action = input("Enter item index to purchase, 'r' to reroll, or 'c' to continue to next round: ").lower()

        if shop_action.isdigit():
            game.shop.purchase_item(int(shop_action), game)
        elif shop_action == 'r':
            game.shop.generate_items() # Reroll shop items
            print("Shop rerolled!")
        elif shop_action == 'c':
            break # Exit shop phase
        else:
            print("Invalid shop action.")

    print("\n--- Game Over ---")
    print(f"Final Score: {game.score}")

if __name__ == "__main__":
    main()


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
        elif action == 'o':
            sort_option = input("Sort hand by 'rank' or 'suit'? ").lower()
            if sort_option in ['rank', 'suit']:
                game.sort_hand(sort_by=sort_option)
                print(f"Hand sorted by {sort_option}.")
            else:
                print("Invalid sort option.")
            continue
        elif action == 't':
            if not game.tarot_cards:
                print("You have no Tarot cards to use.")
                continue
            print("\n--- Your Tarot Cards ---")
            for i, tarot_card in enumerate(game.tarot_cards):
                print(f"[{i}] {tarot_card.name}: {tarot_card.description}")
            print("--------------------")
            try:
                tarot_index = int(input("Enter the index of the Tarot card to use: "))
                game.use_tarot_card(tarot_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 's':
            if not game.spectral_cards:
                print("You have no Spectral cards to use.")
                continue
            print("\n--- Your Spectral Cards ---")
            for i, spectral_card in enumerate(game.spectral_cards):
                print(f"[{i}] {spectral_card.name}: {spectral_card.description}")
            print("--------------------")
            try:
                spectral_index = int(input("Enter the index of the Spectral card to use: "))
                game.use_spectral_card(spectral_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 'p':
            if not game.planet_cards:
                print("You have no Planet cards to use.")
                continue
            print("\n--- Your Planet Cards ---")
            for i, planet_card in enumerate(game.planet_cards):
                print(f"[{i}] {planet_card.name}: {planet_card.description}")
            print("--------------------")
            try:
                planet_index = int(input("Enter the index of the Planet card to use: "))
                game.use_planet_card(planet_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            continue
        elif action == 'd':
            if game.discards <= 0:
                print("No discards remaining!")
                continue
            
            discard_input = input("Enter card indices to discard (e.g., '0 2 4'): ").lower()
            try:
                indices_to_discard = [int(i) for i in discard_input.split()]
                game.discard_cards(indices_to_discard)

                if game.hands == 0:
                    print("\n--- End of Round ---")
                    game.check_blind_cleared()
                    game.end_of_round_effects() # Apply end of round effects
                    shop_phase(game) # Call shop phase
                    game.hands = 4 # Reset for next round
                    game.draw_hand() # Draw new hand for next round
            except ValueError:
                print("Invalid input. Please enter space-separated numbers.")
            continue

        try:
            indices = [int(i) for i in action.split()]
            
            if any(i >= len(game.hand) for i in indices):
                print("Error: Invalid index. Please choose cards from your hand.")
                continue

            cards_to_play = [game.hand[i] for i in indices]
            game.play_hand(cards_to_play)

            if game.hands == 0:
                print("\n--- End of Round ---")
                game.check_blind_cleared()
                game.end_of_round_effects() # Apply end of round effects
                shop_phase(game) # Call shop phase
                game.hands = 4 # Reset for next round
                game.draw_hand() # Draw new hand for next round

        except ValueError:
            print("Invalid input. Please enter space-separated numbers.")

def shop_phase(game):
    while True:
        print("\n--- Shop ---")
        game.shop.display_items()
        shop_action = input("Enter item index to purchase, 'r' to reroll, or 'c' to continue to next round: ").lower()

        if shop_action.isdigit():
            game.shop.purchase_item(int(shop_action), game)
        elif shop_action == 'r':
            game.shop.generate_items() # Reroll shop items
            print("Shop rerolled!")
        elif shop_action == 'c':
            break # Exit shop phase
        else:
            print("Invalid shop action.")

    print("\n--- Game Over ---")
    print(f"Final Score: {game.score}")

if __name__ == "__main__":
    main()
