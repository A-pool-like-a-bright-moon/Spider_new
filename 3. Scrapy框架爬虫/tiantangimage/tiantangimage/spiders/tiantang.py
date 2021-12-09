import scrapy
from tiantangimage.items import TiantangimageItem

class TiantangSpider(scrapy.Spider):
    name = 'tiantang'
    # allowed_domains = ['www.ivsky.com/bizhi/fengjing']
    start_urls = ['https://www.ivsky.com/bizhi/fengjing/']

    def parse(self, response):
        li_list = response.xpath("//body/div[3]/div[4]/ul/li")
        for li in li_list[0:3]:
            img_name_catagory = li.xpath("./div/a/@title").extract_first()  # 合集名
            img_link_catagory = "https://www.ivsky.com" + li.xpath("./div/a/@href").extract_first()  # 合集链接
            yield scrapy.Request(img_link_catagory,callback=self.parse_image_list,meta={"img_name_catagory":img_name_catagory})


    def parse_image_list(self,response):
        item=TiantangimageItem()
        img_name_catagory=response.meta["img_name_catagory"]#合集名
        img_links = response.xpath("/html/body/div[3]/div[4]/ul/li//@src").getall()
        item["img_name_catagory"]=img_name_catagory
        item["img_links"]=img_links
        yield item



