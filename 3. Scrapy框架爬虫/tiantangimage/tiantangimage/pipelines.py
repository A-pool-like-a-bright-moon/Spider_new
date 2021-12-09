# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

# class TiantangimagePipeline:
#     def process_item(self, item, spider):
#         return item
#以上这个原生管道类不能帮我们把图片链接进行请求发送

#基于imagepipeline封装一个管道类
from scrapy.pipelines.images import ImagesPipeline#导入scrapy框架的图片下载类
from scrapy.exceptions import DropItem
from scrapy.http import Request
from tiantangimage.settings import IMAGES_STORE
import os
import scrapy

class TianTangspiderPipeline(ImagesPipeline):

    #根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        for img_link in item["img_links"]:
            img_link="https:"+img_link
            yield scrapy.Request(img_link,meta={"item":item})

    #指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        title=request.meta["item"]["img_name_catagory"]
        name=request.url.split("/")[-1]
        print(title,name)
        path=IMAGES_STORE + "/" + title + "/" + name
        print(name+"下载完成")
        return path


    #路径需要在setting配置文件中设置：IMAGES_STORE = ""
    # def item_completed(self, results, item, info):
    #     image_path=[x['path'] for ok,x in results if ok]
    #     #定义分类保存的路径
    #     img_path="%s/%s" % (self.IMAGES_STORE,item["img_name_catagory"])
    #     if os.path.exists(img_path)==False:
    #         os.mkdir(img_path)
    #     #将文件从默认目录下移动到指定目录下
    #     shutil.move(self.IMAGES_STORE + "/" +image_path[0],img_path)