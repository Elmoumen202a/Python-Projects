import unittest
from countdown_timer import CountdownTimer

class TestCountdownTimer(unittest.TestCase):
    def test_countdown(self):
        # Test with 5 seconds
        with self.subTest(msg="Countdown from 5 seconds"):
            timer = CountdownTimer(5)
            self.assertEqual(timer.countdown(), None)

        # Test with 0 seconds
        with self.subTest(msg="Countdown from 0 seconds"):
            timer = CountdownTimer(0)
            self.assertEqual(timer.countdown(), None)

        # Test with a large number of seconds
        with self.subTest(msg="Countdown from a large number of seconds"):
            timer = CountdownTimer(100)
            self.assertEqual(timer.countdown(), None)

if __name__ == '__main__':
    unittest.main()
