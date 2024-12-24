# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

input_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

# Создаем словарь для подсчета количества вхождений элементов
counts = {}
for item in input_list:
    counts[item] = counts.get(item, 0) + 1

# Создаем список дублирующихся элементов без дубликатов
duplicates = []
for item, count in counts.items():
    if count > 1:
        duplicates.append(item)

# Выводим результат
print(duplicates) 