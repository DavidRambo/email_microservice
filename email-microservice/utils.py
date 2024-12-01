import smtplib
import ssl

from email.message import EmailMessage

from main import EmailSend


async def create_email(email_data: EmailSend):
    em = EmailMessage()
    em["From"] = email_data.sender
    em["To"] = f"{email_data.recipient_name} <{email_data.recipient_addr}>"
    em["Subject"] = email_data.subject
    em.set_content(email_data.message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        email_data.mail_server, email_data.mail_port, context=context
    ) as server:
        server.login(email_data.sender, email_data.password)

        server.sendmail(email_data.sender, em["To"], em.as_string())
