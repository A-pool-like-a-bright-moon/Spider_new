import execjs
import requests

"""
加密参数为pwd
示例账号密码为错误密码，验证码未处理
"""

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    'referer':'https://mp.weixin.qq.com/'
}

# 实例化一个node对象
node = execjs.get()

#j s源文件编译
ctx = node.compile(open('./微信公众平台.js',encoding='utf-8').read())

# 执行js函数
funcname = 'getpwd("{0}")'.format('mmm424062057')
pwd = ctx.eval(funcname)
data = {
    'username':'424062057@qq.com',
    'pwd':pwd
}
print(pwd)

s = requests.Session() # 建立一个会话，登陆后保持携带cookie请求
url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin'
respon = s.post(url=url,headers=headers,data=data).text
print(respon)
