# Import  a library for file handling and data storage
import json

# Function to load expenses from a file
def load_expenses(filename="expenses.json"):
    """
    Load expenses from a JSON file.
    If the file does not exist, return an empty list.
    """
    try:
        with open(filename, "r") as file:  # Open the file in read mode
            return json.load(file)  # Load and return the content of the file as a list
    except FileNotFoundError:
        return []  # If the file is not found, return an empty list

# Function to save expenses to a file
def save_expenses(expenses, filename="expenses.json"):
    """
    Save the list of expenses to a JSON file.
    Overwrites the file with updated data.
    """
    with open(filename, "w") as file:  # Open the file in write mode
        json.dump(expenses, file, indent=4)  # Save expenses in a human-readable format

# Function to add an expense
def add_expense(expenses, category, amount, description=""):
    """
    Add a new expense to the list.
    Arguments:
        expenses (list): List of current expenses
        category (str): The category of the expense
        amount (float): The amount of the expense
        description (str): An optional description of the expense
    """
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)  # Add the expense to the list
    print(f"Expense added: {expense}")  # Confirm the addition

# Function to view all expenses
def view_expenses(expenses):
    """
    Display all expenses in a readable format.
    If there are no expenses, inform the user.
    """
    if not expenses:  # Check if the list is empty
        print("No expenses to display.")
        return

    print("\nYour Expenses:")  # Display header
    for idx, expense in enumerate(expenses, start=1):  # Loop through each expense with an index
        # Print expense details in a formatted manner
        print(f"{idx}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

# Function to calculate total expenses
def calculate_total(expenses):
    """
    Calculate and display the total amount of all expenses.
    """
    # Sum up the 'amount' field of all expenses in the list
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: {total}")  # Display the total amount

# Main program loop
def main():
    """
    Main function to run the expense tracker application.
    Allows the user to add, view, and calculate expenses.
    """
    expenses = load_expenses()  # Load existing expenses from the file
    while True:
        # Display the main menu options
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("Choose an option: ")
        if choice == "1":  # Add expense option
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            add_expense(expenses, category, amount, description)  # Add the expense
            save_expenses(expenses)  # Save updated expenses to the file
        elif choice == "2":  # View expenses option
            view_expenses(expenses)  # Display all expenses
        elif choice == "3":  # Calculate total expenses option
            calculate_total(expenses)  # Calculate and display the total amount
        elif choice == "4":  # Exit the application
            print("Goodbye!")
            break  # Exit the while loop
        else:  # Invalid choice handling
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
