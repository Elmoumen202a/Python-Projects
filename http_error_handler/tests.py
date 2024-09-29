import unittest
from main import handle_http_error, HTTPError

# Unit test class to test the error handling functions
class TestHTTPErrorHandler(unittest.TestCase):
    """
    This class contains unit tests for the handle_http_error function.
    Each test simulates a different HTTP error and checks whether the correct
    custom exception is raised.
    """

    # Test for 400 Bad Request
    def test_400_error(self):
        with self.assertRaises(HTTPError) as context:
            handle_http_error(400)
        self.assertEqual(str(context.exception), "400 Bad Request")

    # Test for 401 Unauthorized
    def test_401_error(self):
        with self.assertRaises(HTTPError) as context:
            handle_http_error(401)
        self.assertEqual(str(context.exception), "401 Unauthorized")

    # Test for 403 Forbidden
    def test_403_error(self):
        with self.assertRaises(HTTPError) as context:
            handle_http_error(403)
        self.assertEqual(str(context.exception), "403 Forbidden")

    # Test for 404 Not Found
    def test_404_error(self):
        with self.assertRaises(HTTPError) as context:
            handle_http_error(404)
        self.assertEqual(str(context.exception), "404 Not Found")

    # Test for 500 Internal Server Error
    def test_500_error(self):
        with self.assertRaises(HTTPError) as context:
            handle_http_error(500)
        self.assertEqual(str(context.exception), "500 Internal Server Error")

    # Test for unhandled status code (e.g., 418 I'm a teapot)
    def test_unhandled_status_code(self):
        """
        This test checks if an unhandled status code (like 418) does not
        raise an exception and simply prints the unhandled status code.
        """
        try:
            handle_http_error(418)  # No exception should be raised
        except HTTPError:
            self.fail("handle_http_error() raised HTTPError unexpectedly!")

# Main block to run the unit tests
if __name__ == '__main__':
    unittest.main()
