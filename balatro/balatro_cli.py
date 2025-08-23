# main.py

"""This module contains the main command-line interface for the Balatro game."""
from typing import Optional
from balatro.game import Game, save_game, load_game
from balatro.deck import BaseDeck, RedDeck, GreenDeck, YellowDeck


def print_help():
    print("\n--- Help ---")
    print("  Enter space-separated card indices (e.g., '0 2 4') to select cards.")
    print("  'p': Play selected cards")
    print("  'd': Discard selected cards")
    print("  't': Use a Tarot card from your inventory.")
    print("  's': Use a Spectral card from your inventory.")
    print("  'p': Use a Planet card from your inventory.")
    print("  'o': Sort your hand by rank or suit.")
    print("  'v': Save the current game.")
    print("  'l': Load a previously saved game.")
    print("  'q': Quit the game.")
    print("--------------------")

def do_action(game: Game, action:str, cards: Optional[str]) -> Optional[Game]: 
    if cards:
        card_indices = [int(idx) for idx in cards.split()]
        selected_cards = [game.hand[i] for i in card_indices]


    if action == 'q':
        return None
    elif action == 'v':
        save_game(game)
        return game
    elif action == 'l':
        loaded_game = load_game()
        if loaded_game:
            game = loaded_game
        return game
    elif action == 'h':
        print_help()
        return game
    elif action == 'o':
        game.change_sort_type()
        game.sort_hand()
        print("Hand sorted.")
        return game
    elif action == 'p':
        if selected_cards:
            game.play_hand(selected_cards)
            return game
        else: 
            print("Did you list the cards you want to play after 'p' ")
            return game
    elif action == 'd':
        if selected_cards:
            game.discard_cards(card_indices)
            return game
    else:
        print("Invalid action or card indices. Please try again.")
        return game



def testing(command_list: list[str] = None): 
    game = Game(deck_type="Base")
    game.draw_hand()
    for command in command_list:
        game = do_action(game, command)
        if game is None: break



            



def main(command_list: list[str] = None):
    """Main function to run the Balatro CLI game."""

    game = Game(deck_type="Base")
    print(f"You have chosen the {game.deck.name}!")
    game.draw_hand()
    print_help()

    # Main game loop
    while True:
        if game.game_over:
            break

        print(game)
        # Get action from commands list or default to 'q' if no commands left
        user_input = input("Enter your action: ").strip().lower()
        action = user_input[:1]         # first character ('' if empty)
        additional_input = user_input[1:]  # everything after the first char
        game = do_action(game, action, additional_input)

        if game is None: break
            


            
