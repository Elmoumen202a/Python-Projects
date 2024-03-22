import unittest
from unittest.mock import patch
from io import StringIO
from icebreaker import *

class TestIcebreakerActivities(unittest.TestCase):

    @patch('builtins.input', side_effect=["John", "Software Engineer", "I love hiking"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_introduce_yourself(self, mock_stdout, mock_input):
        introduce_yourself()
        self.assertEqual(mock_stdout.getvalue(), "Hello, I'm John, I work as a Software Engineer, and here's an interesting fact about me: I love hiking\n")

    @patch('builtins.input', side_effect=["I love coffee", "I have a pet cat", "I can speak five languages"])
    @patch('builtins.print')
    def test_two_truths_and_a_lie(self, mock_print, mock_input):
        two_truths_and_a_lie()
        mock_print.assert_called_with("Now let others guess which one is the lie!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_virtual_scavenger_hunt(self, mock_stdout):
        virtual_scavenger_hunt()
        self.assertEqual(mock_stdout.getvalue(), "It's time for a virtual scavenger hunt!\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_storytelling_time(self, mock_stdout):
        storytelling_time()
        self.assertEqual(mock_stdout.getvalue(), "It's storytelling time!\n")

if __name__ == '__main__':
    unittest.main()
