from ..utils.theme import ThemeManager

def draw_card(term, y, x, card, theme_manager: ThemeManager, selected=False):
    """Draws a single card in the terminal window."""
    rank = card.rank
    suit = card.suit

    if selected:
        color = theme_manager.get_color("selected", term)
    else:
        color = theme_manager.get_suit_color(suit, term)

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
