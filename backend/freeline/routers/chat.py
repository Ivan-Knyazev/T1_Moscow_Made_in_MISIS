from fastapi import APIRouter, status
# from freeline.services.chat_bot import create_bot
from freeline.schemas.message import Message

chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


@chat_router.post("/new_message", description="Использовать для отправки сообщения боту")
async def upload_notion(user_id: str, message: Message):

    # bot = await create_notion(user_id, message)
    msg = "Not Implemented"

    return status.HTTP_201_CREATED, {"message": f"Successfully sended {msg}"}
