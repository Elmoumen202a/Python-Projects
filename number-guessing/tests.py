import unittest
from main import guess_number

class TestGuessNumber(unittest.TestCase):

    def test_guess(self):
        # Test if the game correctly identifies a correct guess
        # Set up
        secret_number = 50  # Set a known secret number
        user_input = [50]   # User input guesses the correct number
        
        # Call the function with the known secret number and user input
        # using monkey patching to override the input function
        with unittest.mock.patch('builtins.input', side_effect=user_input):
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                guess_number()

        # Check the output to see if the game congratulates the user for guessing correctly
        self.assertIn("Congratulations! You guessed the number in 1 guesses.", fake_stdout.getvalue())

        # Additional test cases can be added for scenarios like incorrect guesses, 
        # upper and lower bound guesses, and multiple guesses until correct.

if __name__ == '__main__':
    unittest.main()
