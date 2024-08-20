import unittest
import pandas as pd
from data import load_data, calculate_statistics, filter_data

class TestDataFunctions(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        data = {
            'column_name': [10, 20, 30, 40, 50],
            'other_column': [5, 15, 25, 35, 45]
        }
        self.df = pd.DataFrame(data)

    def test_load_data(self):
        # Ensure that the load_data function works
        df = load_data('sample_data.csv')
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_statistics(self):
        # Ensure that calculate_statistics returns the correct results
        stats = calculate_statistics(self.df)
        self.assertIn('mean', stats.columns)

    def test_filter_data(self):
        # Ensure that filter_data filters data correctly
        filtered_df = filter_data(self.df, 'column_name', 30)
        self.assertEqual(len(filtered_df), 2)

if __name__ == '__main__':
    unittest.main()
