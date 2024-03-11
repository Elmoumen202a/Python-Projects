import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Your email credentials
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'

    # Create a MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        # Log in to your Gmail account
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

# List of recipients
recipients = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# Send emails to each recipient
for recipient in recipients:
    subject = 'Your Subject Here'
    body = 'Your email body here.'

    send_email(subject, body, recipient)

print("Emails sent successfully!")
