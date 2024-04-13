import unittest
from main import URLShortener

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        # Create an instance of URLShortener for each test case
        self.shortener = URLShortener()

    def test_shorten_url(self):
        # Test whether the shorten_url method generates a shortened URL
        original_url = "https://www.example.com"
        short_url = self.shortener.shorten_url(original_url)
        # Assert that the length of the generated short URL is 8 characters
        self.assertEqual(len(short_url), 8)

    def test_get_original_url(self):
        # Test whether the get_original_url method retrieves the original URL
        original_url = "https://www.example.com"
        short_url = self.shortener.shorten_url(original_url)
        retrieved_url = self.shortener.get_original_url(short_url)
        # Assert that the retrieved URL matches the original URL
        self.assertEqual(original_url, retrieved_url)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
