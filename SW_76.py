
import random
import os
from SW_74 import generate_text

def generate_files(extension:str,
                   directory:str, 
                   min_length=6, 
                   max_length=30,
                   min_bytes=256,
                   max_bytes=4096,
                   num_files=42):
        '''Генерирует файлы с заданными параметрами.'''
        if not os.path.exists(directory) or not os.path.isdir(directory):
                os.mkdir(directory)

        for i in range(num_files):
                name_length = random.randint(min_length, max_length)
                filename = generate_text(name_length)
                text_length = random.randint(min_bytes, max_bytes)
                text = generate_text(text_length)
                while True:
                        try:
                            with open(f'{directory}/{filename}.{extension}', "x", encoding='utf-8') as f:
                                f.write(text)
                        except:
                               filename = generate_text(name_length)
                        else:
                               break
if __name__== "__main__":
    generate_files('rnd', 'files_test')