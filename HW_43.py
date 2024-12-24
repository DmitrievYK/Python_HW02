# Создайте функцию генератор чисел Фибоначчи
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib_gen = fibonacci_generator()
for i in range(15):
    print(next(fib_gen))  # Выводит первые 15 чисел Фибоначчи