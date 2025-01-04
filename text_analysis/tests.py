import unittest
from main import analyze_text

class TestTextAnalysis(unittest.TestCase):
    def test_analyze_text(self):
        text = "Das ist ein Beispiel. Es ist einfach zu lesen. Das ist toll!"
        result = analyze_text(text)
        self.assertEqual(result["sentence_count"], 3)
        self.assertEqual(result["word_count"], 10)
        self.assertIn(("das", 2), result["common_words"])
        self.assertIn(("ist", 2), result["common_words"])

    def test_empty_text(self):
        text = ""
        result = analyze_text(text)
        self.assertEqual(result["sentence_count"], 0)
        self.assertEqual(result["word_count"], 0)
        self.assertEqual(result["common_words"], [])

if __name__ == "__main__":
    unittest.main()
