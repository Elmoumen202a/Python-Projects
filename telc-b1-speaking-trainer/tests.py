import unittest
from unittest.mock import patch
from main import generate_question, evaluate_answer

class TestSpeakingTrainer(unittest.TestCase):
    @patch('main.openai.ChatCompletion.create')
    def test_generate_question(self, mock_openai):
        mock_openai.return_value = {
            "choices": [{
                "message": {"content": "Was sind Ihre Hobbys und warum?"}
            }]
        }
        result = generate_question("hobbies")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 5)

    @patch('main.openai.ChatCompletion.create')
    def test_evaluate_answer(self, mock_openai):
        mock_openai.return_value = {
            "choices": [{
                "message": {"content": "Score: 8/10\nFeedback: Good vocabulary with minor grammar errors."}
            }]
        }
        evaluation = evaluate_answer("Question", "Answer")
        self.assertIn('score', evaluation)
        self.assertIn('feedback', evaluation)
        self.assertIsInstance(evaluation['score'], int)

if __name__ == '__main__':
    unittest.main()