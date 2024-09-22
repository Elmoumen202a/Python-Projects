import unittest
from main import read_websites

class TestWebsiteBlocker(unittest.TestCase):
    
    def test_read_websites(self):
        """
        Test if the read_websites function correctly reads and returns a list of websites.
        """
        # Create a sample file with websites
        with open('test_websites.txt', 'w') as f:
            f.write("www.facebook.com\nwww.youtube.com\n")
        
        # Read the websites using the function
        websites = read_websites('test_websites.txt')
        
        # Check if the function returns the correct list of websites
        self.assertEqual(websites, ["www.facebook.com", "www.youtube.com"])

if __name__ == '__main__':
    unittest.main()
