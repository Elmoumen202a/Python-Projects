# tests.py

import unittest
from main import generate_addition_problem, generate_subtraction_problem, generate_multiplication_problem, generate_division_problem

class TestMathProblems(unittest.TestCase):
    """Test cases for the math problem generators."""

    def test_addition(self):
        num1, num2, result = generate_addition_problem()
        self.assertEqual(num1 + num2, result, "Addition problem failed")

    def test_subtraction(self):
        num1, num2, result = generate_subtraction_problem()
        self.assertEqual(num1 - num2, result, "Subtraction problem failed")

    def test_multiplication(self):
        num1, num2, result = generate_multiplication_problem()
        self.assertEqual(num1 * num2, result, "Multiplication problem failed")

    def test_division(self):
        num1, num2, result = generate_division_problem()
        self.assertAlmostEqual(num1 / num2, result, places=2, msg="Division problem failed")

if __name__ == '__main__':
    unittest.main()
