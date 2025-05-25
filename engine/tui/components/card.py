from ..utils.theme import CARD_COLORS, SUIT_COLOR_MAP

def draw_card(term, y, x, card, selected=False):
    """Draws a single card in the terminal window."""
    rank = card.rank
    suit = card.suit

    # Determine color key by suit
    suit_color_key = SUIT_COLOR_MAP.get(suit, "spades")
    # Determine terminal color function based on selection state
    if selected:
        color = CARD_COLORS["selected"](term)
    else:
        color = CARD_COLORS[suit_color_key](term)

    # Card frame
    print(term.move(y, x) + color("┌─────┐"))

    # Rank (top-left)
    rank_display = rank
    if len(rank) == 1:  # For single character ranks, add a space
        rank_display = f"{rank} "
    print(term.move(y + 1, x) + color(f"│{rank_display}   │"))

    # Suit (center)
    print(term.move(y + 2, x) + color(f"│  {suit}  │"))

    # Rank (bottom-right)
    if len(rank) == 1:  # For single character ranks, add a space
        rank_display = f" {rank}"
    else:
        rank_display = rank
    print(term.move(y + 3, x) + color(f"│   {rank_display}│"))

    # Bottom border
    print(term.move(y + 4, x) + color("└─────┘"))
