from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains # 动作链

#实例化一个浏览器对象
driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10) # 弹性等待10秒钟
driver.maximize_window() # 最大化浏览器

# 找到用户名和密码框输入用户信息
user_input = driver.find_element(By.XPATH,'//*[@id="login-username"]')
user_input.send_keys('18622660970')
time.sleep(1)
password_input = driver.find_element(By.CSS_SELECTOR,'#login-passwd')
password_input.send_keys('mmm424062057')
time.sleep(1)

# 找到登陆按钮点击登陆
login_lable=driver.find_element(By.XPATH,'//*[@id="geetest-wrap"]/div/div[5]/a[1]')
login_lable.click()
time.sleep(6) # 点击登陆后等待验证码加载，不然可能截验证码截不全

# 处理图片验证码
img_lable=driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div') # 找到验证码图片的位置
img_lable.screenshot('yzm.png') # 截图该标签位置，即验证码位置，被截图，验证码命名最好结合时间戳命名
time.sleep(2)

# 调用处理验证码的类
#以下四行来自于超级鹰模板
chaojiying = Chaojiying_Client('18622660970', 'mmm424062057', '927214')	#用户中心>>软件ID 生成一个替换 96001
im = open('C://Users//42406//Desktop//Spider_new//7. 涉及各种复杂验证码的爬虫//点触验证码处理-selenium+超级鹰//yzm.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
posi=chaojiying.PostPic(im, 9004) #得到的是个字典{'err_no': 0, 'err_str': 'OK', 'pic_id': '1164016367699600001', 'pic_str': '170,64|135,135|39,113|187,146', 'md5': 'f780c0a7901bf960963152c74c2424bd'}
errid=posi['pic_id'] # 识别超时或者识别错误需要此参数反馈给超级鹰返还积分
posi=posi['pic_str']
print("当前验证码识别结果为：",posi)
#以上四行来自于超级鹰模板
result_list = posi.split('|') #返回的验证码进行分割，得到列表比如 ['125,168','148,193','188,257']
for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]
    ActionChains(driver).move_to_element_with_offset(img_lable,int(x),int(y)).click().perform() # 找到坐标，点击，执行
    time.sleep(0.8)
time.sleep(2)

# 点击确认
driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowclick > div.geetest_panel_next > div > div > div.geetest_panel > a > div').click()
input() # 是因为selenium控制过程中调用了class或者函数后，执行完就会关闭窗口，input可以保证不被关掉窗口
# driver.quit() # 退出浏览器