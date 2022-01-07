# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline#导入scrapy框架的图片下载类

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import Request
from Sunpro.settings import IMAGES_STORE
import scrapy

class SunproPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 是用来对媒体资源进行请求（数据下载），参数item就是接收到的爬虫类提交item对象
        if item.__class__.__name__=="detail_item":
            yield scrapy.Request(item['img_href'],meta={"item":item})

        # 指明输数据存储的路径
    def file_path(self, request, response=None, info=None):
        img_name=request.meta['item']['img_name']
        path = IMAGES_STORE + "/" +img_name +'.jpg'
        print(img_name + "下载完成")
        return path

