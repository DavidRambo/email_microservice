"""FastAPI application for sending emails."""

import fastapi

from fastapi.middleware.cors import CORSMiddleware

from config import settings
from models import EmailSend
from utils import create_email

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)


@app.post("/send-email", status_code=201)
async def send_email(email: EmailSend):
    await create_email(email)
