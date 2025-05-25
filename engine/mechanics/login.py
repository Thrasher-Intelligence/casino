from engine.utils.profiles import load_player, create_player

def login():
    player_name = input("Enter your name: ")

    try:
        player = load_player(player_name)
        print(f"Welcome back, {player.name}!")
    except FileNotFoundError:
        player = create_player(player_name)
        print(f"New player created with name: {player.name}")
    return player
