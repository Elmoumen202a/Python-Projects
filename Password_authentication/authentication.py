# Importing the getpass module for secure password input
import getpass

# Function to authenticate a user based on the provided username and password
def authenticate_user(username, password):
    # Dummy database with username-password pairs
    database = {"youssef.x": "123456", "youssef.y": "654321"}

    # Loop through the database entries
    for stored_username, stored_password in database.items():
        # Check if the provided username matches any stored username
        if username == stored_username:
            # While the provided password does not match the stored password, keep prompting for password
            while password != stored_password:
                password = getpass.getpass("Enter Your Password Again : ")
            # If the loop completes without breaking, the password is verified
            return "Verified"

    # If the loop completes without finding a matching username, return "User not found"
    return "User not found"

# Entry point of the script
if __name__ == "__main__":
    # Get username input from the user
    username_input = input("Enter Your Username : ")
    
    # Get password input from the user without displaying it on the screen
    password_input = getpass.getpass("Enter Your Password : ")
    
    # Call the authentication function with the provided username and password
    result = authenticate_user(username_input, password_input)
    
    # Print the result of the authentication
    print(result)
