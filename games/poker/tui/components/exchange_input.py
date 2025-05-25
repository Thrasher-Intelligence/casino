from engine.tui.components.display_balance import display_balance
from engine.tui.components import draw_hand

def get_exchange_input(term, hand, balance):
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
            display_balance(term, balance)
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
