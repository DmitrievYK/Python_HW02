# перевод pickle в csv

import csv
import pickle
from pathlib import Path

def pickle_to_csv(file:Path):
    with(open(file, "rb") as f_read,
    open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f_write):
        data = pickle.load(f_read)

        keys = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)

        csv_write.writeheader()
        csv_write.writerows(data)

if __name__ == "__main__":
    pickle_to_csv(Path('new_db.pickle'))

