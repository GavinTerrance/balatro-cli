# main.py

from balatro.game import Game

def main():
    """Main function to run the Balatro CLI game."""
    print("Welcome to Balatro CLI!\n")
    
    # Initialize the game
    game = Game()
    game.draw_hand()
    
    print("--- Initial Game State ---")
    print(game)
    print("\n--- Your Hand ---")
    for card in game.hand:
        print(card)
    print("--------------------")

if __name__ == "__main__":
    main()
