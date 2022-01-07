import requests
from lxml import  etree
import pandas as pd
import re

headers={
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Referer": "https://sh.newhouse.fang.com/house/s/"
}

url = 'https://sh.newhouse.fang.com/house/s/pudong/'
# page = requests.get(url=url,headers=headers).text

#本地测试
# with open('fangtianxia.html','w',encoding='utf-8') as fp:
#     fp.write(page)

tree = etree.HTML(open('./fangtianxia.html',encoding='utf-8').read())
# tree = etree.HTML(page)
li_list = tree.xpath('//*[@id="newhouse_loupan_list"]/ul/li')
info_list =[]
for li in li_list:
    # 小区名
    name = ''.join(li.xpath('./div/div[2]/div[1]/div[1]//text()')).strip()
    # 户型
    house_type = ''.join(li.xpath('./div/div[2]/div[2]//text()')[0:-1]).strip().replace('\n','')
    house_type = re.sub('\t+','',house_type)
    # 建筑面积
    area = ''.join(li.xpath('./div/div[2]/div[2]/text()')).replace('—','').replace('/','').strip()
    # 区
    district = ''.join(li.xpath('./div/div[2]/div[3]/div[1]/a/span/text()')).strip().replace('[','').replace(']','')
    # 街道
    street = ''.join(li.xpath('./div/div[2]/div[3]/div[1]/a/text()')).strip()
    # 价格
    price = ''.join(li.xpath('./div/div[2]/div[5]/span/text()')).strip()
    # 电话
    phone = ''.join(li.xpath('./div/div[2]/div[3]/div[2]/p//text()')).strip()
    # 特点
    feature = ''.join(li.xpath('./div/div[2]/div[4]//text()')).strip().replace('\n','\t')
    feature = re.sub('\t+', ' ', feature)

    info_list.append({"小区名": name, "所属区": district, "街道": street, "起步价格": price, "户型": house_type, "面积": area,"特点": feature,"电话":phone})

# 持久化存储
df = pd.DataFrame(info_list,columns=["小区名","所属区","街道","起步价格","户型","面积","特点","电话"])
df.to_csv("./浦东新区房天下房源.csv",encoding='utf-8-sig')