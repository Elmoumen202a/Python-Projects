import pytest
from main_module import image_to_sound

def test_image_to_sound_success():
    # Provide a valid image URL for testing
    image_url = "https://example.com/image.jpg"
    assert image_to_sound(image_url) is True

def test_image_to_sound_failure():
    # Provide an invalid image URL for testing
    image_url = "https://example.com/nonexistent_image.jpg"
    assert image_to_sound(image_url) is False
