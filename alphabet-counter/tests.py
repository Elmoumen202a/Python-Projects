import unittest
from main import count_alphabets

class TestCountAlphabets(unittest.TestCase):
    def test_count_alphabets(self):
        # Test with a simple sentence
        result = count_alphabets("Hello, World!")
        self.assertEqual(result['h'], 1)
        self.assertEqual(result['e'], 1)
        self.assertEqual(result['l'], 3)
        self.assertEqual(result['o'], 2)
        self.assertEqual(result['w'], 1)
        self.assertEqual(result['r'], 1)
        self.assertEqual(result['d'], 1)

        # Test with numbers and special characters
        result = count_alphabets("123abc!@#")
        self.assertEqual(result['a'], 1)
        self.assertEqual(result['b'], 1)
        self.assertEqual(result['c'], 1)

if __name__ == '__main__':
    unittest.main()
