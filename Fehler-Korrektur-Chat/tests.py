# tests.py

import unittest
from main import identify_errors, correct_text

class TestGermanErrorChatAI(unittest.TestCase):

    def test_identify_errors(self):
        self.assertEqual(
            identify_errors("ich bin gegangen."),
            ["Sentences should start with a capital letter."]
        )
        self.assertIn(
            "Incorrect verb placement. Use 'bin gegangen' instead.",
            identify_errors("Ich gegangen habe.")
        )

    def test_correct_text(self):
        self.assertEqual(
            correct_text("Ich gegangen habe."),
            "Ich bin gegangen."
        )

if __name__ == "__main__":
    unittest.main()
