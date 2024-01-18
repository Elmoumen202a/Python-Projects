from authentication import authenticate_user

def test_authentication():
    # Test case 1: Valid username and password
    assert authenticate_user("youssef.x", "123456") == "Verified"

    # Test case 2: Valid username, incorrect password
    assert authenticate_user("youssef.y", "wrong_password") == "Verified"

    # Test case 3: Invalid username
    assert authenticate_user("nonexistent_user", "password") == "User not found"
