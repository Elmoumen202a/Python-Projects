import unittest
from prahprase import generate_prahprase

# Unit tests for the Prahprase generator function
class TestPrahprase(unittest.TestCase):
    # Testing if the generated Prahprase is a string
    def test_generate_prahprase(self):
        prahprase = generate_prahprase()
        self.assertTrue(isinstance(prahprase, str))

# Running the tests if this script is run directly
if __name__ == '__main__':
    unittest.main()
