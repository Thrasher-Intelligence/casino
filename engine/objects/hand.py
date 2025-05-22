from collections import Counter

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.rank_counts = Counter(card.rank for card in cards)
        self.suit_counts = Counter(card.suit for card in cards)

        # Sorted list of rank values (helpful for straights/high card)
        self.sorted_ranks = sorted(
            [self.rank_value(card.rank) for card in cards],
            reverse=True
        )

    def rank_value(self, rank):
        order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                 '7': 7, '8': 8, '9': 9, '10': 10,
                 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return order[rank]

    def exchange(self, indices, deck):
        for idx in sorted(set(indices), reverse=True):
            if 0 <= idx < len(self.cards):
                self.cards.pop(idx)
                self.cards.append(deck.deal(1)[0])
        # Update rank and suit counts after exchange
        self.rank_counts = Counter(card.rank for card in self.cards)
        self.suit_counts = Counter(card.suit for card in self.cards)

    def __str__(self):
        return " ".join(str(card) for card in self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)
