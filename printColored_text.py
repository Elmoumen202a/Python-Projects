import colorama
from colorama import Fore, Back, Style

# Initialize colorama for colored console output
colorama.init(autoreset=True)

# Define a function to print colored messages
def print_colored_messages():
    # Example 1
    print(Fore.BLUE + Back.YELLOW + "Hi World,My name is Yousseef " + Fore.YELLOW + Back.BLUE + "I am your Machine Learning Instructor")

    # Example 2
    print(Back.CYAN + "Hi again my name is Yousseef ")

    # Example 3
    print(Fore.RED + Back.GREEN + "Happy codding!")

# Call the function to execute the colored print statements
print_colored_messages()

# Additional  of colored output
print(Fore.MAGENTA + Back.WHITE + "This is an additional  of colored output")

