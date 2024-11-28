from pydantic import BaseModel


class NotionSettings(BaseModel):
    type: str
    prompt: str | None
    neural_network_model: str
    notion_token: str
    database_id: str
