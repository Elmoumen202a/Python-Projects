from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_weather(city):
    city = city.replace(" ", "+")
    url = f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Check if the request was successful
    except requests.RequestException as e:
        print(f"Error: {e}")
        return

    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        # Attempt to extract weather information
        location = soup.select_one('#wob_loc').getText().strip()
        time = soup.select_one('#wob_dts').getText().strip()
        info = soup.select_one('#wob_dc').getText().strip()
        temperature = soup.select_one('#wob_tm').getText().strip()
        
        # Print the weather information
        print(location)
        print(time)
        print(info)
        print(temperature + "°C")
    except AttributeError:
        # Handle the case when specific HTML elements are not found
        print("Weather information not found for the given city.")
    except Exception as e:
        # Handle unexpected errors during parsing
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    city_input = input("Enter the Name of Any City >> ")
    city_input = city_input + " weather"
    get_weather(city_input)
