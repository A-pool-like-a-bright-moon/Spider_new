import requests
from lxml import etree
import pandas as pd

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    # "referer":"https://sh.fang.lianjia.com/loupan/pudong/"
}

# url = 'https://sh.fang.lianjia.com/loupan/pudong/#pudong'
#
# page = requests.get(url=url,headers=headers).text

'''
本地测试
'''
# with open('lianjia.html','w',encoding='utf-8') as fp:
#     fp.write(page)


tree = etree.HTML(open('lianjia.html',encoding='utf-8').read())
ul = tree.xpath('/html/body/div[3]/ul[2]/li')
info_list = []
for li in ul:

    # 小区名
    name = li.xpath('./div[1]/div[1]/a/text()')[0]

    # 性质
    nature = li.xpath('./div[1]/div[1]/span[1]/text()')[0]

    # 状态
    state = li.xpath('./div[1]/div[1]/span[2]/text()')[0]

    # 区名
    district = li.xpath('./div[1]/div[2]/span[1]/text()')[0]

    # 镇名
    town = li.xpath('./div[1]/div[2]/span[2]/text()')[0]

    # 街道
    street =li.xpath('./div[1]/div[2]/a/text()')[0]

    # 户型
    house_type = li.xpath('./div[1]/a//text()')[0]

    # 建筑面积
    try:
        area = li.xpath('./div[1]/div[3]/span/text()')[0].split(' ')[1]
    except IndexError:
        area = '未知'

    # 价格
    price = li.xpath('./div[1]/div[6]/div/span[1]/text()')[0]

    #特点
    feature = ''.join(li.xpath('./div[1]/div[5]//text()')).replace(' ','').replace("\n",",").strip(',')
    info_list.append({"小区名":name,'性质':nature,"所属区":district,"所属镇":town,"街道":street,"户型":house_type,"面积":area,"价格":price,"特点":feature})

# 持久化存储
df = pd.DataFrame(info_list,columns=["小区名",'性质',"所属区","所属镇","街道","户型","面积",'价格',"特点"])
df.to_csv("./浦东新区链家房源.csv",encoding='utf-8-sig')



