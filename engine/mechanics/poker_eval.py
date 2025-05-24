from collections import Counter

class PokerHandEvaluator:
    def __init__(self, hand):
        self.hand = hand
        self.cards = hand.cards
        self.ranks = [card.rank for card in self.cards]
        self.rank_counts = Counter(self.ranks)

    def evaluate(self):
        if self.is_straight() and self.is_flush():
            return ("straight_flush", self.get_highest_card_desc())
        elif self.is_four_of_a_kind():
            return ("four_of_a_kind", self.get_n_of_a_kind(4))
        elif self.is_full_house():
            return ("full_house", self.get_n_of_a_kind(3))
        elif self.is_flush():
            return ("flush", self.get_flush_suit())
        elif self.is_straight():
            return ("straight", self.get_highest_card_desc())
        elif self.is_three_of_a_kind():
            return ("three_of_a_kind", self.get_n_of_a_kind(3))
        elif self.is_two_pair():
            return ("two_pair", self.get_all_n_of_a_kind(2))
        elif self.is_pair():
            return ("pair", self.get_n_of_a_kind(2))
        else:
            return ("high_card", self.get_highest_card_desc())


    def get_n_of_a_kind(self, n):
        for rank, count in self.rank_counts.items():
            if count == n:
                return rank
        return None

    def get_all_n_of_a_kind(self, n):
        return [rank for rank, count in self.rank_counts.items() if count == n]

    def is_pair(self):
        return len(self.get_all_n_of_a_kind(2)) == 1

    def is_two_pair(self):
        return len(self.get_all_n_of_a_kind(2)) == 2

    def is_three_of_a_kind(self):
        return bool(self.get_n_of_a_kind(3))

    def is_four_of_a_kind(self):
        return bool(self.get_n_of_a_kind(4))

    def is_full_house(self):
        return self.is_three_of_a_kind() and self.is_pair()

    def is_flush(self):
        return any(count == 5 for count in self.hand.suit_counts.values())

    def is_straight(self):
        values = sorted(set(self.hand.sorted_ranks))
        if len(values) != 5:
            return False
        # Check for normal straight
        if values[-1] - values[0] == 4:
            return True
        # Check for wheel straight (A-5-4-3-2)
        if set(values) == {14, 5, 4, 3, 2}:
            return True
        return False

    def get_highest_card_desc(self):
        # Map rank values back to symbols
        rank_names = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                     10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        # Get the rank value of the highest card
        highest_rank_value = self.hand.sorted_ranks[0]
        return rank_names.get(highest_rank_value, str(highest_rank_value))

    def get_flush_suit(self):
        for suit, count in self.hand.suit_counts.items():
            if count == 5:
                return suit
        return None
