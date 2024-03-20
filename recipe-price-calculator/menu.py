from ingredients import IngredientManager

class Menu:
    def __init__(self):
        # Initialize an IngredientManager object to manage ingredient prices
        self.ingredient_manager = IngredientManager()

    def display_menu(self):
        # Display menu options
        print("Menu:")
        print("1. Calculate Price of Recipe")
        print("2. Exit")
        # Prompt user for choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # If choice is 1, calculate the price of a recipe
            self.calculate_recipe_price()
        elif choice == '2':
            # If choice is 2, exit the program
            print("Exiting...")
        else:
            # If choice is invalid, print a message
            print("Invalid choice.")

    def calculate_recipe_price(self):
        # Prompt user to enter a recipe 
        recipe = input("Enter recipe (comma-separated list of ingredients): ")
        # Split the recipe into a list of ingredients
        ingredients = [ingredient.strip() for ingredient in recipe.split(',')]
        # Calculate the total price of the recipe using the IngredientManager
        total_price = self.ingredient_manager.calculate_total_price(ingredients)
        # Display the total price of the recipe
        print(f"Total price for the recipe: ${total_price:.2f}")
