import requests
from lxml import etree
import pandas as pd

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "referer":"https://shanghai.anjuke.com/"
}

url = "https://sh.fang.anjuke.com/loupan/pudong/?from=SearchBar"
# page = requests.get(url=url,headers=headers).text

"""
本地测试
"""
# with open("1.html",'w',encoding="utf-8") as fp:
#     page_new= fp.write(page)
tree=etree.HTML(open('1.html',encoding='utf-8').read())

# tree=etree.HTML(page)
normal = tree.xpath('//*[@id="container"]/div[2]/div[1]/div[3]/div')
info_list = []
for i in normal:
    # 房源名
    name=i.xpath('./div/a[1]/span/text()')[0]
    # print(name)

    # 区名
    descri = i.xpath('./div/a[2]/span/text()')[0]
    district = descri.split()[1]
    # print(district)

    # 镇名
    town = descri.split()[2]
    # print(town)

    # # 街道名
    street = descri.split()[4]
    # print(street)

    # 价格
    price = i.xpath("./a[2]/p/span/text()")[0]
    # print(price)

    # 户型
    span_num =i.xpath("./div/a[3]/span")
    house_type = "".join(i.xpath("./div/a[3]//text()")[1:-2])
    # print(house_type)

    # 建筑面积
    area = span_num[-1].xpath(".//text()")[0].split("：")[-1]

    # 特点
    feature ="".join(i.xpath('./div/a[4]/div//text()'))
    feature = feature.replace(" ","").replace("\n","")
    # print(feature)
    # print(name,district,town,street,price,house_type,area,feature)

    info_list.append({"小区名":name,"所属区":district,"所属镇":town,"街道":street,"起步价格":price,"户型":house_type,"面积":area,"特点":feature})

# 持久化存储
df = pd.DataFrame(info_list,columns=["小区名","所属区","所属镇","街道","起步价格","户型","面积","特点"])
df.to_csv("./浦东新区安居客房源.csv",encoding='utf-8-sig')