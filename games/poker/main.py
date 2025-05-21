from engine.deck import Deck
from engine.mechanics.evaluate import evaluate_hand
from engine.mechanics.exchange import exchange_cards

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
        hand = exchange_cards(hand,deck)
        for card in hand:
            print(f"{card}")
        print(evaluate_hand(hand))
        again=input('Press Enter to play again or type "q" to quit: ')
        if again.lower() == 'q':
            break
    print('Thanks for playing!')
