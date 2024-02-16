import unittest
from checker import check_url

class TestWebsiteConnectivity(unittest.TestCase):
    def test_valid_url(self):
        result, _ = check_url("https://www.google.com", None)  # The second argument is not used for this test
        self.assertTrue(result)

    def test_invalid_url(self):
        result, _ = check_url("https://www.invalidwebsite123456789.com", None)  # The second argument is not used for this test
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
