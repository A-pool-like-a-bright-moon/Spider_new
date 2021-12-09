import asyncio
import os
from builtins import FileExistsError

import aiohttp
import aiofiles
import requests
import time
from lxml import etree

#总体思路：和同步爬取目的相同，过程中将涉及堵塞的部分做成协程，目的是爬取每本小说中的章节内的文字内容，不能每个步骤都用协程处理，这样的话会乱掉，应该从最后一级的堵塞操作开始做协程，即爬取小说内容那一步

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}


async def aiodownload(chapter_link,chapter_name):
    async with aiohttp.ClientSession(headers=headers) as session:#创建一个协程请求会话
        async with await session.get(url=chapter_link, headers=headers) as chapter_detail:
            chapter_detail = await chapter_detail.text()
            chapter_detail_tree = etree.HTML(chapter_detail)
            word = chapter_detail_tree.xpath('//div[@id="content"]/text()')  # 页面文字太多时，pycharm控制台打印出来会不全，保存在本地就可以看到
            word = "".join(word)

            async with aiofiles.open("C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\" + novel_name+"\\"+ chapter_name + '.txt', mode="w",encoding='utf-8') as file:  # open模块是IO操作的，不是os里面的
                await file.write(word)
                print(chapter_name + "下载成功咯！")
async def getcatalog(url):
    novel_detail = requests.get(url=url, headers=headers)  # 该小说详情页内容
    novel_detail.encoding = novel_detail.apparent_encoding  # 编码成 该是的 编码方式
    novel_detail = novel_detail.text
    detail_tree = etree.HTML(novel_detail)  # 实例化此详情页
    chapter_list = detail_tree.xpath('//div[@id="list"]/dl[1]/dd')  # 定位到所有dd
    tasks=[]
    for dd in chapter_list[0:4]:
        chapter_name = dd.xpath('./a/text()')[0]  # 章节名
        chapter_link = "https://www.xbiquge.la/" + dd.xpath('./a/@href')[0]  # 章节链接
        task=asyncio.create_task(aiodownload(chapter_link,chapter_name))
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_url="https://www.xbiquge.la/paihangbang/"
    respon = requests.get(url=book_url, headers=headers).text  # 页面全部内容
    tree = etree.HTML(respon)  # 实例化etree对象
    ranking_list = tree.xpath('//*[@id="main"]/div[2]/ul[1]/li')  # 定位到所有li
    for li in ranking_list[1:4]:#遍历前三名的li
        novel_name =li.xpath('./a/text()')[0]#解析到该li中的名字
        url=li.xpath('./a/@href')[0]#解析到该li中的链接
        path = "C:\\Users\\42406\\Desktop\\Spider\\爬取结果存放夹\\"
        try:
            if os.path.exists(path):
                os.mkdir(path + novel_name)  # 注意：拼接路径带参数要在这里面拼接，而不是拼接好放进来
                print(novel_name + "文件夹创建成功！")
        except FileExistsError as e:
            print(novel_name + "文件夹已经创建过！")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getcatalog(url))