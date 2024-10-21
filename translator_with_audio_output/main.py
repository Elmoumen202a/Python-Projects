# Import the necessary libraries
from googletrans import Translator  # Used for translating text
from gtts import gTTS  # Google Text-to-Speech library to generate audio
import os  # To interact with the operating system (e.g., play the audio file)

def translate_to_german(word):
    """Translate the given English word to German."""
    translator = Translator()  # Create a translator object
    translation = translator.translate(word, src='en', dest='de')  # Translate from English to German
    return translation.text  # Return the translated text (German word)

def generate_audio(text, filename="output.mp3"):
    """Generate an audio file for the given German text."""
    tts = gTTS(text=text, lang='de')  # Create a TTS object for German
    tts.save(filename)  # Save the audio file with the given filename
    return filename  # Return the filename for confirmation

if __name__ == "__main__":
    # Ask the user to enter an English word
    word = input("Enter an English word to translate into German: ")

    # Translate the English word to German
    german_word = translate_to_german(word)
    print(f"The German translation for '{word}' is '{german_word}'.")

    # Generate the audio for the German translation
    audio_file = generate_audio(german_word)
    print(f"Audio has been saved as {audio_file}")

    # Play the audio (optional, works on most OS)
    os.system(f"start {audio_file}")  # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux
