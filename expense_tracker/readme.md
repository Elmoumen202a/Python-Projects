
# Expense Tracker

## Overview
The Expense Tracker is a Python application that helps you manage and track your expenses. 
It allows you to add, view, and calculate total expenses, with data stored in a JSON file for persistence.

## Features
- **Add Expense**: Add an expense with category, amount, and an optional description.
- **View Expenses**: View all recorded expenses in a clean, readable format.
- **Calculate Total**: Calculate the total sum of all your expenses.
- **Persistent Storage**: Data is saved in a JSON file (`expenses.json`) for future use.

## How to Run
1. Ensure Python is installed on your system.
2. Save the `main.py` file and place it in the same directory as this README.
3. Run the program using the command:
   ```bash
   python main.py
   ```

## Files Included
- **main.py**: The core script that contains the application's logic.
- **tests.py**: Contains unit tests to ensure the application's correctness.
- **README.md**: This file, explaining the project's structure and functionality.

## Requirements
No additional Python packages are required. The application uses built-in Python libraries:
- `json` for data storage.

## Example Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Choose an option from the menu:
   ```
   Expense Tracker
   1. Add Expense
   2. View Expenses
   3. Calculate Total
   4. Exit
   ```
3. Follow the prompts to add expenses, view them, or calculate the total.

## Sample Output
### Adding an Expense:
```
Enter category: Food
Enter amount: 15.50
Enter description (optional): Lunch
Expense added: {'category': 'Food', 'amount': 15.5, 'description': 'Lunch'}
```

### Viewing Expenses:
```
Your Expenses:
1. Category: Food, Amount: 15.5, Description: Lunch
2. Category: Transport, Amount: 10.0, Description: Bus fare
```

### Calculating Total:
```
Total Expenses: 25.5
```

## Future Improvements
- Add functionality to edit or delete expenses.
- Categorize expenses by date or month.
- Generate visual reports for expense analysis.

## Testing
Run `tests.py` to verify the functionality of the application:
```bash
python tests.py
```

## 
happy coding :alien:

