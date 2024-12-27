import unittest
from main import find_matching_ausbildung

class TestAusbildungFinder(unittest.TestCase):
    def test_find_matching_ausbildung(self):
        test_data = [
            {"title": "Test Program 1", "language_level": "B1", "field": "IT"},
            {"title": "Test Program 2", "language_level": "B2", "field": "Business"},
        ]
        
        # Mock the data loading function
        def mock_load_ausbildung_data():
            return test_data
        
        # Replace the actual function with the mock
        global load_ausbildung_data
        load_ausbildung_data = mock_load_ausbildung_data
        
        results = find_matching_ausbildung("B1", "IT")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Program 1")

if __name__ == "__main__":
    unittest.main()
