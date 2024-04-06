# Import unittest module to create test cases
import unittest
# Import ContactsList class from main module
from main import ContactsList

# Define a test class to test ContactsList class
class TestContactsList(unittest.TestCase):
    # Set up initial contacts for testing
    def setUp(self):
        self.contacts_list = ContactsList()
        self.contacts_list.add_contact("Alice", "123456")
        self.contacts_list.add_contact("Bob", "789012")

    # Test case to verify adding a contact
    def test_add_contact(self):
        self.contacts_list.add_contact("Charlie", "345678")
        self.assertEqual(self.contacts_list.contacts["Charlie"], "345678")

    # Test case to verify deleting a contact
    def test_delete_contact(self):
        self.contacts_list.delete_contact("Alice")
        self.assertNotIn("Alice", self.contacts_list.contacts)

    # Test case to verify searching for a contact
    def test_search_contact(self):
        result = self.contacts_list.search_contact("Bob")
        self.assertEqual(result, "Name: Bob, Number: 789012")

    # Test case to verify displaying all contacts
    def test_display_all_contacts(self):
        self.contacts_list.display_all_contacts()

if __name__ == '__main__':
    unittest.main()
