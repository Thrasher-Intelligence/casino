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
    assert "four of a kind" in evaluator.evaluate().lower()

def test_full_house():
    hand = make_hand({'Q': 3, 'J': 2})
    evaluator = PokerHandEvaluator(hand)
    assert "full house" in evaluator.evaluate().lower()

def test_two_pair():
    hand = make_hand({'9': 2, '5': 2, 'K': 1})
    evaluator = PokerHandEvaluator(hand)
    assert "two pair" in evaluator.evaluate().lower()

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
    assert "high card" in evaluator.evaluate().lower()

def test_three_of_a_kind():
    hand = make_hand({'7': 3, 'A': 1, '2': 1})
    evaluator = PokerHandEvaluator(hand)
    assert "three of a kind" in evaluator.evaluate().lower()
    assert "7s" in evaluator.evaluate()

def test_one_pair():
    hand = make_hand({'J': 2, 'A': 1, '8': 1, '3': 1})
    evaluator = PokerHandEvaluator(hand)
    assert "pair" in evaluator.evaluate().lower()
    assert "js" in evaluator.evaluate().lower()

def test_flush():
    # Create a hand with all the same suit
    suits = ['♠', '♠', '♠', '♠', '♠']
    cards = [Card('2', suits[0]), Card('5', suits[1]), Card('7', suits[2]),
             Card('J', suits[3]), Card('A', suits[4])]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    assert "flush" in evaluator.evaluate().lower()
    assert "a" in evaluator.evaluate().lower()

def test_straight():
    # Create a regular straight with different suits to avoid a straight flush
    cards = [Card('9', '♠'), Card('10', '♥'), Card('J', '♦'),
             Card('Q', '♣'), Card('K', '♥')]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    assert "straight" in evaluator.evaluate().lower()
    assert "k" in evaluator.evaluate().lower()

def test_wheel_straight():
    # Test A-5-4-3-2 straight (the wheel)
    # Using different suits to avoid a straight flush
    cards = [Card('A', '♠'), Card('2', '♥'), Card('3', '♦'),
             Card('4', '♣'), Card('5', '♥')]
    hand = Hand(cards)

    evaluator = PokerHandEvaluator(hand)
    assert "straight" in evaluator.evaluate().lower()

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
    assert "straight" not in evaluator.evaluate().lower()
    assert "high card" in evaluator.evaluate().lower()

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
    assert "high card" in evaluator.evaluate().lower()
    assert "a" in evaluator.evaluate().lower()

def test_straight_flush():
    # Create a straight flush
    suits = ['♠', '♠', '♠', '♠', '♠']
    cards = [Card('8', suits[0]), Card('9', suits[1]), Card('10', suits[2]), 
             Card('J', suits[3]), Card('Q', suits[4])]
    hand = Hand(cards)
    
    evaluator = PokerHandEvaluator(hand)
    assert "straight flush" in evaluator.evaluate().lower()
    assert "q" in evaluator.evaluate().lower()
