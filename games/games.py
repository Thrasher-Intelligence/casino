from .poker import poker
from .poker.tui import poker as tui_poker

def select_game():
    print('Select a game:')
    print('1. Poker (CLI)')
    print('2. Poker (TUI)')
    choice = input('Enter your choice: ')
    if choice == '1':
        return poker
    elif choice == '2':
        return tui_poker
    else:
        print('Invalid choice')
        return None

def main(player):
    game = select_game()
    if game:
        game(player)
