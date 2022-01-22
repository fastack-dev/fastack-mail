from typing import Optional

from fastack import Controller
from fastapi import BackgroundTasks
from pydantic import BaseModel, EmailStr

from fastack_mail.globals import email
from fastack_mail.message import Message


class MessageBody(BaseModel):
    subject: str
    to: EmailStr
    text: Optional[str] = None
    html: Optional[str] = None
    background_task: Optional[bool] = False


class MailerController(Controller):
    async def post(self, body: MessageBody, background_task: BackgroundTasks):
        data = body.dict()
        data.pop("background_task")
        data["recipients"] = [data.pop("to")]
        message = Message(**data)
        if body.background_task:
            background_task.add_task(email.send, message)
        else:
            await email.send(message)
        return {"detail": "ok"}
