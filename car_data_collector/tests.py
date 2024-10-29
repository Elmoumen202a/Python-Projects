import unittest
from car_data_collector import CarDataCollector

class TestCarDataCollector(unittest.TestCase):

    def setUp(self):
        self.collector = CarDataCollector(car_id="TEST123")

    def test_collect_data(self):
        """Test that data collection adds data to the list."""
        self.collector.collect_data()
        self.assertTrue(len(self.collector.data) > 0)

    def test_average_speed(self):
        """Test average speed calculation."""
        # Set up mock data with only 'speed' for simplicity in this test
        self.collector.data = [{'speed': 60}, {'speed': 80}, {'speed': 100}]
        self.assertEqual(self.collector.average_speed(), 80)

    def test_fuel_efficiency(self):
        """Test fuel efficiency calculation."""
        # Full mock data for each entry
        self.collector.data = [
            {'speed': 60, 'fuel_level': 50, 'engine_temp': 90, 'timestamp': 1},
            {'speed': 80, 'fuel_level': 45, 'engine_temp': 92, 'timestamp': 2},
            {'speed': 100, 'fuel_level': 40, 'engine_temp': 95, 'timestamp': 3}
        ]
        # Ensure fuel efficiency calculation runs without error
        self.assertGreater(self.collector.fuel_efficiency(), 0)

if __name__ == "__main__":
    unittest.main()
