import unittest
from main import is_url_valid

class TestURLValidator(unittest.TestCase):
    
    def test_valid_url(self):
        self.assertTrue(is_url_valid("https://www.google.com"))
        
    def test_invalid_url(self):
        self.assertFalse(is_url_valid("https://www.thisurldoesnotexist1234.com"))
        
    def test_malformed_url(self):
        self.assertFalse(is_url_valid("htp://malformed-url"))
        
    def test_empty_url(self):
        self.assertFalse(is_url_valid(""))
        
    def test_no_scheme_url(self):
        self.assertFalse(is_url_valid("www.google.com"))

if __name__ == "__main__":
    unittest.main()
