import json
# from builtins import print, str
import os
import time
from io import open
import asyncio
import aiohttp
import aiofiles
import requests
import time
from lxml import etree

url = "https://www.xbiquge.la/paihangbang/"#爬取新笔趣阁小说

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}


def req():
    respon = requests.get(url=url, headers=headers).text  # 页面全部内容
    tree = etree.HTML(respon)  # 实例化etree对象
    ranking_list = tree.xpath('//*[@id="main"]/div[2]/ul[1]/li')#定位到所有li
    a=input("请问您想爬取排行榜的第几到几名的小说呢？（请输入起始名次）：")
    b=input("请输入末尾名次：")
    a=int(a)
    b=int(b)+1
    for li in ranking_list[a:b]:#遍历前三名的li
        novel_name =li.xpath('./a/text()')[0]#解析到该li中的名字
        novel_link=li.xpath('./a/@href')[0]#解析到该li中的链接
        novel_detail=requests.get(url=novel_link,headers=headers)#该小说详情页内容
        novel_detail.encoding = novel_detail.apparent_encoding#编码成 该是的 编码方式
        novel_detail=novel_detail.text
        detail_tree=etree.HTML(novel_detail)#实例化此详情页
        chapter_list=detail_tree.xpath('//div[@id="list"]/dl[1]/dd')#定位到所有dd
        path="C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\"
        try:
            if os.path.exists(path):
                os.mkdir(path+novel_name)#注意：拼接路径带参数要在这里面拼接，而不是拼接好放进来
                print(novel_name+"文件夹创建成功！")
        except FileExistsError as e:
            print(novel_name+"文件夹已经创建过！")

        time1=time.time()
        c=int(0)
        d=int(3)+1
        for dd in chapter_list[c:d]:
            chapter_name=dd.xpath('./a/text()')[0]#章节名
            chapter_link="https://www.xbiquge.la/"+dd.xpath('./a/@href')[0]#章节链接
            # print(chapter_name,chapter_link)#打印测试
            chapter_detail=requests.get(url=chapter_link,headers=headers)#章节详情页内容
            chapter_detail.encoding=chapter_detail.apparent_encoding
            chapter_detail=chapter_detail.text
            chapter_detail_tree=etree.HTML(chapter_detail)
            word=chapter_detail_tree.xpath('//div[@id="content"]/text()')#页面文字太多时，pycharm控制台打印出来会不全，保存在本地就可以看到
            word="".join(word)
            with open("C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\"+novel_name+'\\'+chapter_name+".txt",mode='w',encoding='utf-8') as file:#open模块是IO操作的，不是os里面的
                file.write(word)
                print(chapter_name+"下载成功咯！")
        time2=time.time()
        print(f"耗时{time2-time1}秒")
if __name__ == '__main__':
    req()