# Задача 1
# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.
 
 
# Получаем целое число от пользователя
num = int(input("Введите целое число: "))

# Преобразуем номер в шестнадцатеричное представление
hex_repr = ""

if num == 0:
    hex_repr = "0"
else:
    n = abs(num)
    while n > 0:
        remainder = n % 16
        if remainder < 10:
            hex_char = chr(remainder + ord('0'))
        else:
            hex_char = chr(remainder - 10 + ord('a'))
        hex_repr = hex_char + hex_repr
        n //= 16

# Добавляем знак минус для отрицательных чисел
if num < 0:
    hex_repr = '-' + hex_repr

print("Шестнадцатеричное представление:", hex_repr)
print("Проверка с помощью функции hex():", hex(num))