# main.py

from balatro.game import Game

def main():
    """Main function to run the Balatro CLI game."""
    print("Welcome to Balatro CLI!\n")
    
    game = Game()
    game.draw_hand()

    while True:
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

        action = input("Enter card indices to play (e.g., '0 2 4'), 'd' to discard, 's' for shop, or 'q' to quit: ").lower()

        if action == 'q':
            break
        elif action == 's':
            game.shop.display_items()
            shop_action = input("Enter item index to purchase, or 'b' to go back: ").lower()
            if shop_action.isdigit():
                game.shop.purchase_item(int(shop_action), game)
            elif shop_action == 'b':
                pass # Go back to game
            else:
                print("Invalid shop action.")
            continue
        elif action == 'd':
            # Implement discard logic later
            print("Discarding not yet implemented.")
            continue

        try:
            indices = [int(i) for i in action.split()]
            
            if any(i >= len(game.hand) for i in indices):
                print("Error: Invalid index. Please choose cards from your hand.")
                continue

            cards_to_play = [game.hand[i] for i in indices]
            game.play_hand(cards_to_play)

        except ValueError:
            print("Invalid input. Please enter space-separated numbers.")

    print("\n--- Game Over ---")
    print(f"Final Score: {game.score}")

if __name__ == "__main__":
    main()
