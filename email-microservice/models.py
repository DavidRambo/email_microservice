import pydantic

from config import settings


class EmailBase(pydantic.BaseModel):
    """Required fields for creating an email."""

    recipient_name: str
    recipient_addr: pydantic.EmailStr
    subject: str = pydantic.Field(default="A Message from the Wish Lists App")
    message: str


class EmailSend(EmailBase):
    """Required fields for sending an email."""

    mail_server: str = pydantic.Field(default=settings.mail_server)
    mail_port: int = pydantic.Field(default=settings.mail_port)
    sender: pydantic.EmailStr = pydantic.Field(default=settings.sender_addr)
    password: str = pydantic.Field(default=settings.sender_password)
