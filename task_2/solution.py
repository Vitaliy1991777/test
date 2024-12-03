# import requests
# from bs4 import BeautifulSoup
# import re
# from collections import Counter
# import csv

# # Функция для извлечения текста страницы
# def fetch_page(url):
#     response = requests.get(url)
#     return response.text

# # Функция для извлечения всех заголовков
# def get_headers(page_text):
#     soup = BeautifulSoup(page_text, 'html.parser')
#     headers = soup.find_all('h3')
#     return headers

# # Функция для подсчета букв
# def count_first_letters(text):
#     # Преобразуем текст в нижний регистр и разбиваем на слова
#     words = re.findall(r'\b[а-яА-ЯёЁ]\S*', text.lower())
#     # Считаем первую букву каждого слова
#     first_letters = [word[0] for word in words if word]
#     return Counter(first_letters)

# # Функция для получения всех ссылок на страницы, начинающиеся с конкретной группы букв
# def get_letter_pages(base_url, letter_group):
#     # Конструируем URL для конкретной группы букв
#     url = f"{base_url}{letter_group}"
#     page_text = fetch_page(url)
#     return page_text

# # URL базовой страницы для каждой группы букв
# base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from="

# # Буквы, которые нужно обработать
# letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']

# # Открываем CSV файл для записи
# with open("beasts.csv", "w", newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Letter', 'Count']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     # Записываем заголовки
#     writer.writeheader()

#     # Проходим по каждой букве
#     for letter in letters:
#         print(f"Обрабатываем страницы для буквы: {letter}")

#         # Получаем данные для текущей буквы
#         page_text = get_letter_pages(base_url, letter)

#         # Подсчитываем количество слов, начинающихся с этой буквы
#         counter = count_first_letters(page_text)

#         # Записываем результаты в CSV
#         count = counter.get(letter.lower(), 0)  # Считаем только для текущей буквы
#         writer.writerow({'Letter': letter, 'Count': count})

# print("Результаты сохранены в beasts.csv")


import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import csv
import time
from requests.exceptions import Timeout, RequestException

# Функция для извлечения текста страницы с обработкой тайм-аутов
def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)  # Устанавливаем тайм-аут на 10 секунд
        response.raise_for_status()  # Проверка на успешный ответ
        return response.text
    except (Timeout, RequestException) as e:
        print(f"Ошибка запроса: {e}")
        time.sleep(5)  # Задержка перед повторной попыткой
        return fetch_page(url)  # Повторный запрос

# Функция для извлечения всех заголовков
def get_headers(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    headers = soup.find_all('h3')
    return headers

# Функция для подсчета букв
def count_first_letters(text):
    # Преобразуем текст в нижний регистр и разбиваем на слова
    words = re.findall(r'\b[а-яА-ЯёЁ]\S*', text.lower())
    # Считаем первую букву каждого слова
    first_letters = [word[0] for word in words if word]
    return Counter(first_letters)

# Функция для получения всех ссылок на страницы, начинающиеся с конкретной группы букв
def get_letter_pages(base_url, letter_group):
    # Конструируем URL для конкретной группы букв
    url = f"{base_url}{letter_group}"
    page_text = fetch_page(url)
    time.sleep(1)  # Добавляем задержку в 1 секунду
    return page_text

# Функция для парсинга животных по буквам и записи в CSV
def parse_wiki_animals(base_url, letters):
    result = []
    for letter in letters:
        print(f"Обрабатываем страницы для буквы: {letter}")
        page_text = get_letter_pages(base_url, letter)
        counter = count_first_letters(page_text)
        result.append((letter, counter.get(letter.lower(), 0)))  # Сохраняем букву и её количество
        time.sleep(1)
    return result

# Функция для записи данных в CSV файл
def save_to_csv(data, filename="beasts.csv"):
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Letter', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for letter, count in data:
            writer.writerow({'Letter': letter, 'Count': count})
    print(f"Результаты сохранены в {filename}")

# Пример использования
if __name__ == "__main__":
    base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from="
    letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
    
    data = parse_wiki_animals(base_url, letters)
    save_to_csv(data)






