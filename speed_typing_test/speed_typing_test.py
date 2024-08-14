import random  # Importing the random module to shuffle words
import time  # Importing the time module to track time

# Function to load words from a file
def load_words(file_path='C:/Users/x/Desktop/Python-Projects/speed_typing_test/words.txt'):
    """
    Loads words from a text file and returns them as a list.
    Each word is on a new line in the file.

    :param file_path: Path to the file containing words
    :return: List of words
    """
    with open(file_path, 'r') as file:
        words = file.read().splitlines()  # Read all lines and split them into a list
    return words  # Return the list of words

# Function to conduct the speed typing test
def speed_typing_test(words):
    """
    Conducts a speed typing test using a list of words.
    The user is asked to type each word as fast as possible.

    :param words: List of words to use in the test
    """
    print("Typing Speed Test. Type the following words as fast as you can.")
    input("Press Enter to start...\n")  # Prompt user to start the test

    random.shuffle(words)  # Shuffle the words to randomize the test
    test_words = words[:5]  # Select the first 5 words for the test

    # Record the start time
    start_time = time.time()

    # Loop through each word in the test list
    for word in test_words:
        print(f"\nType this word: {word}")  # Display the word to the user
        user_input = input("> ")  # Get user's input

        # Loop until the user types the correct word
        while user_input != word:
            print("Incorrect! Try again.")  # Inform the user if the input is incorrect
            user_input = input("> ")  # Prompt the user to try again

    # Record the end time
    end_time = time.time()
    total_time = end_time - start_time  # Calculate the total time taken

    # Calculate words per minute (WPM)
    wpm = (len(test_words) / total_time) * 60

    # Display the user's typing speed
    print(f"\nYour typing speed is {wpm:.2f} words per minute.")

# Main execution block
if __name__ == "__main__":
    words = load_words()  # Load the words from the file
    speed_typing_test(words)  # Start the typing test

