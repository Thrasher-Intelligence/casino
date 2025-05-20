from games.poker.main import poker

def select_game():
    print('Select a game:')
    print('1. Poker')
    choice = input('Enter your choice: ')
    if choice == '1':
        return poker()
    else:
        print('Invalid choice')
        return None

def main():
    game = select_game()
    if game:
        game()

if __name__ == '__main__':
    main()
