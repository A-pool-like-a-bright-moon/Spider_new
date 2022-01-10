# 许多网站采用验证码来反爬虫，验证码有普通图形验证码、极验滑动验证码、点触验证码、微博宫格验证码等等。
import tesserocr
from PIL import Image
import time
import requests

# 获取验证码
yzm_headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    'Referer':'http://my.cnki.net/elibregister/commonRegister.aspx'
}
t = int(time.time()*1000)

yzm_code = 'http://my.cnki.net/elibregister/CheckCode.aspx?id='+str(t)
yzm = requests.get(url=yzm_code,headers=yzm_headers).content
with open('yzm.jpg','wb') as fp:
    fp.write(yzm)


'''
# 处理图片验证码
image = Image.open('yzm.jpg')  # 利用本地的CheckCode.jpg文件新建了一个Image对象
text = tesserocr.image_to_text(image)  # 调用tesserocr的image_to_text()方法进行文本的识别
print(text)
'''

# 上述方法识别的实际结果会有偏差，这是因为验证码内的多余线条干扰了图片的识别，对于这种情况，我们需要优先对图片进行相关处理——灰度转换、二值化操作等
image = Image.open('yzm.jpg')
image = image.convert('L')  # convert()方法传入参数L可以将图片转化为灰度图像。如果传入数字1即可进行二值化处理。
threshold = 140  # 指定二值化的阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')  # 通过查找表或函数映射此图像 处理成二值化
result = tesserocr.image_to_text(image)
print(result)
data = {'cnkiUserName' : 'uwermengchenyang',
        'cnkiPsd':'mengchenyang',
        'cnkiEmail' : '4257@qq.comn',
        'cnkiValidate' : yzm
        }