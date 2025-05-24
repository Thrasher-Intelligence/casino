# engine/objects/chipstack.py

class ChipStack:
    def __init__(self, chips=None):
        # Default to an empty stack of common denominations
        self.chips = chips or {1: 0, 5: 0, 25: 0, 100: 0}

    def total(self):
        return sum(denom * count for denom, count in self.chips.items())

    def deposit(self, denom, count=1):
        self.chips[denom] = self.chips.get(denom, 0) + count

    def withdraw(self, denom, count=1):
        if self.chips.get(denom, 0) >= count:
            self.chips[denom] -= count
            return True
        return False

    def to_dict(self):
        return self.chips

    @classmethod
    # engine/objects/chips.py

    @classmethod
    def from_dict(cls, data):
        # Convert all keys from strings to integers
        cleaned_data = {int(denom): count for denom, count in data.items()}
        return cls(chips=cleaned_data)

    def __str__(self):
        return " | ".join(f"{count} x ${denom}" for denom, count in sorted(self.chips.items()))

    def clear(self):
        for denom in self.chips:
            self.chips[denom] = 0
