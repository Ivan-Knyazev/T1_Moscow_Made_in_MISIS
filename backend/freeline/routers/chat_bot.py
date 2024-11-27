from fastapi import APIRouter, status
from freeline.services.chat_bot import create_bot
from freeline.schemas.chat_bot import BotSettings

bot_router = APIRouter(
    prefix="/chat-bot",
    tags=["chat-bot"],
)


@bot_router.post("", description="Использовать для загрузки настроек Бота")
async def register_bot(user_id: str, bot_settings: BotSettings):

    bot = await create_bot(user_id, bot_settings)

    return status.HTTP_201_CREATED, {"message": f"Successfully created {bot}"}
