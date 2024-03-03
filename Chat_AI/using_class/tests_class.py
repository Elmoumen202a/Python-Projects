import unittest
from unittest.mock import patch
from io import StringIO
from main_class import ChatAI


class TestChatAI(unittest.TestCase):

    @patch('builtins.input', side_effect=['Hello', 'How are you?', 'Thanks!', 'stop'])
    def test_chat_ai(self, mock_input):
        # Use the patch function to mock user input during the test
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Create an instance of the ChatAI class
            chat_ai = ChatAI()
            # Call the chat loop method to simulate a conversation
            chat_ai.chat_loop()

        # Get the result of the chat session from the mock stdout
        result_lines = mock_stdout.getvalue().strip().split('\n')

        # Check if AI responses start with the expected phrases
        self.assertTrue(result_lines[1].startswith('AI: Hello'))
        self.assertTrue(result_lines[2].startswith('AI: I am doing well, thank you!'))
        self.assertTrue(result_lines[3].startswith('AI: You\'re welcome!'))
        self.assertTrue(result_lines[4].startswith('AI: Chat session ended. Goodbye!'))

# Run the tests if this file is executed as the main script
if __name__ == '__main__':
    unittest.main()
