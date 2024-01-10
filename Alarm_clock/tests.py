from datetime import datetime
from io import StringIO
from unittest.mock import patch
import pytest
from alarm_clock import set_alarm 

def test_set_alarm(capsys):
    # Set the alarm time to the current time plus 1 second for testing purposes
    alarm_time = (datetime.now() + timedelta(seconds=1)).strftime("%I:%M:%S %p")
    
    # Use a patch to simulate user input
    with patch('builtins.input', side_effect=[alarm_time]):
        set_alarm()

    # Capture the printed output during the test
    captured = capsys.readouterr()

    # Check if "Wake Up!" is present in the printed output
    assert "Wake Up!" in captured.out
