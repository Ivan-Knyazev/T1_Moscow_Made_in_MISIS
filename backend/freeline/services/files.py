from fastapi import UploadFile, HTTPException, status

MAX_FILE_SIZE = 1 * 1024 * 1024 * 1024  # 1 Gb


async def write_file(file: UploadFile):
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
