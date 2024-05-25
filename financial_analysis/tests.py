import unittest
import pandas as pd
from main import read_data, preprocess_data, calculate_summary_statistics, categorize_expenses

class TestFinancialAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = pd.DataFrame({
            'Date': pd.to_datetime(['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15']),
            'Category': ['Groceries', 'Rent', 'Utilities', 'Entertainment'],
            'Amount': [-50, -500, -150, -100],
            'Description': ['Grocery shopping', 'Monthly rent', 'Electricity bill', 'Movie night']
        })
        cls.data.to_csv('test_transactions.csv', index=False)

    def test_read_data(self):
        data = read_data('test_transactions.csv')
        self.assertEqual(len(data), 4)

    def test_preprocess_data(self):
        data = preprocess_data(self.data.copy())
        self.assertIn('Month', data.columns)

    def test_calculate_summary_statistics(self):
        data = preprocess_data(self.data.copy())
        total_income, total_expenses, avg_monthly_expenses = calculate_summary_statistics(data)
        self.assertEqual(total_income, 0)
        self.assertEqual(total_expenses, -800)
        self.assertAlmostEqual(avg_monthly_expenses, -400, delta=1e-2)

    def test_categorize_expenses(self):
        data = preprocess_data(self.data.copy())
        category_totals = categorize_expenses(data)
        self.assertEqual(category_totals['Groceries'], -50)
        self.assertEqual(category_totals['Rent'], -500)
        self.assertEqual(category_totals['Utilities'], -150)
        self.assertEqual(category_totals['Entertainment'], -100)

if __name__ == '__main__':
    unittest.main()
