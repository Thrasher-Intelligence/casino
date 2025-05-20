from engine.deck import Deck
from engine.mechanics.pair import check_for_pair

class Game:
    def __init__(self):
        self.games = ['poker']

    def poker(self):
        print('Ready to play?')
        input('Press Enter to start!')
        while True:
            deck = Deck()
            deck.shuffle()
            hand = deck.deal(5)
            print('Your hand:')
            for card in hand:
                print(f"{card}")
            print(check_for_pair(hand))
            again=input('Press Enter to play again or type "q" to quit: ')
            if again.lower() == 'q':
                break
        print('Thanks for playing!')

    # inside the Game class
    # We'll import this in a second.

# game selection logic
# not here forever
def select_game():
    game_instance = Game()
    print('Select a game:')
    print('1. Poker')
    choice = input('Enter your choice: ')
    if choice == '1':
        return game_instance.poker
    else:
        print('Invalid choice')
        return None

def main():
    game = select_game()
    if game:
        game()

if __name__ == '__main__':
    main()
