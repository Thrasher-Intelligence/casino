from typing import Optional
from ..utils.theme import ThemeManager
from .card import draw_card

def draw_hand(term, y, x, hand, selected_indices=None, theme_manager: Optional[ThemeManager] = None):
    """Draws a hand of cards in the terminal window."""
    if selected_indices is None:
        selected_indices = []
    if theme_manager is None:
        theme_manager = ThemeManager()

    for i, card in enumerate(hand.cards):
        is_selected = i in selected_indices
        draw_card(term, y, x + i * 10, card, theme_manager=theme_manager, selected=is_selected)
        # Draw card number below
        print(term.move(y + 6, x + i * 10 + 2) + f"({i+1})")
