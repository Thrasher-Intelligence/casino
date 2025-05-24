import blessed
import time
from engine.objects.deck import Deck
from engine.objects.hand import Hand
from engine.mechanics.poker_eval import PokerHandEvaluator
from engine.tui.components.hand import draw_hand
from engine.tui.components.deal import animate_dealing
from games.poker.tui.components.exchange_input import get_exchange_input
from games.poker.tui.utils import get_hand_message, get_message_display_length

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

        # Evaluate hand with dramatic reveal
        print(term.move(hand_y + 8, (term.width - len("Evaluating hand...")) // 2) + "Evaluating hand...")
        time.sleep(0.8)
        
        evaluator = PokerHandEvaluator(hand)
        result = evaluator.evaluate()
        hand_message = get_hand_message(result)
        
        # Clear evaluation message and show result
        print(term.move(hand_y + 8, 0) + " " * term.width)  # Clear line
        message_x = (term.width - get_message_display_length(hand_message)) // 2
        print(term.move(hand_y + 8, message_x) + term.bold(term.green(hand_message)))
        
        # Add some visual spacing
        print(term.move(hand_y + 9, 0))

        # Play again prompt
        play_again_msg = "Press ENTER to play again or 'q' to quit"
        play_again_x = (term.width - len(play_again_msg)) // 2
        print(term.move(hand_y + 10, play_again_x) + play_again_msg)

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
