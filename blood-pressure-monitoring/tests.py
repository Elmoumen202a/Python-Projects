import unittest
from main import BloodPressureMonitor

class TestBloodPressureMonitor(unittest.TestCase):
    def test_add_reading(self):
        monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
        monitor.add_reading(120, 80)  # // Add a sample reading.
        self.assertEqual(len(monitor.readings), 1)  # // Assert that the reading has been added.

    def test_average_reading(self):
        monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
        monitor.add_reading(120, 80)  # // Add sample readings.
        monitor.add_reading(130, 85)
        self.assertEqual(monitor.average_reading(), (125.0, 82.5))  # // Assert that the average reading is calculated correctly.

    def test_check_reading_normal(self):
        monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
        self.assertEqual(monitor.check_reading(120, 80), "Your blood pressure is within the normal range.")  # // Check a normal reading.

    def test_check_reading_high(self):
        monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
        self.assertEqual(monitor.check_reading(150, 100), "High blood pressure. Please consult a doctor.")  # // Check a high reading.

    def test_check_reading_low(self):
        monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
        self.assertEqual(monitor.check_reading(80, 50), "Low blood pressure. Please consult a doctor.")  # // Check a low reading.

if __name__ == "__main__":
    unittest.main()
