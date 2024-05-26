import random

class Game:
    def __init__(self):
        # Initialize game with locations and starting position
        self.locations = {
            "forest": "You are in a dark forest. You hear wolves howling.",
            "castle": "You have entered a spooky castle. It's eerily quiet.",
            "cave": "You are in a damp cave. Something is lurking in the shadows."
        }
        self.current_location = "forest"
        self.inventory = []

    def start_game(self):
        # Welcome message and start the game loop
        print("Welcome to the Adventure Game!")
        self.describe_location()
        while True:
            command = input("What do you want to do? (explore/move/quit): ").strip().lower()
            if command == "explore":
                self.explore()
            elif command == "move":
                self.move()
            elif command == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Invalid command. Try again.")

    def describe_location(self):
        # Describe the current location
        print(self.locations[self.current_location])

    def explore(self):
        # Explore the current location and find an item
        if self.current_location == "forest":
            item = "a mystical leaf"
        elif self.current_location == "castle":
            item = "an ancient sword"
        else:
            item = "a shiny gem"
        
        print(f"You found {item}!")
        self.inventory.append(item)

    def move(self):
        # Move to a new location
        print("Where do you want to go? (forest/castle/cave): ")
        new_location = input().strip().lower()
        if new_location in self.locations:
            self.current_location = new_location
            self.describe_location()
        else:
            print("You can't go there. Try again.")

if __name__ == "__main__":
    # Create a game instance and start the game
    game = Game()
    game.start_game()
