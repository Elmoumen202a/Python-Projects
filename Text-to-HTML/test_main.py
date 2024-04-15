import unittest
from main import text_to_html

class TestTextToHTML(unittest.TestCase):
    def test_basic_conversion(self):
        text = "This is a test"
        expected_html = "<p>This is a test</p>"
        self.assertEqual(text_to_html(text), expected_html)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()