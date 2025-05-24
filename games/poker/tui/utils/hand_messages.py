def get_hand_message(evaluation_result):
    hand_type, details = evaluation_result

    messages = {
        "straight_flush": f"🎉 STRAIGHT FLUSH! ({details} high) - The ultimate hand!",
        "four_of_a_kind": f"🔥 FOUR OF A KIND! (Four {details}s) - Incredible!",
        "full_house": f"🏠 FULL HOUSE! ({details}s full) - Fantastic hand!",
        "flush": f"♠️ FLUSH! (All {details}) - Beautiful cards!",
        "straight": f"📈 STRAIGHT! ({details} high) - Nice sequence!",
        "three_of_a_kind": f"⚡ THREE OF A KIND! (Three {details}s) - Great hand!",
        "two_pair": f"👥 TWO PAIR! ({' and '.join(map(str, details))}) - Solid hand!",
        "pair": f"👫 PAIR! (Two {details}s) - A decent start!",
        "high_card": f"🎯 HIGH CARD ({details}) - Better luck next time!"
    }

    return messages.get(hand_type, f"Unknown hand: {hand_type}")


def get_message_display_length(message):
    # Remove emojis and other unicode characters for length calculation
    import re
    # This regex removes most emoji characters
    clean_message = re.sub(r'[^\x00-\x7F]+', '', message)
    return len(clean_message)


def get_hand_rank_name(hand_type):
    rank_names = {
        "straight_flush": "Straight Flush",
        "four_of_a_kind": "Four of a Kind",
        "full_house": "Full House",
        "flush": "Flush",
        "straight": "Straight",
        "three_of_a_kind": "Three of a Kind",
        "two_pair": "Two Pair",
        "pair": "Pair",
        "high_card": "High Card"
    }

    return rank_names.get(hand_type, hand_type.replace("_", " ").title())
