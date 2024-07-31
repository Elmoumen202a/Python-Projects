import unittest
import pandas as pd
from main import load_data, analyze_data, save_data

class TestMain(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        }
        self.df = pd.DataFrame(self.test_data)

    def test_load_data(self):
        df = load_data('data.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_analyze_data(self):
        summary_df = analyze_data(self.df)
        self.assertIn('mean', summary_df.index)
        self.assertIn('50%', summary_df.columns)

    def test_save_data(self):
        save_data(self.df, 'test_output.csv')
        df = pd.read_csv('test_output.csv')
        pd.testing.assert_frame_equal(df, self.df)

if __name__ == '__main__':
    unittest.main()
