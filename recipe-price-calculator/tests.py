import unittest
from ingredients import IngredientManager

class TestIngredientManager(unittest.TestCase):
    def setUp(self):
        # Initialize an IngredientManager object for testing
        self.ingredient_manager = IngredientManager()

    def test_calculate_total_price(self):
        # Define a list of ingredients for testing
        ingredients = ["flour", "sugar", "eggs", "milk"]
        # Define the expected total price
        expected_total_price = 4.7
        # Calculate the total price using the IngredientManager
        total_price = self.ingredient_manager.calculate_total_price(ingredients)
        # Assert that the calculated total price matches the expected total price
        self.assertEqual(total_price, expected_total_price)

if __name__ == '__main__':
    unittest.main()
