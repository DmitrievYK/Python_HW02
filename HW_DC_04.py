import requests
from lxml import html
from pprint import pprint
import csv

url = 'https://news.mail.ru/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

response = requests.get(url, headers=header)

tree = html.fromstring(response.text)

# Получаем ссылки на все новости
news_all = tree.xpath('//div[@class="js-module"]//span/a[contains(@href, "mail.ru")]/@href')

news_list = []
unique_links = set()  # Создаем множество для уникальных ссылок

for news in news_all:
    if news in unique_links:
        continue  # Если ссылка уже есть, пропускаем итерацию
    
    unique_links.add(news)  # Добавляем ссылку в множество

    news_info = {}
    
    response_news = requests.get(news, headers=header)
    tree_news = html.fromstring(response_news.text)

    # Извлекаем название и текст новости
    name_news = tree_news.xpath("//header/h1/text()")
    news_text = tree_news.xpath("//header/div[@data-qa='Text']/p/text()")

    news_info["name"] = name_news[0] if name_news else "No title"  # Проверяем наличие заголовка
    news_info["link"] = news
    news_info["text"] = ' '.join(news_text)  # Объединяем текст новостей в одну строку

    news_list.append(news_info)  

# Добавление автоматической нумерации
for index, news in enumerate(news_list, start=1):
    news['id'] = index  

# Сохранение данных в CSV-файл
with open('news.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "link", "text"])
    writer.writeheader()  # Записываем заголовки
    writer.writerows(news_list)  # Записываем данные новостей

print("Данные сохранены в news.csv")

pprint(news_list)