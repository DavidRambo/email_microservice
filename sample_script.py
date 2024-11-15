import smtplib
import ssl

from email.message import EmailMessage


# Use dotenv to populate these
SENDER = "sender@test.com"
PASSWORD = "test"
RECIPIENT = "recipient@test.com"
MESSAGE = """
Test email body.
"""

em = EmailMessage()
em["From"] = SENDER
em["To"] = RECIPIENT
em["Subject"] = "Testing Python email"
em.set_content(MESSAGE)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.test.com", 465, context=context) as server:
    print("Logging in...")
    server.login(SENDER, PASSWORD)

    print("Sending email...")
    server.sendmail(SENDER, RECIPIENT, em.as_string())

print("Email sent.")
