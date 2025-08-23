from balatro.balatro_cli import main

if __name__ == "__main__":
    # Sample commands to simulate a game session
    # This will play a hand, then quit.
    sample_commands = [
        "0 1 2 3 4", # Play first 5 cards
        "q" # Quit the game
    ]
    main(commands=sample_commands)