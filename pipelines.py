# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from jobparser.items import JobparserItem

# class JobparserPipeline:
#     def process_item(self, item, spider):
#         return item

class JobparserPipeline:
    def open_spider(self, spider):
        self.file = open('books.json', 'w', encoding='utf-8')  # Открываем файл для записи данных

    def close_spider(self, spider):
        self.file.close()  # Закрываем файл по завершении работы паука

    def process_item(self, item, spider):        
        price_data = item.get('price')

        if price_data is None:
            item['price'] = None
        elif isinstance(price_data, list): #проверка price_data является ли списком
            # Удаляем лишние пробелы и преобразуем элементы списка вint, если возможно
            price_data = [int(price.strip().replace('₽', '').replace(' ', '')) for price in price_data if price.strip()]

            if len(price_data) > 1:
                # Если две цены
                item['price'] = {
                    'price_old': price_data[0],
                    'price_new': price_data[1],
                }
            elif len(price_data) == 1:
                # Если одна цена
                item['price'] = {
                    'price': price_data[0],
                }
            else:
                item['price'] = None
        else:
            item['price'] = None

        # Преобразуем все поля в строки
        item['name'] = str(item['name'])
        item['url'] = str(item['url'])
        item['annotation_book'] = str(item['annotation_book'])

        # Сохраняем item в JSON формате
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)  # Записываем строку в файл

        return item