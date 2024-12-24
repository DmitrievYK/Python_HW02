# Задача 2
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#  Программа должна возвращать сумму и произведение* дробей. 
#  Для проверки своего кода используйте модуль fractions
 
from fractions import Fraction

# Функция для получения дробей и их суммы/произведения
def process_fractions(fraction1, fraction2):
    # Преобразуем строки во фракции
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    # Находим сумму и произведение
    sum_fraction = frac1 + frac2
    product_fraction = frac1 * frac2

    return sum_fraction, product_fraction

# Получаем дроби от пользователя
fraction1 = input("Введите первую дробь (a/b): ")
fraction2 = input("Введите вторую дробь (a/b): ")

# Вызываем функцию и получаем результаты
sum_result, product_result = process_fractions(fraction1, fraction2)

# Вывод результатов
print(f"Сумма дробей:  {sum_result}, Произведение дробей: {product_result}")