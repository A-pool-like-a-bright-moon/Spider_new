import requests
import execjs
import re

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "referer":"https://passport.kongzhong.com/"
}
url = "https://sso.kongzhong.com/ajaxLogin?j=j&&type=1&service=https://passport.kongzhong.com/&username=424062057%40qq.com&password=312d18c823da00b91420&vcode=cv50&toSave=0&_=1641217014576"
# 获取密钥dc
page = requests.get(url=url,headers=headers).text
# print(page)
ex = '"dc":"(.*?)","kzmsg"'
dc = re.findall(ex,page)[0]
# print(dc)

# 逆向
node = execjs.get()
pwd = '123456'
file = './kongzhong.js'
ctx = node.compile(open(file,encoding='utf-8').read())
funcname = 'getpwd("{0}","{1}")'.format(pwd,dc)
passwd = ctx.eval(funcname)
print(passwd)