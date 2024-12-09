import unittest
from datetime import datetime
from main import alarm_checker

class TestAlarmClock(unittest.TestCase):

    def test_alarm_checker(self):
        # Simulate alarm time
        alarm_time = datetime.now().strftime("%H:%M")
        with self.assertLogs(level='INFO') as log:
            alarm_checker(alarm_time, "Test Alarm")
        self.assertIn("⏰ Alarm! Test Alarm", log.output)

if __name__ == "__main__":
    unittest.main()
