from notion_client import Client
import csv

# Вставьте ваш Integration Token и ID базы знаний
NOTION_TOKEN = "your-integration-token"
DATABASE_ID = "your-database-id"

# Инициализация клиента Notion
notion = Client(auth=NOTION_TOKEN)

def fetch_all_items_from_database(database_id):
    """Функция для получения всех записей из базы знаний с учетом пагинации."""
    results = []
    next_cursor = None

    while True:
        # Выполняем запрос к базе данных
        response = notion.databases.query(
            database_id=database_id, 
            start_cursor=next_cursor
        )
        results.extend(response.get("results", []))

        # Проверяем, есть ли следующая страница
        next_cursor = response.get("next_cursor")
        if not response.get("has_more"):
            break

    return results

def extract_properties(page):
    """Извлечение свойств страницы в удобный формат."""
    properties = page.get("properties", {})
    extracted_data = {}

    for key, value in properties.items():
        if value["type"] == "title":
            extracted_data[key] = " ".join(
                [text["text"]["content"] for text in value["title"]]
            )
        elif value["type"] == "rich_text":
            extracted_data[key] = " ".join(
                [text["text"]["content"] for text in value["rich_text"]]
            )
        elif value["type"] == "number":
            extracted_data[key] = value.get("number", None)
        elif value["type"] == "select":
            extracted_data[key] = value["select"]["name"] if value["select"] else None
        elif value["type"] == "multi_select":
            extracted_data[key] = ", ".join(
                [select["name"] for select in value["multi_select"]]
            )
        elif value["type"] == "date":
            extracted_data[key] = value["date"]["start"] if value["date"] else None
        elif value["type"] == "checkbox":
            extracted_data[key] = value["checkbox"]
        elif value["type"] == "url":
            extracted_data[key] = value.get("url", None)
        elif value["type"] == "email":
            extracted_data[key] = value.get("email", None)
        elif value["type"] == "phone_number":
            extracted_data[key] = value.get("phone_number", None)
        elif value["type"] == "people":
            extracted_data[key] = ", ".join(
                [person["name"] for person in value["people"] if "name" in person]
            )
        elif value["type"] == "files":
            extracted_data[key] = ", ".join(
                [file["name"] for file in value["files"] if "name" in file]
            )
        else:
            extracted_data[key] = None

    return extracted_data

def save_to_csv(data, filename="notion_data.csv"):
    """Сохранение данных в CSV-файл."""
    if not data:
        print("Нет данных для сохранения!")
        return

    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные успешно сохранены в файл {filename}.")

# Основная логика
if __name__ == "__main__":
    print("Получение всех записей из базы знаний...")
    pages = fetch_all_items_from_database(DATABASE_ID)

    print(f"Найдено записей: {len(pages)}")
    all_data = [extract_properties(page) for page in pages]

    print("Сохранение данных в CSV...")
    save_to_csv(all_data)
    print("Готово!")
    
