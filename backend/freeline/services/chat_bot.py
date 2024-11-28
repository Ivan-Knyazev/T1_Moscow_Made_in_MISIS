from fastapi import HTTPException, status
from freeline.schemas.chat_bot import BotSettings


async def create_bot(user_id: str, bot_settings: BotSettings) -> BotSettings:
    return bot_settings
