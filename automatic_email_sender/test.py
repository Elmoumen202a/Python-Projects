from send_email import send_email

# List of recipients
recipients = ['recipient4@example.com', 'recipient5@example.com']

# Send emails to each recipient
for recipient in recipients:
    subject = 'Another Test Email'
    body = 'This is a test email sent from another script.'

    send_email(subject, body, recipient)

print("Test emails sent successfully!")
