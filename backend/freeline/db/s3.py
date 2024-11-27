import boto3
from freeline.env import S3_URI, S3_ACCESS_KEY, S3_SECRET_KEY

# Настройка клиента S3
s3_client = boto3.client(
    service_name="s3",
    endpoint_url=S3_URI,  # Замените на ваш endpoint
    aws_access_key_id=S3_ACCESS_KEY,  # Замените на ваш Access Key
    aws_secret_access_key=S3_SECRET_KEY,  # Замените на ваш Secret Key
    # region_name='us-east-1'  # Замените на ваш регион, если необходимо
)
