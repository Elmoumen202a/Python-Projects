import pytest
from qrcode import generate_QRcode
import os

@pytest.mark.parametrize("link, filename", [
    ("https://example.com", "test_output_1.png"),
    ("https://example.org", "test_output_2.png"),

])
def test_generate_QRcode(link, filename):
    generate_QRcode(link, filename)
    assert os.path.exists(filename)

    # Clean up after the test
    os.remove(filename)

if __name__ == "__main__":
    pytest.main()
