# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class TiantangimageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image=scrapy.Field()
    img_name_catagory=scrapy.Field()#合集名
    img_links=scrapy.Field()#图片链接

