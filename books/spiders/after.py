import scrapy
from itemloaders import ItemLoader

from books.items import BooksItem


class AfterSpider(scrapy.Spider):
    name = 'after'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            loader = ItemLoader(item=BooksItem(),
                                selector=s)

            title_xpath = './/img/@alt'
            price_xpath = './/*[@class="price_color"]/text()'
            available_xpath = './/*[@class="instock availability"]/text()'
            available_xpath2 = './/*[@class="instock availability"]'

            loader.add_xpath('title', title_xpath)
            loader.add_xpath('price', price_xpath)
            loader.add_xpath('currency', price_xpath)
            loader.add_xpath('available', available_xpath)
            loader.add_xpath('available2', available_xpath2)

            item = loader.load_item()
            yield item
