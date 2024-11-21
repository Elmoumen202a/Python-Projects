import unittest
from main import GRAMMAR_QUESTIONS, VOCABULARY_QUESTIONS
import random

class TestTELCB1Practice(unittest.TestCase):
    """
    A test class to validate the structure and functionality of the TELC B1 practice questions.
    """

    def test_grammar_questions(self):
        """
        Test if each grammar question is properly structured as a tuple with
        a string question and a string answer.
        """
        for question, answer in GRAMMAR_QUESTIONS:
            self.assertIsInstance(question, str)  # Ensure the question is a string.
            self.assertIsInstance(answer, str)  # Ensure the answer is a string.
    
    def test_vocabulary_questions(self):
        """
        Test if each vocabulary question is properly structured as a tuple with
        a string question and a string answer.
        """
        for question, answer in VOCABULARY_QUESTIONS:
            self.assertIsInstance(question, str)  # Ensure the question is a string.
            self.assertIsInstance(answer, str)  # Ensure the answer is a string.
    
    def test_random_question(self):
        """
        Test if a random grammar question can be selected and has the correct structure.
        """
        question, answer = random.choice(GRAMMAR_QUESTIONS)
        self.assertIsInstance(question, str)  # Ensure the selected question is a string.
        self.assertIsInstance(answer, str)  # Ensure the selected answer is a string.

if __name__ == "__main__":
    unittest.main()
