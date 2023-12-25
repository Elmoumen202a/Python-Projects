import random

# Generate a random number between 1 and 10
number = random.randrange(1, 10)

# Prompt the user to guess the number
while True:
    try:
        guess = float(input("Enter a number: "))
        
        if guess < number:
            print("The number is too low.")
        elif guess > number:
            print("The number is too high!")
        else:
            # Break out of the loop when the guess is correct
            break
    except ValueError:
        # Handle the case when the input is not a number
        print("Not a valid number. Please enter a number.")

# Print a success message when the correct number is guessed
print("You guessed it right!")
