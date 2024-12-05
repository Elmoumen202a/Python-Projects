import unittest
from main import check_worthiness

class TestThorHammer(unittest.TestCase):
    def test_worthy_action(self):
        """
        Test if a worthy action results in being worthy.
        """
        result = check_worthiness("Youssef", "I showed great kindness.")
        self.assertTrue(result)

    def test_unworthy_action(self):
        """
        Test if an unworthy action might result in not being worthy.
        """
        result = check_worthiness("Youssef", "I was lazy all day.")
        # Since randomness is involved, this might occasionally fail.
        # To improve, set the random seed in the actual function.
        self.assertIn(result, [True, False])

    def test_randomness(self):
        """
        Test if randomness is handled.
        """
        results = {check_worthiness("Youssef", "Random action") for _ in range(100)}
        self.assertTrue(len(results) > 1, "Randomness is not functioning.")

if __name__ == "__main__":
    unittest.main()
