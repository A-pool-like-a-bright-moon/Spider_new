# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class Img699PicItem(scrapy.Item):
     # 分类的标题
     category=scrapy.Field()
     # 存放图片地址
     image_urls=scrapy.Field()
     # 下载成功后返回有关images的一些相关信息
     images=scrapy.Field()


