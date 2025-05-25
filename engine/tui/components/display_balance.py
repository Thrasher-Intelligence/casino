def display_balance(term, balance):
    """Display the player's chip balance at the top right corner of the terminal."""
    balance_str = f"Balance: ${balance}"
    x = max(term.width - len(balance_str) - 2, 0)
    y = 0
    print(term.move(y, x) + term.bold(balance_str) + term.normal)