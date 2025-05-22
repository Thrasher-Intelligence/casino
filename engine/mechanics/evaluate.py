from collections import Counter

def evaluate_hand(hand):
    ranks = [card.rank for card in hand]
    counts = Counter(ranks)
    pairs = [rank for rank, count in counts.items() if count == 2]
    trips = [rank for rank, count in counts.items() if count == 3]
    four_of_a_kind = [rank for rank, count in counts.items() if count == 4]

    if four_of_a_kind:
        return f"You have four of a kind! {four_of_a_kind[0]}s!"
    elif trips and len(pairs) >= 1:
        return f"You have a full house! {trips[0]}s over {pairs[0]}s!"
    elif trips:
        return f"You have three of a kind! {trips[0]}s!"
    elif len(pairs) == 2:
        return f"You have two pairs! {pairs[0]}s and {pairs[1]}s!"
    elif len(pairs) == 1:
        return f"You have a pair of {pairs[0]}s!"
    else:
        return "No pairs found."
