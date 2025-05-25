# Define functions that take a term object and return the desired color function
CARD_COLORS = {
    "hearts": lambda term: term.red,
    "diamonds": lambda term: term.red,
    "spades": lambda term: term.white,
    "clubs": lambda term: term.white,
    "selected": lambda term: term.reverse,
}

# Mapping from suit symbol to color key
SUIT_COLOR_MAP = {
    "♥": "hearts",
    "♦": "diamonds",
    "♠": "spades",
    "♣": "clubs",
}