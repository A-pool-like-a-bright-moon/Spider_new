import requests
import execjs
import re

# 捕获rsa_n的值 用以函数计算公钥
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
url = 'http://login.shikee.com/getkey?v=bc29f453417d5ee9c76aa884186ff26e'
response = requests.get(url=url,headers=headers).text
# print(response)
ex = 'var rsa_n = "(.*?)";'
rsa_n = re.findall(ex,response)[0]
# print(rsa_n)

# 实现密码加密逆向操作
node = execjs.get()
ctx = node.compile(open('./试客联盟_RSA.js',encoding='utf-8').read())
funcname = 'getpwd("{0}","{1}")'.format('123456',rsa_n) # 格式化时候大括号外面只能是双引号而不是单引号
pwd = ctx.eval(funcname)
# print(pwd)