# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import SW_71, SW_72, SW_73, SW_74, SW_75, SW_76, SW_77, HW_61

from SW_71 import generate_nuber_file
from SW_72 import generate_name_file
from SW_73 import process_files
from SW_74 import generate_files
from SW_75 import generate_with_dictionary
from SW_76 import generate_files
from SW_77 import sort_files
from HW_61 import batch_rename


def main():
    d = {
        'doc':5,
        'jpg':10,
        'png':23,
        'txt':15
    }
    generate_nuber_file(10, 'data.txt')  # Генерация файла с числами
    generate_name_file('name.txt', 25)   # Генерация файла с псевдонимами
    process_files('data.txt', 'name.txt', 'res.txt') # Генерация файла в один по двум предыдущим файлам с именами и числами
    generate_files('rnd', 'files_test') # Генерация множества файлов по заданным параметрам
    generate_with_dictionary(d) # Создание новых расширений для файлов 
    generate_files('rnd', 'files_test') # Переименование файлов
    sort_files('files_test') # Cортировка файлов
    batch_rename('new_file', 3, '.rnd', '.md', [1, 5], './files_test') # массовое переименование файлов


if __name__ == "__main__":
    main()

