import scrapy
from price_parser import Price


def get_price(price_raw):
    price_object = Price.fromstring(price_raw)
    return price_object.amount_float


def get_currency(price_raw):
    price_object = Price.fromstring(price_raw)
    currency = price_object.currency
    return currency


class BeforeSpider(scrapy.Spider):
    name = 'before'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.xpath('//ol[@class="row"]/li'):
            title_xpath = './/img/@alt'
            price_xpath = './/*[@class="price_color"]/text()'
            available_xpath = './/*[@class="instock availability"]/text()'

            price_raw = s.xpath(price_xpath).get()
            price = get_price(price_raw)
            currency = get_currency(price_raw)

            available = []
            for data in s.xpath(available_xpath).getall():
                available.append(data.strip())

            item = dict()
            item['title'] = s.xpath(title_xpath).get()
            item['available'] = ''.join(available)
            item['price'] = price
            item['currency'] = currency
            yield item
