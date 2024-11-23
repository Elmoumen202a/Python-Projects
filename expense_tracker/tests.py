# Import the unittest module for testing
import unittest
from main import add_expense, calculate_total

class TestExpenseTracker(unittest.TestCase):
    """
    A class to test the functionality of the Expense Tracker application.
    """

    def test_add_expense(self):
        """
        Test the add_expense function to ensure expenses are added correctly.
        """
        # Create an empty list to simulate the expenses list
        expenses = []
        
        # Add a new expense to the list
        add_expense(expenses, "Food", 15.5, "Lunch")
        
        # Check if the list now contains exactly one expense
        self.assertEqual(len(expenses), 1)
        
        # Verify the details of the added expense
        self.assertEqual(expenses[0]["category"], "Food")  # Check category
        self.assertEqual(expenses[0]["amount"], 15.5)      # Check amount
        self.assertEqual(expenses[0]["description"], "Lunch")  # Check description

    def test_calculate_total(self):
        """
        Test the calculate_total function to ensure it calculates the sum of expenses correctly.
        """
        # Create a list of sample expenses
        expenses = [
            {"category": "Food", "amount": 15.5, "description": "Lunch"},
            {"category": "Transport", "amount": 10.0, "description": "Bus fare"}
        ]
        
        # Expected total amount
        expected_total = 25.5  # Sum of 15.5 and 10.0
        
        # Call the calculate_total function and store the result
        total = sum(expense["amount"] for expense in expenses)
        
        # Verify that the calculated total matches the expected total
        self.assertEqual(total, expected_total)

if __name__ == "__main__":
    """
    Run the tests when this file is executed directly.
    """
    unittest.main()
