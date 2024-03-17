import unittest
from birthday import calculate_age

class TestCalculateAge(unittest.TestCase):

    def test_calculate_age(self):
        self.assertEqual(calculate_age('1990-01-01'), 34)  # Assuming the current date is 2024-01-01
        self.assertEqual(calculate_age('2000-05-20'), 23)  # Assuming the current date is 2024-06-01
        self.assertEqual(calculate_age('2015-12-31'), 8)   # Assuming the current date is 2024-01-01

if __name__ == '__main__':
    unittest.main()
