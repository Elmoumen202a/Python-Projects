# test_phone_info.py
from phoneInfo import get_phone_info

def test_get_phone_info():
    phone_number = "+212XXXXXXXX"
    info = get_phone_info(phone_number)

    assert isinstance(info, dict)
    assert "time_zones" in info
    assert "carrier_name" in info
    assert "location_description" in info
