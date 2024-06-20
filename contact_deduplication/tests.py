import unittest
from main import read_contacts, remove_duplicates, write_contacts

class TestContactDeduplication(unittest.TestCase):
    
    def setUp(self):
        self.contacts = [
            {'name': 'John Doe', 'contact': '1234567890'},
            {'name': 'Jane Smith', 'contact': '0987654321'},
            {'name': 'John Doe', 'contact': '1234567890'},  # Duplicate
            {'name': 'Alice Brown', 'contact': '1112223333'}
        ]

    def test_remove_duplicates(self):
        unique_contacts = remove_duplicates(self.contacts)
        self.assertEqual(len(unique_contacts), 3)
        self.assertNotIn({'name': 'John Doe', 'contact': '1234567890'}, unique_contacts[1:])

    def test_read_contacts(self):
        # Here you can add a test to read a sample file if needed.
        pass

    def test_write_contacts(self):
        # Here you can add a test to write a sample file if needed.
        pass

if __name__ == '__main__':
    unittest.main()
