import unittest
from main import detect_language

class TestLanguageDetection(unittest.TestCase):

    def test_english_text(self):
        text = "This is an example text in English."
        self.assertEqual(detect_language(text), "en")

    def test_spanish_text(self):
        text = "Este es un texto de ejemplo en español."
        self.assertEqual(detect_language(text), "es")

    def test_french_text(self):
        text = "Ceci est un exemple de texte en français."
        self.assertEqual(detect_language(text), "fr")

    def test_invalid_text(self):
        text = ""
        self.assertEqual(detect_language(text), "Unknown")

if __name__ == "__main__":
    unittest.main()
