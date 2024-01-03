import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    """Record audio for the specified duration and save it to a WAV file.

    Parameters:
    - seconds (int): Duration of the recording in seconds.
    - file (str): Name of the output WAV file.

    Returns:
    None
    """
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")
