import random

# List of rooms in the haunted house
rooms = ["Living Room", "Kitchen", "Attic", "Basement", "Library"]

# Ghost's abilities
abilities = ["Telekinesis", "Scaring people", "Invisibility", "Shape-shifting"]

# Function to choose a random room for the ghost
def choose_room():
    """Choose a random room from the haunted house."""
    room = random.choice(rooms)
    print(f"🕯️ You are now haunting the {room}... spooky!")
    return room

# Function to choose a random ability for the ghost
def choose_ability():
    """Choose a random ability for the ghost to use."""
    ability = random.choice(abilities)
    print(f"👻 You have the ability to: {ability}")
    return ability

# Main function to run the game
def main():
    """Main function to run the Ghostty game."""
    print("Welcome to Ghostty! 🎃")
    print("You are a ghost trying to scare people... 👻")
    
    # Choosing a random room and ability
    room = choose_room()
    ability = choose_ability()

    print(f"Now, you need to decide how to use your {ability} in the {room}!")
    action = input("Do you want to scare someone? (yes/no): ")

    if action.lower() == "yes":
        print("🎃 Boo! You've successfully scared someone!")
    else:
        print("👻 Maybe next time... Stay spooky!")

# Run the game
if __name__ == "__main__":
    main()
