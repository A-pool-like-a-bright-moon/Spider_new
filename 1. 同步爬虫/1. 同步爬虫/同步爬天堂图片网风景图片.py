import os
from builtins import FileExistsError, str, int
from io import open
from time import sleep

import requests
from lxml import etree

headers={
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

url="https://www.ivsky.com/bizhi/fengjing/"
def req(url):
    response=requests.get(url=url,headers=headers).text
    tree=etree.HTML(response)
    li_list=tree.xpath("//body/div[3]/div[4]/ul/li")
    for li in li_list[0:3]:
        i = 1
        ima_name_all=li.xpath("./div/a/@title")[0]#合集名
        path="C:\\Users\\42406\\Spider\\爬取结果存放夹\\"
        try:
            if os.path.exists(path):
                os.mkdir(path+ima_name_all)
        except FileExistsError as e:
            print("文件夹已存在")
        ima_name=li.xpath("./div/a/img/@alt")[0]#合集内图片名
        ima_link_all="https://www.ivsky.com"+li.xpath("./div/a/@href")[0]#合集链接
        img_all=requests.get(ima_link_all,headers).text
        img_all_tree=etree.HTML(img_all)
        img_list=img_all_tree.xpath("/html/body/div[3]/div[4]/ul/li")

        for link in img_list:
            i=str(i)
            img_link="https:"+link.xpath("./div/a/img/@src")[0]
            image=requests.get(img_link,headers).content
            with open(path+ima_name_all+'\\'+ima_name+i+'.jpg',"wb") as fp:
                fp.write(image)
                sleep(0.8)
                i=int(i)
                i+=1
if __name__=="__main__":
    req(url)


