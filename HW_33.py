# Напишите программу банкомат. Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти, сумма пополенения или снятия карты 50 у.е.
# процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счете
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)

def menu(balance: Decimal, count: int, flag: bool, operations: list):
    dct = {'intro': 'Добро пожаловать в Банкомат CityBank',
           '1':'Пополнить счет',
           '2':'Снять со счета',
           '3':'Выйти из меню',
           '4':'История операций'} # Добавлена кнопка для просмотра истории операций
    
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}:  {v}')
        else:
            print(v)
    if balance >= LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
    
    choice = input('Выберите команду:')
    if choice == "3":
        print(balance)
        flag = False
        return balance, flag, operations
    elif choice == "1":
        balance, operations = give_money(balance, operations)
        count += 1
    elif choice == "2":
        balance, operations = get_money(balance, operations)
        count += 1
    elif choice == "4":
        print("\nИстория операций:")
        for operation in operations:
            print(operation)
    else:
        print('Неверная команда')
    
    if count % 3 == 0:
        balance *= (1 + BONUS)
    print(balance)
    return balance, flag, operations

def get_money(balance: Decimal, operations: list):
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION
    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION
        if money_to_get + procent <= balance:
            balance -= (money_to_get + procent)  #
            operations.append(f'Снятие: {money_to_get}, Комиссия: {procent}')  # 
            return balance, operations
        else:
            print('Недостаточно средств для снятия')
            return balance, operations
    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50')
        return balance, operations


def give_money(balance: Decimal, operations: list):
    money_to_give = Decimal(input('Введите сумму пополнения: '))
    if money_to_give % MIN_SUM == 0:
        balance += money_to_give  # 
        operations.append(f'Пополнение: {money_to_give}')  # 
        return balance, operations
    else:
        print('Сумма не кратна 50')
        return balance, operations

if __name__ == "__main__":
    print('Добро пожаловать в Банкомат CityBank')
    balance = 0
    count = 1
    flag = True
    operations = []  # Хранение операций
    while flag:
        balance, flag, operations = menu(balance, count, flag, operations)