import unittest
from main_check import are_files_identical

class TestFileComparison(unittest.TestCase):

    def test_identical_files(self):
        self.assertTrue(are_files_identical("pd1.pdf", "pd1.pdf"))

    def test_different_files(self):
        self.assertFalse(are_files_identical("pd1.pdf", "pd2.pdf"))

if __name__ == "__main__":
    unittest.main()
