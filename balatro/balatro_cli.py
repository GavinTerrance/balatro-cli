# main.py

from balatro.game import Game

def main():
    """Main function to run the Balatro CLI game."""
    print("Welcome to Balatro CLI!\n")
    
    game = Game()
    game.draw_hand()

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

        action = input("Enter card indices to play (e.g., '0 2 4'), 'd' to discard, 't' to use Tarot card, 's' to use Spectral card, 'p' to use Planet card, or 'q' to quit: ").lower()

        if action == 'q':
            break
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
