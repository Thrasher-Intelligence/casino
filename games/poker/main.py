from engine.objects import Deck, Hand
from games.poker.mechanics import exchange_cards
from engine.mechanics import PokerHandEvaluator

def poker(player):
    print('Ready to play?')
    input('Press Enter to start!')
    while True:
        deck = Deck()
        deck.shuffle()
        hand = Hand(deck.deal(5))
        print('Your hand:')
        for card in hand:
            print(f"{card}")
        hand = exchange_cards(hand,deck)
        for card in hand:
            print(f"{card}")
        evaluator = PokerHandEvaluator(hand)
        print(evaluator.evaluate())
        again=input('Press Enter to play again or type "q" to quit: ')
        if again.lower() == 'q':
            break
    print('Thanks for playing!')
