from fastapi import APIRouter, UploadFile, File, Form, Request, Response
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import asyncio
import app.internal.ml.rag_fusion as rag
import app.internal.ml.model as llm
from pydantic import BaseModel
from dotenv import load_dotenv
from dataclasses import dataclass
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
import os
import json

router = APIRouter(
    prefix="/api/v1"
)

load_dotenv()
api_key = os.getenv('API_MISTRAL')
api_backend = os.getenv('API_BACKEND')

model_search = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')

@dataclass
class Generate(BaseModel):
    query: str
    model_type: str
    file_names: list


def load_data(file_names: list) -> list[list]:
    docs = []
    docs_emb = []

    for file in file_names:
        ...

    return [docs, docs_emb]


@router.post("/generate")
async def generate(data: Generate):
    docs, docs_emb = load_data(data.file_names)

    return {"message": rag.example(model_search, data.query, api_key)}

