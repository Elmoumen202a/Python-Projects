# main.py

import random

class DatingApp:
    """
    A simple dating app class to simulate matches and messaging between users.
    """

    def __init__(self):
        # Store user profiles in a list
        self.users = []
        # Store matches as a dictionary {user: [matched_users]}
        self.matches = {}

    def add_user(self, username, bio):
        """
        Add a new user to the app.
        """
        user = {"username": username, "bio": bio}
        self.users.append(user)
        self.matches[username] = []
        print(f"User '{username}' added successfully!")

    def show_users(self):
        """
        Show a list of all users.
        """
        print("Available users:")
        for user in self.users:
            print(f"- {user['username']}: {user['bio']}")

    def match_users(self, user1, user2):
        """
        Create a match between two users.
        """
        if user1 not in self.matches or user2 not in self.matches:
            print("One or both users not found!")
            return

        self.matches[user1].append(user2)
        self.matches[user2].append(user1)
        print(f"Matched {user1} with {user2}!")

    def send_message(self, from_user, to_user, message):
        """
        Simulate sending a message between two matched users.
        """
        if to_user in self.matches.get(from_user, []):
            print(f"{from_user} to {to_user}: {message}")
        else:
            print(f"Error: {from_user} and {to_user} are not matched!")

# Example usage
if __name__ == "__main__":
    app = DatingApp()

    # Adding users
    app.add_user("Alice", "Love hiking and movies!")
    app.add_user("Bob", "Tech geek and coffee lover.")
    app.add_user("Charlie", "Adventurer and foodie.")

    # Showing users
    app.show_users()

    # Matching users
    app.match_users("Alice", "Bob")
    app.match_users("Bob", "Charlie")

    # Sending messages
    app.send_message("Alice", "Bob", "Hi Bob! Want to go for a hike?")
    app.send_message("Bob", "Alice", "Sure, sounds fun!")
    app.send_message("Charlie", "Alice", "Hello!")  
