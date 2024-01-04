
from voice_recorder import voice_recorder
import os

def test_voice_recorder():
    # Given
    duration = 5
    output_file = "test_record.wav"
    # When
    voice_recorder(duration, output_file)
    # Then
    assert os.path.exists(output_file)