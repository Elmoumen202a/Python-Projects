import unittest
from main import count_words, common_words

class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        text = "Hello world, hello Python"
        expected = {'hello': 2, 'world,': 1, 'python': 1}
        self.assertEqual(count_words(text), expected)

    def test_common_words(self):
        text = "Hello world, hello Python"
        expected = [('hello', 2), ('world,', 1), ('python', 1)]
        self.assertEqual(common_words(text), expected)
        
if __name__ == "__main__":
    unittest.main()
