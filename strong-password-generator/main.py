import random
import string

def generate_password(length=12):
    """
    Generate a strong password.
    
    Args:
        length (int): Length of the password (default is 12).
    
    Returns:
        str: A strong password.
    """
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+=-"

    # Combining all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure each character set is included in the password
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(special_characters)]

    # Generate the remaining characters randomly
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to mix up the characters
    random.shuffle(password)

    # Convert the password list to a string
    return ''.join(password)

if __name__ == "__main__":
    print(generate_password())
