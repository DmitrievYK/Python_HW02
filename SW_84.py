# Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах на первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и индификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv
# файла представленная как отедельный json
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json
from pathlib import Path


def csv_to_json(from_file:Path, to_file:Path,) -> None:
    json_list = []
    with open(from_file, "r", newline='', encoding="utf-8") as f:
        csv_write = csv.reader(f, dialect="excel-tab", delimiter=',')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                level, id, name = line
                json_dict['level']= int(level)
                json_dict['id']= f"{int(id):010}"
                json_dict['name']= name.title()
                json_dict['hash'] = hash(f'{json_dict['name']}{json_dict['id']}')
                json_list.append(json_dict)
    with open(to_file, 'w', encoding="utf-8") as f:
        json.dump(json_list, f, indent=2)

if __name__ == "__main__":
    csv_to_json(Path('db.csv'), Path("new_db.json"))