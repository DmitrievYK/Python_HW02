import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem
from scrapy.loader import ItemLoader


class LabSpider(scrapy.Spider):
    name = "lab"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/search/%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0/?stype=0"]

    def parse(self, response:HtmlResponse):
        url = "https://www.labirint.ru/"

        # print(response.status, response.url)

        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        
        links = [response.urljoin(link) for link in response.xpath("//a[@class='product-card__name']/@href").getall()]
        # links = response.xpath("//a[@class='product-card__name']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)

    
    def book_parse(self, response:HtmlResponse):
        #Сбор имени, ссылки, цен, аннотации
        name = response.xpath("//h1/text()").get()
        url = response.url
        price = response.xpath("//div[@class='buying']//span[contains(@class, 'number')]//text()").getall()
        annotation_book = response.xpath("//div[@id='product-about']//p//text()").getall()

        #Если не найдем имя книги выведем сообщение в лог, если нет цены то запишем null в значение
        if not name:
            self.logger.warning('Название книги не найдено.')
        if not price:
            price=None

        yield JobparserItem(name=name, url=url, price=price, annotation_book=annotation_book)
