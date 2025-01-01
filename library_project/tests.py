import unittest
from main import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
        self.library.add_book("1984", "George Orwell")

    def test_add_book(self):
        self.library.add_book("To Kill a Mockingbird", "Harper Lee")
        self.assertEqual(len(self.library.books), 3)

    def test_remove_book(self):
        self.library.remove_book("1984")
        self.assertEqual(len(self.library.books), 1)

    def test_search_book(self):
        self.library.search_book("The Great Gatsby")
        self.assertEqual(self.library.books[0]["title"], "The Great Gatsby")

    def test_remove_nonexistent_book(self):
        initial_count = len(self.library.books)
        self.library.remove_book("Nonexistent Book")
        self.assertEqual(len(self.library.books), initial_count)

if __name__ == "__main__":
    unittest.main()
