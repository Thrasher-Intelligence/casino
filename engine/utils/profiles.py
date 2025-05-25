import json
from ..objects import Player
import os

PROFILE_DIR = "profiles"

def save_player(player: Player):
    os.makedirs(PROFILE_DIR, exist_ok=True)
    filename = f"{player.name.lower()}.json"
    filepath = os.path.join(PROFILE_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(player.to_dict(), f, indent=2)

def load_player(name: str) -> Player:
    filename = f"{name.lower()}.json"
    filepath = os.path.join(PROFILE_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No saved profile for player '{name}'")
    with open(filepath, "r") as f:
        data = json.load(f)
    return Player.from_dict(data)

def create_player(name: str) -> Player:
    player = Player(name)
    save_player(player)
    return player
