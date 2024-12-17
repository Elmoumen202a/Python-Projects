import unittest
import speech_recognition as sr
from main import audio_to_text

class TestAudioToText(unittest.TestCase):
    def test_audio_to_text(self):
        recognizer = sr.Recognizer()
        sample_audio = sr.AudioFile('sample.wav')  # A sample audio file for testing
        
        with sample_audio as source:
            audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            self.assertIsInstance(text, str)  # Ensure the output is a string
            print("✅ Test Passed: Audio converted to text successfully.")
        except Exception as e:
            self.fail(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    unittest.main()
