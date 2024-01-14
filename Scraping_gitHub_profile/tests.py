import pytest
from main import get_github_profile_picture

def test_get_github_profile_picture_valid():
    # Test for a valid GitHub profile with a profile picture
    github_profile_url = "https://github.com/Elmoumen202a"
    profile_picture_url = get_github_profile_picture(github_profile_url)
    assert profile_picture_url is not None

def test_get_github_profile_picture_invalid():
    # Test for an invalid GitHub profile without a profile picture
    github_profile_url = "https://github.com/nonexistentuser123"
    profile_picture_url = get_github_profile_picture(github_profile_url)
    assert profile_picture_url is None

# Run tests
if __name__ == "__main__":
    pytest.main(["-v", "tests.py"])
