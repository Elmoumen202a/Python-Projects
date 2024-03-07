import sounddevice as sd
import numpy as np

def record_voice(duration=5, sampling_rate=44100, file_name='recorded_voice.txt'):
    print("Recording... Speak now!")

    # Record audio
    audio_data = sd.rec(int(sampling_rate * duration), samplerate=sampling_rate, channels=1, dtype=np.int16)
    sd.wait()

    # Save audio to a text file
    np.savetxt(file_name, audio_data, fmt='%d', delimiter='\n')

    print(f"Recording saved to {file_name}")

if __name__ == "__main__":
    record_voice()
