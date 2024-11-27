from docx import Document


def convert_docx_to_txt(docx_file, txt_file):
    try:
        # Загружаем документ
        doc = Document(docx_file)

        # Открываем файл для записи текста
        with open(txt_file, 'w', encoding='utf-8') as txt_file:
            # Проходим по всем параграфам в документе
            for paragraph in doc.paragraphs:
                # Записываем текст параграфа в файл
                txt_file.write(paragraph.text + '\n')

        print(f"Файл '{docx_file}' успешно преобразован в '{txt_file.name}'.")
    except Exception as e:
        print(f"Ошибка: {e}")


# АБСОЛЮТНЫЙ Путь к вашему .docx файлу
docx_file_path = "/workspaces/python-2/parsers/parsers/data/base_dogs.docx"

# АБСОЛЮТНЫЙ Путь для сохранения .txt файла
txt_file_path = "output_file.txt"

# Преобразование
convert_docx_to_txt(docx_file_path, txt_file_path)
