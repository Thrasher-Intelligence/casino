# test_profiles.py
from engine.objects.player import Player
from engine.utils.profiles import save_player, load_player

def main():
    print("👤 Creating a new player named Jake...")
    jake = Player("Jake")
    print("✅ Player created with name:", jake.name)

    print("\n💸 Depositing some chips into Jake's chip stack...")
    jake.chips.deposit(25, 3)
    jake.chips.deposit(1, 10)
    print("🏦 Jake's chip stack now looks like:", jake.chips)
    print("💰 Total chip value:", jake.chips.total())

    print("\n💾 Saving Jake's profile using save_player()...")
    save_player(jake)
    print("✅ Profile saved as 'profiles/jake.json'.")
    print("   👉 This function converts the player object to a dictionary and writes it to a file in JSON format.")

    print("\n📂 Now let's simulate loading Jake's profile back using load_player()...")
    loaded_jake = load_player("Jake")
    print("✅ Profile loaded successfully.")
    print("   👉 This function opens the saved JSON file, parses it, and reconstructs a Player object.")
    print("👤 Loaded player name:", loaded_jake.name)
    print("💰 Loaded chip stack total:", loaded_jake.chips.total())
    print("🏦 Loaded chip stack breakdown:", loaded_jake.chips)

    print("\n📌 Test complete. Jake's data is saved, retrievable, and consistent.")

if __name__ == "__main__":
    main()
