from pymongo import MongoClient
import json


client = MongoClient('mongodb://localhost:27017/')

db = client['data']
collection = db['books']

### Загрузка один раз
#Чтение файла
with open('books.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#загрузка книг
if isinstance(data, list):
    collection.insert_many(data)


print(f'Успешно загружено {len(data)} книг.')
### Загрузка один раз


# Вывод количества документов в БД
count = collection.count_documents({})
print(f'Число записей в базе данных: {count}')

# Вывод количества книг с ценой от 10 до 40
query2 = {"price": {'$gte': 10,"$lte": 40}}
print(f"Количество книг c ценой от 10 до 40: {collection.count_documents(query2)}")

# Вывод названия книг с ценой от 55.5 до 55.6
query3 = {"price": {'$gte': 55.5,"$lte": 55.6}}
books_range_price = collection.find(query3)
for books in books_range_price:
    print(f"Название: '{books["title"]}' Цена:{books["price"]}")

# Вывод названия книг с упоминанием слова "system" в описании
query4 = {"description": {'$regex': "system"}}
books_range_regex = collection.find(query4)
for books in books_range_regex:
    print(f"Название: '{books["title"]}'   Описание: {books["description"][:25]}...")