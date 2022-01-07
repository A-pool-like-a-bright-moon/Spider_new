import requests
import execjs
"""
加密参数为pwd
示例账号密码为错误密码，验证码未处理
"""

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


node = execjs.get()
ctx = node.compile(open('./凡科网.js',encoding='utf-8').read())
funcname = 'md5("{0}")'.format('123456')
pwd = ctx.eval(funcname)
print(pwd)

data = {
    'cacct': '424062057@qq.com',
    'pwd': pwd
}

s = requests.Session()
url = 'https://i.fkw.com/ajax/login_h.jsp?dogSrc=3'
response = s.post(url=url,headers=headers,data=data).text
print(response)