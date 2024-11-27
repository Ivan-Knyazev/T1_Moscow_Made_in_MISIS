from pydantic import BaseModel


class CommonPhrases(BaseModel):
    salute: str
    description: str
    end_of_dialogue: str


class KnowledgeBase(BaseModel):
    url: str | None
    prompt: str | None
    neural_network_model: str


class Appearance(BaseModel):
    colors: list[str]
    font: str
    assistant_name: str


class BotSettings(BaseModel):
    common_phrases: CommonPhrases
    knowledge_base: KnowledgeBase
    appearance: Appearance
