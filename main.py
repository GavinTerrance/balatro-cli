# main.py

from balatro.game import Game

def main():
    """Main function to run the Balatro CLI game."""
    print("Welcome to Balatro CLI!\n")
    
    game = Game()
    game.draw_hand()

    while game.hands > 0:
        print("\n--------------------")
        print(game)
        print("\n--- Your Hand ---")
        for i, card in enumerate(game.hand):
            print(f"[{i}] {card}")
        print("--------------------")

        action = input("Enter card indices to play (e.g., '0 2 4'), or 'd' to discard: ").lower()

        if action == 'q':
            break

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
