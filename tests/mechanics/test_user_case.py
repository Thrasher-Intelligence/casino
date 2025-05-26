import pytest
from engine.objects.card import Card
from engine.objects.hand import Hand
from engine.objects.deck import Deck
from engine.mechanics.poker_eval import PokerHandEvaluator
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_specific_user_case():
    """Test the specific card order mentioned by the user: 10, 9, J, 8, 7"""
    cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    hand = Hand(cards)
    
    # Print the hand's sorted ranks for debugging
    print(f"User case - Original hand: {[str(card) for card in hand.cards]}")
    print(f"User case - Sorted ranks: {hand.sorted_ranks}")
    print(f"User case - Unique sorted ranks: {sorted(set(hand.sorted_ranks))}")
    
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    
    # Print the evaluation result for debugging
    print(f"User case - Evaluation result: {result}")
    
    assert result[0] == "straight", f"Expected 'straight', got '{result[0]}'"
    assert result[1] == "J", f"Expected highest card to be 'J', got '{result[1]}'"

def test_check_hand_initialization():
    """Test how the hand is initialized and sorted to ensure proper rank order processing."""
    cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    
    # Print original card order
    print("Original card order:")
    for card in cards:
        print(f"{card}")
    
    hand = Hand(cards)
    
    # Print card values after hand creation
    print("\nCards in hand after initialization:")
    for card in hand.cards:
        print(f"{card} (rank value: {hand.rank_value(card.rank)})")
    
    # Print the sorted ranks
    print(f"\nHand's sorted_ranks attribute: {hand.sorted_ranks}")
    
    # Check if the sorted_ranks attribute accurately represents the hand
    expected_ranks = [11, 10, 9, 8, 7]  # J=11, 10=10, 9=9, 8=8, 7=7
    assert hand.sorted_ranks == expected_ranks, f"Expected {expected_ranks}, got {hand.sorted_ranks}"

def test_tui_simulation():
    """Simulate the TUI (Text User Interface) evaluation process to check for potential issues."""
    cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    
    # Create hand directly without any preliminary processing
    hand = Hand(cards)
    
    # Print the hand as it would appear in the UI
    print("Hand as displayed in UI:")
    print(" ".join(str(card) for card in hand.cards))
    
    # Evaluate the hand as would happen in the poker game
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    
    print(f"Evaluation in simulated UI: {result}")
    assert result[0] == "straight", f"Expected 'straight', got '{result[0]}'"

def test_exact_tui_evaluation_flow():
    """Simulates the exact evaluation flow as it happens in the TUI implementation."""
    # Create the cards in the exact order specified by the user
    cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    
    # First, create a deck and deal cards just like in the game
    deck = Deck()
    deck.shuffle()
    
    # Manually replace the first 5 cards with our test case
    # This is equivalent to mocking the initial deal
    for i in range(5):
        deck.cards[i] = cards[i]
    
    # Deal cards as happens in the game
    game_hand = Hand(deck.deal(5))
    
    print("\nEXACT TUI FLOW SIMULATION:")
    print("Cards as dealt:")
    for card in game_hand.cards:
        print(f"{card}")
    
    print("\nHand's internal representation:")
    print(f"Raw cards: {[str(c) for c in game_hand.cards]}")
    print(f"Sorted ranks: {game_hand.sorted_ranks}")
    print(f"Rank counts: {game_hand.rank_counts}")
    print(f"Suit counts: {game_hand.suit_counts}")
    
    # Perform evaluation exactly as in the TUI
    evaluator = PokerHandEvaluator(game_hand)
    
    # Debug the straight detection logic step by step
    values = sorted(set(game_hand.sorted_ranks))
    print(f"\nIs straight calculation:")
    print(f"1. game_hand.sorted_ranks: {game_hand.sorted_ranks}")
    print(f"2. set(game_hand.sorted_ranks): {set(game_hand.sorted_ranks)}")
    print(f"3. sorted(set(game_hand.sorted_ranks)): {values}")
    print(f"4. values[-1]: {values[-1]}, values[0]: {values[0]}")
    print(f"5. values[-1] - values[0]: {values[-1] - values[0]}")
    print(f"6. is_straight check #1 (values[-1] - values[0] == 4): {values[-1] - values[0] == 4}")
    print(f"7. is_straight check #2 (set(values) == {{14, 5, 4, 3, 2}}): {set(values) == {14, 5, 4, 3, 2}}")
    print(f"8. Final is_straight result: {evaluator.is_straight()}")
    
    # Get the evaluation result
    result = evaluator.evaluate()
    print(f"\nTUI Evaluation result: {result}")
    
    # This should be a straight
    assert result[0] == "straight", f"Expected 'straight', got '{result[0]}'"
    assert result[1] == "J", f"Expected highest card to be 'J', got '{result[1]}'"
    
    # Now import the hand message utility to see what would be displayed
    from games.poker.tui.utils.hand_messages import get_hand_message
    hand_message = get_hand_message(result)
    print(f"\nMessage displayed in TUI: {hand_message}")

def test_exact_real_game_scenario():
    """Test the exact hand from the user's real game scenario with precise suit combinations."""
    # The exact hand as reported by the user: 10♣, 9♣, J♥, 8♠, 7♣
    cards = [
        Card('10', '♣'),
        Card('9', '♣'),
        Card('J', '♥'),
        Card('8', '♠'),
        Card('7', '♣')
    ]
    
    print("\nREAL GAME SCENARIO:")
    print("Exact hand from the game:")
    for card in cards:
        print(f"{card}")
    
    hand = Hand(cards)
    
    # Print detailed diagnostics
    print(f"\nHand details:")
    print(f"Raw cards: {[str(c) for c in hand.cards]}")
    print(f"Sorted ranks: {hand.sorted_ranks}")
    print(f"Rank counts: {hand.rank_counts}")
    print(f"Suit counts: {hand.suit_counts}")
    
    # Check the straight detection logic
    evaluator = PokerHandEvaluator(hand)
    values = sorted(set(hand.sorted_ranks))
    print(f"\nStraight detection details:")
    print(f"1. hand.sorted_ranks: {hand.sorted_ranks}")
    print(f"2. set(hand.sorted_ranks): {set(hand.sorted_ranks)}")
    print(f"3. sorted(set(hand.sorted_ranks)): {values}")
    print(f"4. values[-1] - values[0]: {values[-1] - values[0]}")
    print(f"5. Is this equal to 4? {values[-1] - values[0] == 4}")
    print(f"6. Final is_straight result: {evaluator.is_straight()}")
    
    # Get the evaluation result
    result = evaluator.evaluate()
    print(f"\nEvaluation result: {result}")
    
    # This should be a straight
    assert result[0] == "straight", f"Expected 'straight', got '{result[0]}'"

if __name__ == "__main__":
    test_specific_user_case()
    test_check_hand_initialization()
    test_tui_simulation()
    test_exact_tui_evaluation_flow()
    test_exact_real_game_scenario()