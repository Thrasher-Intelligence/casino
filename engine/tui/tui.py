import blessed
import time
from engine.objects.deck import Deck
from engine.objects.hand import Hand
from engine.mechanics.poker_eval import PokerHandEvaluator
from engine.tui.components.hand import draw_hand
from engine.tui.components.deal import animate_dealing

def get_exchange_input(term, hand):
    """Get user input for card exchange through terminal interface."""
    selected_indices = []
    current_index = 0
    hand_x = (term.width - 50) // 2
    hand_y = 5

    with term.cbreak():
        while True:
            # Draw current state
            print(term.clear)
            print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
            message = "Select cards to exchange (use arrow keys, SPACE to select, ENTER to confirm)"
            print(term.move(3, (term.width - len(message)) // 2) + message)

            # Draw hand with highlighted current selection
            draw_hand(term, hand_y, hand_x, hand, selected_indices)

            # Highlight current selection with a cursor
            cursor_pos_y = hand_y + 5
            cursor_pos_x = hand_x + current_index * 10 + 2
            print(term.move(cursor_pos_y, cursor_pos_x) + term.bold("^^^"))

            # Status message
            status_text = "SPACE: select/unselect card | ENTER: confirm | Q: quit without exchange"
            print(term.move(term.height - 2, (term.width - len(status_text)) // 2) + status_text)

            # Get key input
            key = term.inkey()

            if key.name == 'KEY_LEFT' and current_index > 0:
                current_index -= 1
            elif key.name == 'KEY_RIGHT' and current_index < len(hand.cards) - 1:
                current_index += 1
            elif key == ' ':  # Space to toggle selection
                if current_index in selected_indices:
                    selected_indices.remove(current_index)
                else:
                    selected_indices.append(current_index)
            elif key.name == 'KEY_ENTER' or key == '\n' or key == '\r':  # Enter key to confirm
                break
            elif key.lower() == 'q':  # Q to quit without exchange
                return []

    return selected_indices

def tui_poker_game(term):
    """Main poker game loop with TUI."""
    print(term.clear)

    # Main game loop
    playing = True
    while playing:
        # Initialize deck and deal cards
        deck = Deck()
        deck.shuffle()
        hand = Hand(deck.deal(5))

        # Animate dealing
        animate_dealing(term, hand, deck, "Dealing cards...")

        # Show full hand
        print(term.clear)
        hand_x = (term.width - 50) // 2
        hand_y = 5
        print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
        print(term.move(3, 0) + "Your hand:")
        draw_hand(term, hand_y, hand_x, hand)
        time.sleep(1)  # Give player time to see initial hand

        # Card exchange phase
        print(term.clear)
        print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
        print(term.move(3, 0) + "Would you like to exchange any cards?")
        draw_hand(term, hand_y, hand_x, hand)

        # Get exchange input
        indices = get_exchange_input(term, hand)

        if indices:
            # Exchange cards
            hand.exchange(indices, deck)

            # Show animation for exchange
            print(term.clear)
            print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
            print(term.move(3, 0) + "Exchanging cards...")
            time.sleep(0.5)

        # Show final hand
        print(term.clear)
        print(term.move(0, (term.width - len("Poker TUI")) // 2) + term.bold("Poker TUI"))
        print(term.move(3, 0) + "Your final hand:")
        draw_hand(term, hand_y, hand_x, hand)

        # Evaluate hand
        evaluator = PokerHandEvaluator(hand)
        result = evaluator.evaluate()
        print(term.move(hand_y + 8, hand_x) + term.bold(result))

        # Play again?
        print(term.move(hand_y + 10, hand_x) + "Press ENTER to play again or 'q' to quit")

        # Wait for user input
        with term.cbreak():
            while True:
                key = term.inkey()
                if key.lower() == 'q':
                    playing = False
                    break
                elif key.name == 'KEY_ENTER' or key == '\n' or key == '\r':  # Enter key
                    break

    # Final message
    print(term.clear)
    print(term.move(term.height // 2, (term.width - len("Thanks for playing!")) // 2) + "Thanks for playing!")
    time.sleep(1)

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
