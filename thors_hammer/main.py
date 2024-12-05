import random

def check_worthiness(name, action):
    """
    Determines if a person is worthy of lifting Thor's hammer.
    
    Parameters:
        name (str): Name of the person.
        action (str): Action they perform to prove their worth.
        
    Returns:
        bool: True if worthy, False otherwise.
    """
    worthy_traits = ["bravery", "kindness", "sacrifice", "honor"]
    
    if any(trait in action.lower() for trait in worthy_traits):
        return True
    
    # Random chance to add a fun twist
    return random.choice([True, False])

def main():
    print("Welcome to Thor's Hammer Challenge!")
    name = input("What is your name, mortal? ")
    action = input("Describe one action you've done to prove your worth: ")
    
    if check_worthiness(name, action):
        print(f"Congratulations, {name}! You are worthy to wield Mjölnir! ⚡")
    else:
        print(f"Sorry, {name}. You are not worthy to lift Mjölnir. 🪨")

if __name__ == "__main__":
    main()
