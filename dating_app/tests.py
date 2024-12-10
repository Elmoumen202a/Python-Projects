# tests.py

import unittest
from main import DatingApp

class TestDatingApp(unittest.TestCase):

    def setUp(self):
        """
        Create a fresh instance of the DatingApp for each test.
        """
        self.app = DatingApp()
        self.app.add_user("TestUser1", "Test Bio 1")
        self.app.add_user("TestUser2", "Test Bio 2")

    def test_add_user(self):
        """
        Test adding a user.
        """
        self.app.add_user("NewUser", "New Bio")
        self.assertIn("NewUser", [user["username"] for user in self.app.users])

    def test_match_users(self):
        """
        Test matching two users.
        """
        self.app.match_users("TestUser1", "TestUser2")
        self.assertIn("TestUser2", self.app.matches["TestUser1"])
        self.assertIn("TestUser1", self.app.matches["TestUser2"])

    def test_send_message(self):
        """
        Test sending a message between matched and unmatched users.
        """
        self.app.match_users("TestUser1", "TestUser2")
        self.assertIsNone(self.app.send_message("TestUser1", "TestUser2", "Hello!"))
        self.assertIsNone(self.app.send_message("TestUser1", "UnmatchedUser", "Hello!"))

if __name__ == "__main__":
    unittest.main()
