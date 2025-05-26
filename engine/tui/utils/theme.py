THEME_LIGHT = {
    "hearts": lambda term: term.red,
    "diamonds": lambda term: term.red,
    "spades": lambda term: term.white,
    "clubs": lambda term: term.white,
    "selected": lambda term: term.reverse,
}

THEME_DARK = {
    "hearts": lambda term: term.magenta,
    "diamonds": lambda term: term.magenta,
    "spades": lambda term: term.cyan,
    "clubs": lambda term: term.cyan,
    "selected": lambda term: term.bold_reverse,
}

class ThemeManager:
    SUIT_COLOR_MAP = {
        "♥": "hearts",
        "♦": "diamonds",
        "♠": "spades",
        "♣": "clubs",
    }

    def __init__(self, theme_name="light"):
        if theme_name == "dark":
            self.theme = THEME_DARK
        else:
            self.theme = THEME_LIGHT

    def get_color(self, key, term):
        # Return the color function for the key, or default to identity
        return self.theme.get(key, lambda t: t)(term)

    def get_suit_color(self, suit, term):
        key = self.SUIT_COLOR_MAP.get(suit, "spades")
        return self.get_color(key, term)