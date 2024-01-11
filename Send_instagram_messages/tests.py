from send import send_instagram_message

def test_send_instagram_message():
    # Provide your test credentials
    username = "Your Test Username"
    password = "Your Test Password"
    message = "Test message"
    receiver_username = "Test Receiver's Username"

    # Call the function
    send_instagram_message(username, password, message, receiver_username)

    # Add assertions or checks based on the behavior you expect
    # For example, you can check if the message was sent successfully or if the login/logout worked as expected.
    # assert some_condition, "Test failed: Some explanation"

# Run the tests using pytest
# in the terminal, run: pytest tests.py
