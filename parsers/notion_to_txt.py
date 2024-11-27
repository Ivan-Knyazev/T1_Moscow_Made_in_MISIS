from notion_client import Client

# Укажите токен API и ID базы
# NOTION_TOKEN = "your-integration-token"
NOTION_TOKEN = "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"
# DATABASE_ID = "your-database-id"
DATABASE_ID = "1b0bab76bfba4de8b9b4cd24bcc89e0f"

# Инициализация клиента
notion = Client(auth=NOTION_TOKEN)

def fetch_all_pages(database_id):
    """Получает все страницы из базы данных."""
    pages = []
    next_cursor = None

    while True:
        response = notion.databases.query(
            database_id=database_id,
            start_cursor=next_cursor
        )
        pages.extend(response.get("results", []))
        next_cursor = response.get("next_cursor")
        if not response.get("has_more"):
            break
    return pages

def fetch_page_content(page_id):
    """Получает содержимое страницы по ID."""
    response = notion.blocks.children.list(block_id=page_id)
    return response.get("results", [])

def extract_text_from_blocks(blocks):
    """Извлекает текст из блоков."""
    text_content = []
    for block in blocks:
        block_type = block.get("type")
        if block_type in ["paragraph", "heading_1", "heading_2", "heading_3"]:
            text = block[block_type].get("rich_text", [])
            for part in text:
                text_content.append(part.get("text", {}).get("content", ""))
        elif block_type == "bulleted_list_item":
            text = block["bulleted_list_item"].get("rich_text", [])
            for part in text:
                text_content.append(f"- {part.get('text', {}).get('content', '')}")
        elif block_type == "numbered_list_item":
            text = block["numbered_list_item"].get("rich_text", [])
            for part in text:
                text_content.append(f"1. {part.get('text', {}).get('content', '')}")
        # Добавьте обработку других типов блоков, если нужно
    return "\n".join(text_content)

def save_to_txt(content, filename="notion_export.txt"):
    """Сохраняет текст в файл."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Содержимое сохранено в файл {filename}")

# Основная логика программы
if __name__ == "__main__":
    print("Получение страниц из базы знаний...")
    pages = fetch_all_pages(DATABASE_ID)
    print(f"Найдено страниц: {len(pages)}")

    all_content = []

    for page in pages:
        page_id = page["id"]

        # Проверяем наличие заголовка
        properties = page.get("properties", {})
        title_property = properties.get("Name", {}).get("title", [])
        page_title = title_property[0]["text"]["content"] if title_property else "Без названия"

        print(f"Обработка страницы: {page_title}")
        
        blocks = fetch_page_content(page_id)
        page_content = extract_text_from_blocks(blocks)
        all_content.append(f"# {page_title}\n\n{page_content}\n")

    # Объединяем содержимое всех страниц
    final_content = "\n\n".join(all_content)

    # Сохраняем в файл
    save_to_txt(final_content)
