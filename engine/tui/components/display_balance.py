def display_balance(term, balance, player_name=None):
    """Display the player's chip balance and optionally their name above the balance at the top right corner of the terminal."""
    balance_str = f"Balance: ${balance}"
    x = max(term.width - len(balance_str) - 2, 0)
    y = 0
    if player_name:
        name_str = f"{player_name}"
        name_x = max(term.width - len(name_str) - 2, 0)
        print(term.move(y, name_x) + term.bold(name_str) + term.normal)
        y += 1
    print(term.move(y, x) + term.bold(balance_str) + term.normal)