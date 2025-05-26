import time
from typing import Optional
from .card import draw_card
from .display_balance import display_balance
from ..utils.theme import ThemeManager

def animate_dealing(term, hand, deck, message, balance, player_name=None, theme_manager: Optional[ThemeManager] = None):
    """Animate dealing cards one by one."""
    hand_x = (term.width - 50) // 2  # Center the hand
    hand_y = 5

    if theme_manager is None:
        theme_manager = ThemeManager()

    for i in range(5):
        print(term.clear)
        print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
        display_balance(term, balance, player_name)
        print(term.move(3, 0) + message)

        # Draw already dealt cards
        for j in range(i):
            draw_card(term, hand_y, hand_x + j * 10, hand.cards[j], theme_manager=theme_manager)
            print(term.move(hand_y + 6, hand_x + j * 10 + 2) + f"({j+1})")
        time.sleep(0.2)  # Pause for animation effect
