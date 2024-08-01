import unittest  # Import the unittest module for testing
from binary_search import binary_search  # Import the binary_search function

class TestBinarySearch(unittest.TestCase):
    def test_element_present(self):
        # Test cases where the target element is present in the array
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)  # Target 3 is at index 2
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)  # Target 1 is at index 0
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)  # Target 5 is at index 4

    def test_element_not_present(self):
        # Test cases where the target element is not present in the array
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)  # Target 6 is not in the array
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)  # Target 0 is not in the array

    def test_empty_list(self):
        # Test case for an empty array
        self.assertEqual(binary_search([], 1), -1)  # No elements to search

if __name__ == "__main__":
    unittest.main()  # Run the tests
