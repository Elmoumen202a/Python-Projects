import unittest
from main import love_calculator

class TestLoveCalculator(unittest.TestCase):
    """
    Unit test class for the love_calculator function.
    """
    
    def test_love_calculator(self):
        """
        Test the love_calculator function with various cases.
        """
        # Check if the result is an integer
        self.assertIsInstance(love_calculator("Alice", "Bob"), int)
        # Check if the result is within the expected range
        self.assertTrue(0 <= love_calculator("Alice", "Bob") <= 100)
        # Check if the same names always return the same result
        self.assertEqual(love_calculator("Alice", "Alice"), love_calculator("Alice", "Alice"))
        # Check if reversing the names changes the result
        self.assertNotEqual(love_calculator("Alice", "Bob"), love_calculator("Bob", "Alice"))

if __name__ == "__main__":
    unittest.main()
