import smtplib
from email.mime.text import MIMEText

def send_feedback(sender_email, receiver_email, feedback_message, smtp_server='smtp.example.com', port=587, login=None, password=None):
    """
    Sends feedback from sender to receiver.

    Parameters:
        sender_email (str): The email address of the sender.
        receiver_email (str): The email address of the receiver.
        feedback_message (str): The feedback message that will be sent.
        smtp_server (str): The address of the SMTP server. Default is 'smtp.example.com'.
        port (int): The port to use for the SMTP server. Default is 587.
        login (str): The login email for the SMTP server.
        password (str): The password for the SMTP server.

    Returns:
        str: A success or error message.
    """
    
    try:
        # Create the email message object with the feedback content
        msg = MIMEText(feedback_message)
        msg['Subject'] = 'Feedback'  # Email subject
        msg['From'] = sender_email    # Sender's email
        msg['To'] = receiver_email    # Receiver's email
        
        # Set up the SMTP server connection
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Start TLS for security
            server.login(login, password)  # Log in to the SMTP server
            # Send the email from sender to receiver
            server.sendmail(sender_email, receiver_email, msg.as_string())
        
        # Return success message if email is sent
        return "Feedback sent successfully!"
    
    except Exception as e:
        # Return error message if something goes wrong
        return f"Failed to send feedback: {str(e)}"

if __name__ == "__main__":
    # Example usage with sample data
    sender = "you@example.com"  # Sender's email
    receiver = "feedback@example.com"  # Receiver's email
    feedback = "This is an automatic feedback message."  # Feedback content
    smtp_server = "smtp.example.com"  # SMTP server address
    login = "you@example.com"  # Login for the SMTP server
    password = "yourpassword"  # Password for the SMTP server
    
    # Call the send_feedback function and print the result
    result = send_feedback(sender, receiver, feedback, smtp_server, login=login, password=password)
    print(result)
