from pydantic import BaseModel


class Message(BaseModel):
    payload: str
