# Math Exercises

This project provides simple Python functions to generate random math problems and verify their correctness using unit tests.

## Files

- **`main.py`**: Contains functions to generate random addition, subtraction, multiplication, and division problems.
- **`tests.py`**: Includes unit tests to validate the functions in `main.py`.
- **`readme.md`**: This file.

## Usage

1. **Run the program**:
   - To generate math problems, you can call the functions in `main.py` and use them as needed.

2. **Run the tests**:
   - To ensure everything is working correctly, run the tests with the command:
     ```bash
     python -m unittest tests.py
     ```

## Functions

- **`generate_addition_problem()`**: Returns a tuple of two random numbers and their sum.
- **`generate_subtraction_problem()`**: Returns a tuple of two random numbers (where the second is less than or equal to the first) and their difference.
- **`generate_multiplication_problem()`**: Returns a tuple of two random numbers (between 1 and 10) and their product.
- **`generate_division_problem()`**: Returns a tuple of two random numbers and their quotient. The second number is between 1 and 10.

Feel free to expand the project with more complex problems and features.
