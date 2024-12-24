# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from datetime import datetime as dt
from calendar import isleap 

def check_date(date:str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _is_leap_year(t.year)
        return True
    except ValueError:
        return False
def _is_leap_year(year:int):
    print('Високосный' if isleap(year) else 'Не високосный') 

parser = argparse.ArgumentParser(description='Check date.')
parser.add_argument('date', type=str, help='Date to check in the format YYYY-MM-DD')

args = parser.parse_args()
print(check_date(args.date))

# if __name__ == "__main__":
#     print(check_date(args.date))
