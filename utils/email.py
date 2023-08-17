import os

from fastapi_mail import (
    ConnectionConfig,
    MessageSchema,
    FastMail,
    MessageType,
)
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

email_conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=os.getenv("MAIL_PORT"),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


class EmailSchema(BaseModel):
    email: EmailStr


class EmailService:
    def __init__(self, conf: ConnectionConfig):
        self._email_client = FastMail(conf)

    async def send_mail(self, email: EmailSchema, message: str):
        message = MessageSchema(
            subject="Test Task email",
            recipients=[email.dict().get("email")],
            body=message,
            subtype=MessageType.html
        )
        await self._email_client.send_message(message)
        return JSONResponse(status_code=200, content={"message": "email has been sent"})
