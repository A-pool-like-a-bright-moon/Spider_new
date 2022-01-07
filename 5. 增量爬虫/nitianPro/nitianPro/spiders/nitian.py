import scrapy
from redis import Redis
from nitianPro.items import NitianproItem


class NitianSpider(scrapy.Spider):
    name = 'nitian'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.bswtan.com/13/13510/']
    #创建redis连接对象
    conn = Redis(host='127.0.0.1',port=6379)

    #爬到所有章节和章节链接，后续再爬的时候不会爬爬过的
    def parse(self, response):
        chapter_list=response.xpath('//*[@id="list"]/dl/dd')
        novel_name=response.xpath('//*[@id="info"]/h1/text()').extract_first()
        for dd in chapter_list[0:3]:
            dd_href = "https://www.bswtan.com/13/13510/" + dd.xpath('.//@href').extract_first()
            dd_name=dd.xpath('./a/text()').extract_first()
            #将章节url存入redis的set中
            ex = self.conn.sadd('urls',dd_href)
            if ex ==1:
                print('该章节没有被爬取过，可以进行数据爬取')
                yield scrapy.Request(url=dd_href,callback=self.parse_detail,meta={'dd_name':dd_name,'novel_name':novel_name})
            else:
                print('该章节已经收录过，暂无新数据可爬')


    #没有爬过的章节，进入章节详情页爬取该章节的内容
    def parse_detail(self,response):
        novel_name=response.meta['novel_name']
        contxt=response.xpath('//*[@id="content"]/text()').extract()
        contxt=''.join(contxt)
        dd_name=response.meta['dd_name']
        item=NitianproItem()
        item['novel_name']=novel_name
        item['contxt']=contxt
        item['dd_name']=dd_name
        yield item

