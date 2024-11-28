from fastapi import UploadFile, HTTPException, APIRouter, status
from freeline.services.files import local_write_file, put_file_to_s3

file_router = APIRouter(
    prefix="/file",
    tags=["file"],
)

# Разрешенные типы файлов
ALLOWED_DB_EXTENSIONS = {'txt', 'doc', 'docx', 'pdf'}
ALLOWED_PHOTO_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def is_allowed_db_file(filename: str | None) -> bool:
    if filename is None:
        return False
    else:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_DB_EXTENSIONS


def get_file_type(filename: str) -> str:
    for type in ALLOWED_DB_EXTENSIONS:
        if '.' in filename and filename.rsplit('.', 1)[1].lower() == type:
            return type
    else:
        return ""


@file_router.post("/upload", description="Использовать для загрузки Базы Знаний файлом")
async def upload_file(user_id: str, file: UploadFile):
    # Проверка типа файла
    if not is_allowed_db_file(file.filename):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

    if file.filename is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")
    else:
        file_type = get_file_type(filename=file.filename)

    await put_file_to_s3(bucket_name=user_id, file=file, file_type=file_type)

    return {"message": f"Successfully uploaded {file.filename}"}


@file_router.post("/upload/db-local", description="НЕ использовать, тестовый эндпойнт, загружает файлы на диск")
async def local_upload_file(file: UploadFile):
    # Проверка типа файла
    if not is_allowed_db_file(file.filename):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

    await local_write_file(file=file)

    return {"message": f"Successfully uploaded {file.filename}"}
