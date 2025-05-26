from engine.utils.profiles import load_player, create_player, list_profiles
from engine.utils.profiles import player_exists

def get_all_profiles():
    """
    Returns a list of tuples: (player_name, chip_total)
    """
    return [(p.name, p.chips.total()) for p in list_profiles()]

def load_existing_profile(name):
    return load_player(name)

def create_new_profile(name):
    if player_exists(name):
        raise ValueError("Profile already exists.")
    return create_player(name)
