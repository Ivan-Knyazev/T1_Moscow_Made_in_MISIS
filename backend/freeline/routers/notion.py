from fastapi import APIRouter, status
# from freeline.services.chat_bot import create_bot
from freeline.schemas.notion import NotionSettings

notion_router = APIRouter(
    prefix="/notion",
    tags=["notion"],
)


@notion_router.post("/upload", description="Использовать для загрузки Базы Знаний через notion")
async def upload_notion(user_id: str, notion_settings: NotionSettings):

    # bot = await create_notion(user_id, notion_settings)
    bot = "Not Implemented"

    return status.HTTP_201_CREATED, {"message": f"Successfully created {bot}"}
