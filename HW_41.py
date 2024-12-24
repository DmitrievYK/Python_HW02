# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    # Получаем путь к директории
    directory = os.path.dirname(file_path)
    # Получаем имя файла и расширение
    file_name_with_extension = os.path.basename(file_path)
    # Разделяем имя файла и расширение на две переменные
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    
    return (directory, file_name, file_extension)

# Пример использования
absolute_path = "/home/user/documents/example.txt"
result = split_file_path(absolute_path)
print(result)