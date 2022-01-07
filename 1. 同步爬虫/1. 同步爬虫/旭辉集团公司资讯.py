import requests
from lxml import  etree
import time



t = str(int(round(time.time())))

headers={
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
'Referer':'https://www.cifi.com.cn/',
    'cookie':'_pk_ref.5.8790=%5B%22%22%2C%22%22%2C1641533195%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dc_79crHEff3HSS0EZGnDja2W_rYJfVs3lASlHlxA12X7O5bjL_nn6jCOUGrRr3JW%26wd%3D%26eqid%3D8616b2c90000604c0000000461d7cf06%22%5D; _pk_ses.5.8790=*; tj95eceba51d1749cd98415c14e7456b=1; PHPSESSID=hum4ri33fjuik00d13ds4rg8t1; Z0fLYP_think_language=zh-CN; _pk_id.5.8790=4a0b5bff4af3d7f3.1641364657.8.'+t+'.1641533193.; KLBRSID=334f0aaa0a3320c81e681fc961c6aaf3|'+t+'|1641533193',
    'Origin': 'https://www.cifi.com.cn'
}


url = 'https://www.cifi.com.cn/news/index_2.html'
# page = requests.get(url=url,headers=headers).text

"""
本地测试
"""
# with open("xuhui.html",'w',encoding="utf-8") as fp:
#     page_new= fp.write(page)
tree=etree.HTML(open('xuhui.html',encoding='utf-8').read())

# tree = etree.HTML(page)
ul = tree.xpath("//div[@class='news_list02']/ul/li")
for li in ul[1:3]:
    name = li.xpath("./h3/a/text()")[0]
    href = 'https://www.cifi.com.cn'+ li.xpath("./h3/a/@href")[0]
    content_page = requests.get(url=href,headers=headers).text
    tree2 = etree.HTML(content_page)
    content = tree2.xpath('//div[@class="news_edit"]//p//text()')
    content = ''.join(content)
    print(name,href,content)
