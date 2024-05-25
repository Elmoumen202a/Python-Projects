import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def read_data(file_path):
    #Read the transaction data from a CSV file.
    data = pd.read_csv(file_path, parse_dates=['Date'])
    return data

def preprocess_data(data):
    #Preprocess the data for analysis.
    data['Month'] = data['Date'].dt.to_period('M')
    return data

def calculate_summary_statistics(data):
    #Calculate summary statistics from the data.
    total_income = data[data['Amount'] > 0]['Amount'].sum()
    total_expenses = data[data['Amount'] < 0]['Amount'].sum()
    avg_monthly_expenses = data[data['Amount'] < 0].groupby('Month')['Amount'].sum().mean()
    return total_income, total_expenses, avg_monthly_expenses

def categorize_expenses(data):
   #Categorize expenses and calculate totals per category.
    expenses = data[data['Amount'] < 0]
    category_totals = expenses.groupby('Category')['Amount'].sum()
    return category_totals

def plot_expense_distribution(category_totals):
    #Plot the expense distribution by category.
    plt.figure(figsize=(10, 6))
    category_totals.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.ylabel('')
    plt.show()

def plot_expense_trends(data):
    # Plot the expense trends over time
    monthly_expenses = data[data['Amount'] < 0].groupby('Month')['Amount'].sum()
    plt.figure(figsize=(10, 6))
    monthly_expenses.plot(kind='line', marker='o')
    plt.title('Monthly Expense Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Expenses')
    plt.grid(True)
    plt.show()

def main():
    file_path = 'data/transactions.csv'
    data = read_data(file_path)
    data = preprocess_data(data)
    total_income, total_expenses, avg_monthly_expenses = calculate_summary_statistics(data)
    category_totals = categorize_expenses(data)
    
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Average Monthly Expenses: ${avg_monthly_expenses:.2f}")
    
    plot_expense_distribution(category_totals)
    plot_expense_trends(data)

if __name__ == "__main__":
    main()
