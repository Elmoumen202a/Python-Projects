import unittest
from main import countdown_to_christmas, random_christmas_wish

class TestChristmasFunctions(unittest.TestCase):
    def test_countdown_to_christmas(self):
        days = countdown_to_christmas()
        self.assertIsInstance(days, int)
        self.assertGreaterEqual(days, 0)

    def test_random_christmas_wish(self):
        wish = random_christmas_wish()
        self.assertIsInstance(wish, str)
        self.assertTrue(len(wish) > 0)

if __name__ == "__main__":
    unittest.main()
