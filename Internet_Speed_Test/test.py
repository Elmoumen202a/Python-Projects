import pytest
from speedTest import check_speed

def test_check_speed(capsys):
    # Call the function and capture the printed output
    check_speed()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the expected strings are present in the output
    assert "Wifi Download Speed is" in captured.out
    assert "Wifi Upload Speed is" in captured.out
