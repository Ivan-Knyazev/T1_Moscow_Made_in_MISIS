FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN ["pip3", "install", "-r", "requirements.txt"]

COPY . .

# EXPOSE 8000

ENTRYPOINT ["uvicorn", "freeline.main:app", "--port", "8000", "--host", "0.0.0.0"]