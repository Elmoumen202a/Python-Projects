import random

# Dice class to simulate a dice
class Dice:
    def __init__(self, sides=6):
        # Number of sides on the dice, default is 6
        self.sides = sides  

    def roll(self):
        # Returns a random number between 1 and the number of sides
        return random.randint(1, self.sides)

# Main function to run the dice rolling simulator
def main():
    # Create a standard 6-sided dice
    dice = Dice() 
    # Flag to control the rolling loop
    rolling = True  

    print("Welcome to the Dice Rolling Simulator!")
    while rolling:
        # Roll the dice
        roll_result = dice.roll()  
        # Print the result
        print(f"You rolled a {roll_result}")  
        # Ask user if they want to roll again
        user_input = input("Roll again? (y/n): ").strip().lower()  
        # Exit the loop if the user does not input 'y'
        if user_input != 'y':
            rolling = False  
    # Goodbye message
    print("Thank you for playing!")  

# Entry point of the program
if __name__ == "__main__":
    main()
