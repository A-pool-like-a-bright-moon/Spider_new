import requests
import execjs
from lxml import etree

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

#获取公钥key
url = 'https://passport.wanmei.com/sso/login' #若该链接找不到id为e的标签，可能该页面存在iframe嵌套，需要点击登录框附近，右击查看框架源代码，去掉view-source,在该页面查找标签
page_text = requests.post(url=url,headers=headers).text
tree = etree.HTML(page_text)
key = tree.xpath('//input[@id="e"]/@value')[0]
print(key)

#密码参数逆向
node = execjs.get()
ctx = node.compile(open('./完美世界登陆密码加密js_RSA.js',encoding='utf-8').read())
funcname = 'getpwd("{0}","{1}")'.format('123456',key)
pwd = ctx.eval(funcname)
print(pwd)