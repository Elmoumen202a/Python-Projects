import unittest
from main import count_words, estimate_pages

class TestCalculusWordCounter(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("This is a test"), 4)
        self.assertEqual(count_words("This is another test"), 4)
        self.assertEqual(count_words(""), 0)

    def test_estimate_pages(self):
        self.assertEqual(estimate_pages(1000), 4)
        self.assertEqual(estimate_pages(500), 2)
        self.assertEqual(estimate_pages(250), 1)
        self.assertEqual(estimate_pages(251), 1.004)

if __name__ == '__main__':
    unittest.main()
