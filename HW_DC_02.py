# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ 
# и извлечь информацию о всех книгах на сайте 
# во всех категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.

import requests
from bs4 import BeautifulSoup
import json
import re

base_url = 'http://books.toscrape.com/'
books = []
page_number = 1

while True:
    # Формируем URL для текущей страницы
    response = requests.get(f'{base_url}catalogue/page-{page_number}.html')
    
    # Проверяем, есть ли доступ к странице
    if response.status_code != 200:
        break

    # Парсим HTML-код страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все книги на странице
    for article in soup.select('article.product_pod'):
        book_url = base_url + 'catalogue/'+ article.h3.a['href']

        # Получаем информацию о книге
        response_book = requests.get(book_url)
        soup_book = BeautifulSoup(response_book.text, 'html.parser')

        title = soup_book.h1.text

        price_element = soup_book.select_one('p.price_color')
        price = price_element.text.strip().replace('£', '').replace('Â', '').strip() if price_element else None

        # Пробуем преобразовать цену в float
        try:
            price = float(price) if price is not None else None
        except ValueError:
            print(f"Не удалось преобразовать цену для книги '{title}': {price}")
            price = None # Устанавливаем цену в None, если преобразование не удалось

        # Получаем количество в наличии
        stock_text = soup_book.select_one('p.instock.availability')
        if stock_text:
            stock = int(re.search(r'\((\d+)', stock_text.text.strip()).group(1))  # Получаем число из строки
        else:
            stock = 0  # Или любое другое значение по умолчанию
        
        # Получаем описание
        description = soup_book.select_one('#product_description + p').text if soup_book.select_one('#product_description + p') else ''

        # Добавляем книгу в список
        books.append({
            'title': title,
            'price': price,
            'stock': stock,
            'description': description
        })

    # Переходим на следующую страницу
    print(f'Переход на страницу {page_number} завершен.')
    page_number += 1

# Сохраняем данные в JSON-файл
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print(f'Сохранено {len(books)} книг в файле "books.json".')

