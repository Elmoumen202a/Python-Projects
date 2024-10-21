import unittest  # Import the unittest module for testing
from main import translate_to_german, generate_audio  # Import the functions to test
import os  # Used to check if the audio file is created

class TestTranslation(unittest.TestCase):

    def test_translation(self):
        """Test if the translation of English words to German works correctly."""
        self.assertEqual(translate_to_german("apple"), "Apfel")  # Check if 'apple' translates to 'Apfel'
        self.assertEqual(translate_to_german("cat"), "Katze")  # Check if 'cat' translates to 'Katze'

    def test_generate_audio(self):
        """Test if the audio file is generated successfully."""
        german_text = "Apfel"  # Sample German word
        filename = generate_audio(german_text, "test_output.mp3")  # Generate an audio file
        self.assertTrue(os.path.exists(filename))  # Check if the file was created
        os.remove(filename)  # Remove the file after testing to clean up

if __name__ == '__main__':
    unittest.main()  # Run the tests
