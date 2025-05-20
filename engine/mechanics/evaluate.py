from collections import Counter

def evaluate_hand(hand):
    ranks = [card.rank for card in hand]
    counts = Counter(ranks)
    pairs = [rank for rank, count in counts.items() if count == 2]
    trips = [rank for rank, count in counts.items() if count == 3]
    full_house = [rank for rank, count in counts.items() if count == 2 and rank in trips]
    four_of_a_kind = [rank for rank, count in counts.items() if count == 4]

    if pairs:
        return f"You have a pair of {pairs[0]}s!"
    elif trips:
        return f"You have three of a kind! {trips[0]}s!"
    elif full_house:
        return f"You have a full house! {pairs[0]}s and {trips[0]}s!"
    elif four_of_a_kind:
        return f"You have four of a kind! {four_of_a_kind[0]}s!"
    else:
        return "No pairs found."
