import blessed
import time
from engine.objects.deck import Deck
from engine.objects.hand import Hand
from engine.mechanics.poker_eval import PokerHandEvaluator
from engine.tui.components.hand import draw_hand
from engine.tui.components.deal import animate_dealing

def poker():
    """Entry point for the TUI poker game."""
    try:
        term = blessed.Terminal()
        with term.hidden_cursor():
            tui_poker_game(term)
    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    poker()
