def change_eighth_char(filename, new_char):
    try:
        # Open the file in read mode to read its content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Check if the content has at least eight characters
        if len(content) < 8:
            raise ValueError("The file does not have at least eight characters.")

        # Replace the eighth character with the new character
        new_content = content[:7] + new_char + content[8:]
        
        # Write the modified content back to the file
        with open(filename, 'w') as file:
            file.write(new_content)
        
        # Print a success message
        print("Eighth character changed successfully.")
    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"File '{filename}' not found.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take filename and new character input from the user
    filename = input("Enter the filename: ")
    new_char = input("Enter the new character: ")
    # Call the function to change the eighth character
    change_eighth_char(filename, new_char)
