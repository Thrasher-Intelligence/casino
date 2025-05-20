from engine.deck import Deck
from engine.mechanics.evaluate import evaluate_hand

def poker():
    print('Ready to play?')
    input('Press Enter to start!')
    while True:
        deck = Deck()
        deck.shuffle()
        hand = deck.deal(5)
        print('Your hand:')
        for card in hand:
            print(f"{card}")
        print(evaluate_hand(hand))
        again=input('Press Enter to play again or type "q" to quit: ')
        if again.lower() == 'q':
            break
    print('Thanks for playing!')
