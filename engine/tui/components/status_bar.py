def draw_status_bar(term, message):
    """Displays a status message at the bottom of the window."""
    print(term.move(term.height - 1, 0) + term.reverse(message[:term.width - 1].ljust(term.width - 1)))
