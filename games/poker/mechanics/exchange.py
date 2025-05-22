def exchange_cards(hand, deck):
    print("Would you like to exchange any cards?")
    exchange_input = input("Enter the card numbers you want to exchange, separated by commas (e.g., 1,2,3): ")

    if exchange_input.strip():
        try:
            indices = [int(i.strip()) - 1 for i in exchange_input.split(",")]
            hand.exchange(indices, deck)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    return hand
