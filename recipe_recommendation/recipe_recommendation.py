import random
from datetime import datetime

class RecipeRecommendation:
    def __init__(self):
        self.recipes = {
            "Spaghetti Carbonara": [
                "Boil water in a large pot.",
                "Cook spaghetti according to package instructions.",
                "In a separate pan, fry pancetta until crispy.",
                "In a bowl, mix eggs, Parmesan cheese, and black pepper.",
                "Drain spaghetti and add it to the pan with pancetta.",
                "Pour the egg mixture over the spaghetti and toss until coated.",
                "Serve immediately with additional Parmesan cheese and black pepper."
            ],
            "Chicken Tikka Masala": [
                "Marinate chicken in yogurt, lemon juice, and spices for at least 1 hour.",
                "Grill or bake chicken until cooked through.",
                "In a pan, sauté onions, garlic, and ginger until softened.",
                "Add tomato sauce, cream, and spices to the pan.",
                "Simmer sauce until thickened.",
                "Add cooked chicken to the sauce and simmer for a few more minutes.",
                "Serve hot with rice or naan bread."
            ],
            
        }

    def get_recipe_of_the_day(self):
        # Get today's date
        today = datetime.now().date()

        # Use the date to generate a random index
        random.seed(today.year + today.month + today.day)
        index = random.randint(0, len(self.recipes) - 1)

        return list(self.recipes.keys())[index], self.recipes[list(self.recipes.keys())[index]]

if __name__ == "__main__":
    recommendation = RecipeRecommendation()
    recipe_name, recipe_steps = recommendation.get_recipe_of_the_day()
    print("Today's recommended recipe is:", recipe_name)
    print("Steps to prepare:")
    for step_num, step in enumerate(recipe_steps, start=1):
        print(f"{step_num}. {step}")
