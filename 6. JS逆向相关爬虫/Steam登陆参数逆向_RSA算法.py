import requests
import execjs
import time

"""
加密参数为pwd
示例账号密码为错误密码，验证码未处理
"""

# 获取公钥
url = 'https://store.steampowered.com/login/getrsakey/'
mili =int(round(time.time()*1000)) # 13位时间戳
data = {
    'donotcache':mili,
    'username':'424062057@qq.com'
}
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    'referer':'https://store.steampowered.com/login/?redir=about&redir_ssl=1&snr=1_14_4__global-header'
}
response_json = requests.post(url=url,headers=headers,data=data).json()
mod = response_json['publickey_mod']
exp = response_json['publickey_exp']

# 密码逆向
node = execjs.get()
ctx = node.compile(open('./steamjs文件.js',encoding='utf-8').read())
funcname = 'getpwd("{0}","{1}","{2}")'.format('123456',mod,exp)
pwd = ctx.eval(funcname)
print(pwd)

# 登陆
s = requests.Session() # 建立一个会话，登陆后保持携带cookie请求
url_login = 'https://store.steampowered.com/login/dologin/'
respon = s.post(url=url_login,headers=headers,data=data).text
print(respon)