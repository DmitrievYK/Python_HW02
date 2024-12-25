# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный иденфикатор
# и уровень доступа (от 1 до 7).
# после каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключем для имени.
# Убедитесь, что все иднтификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраниться.

import json
import os

def access_users(file_name='db.json'):
    db = {}
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            db = json.load(f)
    with open(file_name, "w", encoding='utf-8') as f:
        while True:
            while True:
                try:
                    user_lvl = int(input('Введите уровень от 1 до 7 или букву для выхода: '))
                except:
                    json.dump(db, f)
                    exit()
                else:
                    break
            if not 1 <= user_lvl <= 7:
                continue
            if user_lvl not in db:
                db[user_lvl] = {}
            while True:
                try:
                    user_id = int(input("Введите идентификатор: "))
                except:
                    print('Некоректный ввод')
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            if ident == user_id:
                                print('Индификатор должен быть уникальным')
                                flag = True
                                break
                    if flag:
                        continue
                    else:
                        break
            while True:
                user_name = input('Введите имя: ')
                if user_name:
                    break
                else:
                    print('Имя не должно быть пустым!')
            db[user_lvl][user_id] = user_name

if __name__ == "__main__":
    access_users()