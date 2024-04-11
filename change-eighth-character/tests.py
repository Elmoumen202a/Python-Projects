import unittest
from main import change_eighth_char

class TestChangeEighthChar(unittest.TestCase):
    def test_change_eighth_char(self):
        # Create a test file with initial content
        filename = "test_file.txt"
        with open(filename, "w") as file:
            file.write("12345678")
        
        # Call the function to change the eighth character
        change_eighth_char(filename, "X")

        # Check if the content of the file has been modified as expected
        with open(filename, "r") as file:
            content = file.read()
        
        self.assertEqual(content, "123456X8")

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
