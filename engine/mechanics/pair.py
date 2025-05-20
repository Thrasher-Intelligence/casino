from collections import Counter

def check_for_pair(hand):
    ranks = [card.rank for card in hand]
    counts = Counter(ranks)
    pairs = [rank for rank, count in counts.items() if count == 2]

    if pairs:
        return f"You have a pair of {pairs[0]}s!"
    else:
        return "No pairs found."
