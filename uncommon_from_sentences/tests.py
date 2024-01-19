# Import the unittest module to create test cases
import unittest

# Import the uncommonFromSentences function from your module
from uncommonFromSentences import uncommonfromSentences

# Create a test class that inherits from unittest.TestCase
class TestUncommonWords(unittest.TestCase):

    # Define a test method to check the uncommonFromSentences function
    def test_uncommon_from_sentences(self):
        # Test case 1: Check if uncommon words are correctly identified
        self.assertEqual(uncommonfromSentences("this code is cool", "this code is Python"), ['cool', 'Python'])
        
        # Test case 2: Check if uncommon words are correctly identified in another example
        self.assertEqual(uncommonfromSentences("example of another code", "example of Python code"), ['another', 'Python'])

# Run the tests if the script is executed as the main module
if __name__ == '__main__':
    unittest.main()
