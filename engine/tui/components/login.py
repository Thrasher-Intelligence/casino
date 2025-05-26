# engine/tui/components/login.py
import blessed
from engine.mechanics import login as login_logic

def login():
    term = blessed.Terminal()
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        profiles = login_logic.get_all_profiles()
        profiles.append(("[New Profile]", None))

        index = 0
        while True:
            print(term.home + term.clear)
            print(term.center(term.bold("Nasty Boyz Casino – Select Your Profile")) + "\n")

            for i, (name, chips) in enumerate(profiles):
                line = f"{name} – ${chips}" if chips is not None else name
                if i == index:
                    print(term.reverse(line.center(term.width)))
                else:
                    print(line.center(term.width))

            key = term.inkey()
            if key.name == "KEY_UP":
                index = (index - 1) % len(profiles)
            elif key.name == "KEY_DOWN":
                index = (index + 1) % len(profiles)
            elif key.name == "KEY_ENTER" or key == "\n":
                selected = profiles[index]
                if selected[1] is not None:
                    return login_logic.load_existing_profile(selected[0])
                else:
                    name = new_profile_prompt(term)
                    try:
                        return login_logic.create_new_profile(name)
                    except ValueError:
                        show_message(term, f"⚠️ Profile '{name}' already exists!", delay=2)
            elif key.lower() == 'q':
                print(term.clear + term.move_y(term.height // 2) + term.center("Exiting..."))
                exit()

def new_profile_prompt(term):
    name = ""
    while True:
        print(term.home + term.clear)
        print(term.center("Create New Profile") + "\n")
        print(term.center("Type your name and press ENTER:\n"))
        print(term.center(name + "_"))

        key = term.inkey()
        if key.name == "KEY_ENTER" or key == "\n":
            if name.strip():
                return name.strip()
        elif key.name == "KEY_BACKSPACE":
            name = name[:-1]
        elif key.is_sequence:
            continue  # skip arrow keys and such
        else:
            name += str(key)

def show_message(term, message, delay=2):
    import time
    print(term.clear + term.move_y(term.height // 2) + term.center(message))
    time.sleep(delay)

if __name__ == "__main__":
    player = login()
    print(f"Logged in as: {player.name}")
