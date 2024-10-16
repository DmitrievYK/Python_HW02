# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
	

#Ввод постоянных
MIN_LIMIT = 1
MAX_LIMIT = 100000

# Запрос числа у пользователя
number = int(input("Введите число (от 1 до 100000): "))

# Проверка на допустимость числа
if number < MIN_LIMIT or number > MAX_LIMIT:
    print("Число должно быть от 1 до 100000.")
else:
    # Предположим, что число простое
    is_prime = True

    # Проверяем делимость на числа от 2 до квадратного корня из number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # Вывод результата
    print(f"Ваше число {number} Простое? - {is_prime}")