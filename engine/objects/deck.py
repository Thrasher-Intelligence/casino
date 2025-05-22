import random
from engine.objects.card import Card

# Defining Deck class
class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=1):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt

    def return_to_deck(self,card):
        self.cards.extend(card)

    def discard(self,card):
        if not hasattr(self, 'discarded'):
            self.discarded = []
        self.discarded.extend(card)
