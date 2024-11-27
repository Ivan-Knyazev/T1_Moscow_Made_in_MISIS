from botocore.exceptions import NoCredentialsError, ClientError
from fastapi import UploadFile, HTTPException, status
from freeline.db.s3 import s3_client
from freeline.parsers.pdf_to_txt import convert_pdf_to_txt
# from freeline.env import S3_ACCESS_KEY


MAX_FILE_SIZE = 1 * 1024 * 1024 * 1024  # 1 Gb


async def put_file_to_s3(bucket_name: str, file: UploadFile, file_type: str):
    batches = []

    # Проверка размера файла
    try:
        contents = await file.read()
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="The file size exceeds the allowed limit")
        # Сохранение файла
        if file.filename is not None:
            path = file.filename
            with open(path, "wb") as f:
                f.write(contents)
            if file_type == "pdf":
                batches = convert_pdf_to_txt(path)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Something went wrong')

    # Проверка существования бакета и создание, если он не существует
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            # Бакет не существует, создаем его
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            raise HTTPException(
                status_code=500, detail=f"Error checking bucket: {e}")

    # Загрузка файла в S3
    try:
        i = 0
        for batch in batches:
            with open('temp_file.txt', 'w') as file:
                file.write(batch)
            # s3_client.put_object(Bucket=bucket_name,
            #                      Key=object_key, Body=batch)
                s3_client.upload_fileobj(
                    file.file, bucket_name, f'file_{i}.txt')
        return {"status": "ok", "filename": file.filename, "bucket": bucket_name}
    except NoCredentialsError:
        raise HTTPException(
            status_code=403, detail="Credentials not available")
    except ClientError as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading file: {e}")


async def local_write_file(file: UploadFile):
    try:
        contents = await file.read()

        # Проверка размера файла
        if len(contents) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="The file size exceeds the allowed limit")

        # Сохранение файла
        if file.filename is not None:
            path = "./backend/upload_files/" + file.filename
            with open(path, "wb") as f:
                f.write(contents)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Something went wrong')

    finally:
        await file.close()
