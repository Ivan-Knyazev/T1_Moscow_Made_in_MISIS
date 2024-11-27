from fastapi import UploadFile, HTTPException, APIRouter, status
from freeline.services.files import write_file

file_router = APIRouter(
    prefix="/file",
    tags=["file"],
)

# Разрешенные типы файлов
ALLOWED_DB_EXTENSIONS = {'doc', 'docx', 'pdf'}
ALLOWED_PHOTO_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def is_allowed_db_file(filename: str | None) -> bool:
    if filename is None:
        return False
    else:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_DB_EXTENSIONS


@file_router.post("/upload/db")
async def upload_file(file: UploadFile):
    # Проверка типа файла
    if not is_allowed_db_file(file.filename):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

    await write_file(file=file)

    return {"message": f"Successfully uploaded {file.filename}"}
