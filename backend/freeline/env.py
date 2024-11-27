import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_PORT = os.environ.get("BACKEND_PORT")

ML_HOST = os.environ.get("ML_HOST")
ML_PORT = os.environ.get("ML_PORT")
ML_URI = f"http://{ML_HOST}:{ML_PORT}/get_nlp_search"


# For Postgres
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

# driver://user:pass@localhost/dbname
POSTGRES_URI = f"postgresql+asyncpg://{POSTGRES_USER}:{
    POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


# For S3
S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_KEY = os.environ.get("S3_SECRET_KEY")
S3_HOST = os.environ.get("S3_HOST")
S3_PORT = os.environ.get("S3_PORT")

S3_URI = f"http://{S3_HOST}:{S3_PORT}"
