# tests.py
import unittest
from numbers_to_words import convert_to_words

class TestNumbersToWordsConversion(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(convert_to_words(123), 'One Hundred Twenty Three')
        self.assertEqual(convert_to_words(56789), 'Fifty Six Thousand Seven Hundred Eighty Nine')
        self.assertEqual(convert_to_words(123456789), 'One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine')
        # Add more positive test cases

    def test_zero(self):
        self.assertEqual(convert_to_words(0), 'Zero')

    def test_negative_numbers(self):
        # Additional feature: Handling negative numbers
        self.assertEqual(convert_to_words(-123), 'Negative One Hundred Twenty Three')

    def test_large_numbers(self):
        # Additional feature: Handling large numbers
        self.assertEqual(convert_to_words(987654321987), 'Nine Hundred Eighty Seven Billion Six Hundred Fifty Four Million Three Hundred Twenty One Thousand Nine Hundred Eighty Seven')

if __name__ == '__main__':
    unittest.main()
