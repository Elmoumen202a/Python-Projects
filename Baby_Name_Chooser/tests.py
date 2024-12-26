import unittest
from main import suggest_name

class TestBabyNameChooser(unittest.TestCase):
    def test_high_points(self):
        result = suggest_name("high", "blue", "classic")
        self.assertIn(result, ["Alexander", "Sophia", "Sky", "Azure", "William", "Elizabeth"])

    def test_invalid_input(self):
        result = suggest_name("invalid", "yellow", "unknown")
        self.assertEqual(result, "No suggestions available.")

    def test_combined_input(self):
        result = suggest_name("medium", "green", "modern")
        self.assertIn(result, ["Mia", "Liam", "Jade", "Forest", "Zayn", "Nova"])

if __name__ == "__main__":
    unittest.main()
