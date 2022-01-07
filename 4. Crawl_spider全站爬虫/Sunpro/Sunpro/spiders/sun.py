import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sunpro.items import SunproItem,detail_item

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.58pic.com/piccate/53-0-0-p3.html']#起始url
    link1=LinkExtractor(allow=r'piccate/53-0-0-p[0-9]\.html')#第一个链接提取器，提取每页的链接
    link2=LinkExtractor(allow=r'www\.58pic\.com/newpic/\d+\.html')#第二个链接提取器，提取图片详情页的链接

    rules = (
        Rule(link1, callback='parse_item', follow=True),

        Rule(link2,callback='parse_detail',follow=False)
    )
    def parse_item(self, response):#解析图片名
        # img_list=response.xpath('/html/body/div[3]/div[5]/div[1]/div')
        # for i in img_list:
        #     img_name=i.xpath('./a/div[2]/div[1]/p/text()').extract_first()
        #     print(img_name)
        # item=SunproItem()
        pass
    def parse_detail(self,response):#进入到详情页，下载大图
        img_href="https:"+response.xpath('/html/body/div[3]/div[3]/div[3]/div[1]/div[2]/div[1]/img/@src').extract_first()
        img_name=response.xpath('/html/body/div[3]/div[3]/div[3]/div[1]/div[2]/div[1]/img/@alt').extract_first()
        item=detail_item()
        item['img_name']=img_name
        item['img_href']=img_href
        yield item
