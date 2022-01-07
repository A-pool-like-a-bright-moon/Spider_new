# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from io import open
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NitianproPipeline:
    def process_item(self, item, spider):
        dd_name=item['dd_name']
        contxt=item['contxt']
        contxt=''.join(contxt)
        novel_name=item['novel_name']
        dir = "C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\" + novel_name
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open ("C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\" + novel_name + '\\' + dd_name+".txt",mode='w',encoding='utf-8') as file:  # open模块是IO操作的，不是os里面的
            file.write(contxt)
            print(dd_name + "下载成功咯！")
        return item
