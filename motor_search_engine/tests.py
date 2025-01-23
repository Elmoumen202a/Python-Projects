import unittest
from main import search_motor

class TestMotorSearch(unittest.TestCase):
    def test_search_exact_match(self):
        result = search_motor("Tesla Model S")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], "Tesla Model S")

    def test_search_partial_match(self):
        result = search_motor("motorcycle")
        self.assertEqual(len(result), 3)  # There are 3 motorcycles in the database

    def test_search_no_match(self):
        result = search_motor("Spaceship")
        self.assertEqual(len(result), 0)

    def test_search_case_insensitive(self):
        result = search_motor("tesla")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], "Tesla Model S")

if __name__ == "__main__":
    unittest.main()
