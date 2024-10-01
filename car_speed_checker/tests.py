import unittest
from main import Car

class TestCarSpeedChecker(unittest.TestCase):
    
    def test_speed_within_limit(self):
        car = Car(speed_limit=80)
        result = car.check_speed(70)
        self.assertEqual(result, "Speed 70 km/h is within the limit.")
    
    def test_speed_over_limit(self):
        car = Car(speed_limit=80)
        result = car.check_speed(90)
        self.assertEqual(result, "Speed 90 km/h is over the limit!")

    def test_average_speed(self):
        car = Car(speed_limit=80)
        car.check_speed(70)
        car.check_speed(90)
        result = car.average_speed()
        self.assertEqual(result, "Average speed: 80.00 km/h")
    
    def test_no_speeds_recorded(self):
        car = Car(speed_limit=80)
        result = car.average_speed()
        self.assertEqual(result, "No speeds recorded.")

    def test_speed_history(self):
        car = Car(speed_limit=80)
        car.check_speed(70)
        car.check_speed(90)
        self.assertEqual(car.speed_history(), [70, 90])

if __name__ == "__main__":
    unittest.main()
