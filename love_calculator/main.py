import random

def love_calculator(name1, name2):
    """
    Calculate a love percentage based on the lengths of the two names
    and a pseudo-random seed.

    -param name1: The first name as a string
    -param name2: The second name as a string
    -return: A percentage as an integer between 0 and 100
    """
    # Combine the lengths of both names to create a seed for randomness
    random.seed(len(name1) + len(name2))
    # Generate a random percentage between 0 and 100
    return random.randint(0, 100)

def main():
    """
    Main function to interact with the user and calculate the love percentage.
    """
    print("Welcome to the Love Calculator!")
    # Prompt the user to enter the first name
    name1 = input("Enter the first name: ")
    # Prompt the user to enter the second name
    name2 = input("Enter the second name: ")
    
    # Calculate the love percentage
    love_percentage = love_calculator(name1, name2)
    # Display the result to the user
    print(f"The love percentage between {name1} and {name2} is {love_percentage}%")

if __name__ == "__main__":
    main()
