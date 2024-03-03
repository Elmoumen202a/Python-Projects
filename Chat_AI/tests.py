# tests.py
import unittest
from unittest.mock import patch
from io import StringIO
from main import chat_ai

class TestChatAI(unittest.TestCase):

    @patch('builtins.input', side_effect=['Hello', 'How are you?', 'Thanks!', 'stop'])
    def test_chat_ai(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            chat_ai(input_function=mock_input)

        result_output = mock_stdout.getvalue().strip()
        expected_output = """Chat with the AI (Type 'stop' to end):
AI: Hello!
AI: I am doing well, thank you!
AI: You're welcome!
AI: Chat session ended. Goodbye!""".strip()

        # Compare the entire outputs
        self.assertEqual(result_output, expected_output)

if __name__ == '__main__':
    unittest.main()
