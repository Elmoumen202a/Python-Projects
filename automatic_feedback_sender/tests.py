import unittest
from main import send_feedback

class TestFeedbackSender(unittest.TestCase):
    """
    Unit test class to test the feedback sender function from the main.py file.
    """

    def test_send_feedback_success(self):
        """
        Test case for a successful feedback send.

        This test simulates a scenario where valid sender email, receiver email,
        feedback message, and SMTP server details are provided. The expected 
        outcome is that the feedback will be sent successfully.
        """
        # Call the send_feedback function with valid inputs
        result = send_feedback(
            sender_email="test_sender@example.com",  # Mock sender email
            receiver_email="test_receiver@example.com",  # Mock receiver email
            feedback_message="Test feedback",  # Sample feedback message
            smtp_server="smtp.example.com",  # Mock SMTP server
            login="test_sender@example.com",  # Mock login email
            password="testpassword"  # Mock password
        )
        # Check if the result is as expected (successful feedback sent)
        self.assertEqual(result, "Feedback sent successfully!")

    def test_send_feedback_failure(self):
        """
        Test case for feedback sending failure due to invalid sender email.

        This test simulates a scenario where an invalid sender email is provided,
        which should result in a failure to send the feedback. The expected
        outcome is that an error message is returned.
        """
        # Call the send_feedback function with an invalid sender email
        result = send_feedback(
            sender_email="invalid_email",  # Invalid email format
            receiver_email="test_receiver@example.com",  # Valid receiver email
            feedback_message="Test feedback",  # Sample feedback message
            smtp_server="smtp.example.com",  # Mock SMTP server
            login="test_sender@example.com",  # Mock login email
            password="testpassword"  # Mock password
        )
        # Check if the result contains the failure message
        self.assertIn("Failed to send feedback", result)

if __name__ == '__main__':
    """
    This part of the script runs the unit tests when executed directly.
    """
    unittest.main()
