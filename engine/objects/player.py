# engine/objects/player.py
from engine.objects.chips import ChipStack

class Player:
    def __init__(self, name, chips=None):
        self.name = name
        self.chips = chips or ChipStack()
        self.hand = []

    def reset_hand(self):
        self.hand = []

    def to_dict(self):
        return {
            "name": self.name,
            "chips": self.chips.chips,
        }

    @classmethod
    def from_dict(cls, data):
        chips = ChipStack.from_dict(data["chips"])
        return cls(data["name"], chips=chips)
