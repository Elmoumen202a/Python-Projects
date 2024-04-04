# Importing the function to generate Prahprase text
from prahprase import generate_prahprase

# Main function to run the Prahprase generator
def main():
    # Generating a Prahprase text
    prahprase = generate_prahprase()
    # Printing the generated Prahprase text
    print(prahprase)

# Allowing main function to be executed if this script is run directly
if __name__ == "__main__":
    main()
