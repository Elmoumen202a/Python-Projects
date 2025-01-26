
import unittest
import time
from main import TimerStopwatch

class TestTimerStopwatch(unittest.TestCase):
    def test_initial_time(self):
        """
        Test that the initial time is set to 0.
        """
        app = TimerStopwatch(None)
        self.assertEqual(app.time_elapsed, 0)

    def test_start_stop(self):
        """
        Test that starting and stopping the timer updates time correctly.
        """
        app = TimerStopwatch(None)
        app.start()
        time.sleep(2)  # Simulate running for 2 seconds
        app.stop()
        self.assertGreater(app.time_elapsed, 0)

    def test_reset(self):
        """
        Test that resetting the timer sets the time back to 0.
        """
        app = TimerStopwatch(None)
        app.start()
        time.sleep(2)
        app.stop()
        app.reset()
        self.assertEqual(app.time_elapsed, 0)

if __name__ == "__main__":
    unittest.main()
