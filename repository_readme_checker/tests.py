import os
import unittest
from main import check_and_create_readme

class TestReadmeCreation(unittest.TestCase):

    def setUp(self):
        # Set up a test directory
        self.test_dir = "test_repo"
        os.mkdir(self.test_dir)
        self.readme_path = os.path.join(self.test_dir, 'readme.md')

    def tearDown(self):
        # Clean up by removing the test directory and files
        if os.path.exists(self.readme_path):
            os.remove(self.readme_path)
        os.rmdir(self.test_dir)

    def test_readme_creation(self):
        # Ensure readme.md is created if it doesn't exist
        check_and_create_readme(self.test_dir)
        self.assertTrue(os.path.exists(self.readme_path))

    def test_readme_already_exists(self):
        # Ensure no overwrite if readme.md exists
        with open(self.readme_path, 'w') as f:
            f.write("Existing readme content")
        
        check_and_create_readme(self.test_dir)
        
        with open(self.readme_path, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, "Existing readme content")

if __name__ == '__main__':
    unittest.main()
