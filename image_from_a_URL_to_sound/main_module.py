from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import requests
from io import BytesIO


def image_to_sound(image_url):
    """
    Convert an image from a URL to sound.

    Parameters:
    - image_url (str): URL of the image.

    Returns:
    - bool: True if successful, False otherwise.
    """
    try:
        # Download the image from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        image_data = BytesIO(response.content)

        # Open the image data
        loaded_image = Image.open(image_data)

        # Extract text from the image
        decoded_text = image_to_string(loaded_image)

        # Clean up the text
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)

        # Convert text to speech and save as an audio file
        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")

        return True

    except requests.exceptions.RequestException as request_error:
        print("Error downloading image from URL:", request_error)

    except Exception as bug:
        # Handle other exceptions gracefully and print an error message
        print("An error occurred while executing the code:", bug)

    return False


if __name__ == "__main__":
    # Example usage with a URL
    image_to_sound("https://example.com/image.jpg")
    input()
