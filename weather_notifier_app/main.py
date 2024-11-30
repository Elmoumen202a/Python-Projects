import requests

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant data
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        city_name = weather_data['name']
        country = weather_data['sys']['country']

        return f"Weather in {city_name}, {country}: {temp}°C, {description.capitalize()}"
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"Error: {err}"

# Function to provide recommendations based on the weather
def get_recommendation(temp, description):
    if "rain" in description or "drizzle" in description:
        return "Recommendation: Don't forget an umbrella!"
    elif temp > 30:
        return "Recommendation: Stay hydrated and wear sunscreen!"
    elif temp < 10:
        return "Recommendation: Dress warmly, it's cold outside!"
    else:
        return "Recommendation: Enjoy the weather!"

# Main program
if __name__ == "__main__":
    city = input("Enter the name of a city: ")
    weather_info = get_weather(city)

    if "Weather in" in weather_info:
        print(weather_info)
        temp = float(weather_info.split(':')[1].split('°C')[0].strip())
        description = weather_info.split(',')[-1].strip().lower()
        print(get_recommendation(temp, description))
    else:
        print(weather_info)
