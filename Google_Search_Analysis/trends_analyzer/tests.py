import unittest
from main_analyze import analyze_trends
import pandas as pd

class TestTrendsAnalyzer(unittest.TestCase):
    def test_analyze_trends(self):
        # Ensure the analyze_trends function returns a DataFrame
        result = analyze_trends()
        self.assertIsInstance(result, pd.DataFrame)

        # Ensure the DataFrame has the expected columns
        expected_columns = ["Machine Learning"]
        self.assertListEqual(list(result.columns), expected_columns)

        # Ensure the DataFrame has 10 rows
        expected_rows = 10
        self.assertEqual(len(result), expected_rows)

        # Add more test cases based on your specific requirements

if __name__ == '__main__':
    unittest.main()
