import pytest
from engine.objects.card import Card
from engine.objects.hand import Hand
from engine.mechanics.poker_eval import PokerHandEvaluator
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def make_hand(rank_counts):
    """
    Helper to create a hand based on rank counts.
    rank_counts = {'A': 4, 'K': 1} → 4 Aces, 1 King
    """
    suits = ['♠', '♥', '♦', '♣']
    cards = []
    suit_index = 0
    for rank, count in rank_counts.items():
        for i in range(count):
            cards.append(Card(rank, suits[suit_index % len(suits)]))
            suit_index += 1
    return Hand(cards)

def test_four_of_a_kind():
    hand = make_hand({'A': 4, 'K': 1})
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "four_of_a_kind"

def test_full_house():
    hand = make_hand({'Q': 3, 'J': 2})
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "full_house"

def test_two_pair():
    hand = make_hand({'9': 2, '5': 2, 'K': 1})
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "two_pair"

def test_no_pairs():
    # Explicitly create cards with different suits to avoid a flush
    cards = [
        Card('2', '♠'),
        Card('4', '♥'),
        Card('6', '♦'),
        Card('8', '♣'),
        Card('10', '♠')
    ]
    hand = Hand(cards)
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "high_card"

def test_three_of_a_kind():
    hand = make_hand({'7': 3, 'A': 1, '2': 1})
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "three_of_a_kind"
    assert result[1] == "7"

def test_one_pair():
    hand = make_hand({'J': 2, 'A': 1, '8': 1, '3': 1})
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "pair"
    assert result[1] == "J"

def test_flush():
    # Create a hand with all the same suit
    suits = ['♠', '♠', '♠', '♠', '♠']
    cards = [Card('2', suits[0]), Card('5', suits[1]), Card('7', suits[2]),
             Card('J', suits[3]), Card('A', suits[4])]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "flush"
    assert result[1] == "♠"

def test_straight():
    # Create a regular straight with different suits to avoid a straight flush
    cards = [Card('9', '♠'), Card('10', '♥'), Card('J', '♦'),
             Card('Q', '♣'), Card('K', '♥')]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "straight"
    assert result[1] == "K"

def test_wheel_straight():
    # Test A-5-4-3-2 straight (the wheel)
    # Using different suits to avoid a straight flush
    cards = [Card('A', '♠'), Card('2', '♥'), Card('3', '♦'),
             Card('4', '♣'), Card('5', '♥')]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "straight"

def test_not_straight():
    # Explicitly create cards with different suits to avoid a flush
    cards = [
        Card('2', '♠'),
        Card('4', '♥'),
        Card('6', '♦'),
        Card('8', '♣'),
        Card('10', '♠')
    ]
    hand = Hand(cards)
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] != "straight"
    assert result[0] == "high_card"

def test_high_card():
    # Explicitly create cards with different suits to avoid a flush
    cards = [
        Card('2', '♠'),
        Card('5', '♥'),
        Card('9', '♦'),
        Card('J', '♣'),
        Card('A', '♠')
    ]
    hand = Hand(cards)
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "high_card"
    assert result[1] == "A"

def test_straight_flush():
    # Create a straight flush
    suits = ['♠', '♠', '♠', '♠', '♠']
    cards = [Card('8', suits[0]), Card('9', suits[1]), Card('10', suits[2]), 
             Card('J', suits[3]), Card('Q', suits[4])]
    hand = Hand(cards)
        
    evaluator = PokerHandEvaluator(hand)
    result = evaluator.evaluate()
    assert result[0] == "straight_flush"
    assert result[1] == "Q"
