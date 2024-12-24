# Напишите функцию, которая заполняет файл (добавляет в конец) случайные
# пары числе. Первое число int, второе float разделенные вертикальной чертной.
# Минимальное число (-1000), максимальное (+1000).
# Количество строк и имя файла передаются как аргументы функции.

import os
import random as rd

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def generate_nuber_file(count_list:int, file_name:str):
        '''Заполняет файл случайными числами.'''
        with open(file_name, 'w', encoding='utf-8') as f:
            for i in range(count_list):
                f.write(f'{rd.randint(MIN_NUMBER, MAX_NUMBER)} | {rd.random() * 2000 - 1000}')
                f.write('\n ' if i < (count_list - 1) else "")


if __name__ == "__main__":
     generate_nuber_file(10, 'data.txt')