# Recipe Price Calculator

This Python project calculates the price of ingredients in a recipe and allows the user to put it in a menu. It consists of three main files:

1. `main.py`: Contains the main entry point for the program. It interacts with the user and calls functions from other modules accordingly.
2. `menu.py`: Handles the menu logic and user interaction. It prompts the user for choices and calls appropriate functions.
3. `ingredients.py`: Manages ingredient prices and calculates the total price of a recipe based on the ingredients provided.
4. `tests.py`: Contains unit tests for the functionality in `ingredients.py`.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/Elmoumen202a/Python-Projects
    cd recipe-price-calculator
    ```

2. Run the program:

    ```bash
    python main.py
    ```

3. Follow the prompts to calculate the price of a recipe or exit the program.

## File Descriptions

- `main.py`: 
  - This file serves as the main entry point for the program.
  - It imports `Menu` class from `menu.py` to display the menu and handle user interaction.

- `menu.py`: 
  - Defines the `Menu` class responsible for displaying the menu and interacting with the user.
  - The `Menu` class initializes an `IngredientManager` object from `ingredients.py` to handle ingredient prices.
  - Users can choose to calculate the price of a recipe or exit the program.

- `ingredients.py`:
  - Contains the `IngredientManager` class that manages ingredient prices and calculates the total price of a recipe.
  - Ingredient prices are stored in a dictionary.
  - The `calculate_total_price` method calculates the total price of a recipe based on the provided ingredients.

- `tests.py`:
  - Contains unit tests for the `IngredientManager` class in `ingredients.py`.
  - Tests are written using the `unittest` framework.
  - Tests include checking the correctness of the total price calculation.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
