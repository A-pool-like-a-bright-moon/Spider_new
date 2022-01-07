# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NitianproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    contxt=scrapy.Field()
    dd_name=scrapy.Field()
    novel_name=scrapy.Field()
