import curses
import time

from engine.objects.deck import Deck
from engine.objects.hand import Hand
from engine.mechanics.poker_eval import PokerHandEvaluator

def draw_card(win, y, x, card, selected=False):
    """Draws a single card in the curses window."""
    rank = card.rank
    suit = card.suit

    # Use color pair 1 for red suits (hearts/diamonds), color pair 2 for black suits
    color_pair = curses.color_pair(1) if suit in ['♥', '♦'] else curses.color_pair(2)

    attrs = color_pair
    if selected:
        attrs |= curses.A_REVERSE

    # Card frame
    win.addstr(y, x, "┌─────┐", attrs)

    # Rank (top-left)
    rank_display = rank
    if len(rank) == 1:  # For single character ranks, add a space
        rank_display = f"{rank} "
    win.addstr(y + 1, x, f"│{rank_display}   │", attrs)

    # Suit (center)
    win.addstr(y + 2, x, f"│  {suit}  │", attrs)

    # Rank (bottom-right)
    if len(rank) == 1:  # For single character ranks, add a space
        rank_display = f" {rank}"
    else:
        rank_display = rank
    win.addstr(y + 3, x, f"│   {rank_display}│", attrs)

    # Bottom border
    win.addstr(y + 4, x, "└─────┘", attrs)

def draw_hand(win, y, x, hand, selected_indices=None):
    """Draws a hand of cards in the curses window."""
    if selected_indices is None:
        selected_indices = []

    for i, card in enumerate(hand.cards):
        is_selected = i in selected_indices
        draw_card(win, y, x + i * 10, card, is_selected)
        # Draw card number below
        win.addstr(y + 6, x + i * 10 + 2, f"({i+1})")

def draw_status_bar(win, message):
    """Displays a status message at the bottom of the window."""
    max_y, max_x = win.getmaxyx()
    win.addstr(max_y - 1, 0, message[:max_x - 1], curses.A_REVERSE)
    win.clrtoeol()

def animate_dealing(win, hand, deck, message):
    """Animate dealing cards one by one."""
    max_y, max_x = win.getmaxyx()
    hand_x = (max_x - 50) // 2  # Center the hand
    hand_y = 5

    for i in range(5):
        win.clear()
        win.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
        win.addstr(3, 0, message)

        # Draw already dealt cards
        for j in range(i):
            draw_card(win, hand_y, hand_x + j * 10, hand.cards[j])
            win.addstr(hand_y + 6, hand_x + j * 10 + 2, f"({j+1})")

        win.refresh()
        time.sleep(0.2)  # Pause for animation effect

def get_exchange_input(win, hand):
    """Get user input for card exchange through curses interface."""
    max_y, max_x = win.getmaxyx()
    selected_indices = []
    current_index = 0
    hand_x = (max_x - 50) // 2
    hand_y = 5

    while True:
        # Draw current state
        win.clear()
        win.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
        win.addstr(3, 0, "Select cards to exchange (use arrow keys, SPACE to select, ENTER to confirm)")

        # Draw hand with highlighted current selection
        draw_hand(win, hand_y, hand_x, hand, selected_indices)

        # Highlight current selection with a cursor
        cursor_pos_y = hand_y + 5
        cursor_pos_x = hand_x + current_index * 10 + 2
        win.addstr(cursor_pos_y, cursor_pos_x, "^^^", curses.A_BOLD)

        # Status message
        draw_status_bar(win, "SPACE: select/unselect card | ENTER: confirm | Q: quit without exchange")

        win.refresh()

        # Get key input
        key = win.getch()

        if key == curses.KEY_LEFT and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_RIGHT and current_index < len(hand.cards) - 1:
            current_index += 1
        elif key == ord(' '):  # Space to toggle selection
            if current_index in selected_indices:
                selected_indices.remove(current_index)
            else:
                selected_indices.append(current_index)
        elif key == 10:  # Enter key to confirm
            break
        elif key == ord('q') or key == ord('Q'):  # Q to quit without exchange
            return []

    return selected_indices

def tui_poker_game(stdscr):
    """Main poker game loop with TUI."""
    # Set up curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    # Set up colors if terminal supports it
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Red for hearts/diamonds
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White for spades/clubs

    max_y, max_x = stdscr.getmaxyx()

    # Main game loop
    playing = True
    while playing:
        # Initialize deck and deal cards
        deck = Deck()
        deck.shuffle()
        hand = Hand(deck.deal(5))

        # Animate dealing
        animate_dealing(stdscr, hand, deck, "Dealing cards...")

        # Show full hand
        stdscr.clear()
        hand_x = (max_x - 50) // 2
        hand_y = 5
        stdscr.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
        stdscr.addstr(3, 0, "Your hand:")
        draw_hand(stdscr, hand_y, hand_x, hand)
        stdscr.refresh()
        time.sleep(1)  # Give player time to see initial hand

        # Card exchange phase
        stdscr.clear()
        stdscr.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
        stdscr.addstr(3, 0, "Would you like to exchange any cards?")
        draw_hand(stdscr, hand_y, hand_x, hand)
        stdscr.refresh()

        # Get exchange input
        indices = get_exchange_input(stdscr, hand)

        if indices:
            # Exchange cards
            hand.exchange(indices, deck)

            # Show animation for exchange
            stdscr.clear()
            stdscr.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
            stdscr.addstr(3, 0, "Exchanging cards...")
            stdscr.refresh()
            time.sleep(0.5)

        # Show final hand
        stdscr.clear()
        stdscr.addstr(0, (max_x - len("Poker TUI")) // 2, "Poker TUI", curses.A_BOLD)
        stdscr.addstr(3, 0, "Your final hand:")
        draw_hand(stdscr, hand_y, hand_x, hand)

        # Evaluate hand
        evaluator = PokerHandEvaluator(hand)
        result = evaluator.evaluate()
        stdscr.addstr(hand_y + 8, hand_x, result, curses.A_BOLD)

        # Play again?
        stdscr.addstr(hand_y + 10, hand_x, "Press ENTER to play again or 'q' to quit")
        stdscr.refresh()

        # Wait for user input
        while True:
            key = stdscr.getch()
            if key == ord('q') or key == ord('Q'):
                playing = False
                break
            elif key == 10:  # Enter key
                break

    # Final message
    stdscr.clear()
    stdscr.addstr(max_y // 2, (max_x - len("Thanks for playing!")) // 2, "Thanks for playing!")
    stdscr.refresh()
    time.sleep(1)

def poker():
    """Entry point for the TUI poker game."""
    try:
        curses.wrapper(tui_poker_game)
    except Exception as e:
        import traceback
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    poker()
