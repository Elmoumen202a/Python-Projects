import unittest
from main import CaloriesCalculator

class TestCaloriesCalculator(unittest.TestCase):
    def setUp(self):
        # Create an instance of CaloriesCalculator before each test
        self.calculator = CaloriesCalculator()

    def test_add_food(self):
        # Test adding food and checking if total calories are updated correctly
        self.calculator.add_food("Apple", 52)
        self.assertEqual(self.calculator.get_total_calories(), 52)

        self.calculator.add_food("Banana", 105)
        self.assertEqual(self.calculator.get_total_calories(), 157)

if __name__ == "__main__":
    # Run tests if the script is executed directly
    unittest.main()
