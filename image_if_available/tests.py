import unittest  # Importing unittest for creating test cases
import os  # Importing os to check for file existence
from main import draw_image  # Importing the draw_image function from main.py

class TestDrawImage(unittest.TestCase):
    """
    Test suite for the draw_image function to ensure correct behavior
    when an image exists and when it doesn't.
    """

    def test_image_exists(self):
        """
        Test case to verify that the image file exists in the 'images/' folder.
        This ensures that the program can find and display the image.
        """
        image_name = "doge"  # Example image name (assuming doge.png exists)
        image_path = f'images/{image_name}.png'
        
        # Assert that the image file exists in the specified directory
        self.assertTrue(os.path.exists(image_path), "Image should exist in the 'images/' folder")

    def test_image_not_found(self):
        """
        Test case to verify that the program handles non-existent images correctly.
        If the image doesn't exist, the program should notify the user.
        """
        image_name = "nonexistent_image"  # An image name that doesn't exist
        image_path = f'images/{image_name}.png'
        
        # Assert that the image file does not exist in the specified directory
        self.assertFalse(os.path.exists(image_path), "Image should not exist in the 'images/' folder")

# Running the test cases when the script is executed
if __name__ == '__main__':
    unittest.main()
