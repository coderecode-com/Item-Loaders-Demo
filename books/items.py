# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import (TakeFirst,
                                    MapCompose)
from price_parser import Price
from w3lib.html import remove_tags


def get_price(price_raw):
    price_object = Price.fromstring(price_raw)
    return price_object.amount_float


def get_currency(price_raw):
    price_object = Price.fromstring(price_raw)
    currency = price_object.currency
    return currency


class BooksItem(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()  # calling method
    )
    price = scrapy.Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()  # calling method
    )
    available = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()  # calling method
    )
    available2 = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()  # calling method
    )

    currency = scrapy.Field(
        input_processor=MapCompose(get_currency),
        output_processor=TakeFirst()  # calling method
    )
