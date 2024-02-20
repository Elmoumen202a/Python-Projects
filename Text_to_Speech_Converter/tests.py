import unittest
from text_to_speech import text_to_speech

class TestTextToSpeech(unittest.TestCase):

    def test_valid_url(self):
        # Test with a valid URL
        url = 'https://hackr.io/blog/top-tech-companies-hiring-python-developers'
        self.assertIsNone(text_to_speech(url))

    def test_invalid_url(self):
        # Test with an invalid URL
        url = 'invalid_url'
        with self.assertRaises(Exception):
            text_to_speech(url)

if __name__ == '__main__':
    unittest.main()
