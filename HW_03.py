# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

# Задаем границы
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

# Генерируем случайное число
num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Количество попыток
attempts = 10

print("Угадай число от 0 до 1000 за 10 попыток!")

# Цикл попыток
for attempt in range(attempts):
    trial = int(input(f"Попытка {attempt + 1}: Ваше число: "))
    
    if trial < LOWER_LIMIT or trial > UPPER_LIMIT:
        print(f"Пожалуйста, введите число от {LOWER_LIMIT} до {UPPER_LIMIT}.")
        continue

    if trial < num:
        print("Больше!")
    elif trial > num:
        print("Меньше!")
    else:
        print(f"Поздравляю! Вы угадали число {num} за {attempt + 1} попыток!")
        break
else:
    print(f"К сожалению, вы не угадали число. Загаданное число было {num}.")