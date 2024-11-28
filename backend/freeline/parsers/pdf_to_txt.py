import pdfplumber
import textwrap


def convert_pdf_to_txt(pdf_file):
    try:
        # Открываем PDF-документ
        with pdfplumber.open(pdf_file) as pdf:
            # Проходим по всем страницам
            full_text = ""
            for page in pdf.pages:
                # Извлекаем текст со страницы
                text = page.extract_text()
                if text:  # Если текст есть, записываем его в файл
                    full_text += text
                    # txt_output.write(text + '\n')
            print(f"Файл '{pdf_file}' успешно преобразован'.")
            batch_size = 1000
            batches = textwrap.wrap(full_text, batch_size)
            return batches

    except Exception as e:
        print(f"Ошибка: {e}")


# АБСОЛЮТНЫЙ Путь к вашему PDF файлу
pdf_file_path = "/workspaces/python-2/parsers/parsers/data/base_dogs.pdf"

# АБСОЛЮТНЫЙ Путь для сохранения TXT файла
txt_file_path = "output_from_pdf.txt"

# Преобразование
# convert_pdf_to_txt(pdf_file_path, txt_file_path)
