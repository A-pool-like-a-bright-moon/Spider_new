from builtins import FileExistsError
from lxml import etree
import aiohttp,aiofiles,os,asyncio
import requests

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

url="https://www.ivsky.com/bizhi/fengjing/"

async def aiodownload(image_link,i):  # 协程方式的函数
    async with aiohttp.ClientSession(headers=headers) as session:#创建一个协程会话对象，相当于同步的requests
        async with await session.get(url=image_link) as image:#发起请求，发起网络请求是堵塞的，所以用await挂起
            image=await image.read()
            i=str(i)
            async with aiofiles.open(path + ima_name_all + '\\' + ima_name + i + '.jpg', "wb") as fp:
                await fp.write(image)
                print(ima_name + i + ".jpg下载成功。")


async def get_collection_link(ima_link_all):
    img_all = requests.get(ima_link_all, headers).text #合集页面
    img_all_tree = etree.HTML(img_all)
    img_list = img_all_tree.xpath("/html/body/div[3]/div[4]/ul/li")
    tasks=[]
    for i,link in enumerate(img_list):
        image_link = "https:" + link.xpath("./div/a/img/@src")[0] #每张图片的链接
        task=asyncio.create_task(aiodownload(image_link,i))
        tasks.append(task)
    await asyncio.wait(tasks)
if __name__ == "__main__":
    response = requests.get(url=url).text  # 相当于读，阻塞操作，await挂起
    tree = etree.HTML(response)
    li_list = tree.xpath("//body/div[3]/div[4]/ul/li")
    for li in li_list[0:3]:#爬取前三个合集
        i = 1
        ima_name_all = li.xpath("./div/a/@title")[0]  # 合集名
        ima_name = li.xpath("./div/a/img/@alt")[0]  # 合集内图片名
        ima_link_all = "https://www.ivsky.com" + li.xpath("./div/a/@href")[0]  # 合集链接
        path = "C:\\Users\\42406\\Spider\\爬取结果存放夹\\"
        try:
            if os.path.exists(path):
                os.mkdir(path + ima_name_all)
        except FileExistsError as e:
            print("文件夹已存在")
        asyncio.run(get_collection_link(ima_link_all))