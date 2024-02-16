import unittest
from checker import check_url

class TestWebsiteConnectivity(unittest.TestCase):
    def test_valid_url(self):
        self.assertTrue(check_url("https://www.google.com"))

    def test_invalid_url(self):
        self.assertFalse(check_url("https://www.invalidwebsite123456789.com"))

if __name__ == '__main__':
    unittest.main()
