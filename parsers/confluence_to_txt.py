import requests
import json
import os

# Настройки
CONFLUENCE_BASE_URL = "https://support.itrium.ru"
API_USERNAME = "venekbespalov@mail.ru"
API_TOKEN = "ATATT3xFfGF05RfA2Nddz1iiQ3nOzuTIL8rFc698pT3nX8nByVesglRABfOAwskNMlIuClxRddvWFQuTG00coKZKOunN7KdZToP_Uc_yx8u9Emaez3bOVU7ZLiUbQ0dLIYvM8hJERso1qHTPPyuBVbvj7hJ3G5PcjIbhzeK2FMaWWpEq8lTp3Ps=9746EA7A"

from bs4 import BeautifulSoup


# Преобразование HTML в текст
def html_to_text(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

# Основная функция для получения содержимого базы знаний
def fetch_confluence_space_content(space_key):
    """
    Получает все страницы из указанного пространства Confluence.
    :param space_key: Ключ пространства в Confluence
    :return: Список страниц с их содержимым
    """
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    params = {
        "spaceKey": space_key,
        "expand": "body.storage",
        "limit": 100
    }
    auth = (API_USERNAME, API_TOKEN)

    all_pages = []
    while url:
        response = requests.get(url, params=params, auth=auth)
        if response.status_code != 200:
            raise Exception(f"Ошибка {response.status_code}: {response.text}")
        
        data = response.json()
        all_pages.extend(data.get("results", []))
        url = data.get("_links", {}).get("next")
        if url:
            url = f"{CONFLUENCE_BASE_URL}{url}"

    return all_pages

# Сохранение данных в текстовый файл
def save_to_txt(pages, filename="confluence_export.txt"):
    """
    Сохраняет содержимое страниц в файл.
    :param pages: Список страниц
    :param filename: Имя выходного файла
    """
    with open(filename, "w", encoding="utf-8") as file:
        for page in pages:
            title = page.get("title", "Без названия")
            content_html = page.get("body", {}).get("storage", {}).get("value", "Нет содержимого")
            content = html_to_text(content_html)  # Преобразуем HTML в текст
            file.write(f"# {title}\n\n{content}\n\n")
    print(f"Содержимое сохранено в файл {filename}")

# Основная логика программы
if __name__ == "__main__":
    space_key = input("Введите ключ пространства Confluence (например, 'DEV'): ")
    print(f"Получение страниц из пространства '{space_key}'...")
    
    try:
        pages = fetch_confluence_space_content(space_key)
        print(f"Найдено страниц: {len(pages)}")
        save_to_txt(pages)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
