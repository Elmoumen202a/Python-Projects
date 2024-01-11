from instabot import Bot

def send_instagram_message(username, password, message, receiver_username):
    """
    Function to log in to Instagram, send a message to a user, and then log out.

    Parameters:
    - username: Your Instagram username.
    - password: Your Instagram password.
    - message: The message you want to send.
    - receiver_username: The username of the recipient.

    Returns:
    None
    """
    # Initialize the InstaBot
    bot = Bot()
    # Log in to Instagram
    bot.login(username=username, password=password)
    # Send a message
    bot.send_message(message, [receiver_username])
    # Log out
    bot.logout()

# You can call the function with your credentials and message
send_instagram_message("Your Username", "Your Password", "Hi Brother", "Receiver's Username")
