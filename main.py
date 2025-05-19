from ui.cli import start_game

def main():
    print("Welcome to the Casino!")
    game=input("what would you like to play?")

    if game == "poker":
        start_game()

main()
