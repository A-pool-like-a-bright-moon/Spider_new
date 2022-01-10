import requests
from lxml import etree
import re
from fontTools.ttLib import TTFont


'''
获取加密字符映射关系
'''
font_url = 'https://www.shixiseng.com/interns/iconfonts/file?rand=0.7354002191093427'
headers_font = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Referer' : 'https://www.shixiseng.com/'
}
font_response = requests.get(font_url, headers=headers_font)
# 文件类型未知，因此用使用content格式
font_data = font_response.content
# 保存到本地
with open('加密font文件_sxs.woff', 'wb') as f:
    f.write(font_data)
# 解析加密的font文件
font_obj = TTFont('加密font文件_sxs.woff')
# 将文件转成明文的xml文件
font_obj.saveXML('加密font文件_sxs.xml')


# 获取字体加密的关系映射表
cmap_list = font_obj.getBestCmap()
# 字典的key值会自动转成十进制，用字典推导式把key值转回到十六进制
cmap_dict ={hex(k):v for k,v in font_obj['cmap'].getBestCmap().items()}
print('字体加密关系映射表：', cmap_list)
with open('加密font文件_sxs.xml') as f:
    xml=f.read()
    keys=re.findall('<map code="(0x.*?)" name="uni.*?"/>',xml)[:99]
    values=re.findall('<map code="0x.*?" name="uni(.*?)"/>',xml)[:99]
    for i in range(len(values)):
        if len(values[i])<4:#字母和数字 编码再解码成unicode_escape形式
            values[i]=('\\u00'+values[i]).encode('utf-8').decode('unicode_escape')
        else:#汉字
            values[i]=('\\u'+values[i]).encode('utf-8').decode('unicode_escape')
    word_dict=dict(zip(keys, values))

'''
以上已经获取了加密字符关系，下面开始解析原文
'''
url ='https://www.shixiseng.com/interns?keyword=%E6%8A%80%E6%9C%AF&city=%E5%85%A8%E5%9B%BD&type=intern&from=menu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
# 发送请求，获取响应
response = requests.get(url=url, headers=headers).text.replace('&#','0')
py_data = etree.HTML(response)
# 提取文本中的目标数据
title_list = py_data.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div')
for i in title_list:
    title =i.xpath('./div[1]/div[1]/p[1]/a/@title')
    title = title[0].replace('&#','0')

    # 替换字符串中的乱码为映射字典的值
    for old, new in word_dict.items():
        title = title.replace(old, new)
    print(title)


