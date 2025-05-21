def exchange_cards(cards, deck):
    print("Would you like to exchange any cards?")
    exchange_input = input("Enter the card numbers you want to exchange, separated by commas (e.g., 1,2,3): ")

    if exchange_input.strip():
        try:
            # Convert input string to list of zero-based indices
            exchange_indices = [int(i.strip()) - 1 for i in exchange_input.split(",")]

            # Remove old cards from the back
            for idx in sorted(exchange_indices, reverse=True):
                if 0 <= idx < len(cards):
                    cards.pop(idx)
                    cards.append(deck.deal(1)[0])  # ✅ Correct usage
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    return cards
