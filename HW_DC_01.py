import requests
import json
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
params = {
    "client_id": os.getenv("client_id"),
    "client_secret": os.getenv("client_secret"),
    "near": city,
    "query": "restaurant"
}

headers = {
    "Accept": "application/json",
    "Authorization": os.getenv("Authorization") 
}

# Отправка запроса API
response = requests.get(url, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["address"])
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)