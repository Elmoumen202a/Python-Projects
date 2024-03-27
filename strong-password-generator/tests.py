import unittest
from main import generate_password

class TestPasswordGeneration(unittest.TestCase):
    def test_password_length(self):
        self.assertEqual(len(generate_password()), 12)

    def test_password_strength(self):
        password = generate_password()
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()_+=" for c in password))

if __name__ == '__main__':
    unittest.main()
