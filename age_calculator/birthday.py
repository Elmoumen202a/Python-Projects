from datetime import datetime

def calculate_age(birth_date):
    """
    Calculate age based on the given birth date.

    Args:  birth_date (str) => A string representing the birth date in the format 'YYYY-MM-DD'.

    Returns:  age (int) => The age calculated based on the current date and the birth date.
    """
    # Convert birth date string to datetime object
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate age by subtracting birth year from current year
    age = current_date.year - birth_date.year
    
    # Adjust age if the birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def main():
    # Get user input for birth date
    user_input = input("Enter your birthday (YYYY-MM-DD): ")
    
    try:
        age = calculate_age(user_input)
        print("Your age is:", age)
    except ValueError:
        print("Please enter a valid date in the format YYYY-MM-DD")

if __name__ == "__main__":
    main()
