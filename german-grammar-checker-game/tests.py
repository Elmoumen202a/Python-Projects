import unittest
from main import GermanGrammarGame

class TestGermanGrammarGame(unittest.TestCase):
    def setUp(self):
        # Create an instance of the game to use in the tests
        self.game = GermanGrammarGame()

    def test_initial_score(self):
        # Test that the initial score is 0
        self.assertEqual(self.game.score, 0)

    def test_ask_question_correct(self):
        # Test asking a question and getting the correct answer
        question = {
            "question": "What is the correct form of the article in '___ Hund ist groß.'?",
            "options": ["Der", "Die", "Das"],
            "answer": "Der"
        }
        # Mock the input to simulate the user selecting the correct answer
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.game.ask_question(question)
        # Check if the score has been incremented
        self.assertEqual(self.game.score, 1)

    def test_ask_question_incorrect(self):
        # Test asking a question and getting an incorrect answer
        question = {
            "question": "What is the correct form of the article in '___ Hund ist groß.'?",
            "options": ["Der", "Die", "Das"],
            "answer": "Der"
        }
        # Mock the input to simulate the user selecting an incorrect answer
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.game.ask_question(question)
        # Check that the score has not been incremented
        self.assertEqual(self.game.score, 0)

if __name__ == '__main__':
    # Run the tests
    unittest.main()
