import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email(subject: str, content: str):
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=EMAIL_RECEIVER,
        subject=subject,
        plain_text_content=content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)
        print(f"Email sent to {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"Error sending email: {e}")
