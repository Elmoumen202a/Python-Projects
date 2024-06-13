import unittest
from main import get_emails

class TestEmailSender(unittest.TestCase):

    def test_get_emails(self):
        # Expected list of email addresses
        expected_emails = ['test1@example.com', 'test2@example.com', 'test3@example.com']
        
        # Test file path
        test_file_path = 'test_field.txt'
        
        # Write the test email addresses to the test file
        with open(test_file_path, 'w') as f:
            f.write('\n'.join(expected_emails))
        
        # Get the emails from the test file
        emails = get_emails(test_file_path)
        
        # Assert that the emails read from the file match the expected emails
        self.assertEqual(emails, expected_emails)

if __name__ == '__main__':
    unittest.main()
