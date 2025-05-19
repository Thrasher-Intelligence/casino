from engine.deck import Deck

def start_game():
    # Changing the way the deck is shuffled. 05/18/2025
    print('Ready to play?')
    input('Press Enter to start!')
    while True:
        deck = Deck()
        deck.shuffle()
        hand = deck.deal(5)
        print('Your hand:')
        for card in hand:
            print(f"{card}")
        again=input('Press Enter to play again or type "q" to quit: ')
        if again.lower() == 'q':
            break
    print('Thanks for playing!')
