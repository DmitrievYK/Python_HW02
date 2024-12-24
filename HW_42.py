# Напишите однострочный генератор словаря, который принимает на вход три 
# списка одинаковой длины: имена str, ставка int, премия str с указанием 
# процентов вида “10.25%”. В результате получаем словарь с именем в качестве 
# ключа и суммой премии в качестве значения. Сумма рассчитывается как 
# ставка умноженная на процент премии

def calculate_bonus(names, rates, bonuses):
    return {name: rate * (float(bonus[:-1]) / 100) for name, rate, bonus in zip(names, rates, bonuses)}

# пример для запуска
names = ["Аня", "Вася", "Дед Максим"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "15%", "20%"]

result = calculate_bonus(names, rates, bonuses)
print(result) 