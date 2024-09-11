# main.py

import random

def generate_addition_problem():
    """Generate a random addition problem."""
    num1 = random.randint(1, 100)  # Generate a random number between 1 and 100
    num2 = random.randint(1, 100)  # Generate another random number between 1 and 100
    return num1, num2, num1 + num2  # Return the numbers and their sum

def generate_subtraction_problem():
    """Generate a random subtraction problem."""
    num1 = random.randint(1, 100)  # Generate a random number between 1 and 100
    num2 = random.randint(1, num1)  # Generate another random number that is less than or equal to num1
    return num1, num2, num1 - num2  # Return the numbers and their difference

def generate_multiplication_problem():
    """Generate a random multiplication problem."""
    num1 = random.randint(1, 10)  # Generate a random number between 1 and 10
    num2 = random.randint(1, 10)  # Generate another random number between 1 and 10
    return num1, num2, num1 * num2  # Return the numbers and their product

def generate_division_problem():
    """Generate a random division problem."""
    num1 = random.randint(1, 100)  # Generate a random number between 1 and 100
    num2 = random.randint(1, 10)   # Generate another random number between 1 and 10
    return num1, num2, num1 / num2  # Return the numbers and their quotient
