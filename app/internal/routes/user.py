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
import numpy as np
import boto3
import os
import json

router = APIRouter(
    prefix="/api/v1"
)

load_dotenv()
api_key = os.getenv('API_MISTRAL')
api_key_openai = os.getenv('API_LLAMA_70B')
api_backend = os.getenv('API_BACKEND')
S3_ACCESS_KEY=os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY=os.getenv('S3_SECRET_KEY')
S3_URI=os.getenv('S3_HOST')
S3_PORT=os.getenv('S3_PORT')

model_search = SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')

@dataclass
class Generate(BaseModel):
    query: str
    model_type: str
    bucket_name: str
    file_names: list


def load_data(file_names: list, bucket_name: str, rag_fusion: rag.Rag_fusion, query) -> list:
    arr_data = []

    for file_docs, file in file_names:


        # Настройка клиента S3
        s3 = boto3.client(
            service_name="s3",
            endpoint_url=S3_URI,  # Замените на ваш endpoint
            aws_access_key_id=S3_ACCESS_KEY,  # Замените на ваш Access Key
            aws_secret_access_key=S3_SECRET_KEY,  # Замените на ваш Secret Key
            # region_name='us-east-1'  # Замените на ваш регион, если необходимо
        )

        # Кладём что-то в бакет
        response = s3.get_object(Bucket=bucket_name,
                                 Key=file)  # Замените 'your_bucket_name' на имя вашего бакета
        file_content = response['Body'].read()

        response2 = s3.get_object(Bucket=bucket_name,
                                 Key=file_docs)  # Замените 'your_bucket_name' на имя вашего бакета
        file_content2 = response2['Body'].read()

        arr_data += rag.Rag_fusion(docs=file_content2, doc_emb=np.load(file_content)).score_docs(query=query, model_search=model_search)

    return arr_data


@router.post("/generate")
async def generate(data: Generate):
    arr_data = load_data(file_names=data.file_names, bucket_name=data.bucket_name)

    if data.model_type == "mistral":
        return {"message": rag.Rag_fusion(query=data.query).generate_with_arr(model=llm.Model_API(api_key).generate, arr_data=arr_data)}
    elif data.model_type == "llama3-8B":
        return {"message": rag.Rag_fusion(query=data.query).generate_with_arr(model=llm.ollama, arr_data=arr_data)}
    elif data.model_type == "llama3-70B":
        return {"message": rag.Rag_fusion(query=data.query).generate_with_arr(model=llm.Model_llama_70B(api_key=api_key_openai).generate, arr_data=arr_data)}
    else:
        return {"message": rag.example(model_search, data.query, api_key)}

