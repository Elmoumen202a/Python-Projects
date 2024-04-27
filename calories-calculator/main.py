class CaloriesCalculator:
    def __init__(self):
        # Initialize total calories to 0
        self.total_calories = 0

    def add_food(self, food_name, calories):
        # Add calories of the food to the total
        self.total_calories += calories
        # Print a message confirming the addition
        print(f"Added {food_name} with {calories} calories.")

    def get_total_calories(self):
        # Return the total calories consumed
        return self.total_calories

if __name__ == "__main__":
    # Create an instance of CaloriesCalculator
    calculator = CaloriesCalculator()

    # Continuously prompt the user to input food and calories until 'q' is entered
    while True:
        food_name = input("Enter the name of the food (or 'q' to quit): ")
        if food_name.lower() == 'q':
            break
        calories = float(input("Enter the calories for this food: "))
        calculator.add_food(food_name, calories)

    # Display the total calories consumed
    print(f"Total calories consumed today: {calculator.get_total_calories()}")
