import time

import scrapy
from biqugescrapy.items import BiqugescrapyItem

class BiqugeSpider(scrapy.Spider):

    name = 'biquge'
    # allowed_domains = ['https://www.xbiquge.la/0/10/']
    start_urls = ['https://www.xbiquge.la/paihangbang/']
    def parse(self, response):
        ranking_list = response.xpath('//*[@id="main"]/div[2]/ul[1]/li')  # 定位到所有li
        for li in ranking_list[1:3]:  # 遍历前三名小说的li
            novel_name = li.xpath('./a/text()').extract_first()  # 解析到该li中的名字
            novel_link = li.xpath('./a/@href').extract_first() # 解析到该li中的链接
            yield scrapy.Request(novel_link,callback=self.parse_chapter,meta={"novel_name":novel_name})#手动请求小说链接，请求后交给parse_chapter函数，并通过meta携带当前函数解析出来的内容，即novel_name与novel_link,解析章节列表

    def parse_chapter(self,response):
        chapter_list=response.xpath('//div[@id="list"]/dl[1]/dd')
        novel_name=response.meta["novel_name"]
        for dd in chapter_list[0:4]:
            chapter_name = dd.xpath('./a/text()').extract_first()  # 章节名
            chapter_link = "https://www.xbiquge.la/" + dd.xpath('./a/@href').extract_first()  # 章节链接
            yield scrapy.Request(chapter_link,callback=self.parse_detail,meta={"chapter_name":chapter_name,"novel_name":novel_name})

    def parse_detail(self,response):
        item=BiqugescrapyItem()
        word=response.xpath('//div[@id="content"]/text()').extract()
        word="".join(word)
        novel_name=response.meta["novel_name"]
        chapter_name=response.meta["chapter_name"]
        item['word'] = word
        item['novel_name']=novel_name
        item["chapter_name"]=chapter_name

        yield item

