# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):

    pass

class detail_item(scrapy.Item):
    img_name=scrapy.Field()
    img_href=scrapy.Field()

