import unittest
from recipe_recommendation import RecipeRecommendation

class TestRecipeRecommendation(unittest.TestCase):
    def setUp(self):
        self.recommendation = RecipeRecommendation()

    def test_get_recipe_of_the_day(self):
        # Ensure that the recommended recipe is in the list of recipes
        recommended_recipe = self.recommendation.get_recipe_of_the_day()
        self.assertIn(recommended_recipe, self.recommendation.recipes)

if __name__ == "__main__":
    unittest.main()
