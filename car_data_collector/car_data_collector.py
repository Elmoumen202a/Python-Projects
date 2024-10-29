import random
import time

class CarDataCollector:
    """Class to collect and analyze car data."""

    def __init__(self, car_id):
        self.car_id = car_id
        self.data = []

    def collect_data(self):
        """Collects simulated data from the car sensors."""
        speed = random.randint(20, 120)  # Simulate speed in km/h
        fuel_level = random.uniform(5, 50)  # Simulate fuel level in liters
        engine_temp = random.uniform(60, 100)  # Simulate engine temperature in Celsius
        timestamp = time.time()  # Current time in seconds since epoch
        # Store data in a dictionary
        car_data = {
            'speed': speed,
            'fuel_level': fuel_level,
            'engine_temp': engine_temp,
            'timestamp': timestamp
        }
        self.data.append(car_data)
        print(f"Data collected: {car_data}")

    def average_speed(self):
        """Calculates the average speed from collected data."""
        speeds = [entry['speed'] for entry in self.data]
        return sum(speeds) / len(speeds) if speeds else 0

    def fuel_efficiency(self):
        """Simulates fuel efficiency analysis based on fuel level and distance."""
        fuel_used = 50 - self.data[-1]['fuel_level'] if self.data else 0
        return (self.average_speed() * len(self.data)) / fuel_used if fuel_used else 0

# Run a sample collection process
if __name__ == "__main__":
    car_collector = CarDataCollector(car_id="CAR123")
    for _ in range(5):  # Collect data 5 times
        car_collector.collect_data()
        time.sleep(1)  # Wait 1 second between data collections
    print(f"Average Speed: {car_collector.average_speed()} km/h")
    print(f"Fuel Efficiency: {car_collector.fuel_efficiency()} km/l")
