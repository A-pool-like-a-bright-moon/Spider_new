# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from builtins import FileExistsError
from io import open
import os

from itemadapter import ItemAdapter


class BiqugescrapyPipeline:#重写父类，让这个函数只在爬虫开始时执行一次，避免重复创建打开文件夹


    def process_item(self, item, spider):
        chapter_name=item['chapter_name']
        word=item['word']
        word="".join(word)
        novel_name=item['novel_name']
        dir="C:\\Users/42406\\Spider\爬取结果存放夹\\" + novel_name
        if not os.path.exists(dir):
            os.makedirs(dir)


        with open ("C:\\Users/42406\\Spider\爬取结果存放夹\\" + novel_name + '\\' + chapter_name+".txt",mode='w',encoding='utf-8') as file:  # open模块是IO操作的，不是os里面的
            file.write(word)
            print(chapter_name + "下载成功咯！")
        return item
