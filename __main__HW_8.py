# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from pathlib import Path
import SW_81, SW_82, SW_83, SW_84, SW_85, SW_86, SW_87, HW_71

from SW_81 import txt_to_json
from SW_82 import access_users
from SW_83 import json_to_csv
from SW_84 import csv_to_json
from SW_85 import json_to_pickle
from SW_86 import pickle_to_csv
from SW_87 import csv2pickles
from HW_71 import directory_walker


def main():

    txt_to_json() # Перевод txt в json
    access_users() # Генерация базы данных с индеф. именами, уровнями
    json_to_csv() # Первод формата json в csv
    csv_to_json(Path('db.csv'), Path("new_db.json")) # Перевод из csv в json с корректировками
    json_to_pickle() # Преобразование json в pickle 
    pickle_to_csv(Path('new_db.pickle')) # Преобразование pickle в csv
    csv2pickles(Path('new_db.csv')) # Перевод csv в pickle
    directory_walker('./files_test') # Поиск по папкам, сохранение в разные форматы с указаниями


if __name__ == "__main__":
    main()

