import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, from_password, smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Sends an email with the given subject and body to the specified recipient.

    Parameters:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_email (str): The recipient's email address.
        from_email (str): The sender's email address.
        from_password (str): The sender's email password.
        smtp_server (str): The SMTP server address (default is 'smtp.gmail.com').
        smtp_port (int): The SMTP server port (default is 587).
    """
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")

def get_emails(file_path):
    """
    Reads email addresses from a file and returns them as a list.

    Parameters:
        file_path (str): The path to the file containing email addresses.

    Returns:
        list: A list of email addresses.
    """
    with open(file_path, 'r') as file:  # "file_path" change to path to the file containing email addresses
        # Read each line, strip any extra whitespace, and add to the list
        emails = [line.strip() for line in file if line.strip()]
    return emails

if __name__ == "__main__":
    # Get email details from user input
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    from_email = input("Enter your email: ")
    from_password = input("Enter your password: ")
    file_path = 'field.txt'  # Define the file path here

    # Get the list of email addresses
    email_list = get_emails(file_path)

    # Send the email to each address in the list
    for email in email_list:
        send_email(subject, body, email, from_email, from_password)
