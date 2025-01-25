
 # Library to handle HTTP requests
import requests 
# Library for creating ASCII art from text
import pyfiglet  
 # Library for adding colors to console output
from termcolor import colored 

def fetch_joke():
    """Fetch a random joke from the Joke API.

    Returns:
        str: The joke text or an error message.
    """
    url = "https://official-joke-api.appspot.com/random_joke"  # API endpoint for jokes
    try:
        # Sending a GET request to fetch the joke
        response = requests.get(url)
        if response.status_code == 200:  # Check if the request was successful
            joke = response.json()  # Parse the JSON response
            # Return the joke in a formatted way (setup and punchline)
            return f"{joke['setup']}\n{joke['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again."  # Error message for failed request
    except Exception as e:
        # Return error message if something goes wrong
        return f"Error: {e}"

def display_joke(joke):
    """Display the joke in a cool format with ASCII art and colors.

    Args:
        joke (str): The joke text to display.
    """
    # Create ASCII art for the title
    ascii_banner = pyfiglet.figlet_format("Joke Generator")
    print(colored(ascii_banner, "cyan"))  # Print the title in cyan color
    print(colored("Fetching a random joke for you...", "yellow"))  # Display a message
    print(colored(joke, "green"))  # Print the joke in green color

# Main execution starts here
if __name__ == "__main__":
    joke = fetch_joke()  # Fetch a random joke
    display_joke(joke)  # Display the joke in the console
