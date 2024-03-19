import unittest
from telephone_book import TelephoneBook

class TestTelephoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = TelephoneBook()
        self.phone_book.add_entry("John", "1234567890")
        self.phone_book.add_entry("Alice", "9876543210")

    def test_lookup_number(self):
        self.assertEqual(self.phone_book.lookup_number("John"), "1234567890")

    def test_lookup_name(self):
        self.assertEqual(self.phone_book.lookup_name("9876543210"), "Alice")

    def test_nonexistent_number(self):
        self.assertEqual(self.phone_book.lookup_number("Bob"), "Number not found")

    def test_nonexistent_name(self):
        self.assertEqual(self.phone_book.lookup_name("0000000000"), "Name not found")

if __name__ == "__main__":
    unittest.main()
