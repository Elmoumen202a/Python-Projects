import speech_recognition as sr

def audio_to_text():
    recognizer = sr.Recognizer()  # Initialize the recognizer
    microphone = sr.Microphone()  # Set up the microphone

    print("\n🎤 Speak something... (listening)")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio_data = recognizer.listen(source)  # Listen to the audio input
        print("✅ Audio received. Converting to text...")

    try:
        # Convert audio to text using Google's Speech Recognition
        text = recognizer.recognize_google(audio_data)
        print("\n📝 Text Output: \n", text)
    except sr.UnknownValueError:
        print("\n❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"\n❌ Error with the request: {e}")

if __name__ == "__main__":
    audio_to_text()
