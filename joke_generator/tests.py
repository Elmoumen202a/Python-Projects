
import unittest  
from main import fetch_joke  

class TestJokeGenerator(unittest.TestCase):
    """Test suite for the Joke Generator project."""

    def test_fetch_joke(self):
        """Test if the joke fetching function returns a string and is not empty."""
        joke = fetch_joke()  # Call the function to fetch a joke
        self.assertIsInstance(joke, str)  # Check if the result is a string
        self.assertTrue(len(joke) > 0)  # Ensure the joke is not empty

# Run the tests if this file is executed
if __name__ == "__main__":
    unittest.main()
