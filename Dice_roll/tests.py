import unittest
from unittest.mock import patch
from DiceRollGenerator import num_dice, roll_dice

class TestDiceRollGenerator(unittest.TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_num_dice_valid_input(self, mock_input):
        result = num_dice()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['3', '2'])
    def test_num_dice_invalid_then_valid_input(self, mock_input):
        result = num_dice()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['1'])
    def test_roll_dice_single_die(self, mock_input):
        with patch('builtins.print') as mock_print:
            roll_dice(1)
            mock_print.assert_called_with('The value is: ')

    @patch('builtins.input', side_effect=['2'])
    def test_roll_dice_double_dice(self, mock_input):
        with patch('builtins.print') as mock_print:
            roll_dice(2)
            mock_print.assert_any_call('Dice One:')
            mock_print.assert_any_call('Dice Two:')
            mock_print.assert_any_call('Total:')

if __name__ == '__main__':
    unittest.main()
