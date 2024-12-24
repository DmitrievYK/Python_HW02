from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

def generate_random_number(lower_limit, upper_limit):
    """Генерирует случайное число в заданных границах."""
    return randint(lower_limit, upper_limit)

def get_user_guess(attempt):
    """Запрашивает у пользователя ввод числа."""
    return int(input(f"Попытка {attempt + 1}: Ваше число: "))

def evaluate_guess(trial, num):
    """Оценивает предположение пользователя и выводит подсказку."""
    if trial < num:
        return "Больше!"
    elif trial > num:
        return "Меньше!"
    else:
        return None  # Угадал

def play_game(attempts):
    """Основная функция игры."""
    num = generate_random_number(LOWER_LIMIT, UPPER_LIMIT)
    print("Угадай число от 0 до 1000 за 10 попыток!")

    for attempt in range(attempts):
        trial = get_user_guess(attempt)

        if trial < LOWER_LIMIT or trial > UPPER_LIMIT:
            print(f"Пожалуйста, введите число от {LOWER_LIMIT} до {UPPER_LIMIT}.")
            continue

        result = evaluate_guess(trial, num)
        if result is None:
            print(f"Поздравляю! Вы угадали число {num} за {attempt + 1} попыток!")
            break
        else:
            print(result)
    else:
        print(f"К сожалению, вы не угадали число. Загаданное число было {num}.")

# Запуск игры
play_game(attempts=10)