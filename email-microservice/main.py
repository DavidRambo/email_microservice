"""FastAPI application for sending emails."""

import fastapi

from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)
