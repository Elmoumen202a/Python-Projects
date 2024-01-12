from weather import get_weather
import pytest

def test_get_weather():
    # Test for a valid city
    get_weather("New York")
    
    # Test for an invalid city (this should print an error message)
    get_weather("Invalid City Name")

if __name__ == "__main__":
    pytest.main()
