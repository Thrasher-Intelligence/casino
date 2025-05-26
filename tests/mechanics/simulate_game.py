import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from engine.objects.card import Card
from engine.objects.hand import Hand
from engine.objects.deck import Deck
from engine.mechanics.poker_eval import PokerHandEvaluator
from games.poker.tui.utils.hand_messages import get_hand_message

def simulate_game_with_specific_hand():
    """
    Simulate the poker game flow with the specific hand reported by the user.
    This test recreates the situation where a straight wasn't recognized.
    """
    print("=== POKER GAME SIMULATION ===")
    print("Testing hand: 10♣, 9♣, J♥, 8♠, 7♣")
    
    # Create a deck (like in the real game)
    deck = Deck()
    deck.shuffle()
    
    # Replace the top 5 cards with our specific test case
    test_cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    
    # Replace the first 5 cards in the deck
    for i in range(5):
        deck.cards[i] = test_cards[i]
    
    # Deal the hand as in the game
    hand = Hand(deck.deal(5))
    
    # Display the hand
    print("\nYour hand:")
    for card in hand.cards:
        print(f"{card}")
    
    # Print internal representation for debugging
    print("\nInternal representation:")
    print(f"Cards: {[str(c) for c in hand.cards]}")
    print(f"Sorted ranks: {hand.sorted_ranks}")
    print(f"Rank counts: {hand.rank_counts}")
    print(f"Suit counts: {hand.suit_counts}")
    
    # Evaluate the hand
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    
    # Print evaluation steps
    print("\nEvaluation process:")
    values = sorted(set(hand.sorted_ranks))
    print(f"1. Sorted ranks: {hand.sorted_ranks}")
    print(f"2. Unique sorted values: {values}")
    print(f"3. Is a straight?: {evaluator.is_straight()}")
    
    # Get the result
    print(f"\nEvaluation result: {result}")
    
    # Get the message that would be displayed
    hand_message = get_hand_message(result)
    print(f"UI message: {hand_message}")
    
    # Print evaluation order checks
    print("\nEvaluation order checks:")
    print(f"Is straight and flush? {evaluator.is_straight() and evaluator.is_flush()}")
    print(f"Is four of a kind? {evaluator.is_four_of_a_kind()}")
    print(f"Is full house? {evaluator.is_full_house()}")
    print(f"Is flush? {evaluator.is_flush()}")
    print(f"Is straight? {evaluator.is_straight()}")
    print(f"Is three of a kind? {evaluator.is_three_of_a_kind()}")
    print(f"Is two pair? {evaluator.is_two_pair()}")
    print(f"Is pair? {evaluator.is_pair()}")
    
    return result

if __name__ == "__main__":
    result = simulate_game_with_specific_hand()
    hand_type, details = result
    
    if hand_type == "straight":
        print("\n✅ TEST PASSED: Hand correctly identified as a straight!")
    else:
        print(f"\n❌ TEST FAILED: Hand incorrectly identified as {hand_type}!")