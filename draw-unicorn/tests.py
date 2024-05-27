import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestDrawUnicorn(unittest.TestCase):
    @patch('builtins.input', side_effect=["  /\\", " //\\\\", "||**||", "  \\/", "END"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_draw_unicorn(self, mock_stdout, mock_input):
        main.draw_unicorn()
        output = mock_stdout.getvalue()
        expected_output = (
            "Welcome to the Draw Unicorn game!\n"
            "Draw a unicorn using ASCII art.\n"
            "When you're done, type 'END' on a new line to finish.\n"
            "  /\\\n"
            " //\\\\\n"
            "||**||\n"
            "  \\/\n"
            "\nHere is your unicorn drawing:\n"
            "  /\\\n"
            " //\\\\\n"
            "||**||\n"
            "  \\/\n"
        )
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
