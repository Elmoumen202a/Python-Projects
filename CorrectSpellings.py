# Import the SpellChecker class from spellchecker module
from spellchecker import SpellChecker

def main():
    # Create a SpellChecker instance
    spell_checker = SpellChecker()

    # Get user input
    input_word = input("Please enter a word: ")

    # Check if the input word is correct
    if spell_checker.correction(input_word) == input_word:
        print("It is correct")
    else:
        # Get the corrected spelling of the word
        correction_word = spell_checker.correction(input_word)
        print("Correct Spelling of the word is:", correction_word)

if __name__ == "__main__":
    main()

