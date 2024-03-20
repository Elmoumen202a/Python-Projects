class IngredientManager:
    def __init__(self):
        # Define ingredient prices in a dictionary
        self.ingredient_prices = {
            "flour": 1.5,
            "sugar": 2.0,
            "eggs": 0.2,
            "milk": 1.0,
            # Add more ingredients and their prices as needed
        }

    def calculate_total_price(self, ingredients):
        # Initialize total price
        total_price = 0
        # Iterate over each ingredient in the recipe
        for ingredient in ingredients:
            # Check if the ingredient exists in the ingredient prices dictionary
            if ingredient in self.ingredient_prices:
                # If it exists, add its price to the total price
                total_price += self.ingredient_prices[ingredient]
            else:
                # If the ingredient price is not available, print a warning message
                print(f"Warning: Price for {ingredient} is not available.")
        # Return the total price of the recipe
        return total_price
