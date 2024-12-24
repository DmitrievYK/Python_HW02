# Доработайте предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с
# Расширения и количество файлов функция принимает
# Количество переданных расширений можеть быть любым
# Количество файлов для каждого расширения различно
# Внутри используйте вызов функции из прошлой задачи

from SW_74 import generate_files

def generate_with_dictionary(dictionary:dict):
    for key, value in dictionary.items():
        generate_files(key, 'files_test', num_files=value)

if __name__ == "__main__":
    d = {
        'doc':5,
        'jpg':10,
        'png':23,
        'txt':15
    }
    generate_with_dictionary(d)
