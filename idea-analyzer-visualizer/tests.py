import unittest
from main import analyze_idea

# Test class for the Idea Analyzer
class TestIdeaAnalyzer(unittest.TestCase):
    # Test case for the analyze_idea function
    def test_analyze_idea(self):
        """
        Test if the analyze_idea function correctly extracts keywords.
        """
        input_idea = "Python is great for data analysis and visualization."
        # Expected output: dictionary of words and their frequencies
        expected_output = {
            "python": 1,
            "is": 1,
            "great": 1,
            "for": 1,
            "data": 1,
            "analysis": 1,
            "and": 1,
            "visualization.": 1,
        }
        # Assert that the function output matches the expected output
        self.assertEqual(analyze_idea(input_idea), expected_output)

# Run the tests
if __name__ == "__main__":
    unittest.main()
