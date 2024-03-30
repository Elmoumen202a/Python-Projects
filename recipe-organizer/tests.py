import unittest
from main import *

class TestRecipeOrganizer(unittest.TestCase):
    def test_load_recipes(self):
        recipes = load_recipes()
        self.assertIsInstance(recipes, list)

    def test_save_recipes(self):
        recipes = [{"name": "Test Recipe", "ingredients": ["Ingredient1", "Ingredient2"], 
                    "instructions": "Test instructions", "category": "Test category"}]
        save_recipes(recipes)
        loaded_recipes = load_recipes()
        self.assertEqual(loaded_recipes, recipes)

    # Add more tests for other functions as needed

if __name__ == "__main__":
    unittest.main()
