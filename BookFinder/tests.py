import unittest
from main import find_books_by_title

class TestBookFinder(unittest.TestCase):
    def test_find_books_by_title_valid(self):
        """
        Test searching for a book with a valid title.
        """
        books = find_books_by_title("Pride and Prejudice")
        self.assertIsInstance(books, list)
        self.assertGreater(len(books), 0)

    def test_find_books_by_title_invalid(self):
        """
        Test searching for a book with an invalid or non-existent title.
        """
        books = find_books_by_title("asdfghjklqwerty")
        self.assertIsInstance(books, list)
        self.assertEqual(len(books), 0)

    def test_find_books_by_title_empty(self):
        """
        Test searching with an empty string.
        """
        books = find_books_by_title("")
        self.assertIsInstance(books, list)
        self.assertEqual(len(books), 0)

if __name__ == "__main__":
    unittest.main()
