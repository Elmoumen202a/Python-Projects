import unittest
from main import get_weather, get_recommendation

class TestWeatherApp(unittest.TestCase):

    def test_get_weather_valid_city(self):
        result = get_weather("London")
        self.assertIn("Weather in London", result)

    def test_get_weather_invalid_city(self):
        result = get_weather("InvalidCityName")
        self.assertIn("HTTP error occurred", result)

    def test_get_recommendation_hot_weather(self):
        result = get_recommendation(35, "clear sky")
        self.assertEqual(result, "Recommendation: Stay hydrated and wear sunscreen!")

    def test_get_recommendation_cold_weather(self):
        result = get_recommendation(5, "cloudy")
        self.assertEqual(result, "Recommendation: Dress warmly, it's cold outside!")

    def test_get_recommendation_rainy_weather(self):
        result = get_recommendation(20, "rain")
        self.assertEqual(result, "Recommendation: Don't forget an umbrella!")

if __name__ == "__main__":
    unittest.main()
