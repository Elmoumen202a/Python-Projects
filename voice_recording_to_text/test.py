from main import record_voice

def test_record_voice():
    # Test recording function
    record_voice(duration=3, file_name='test_recording.txt')

if __name__ == "__main__":
    test_record_voice()
