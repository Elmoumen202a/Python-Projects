import unittest
from main import check_text_mistakes

class TestTextMistakeChecker(unittest.TestCase):
    def test_spelling_errors(self):
        """
        Test case to check for spelling errors.
        """
        text = "This is an example sentense with speling mistakes."
        expected_mistakes = ["Spelling error: 'speling'"]

        actual_mistakes = check_text_mistakes(text)

        self.assertEqual(actual_mistakes, expected_mistakes)

    def test_grammar_mistakes(self):
        """
        Test case to check for grammar mistakes.
        """
        text = "This is an example sentense with speling mistakes."
        expected_mistakes = ["Grammar mistake: 'sentense' should be 'sentence'"]

        actual_mistakes = check_text_mistakes(text)

        self.assertEqual(actual_mistakes, expected_mistakes)

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
