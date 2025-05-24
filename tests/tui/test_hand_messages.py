import pytest
import sys
import os

# Import the module under test
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from games.poker.tui.utils.hand_messages import (
    get_hand_message,
    get_message_display_length,
    get_hand_rank_name
)


class TestHandMessages:
    """Tests for the hand_messages module used in the poker TUI."""

    @pytest.mark.parametrize("evaluation_result, expected_substr", [
        (("straight_flush", "A"), "STRAIGHT FLUSH"),
        (("four_of_a_kind", "K"), "FOUR OF A KIND"),
        (("full_house", "Q"), "FULL HOUSE"),
        (("flush", "hearts"), "FLUSH"),
        (("straight", "10"), "STRAIGHT"),
        (("three_of_a_kind", "J"), "THREE OF A KIND"),
        (("two_pair", ["A", "8"]), "TWO PAIR"),
        (("pair", "9"), "PAIR"),
        (("high_card", "K"), "HIGH CARD"),
    ])
    def test_get_hand_message_type(self, evaluation_result, expected_substr):
        """Test that messages contain the correct hand type."""
        message = get_hand_message(evaluation_result)
        assert expected_substr in message

    @pytest.mark.parametrize("evaluation_result, expected_substr", [
        (("straight_flush", "A"), "A high"),
        (("four_of_a_kind", "K"), "Four Ks"),
        (("full_house", "Q"), "Qs full"),
        (("flush", "hearts"), "hearts"),
        (("straight", "10"), "10 high"),
        (("three_of_a_kind", "J"), "Three Js"),
        (("two_pair", ["A", "8"]), "A and 8"),
        (("pair", "9"), "9s"),
        (("high_card", "K"), "K"),
    ])
    def test_get_hand_message_details(self, evaluation_result, expected_substr):
        """Test that messages contain the correct hand details."""
        message = get_hand_message(evaluation_result)
        assert expected_substr in message

    def test_unknown_hand_type(self):
        """Test handling of unknown hand types."""
        result = get_hand_message(("unknown_type", "details"))
        assert "Unknown hand: unknown_type" in result

    @pytest.mark.parametrize("message, expected_length", [
        ("🎉 STRAIGHT FLUSH!", 16),  # emoji is removed in length calculation
        ("No emojis here", 14),
        ("⚡ THREE OF A KIND!", 17),
        ("♠️ FLUSH! (All hearts)", 20),
    ])
    def test_get_message_display_length(self, message, expected_length):
        """Test that display length calculation handles emojis correctly."""
        length = get_message_display_length(message)
        assert length == expected_length

    @pytest.mark.parametrize("hand_type, expected_name", [
        ("straight_flush", "Straight Flush"),
        ("four_of_a_kind", "Four of a Kind"),
        ("full_house", "Full House"),
        ("flush", "Flush"),
        ("straight", "Straight"),
        ("three_of_a_kind", "Three of a Kind"),
        ("two_pair", "Two Pair"),
        ("pair", "Pair"),
        ("high_card", "High Card"),
        ("unknown_type", "Unknown Type"),  # Test automatic formatting
    ])
    def test_get_hand_rank_name(self, hand_type, expected_name):
        """Test converting hand type keys to human-readable names."""
        name = get_hand_rank_name(hand_type)
        assert name == expected_name