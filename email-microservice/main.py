"""FastAPI application for sending emails."""

import fastapi
import pydantic

from fastapi.middleware.cors import CORSMiddleware

from config import settings

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)


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


@app.post("/send-email", status_code=201)
def send_email(email: EmailSend):
    pass
