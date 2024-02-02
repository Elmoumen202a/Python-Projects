from main_code import ip_address

def test_ip_address_obfuscation():
    assert ip_address("1.1.2.3") == "1[.]1[.]2[.]3"
    assert ip_address("192.168.0.1") == "192[.]168[.]0[.]1"

