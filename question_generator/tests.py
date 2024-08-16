import unittest
from main import QuestionGenerator

class TestQuestionGenerator(unittest.TestCase):
    # Setup method to initialize a QuestionGenerator instance for testing
    def setUp(self):
        self.generator = QuestionGenerator()

    # Test to ensure the generated question is part of the predefined list
    def test_generate_question(self):
        question = self.generator.generate_question()
        self.assertIn(question, self.generator.questions)  # Assert that the question is in the list

# If this script is run directly, execute the tests
if __name__ == "__main__":
    unittest.main()
