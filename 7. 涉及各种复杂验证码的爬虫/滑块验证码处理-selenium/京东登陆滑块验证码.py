from PIL import Image
from selenium.webdriver.common.by import By
'''
验证识别需要完成以下三步：
1）模拟点击验证按钮
使用Selenium模拟点击按钮
2）识别滑动缺口的位置
带缺口的大图像灰度处理，找出缺口位置，图片和网页上的比例是不一样的，或者图片有边界，需要调整本地的图片尺寸
3）模拟拖动滑块
一般的滑块验证码需要模拟加速减速，京东的滑块验证码更恐怖一些，用了机器学习辨别机器的手法，只有完全模拟人的
操作才可以通过，此处用到pyautogui完全模拟真人，并且试错两次后才执行成功的
'''

from urllib import request
from selenium import webdriver
import cv2
import random
import time
import pyautogui


# 下载带缺口的大图，opencv获取最佳匹配位置
def findPic(target="img1.png", template="img2.png"):#360*140，50*50
    # 读取带缺口的大图
    target_rgb = cv2.imread(target)
    # 灰度化
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    # 读取小缺口组件图片
    template_rgb = cv2.imread(template, 0)
    # 匹配两者位置
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    # 获取最佳匹配位置
    value = cv2.minMaxLoc(res)
    # 返回最佳位置的X坐标
    print(value[2][0])
    return value[2][0]


# 打开浏览器
driver = webdriver.Chrome()
driver.get("https://passport.jd.com/new/login.aspx")
# 点击账户登陆方式
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="loginname"]').send_keys('123456')
driver.find_element(By.XPATH,'//*[@id="nloginpwd"]').send_keys('123456')
driver.find_element(By.XPATH,'//*[@id="loginsubmit"]').click()

while True:
    try:
        # 从网页上获取组件
        target = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[1]/div[2]/div[1]/img')
        template = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div[1]/div[2]/div[2]/img')
        # 获取模块的url路径
        src1 = target.get_attribute("src")
        src2 = template.get_attribute("src")
        # 下载图片
        request.urlretrieve(src1,"img1.png")
        request.urlretrieve(src2,"img2.png")
        #调整图片尺寸为和网页的一样
        im1 = Image.open("img1.png")
        im2 = Image.open("img2.png")
        x1_adjust = 278
        y1_adjust = 108
        x2_adjust = 39
        y2_adjust = 39
        out1 = im1.resize((x1_adjust,y1_adjust),Image.ANTIALIAS)
        out2 = im2.resize((x2_adjust, y2_adjust), Image.ANTIALIAS)
        out1.save("img1.png")
        out2.save("img2.png")

        x = findPic()
        w1 = cv2.imread('img1.png').shape[1]
        w2 = target.size['width']
        x = x / w1 * w2
        # 按钮坐标
        offset_x,offset_y = 898,609
        # pyautogui库操作鼠标指针
        pyautogui.moveTo(offset_x,offset_y,duration=0.1 + random.uniform(0,0.1 + random.randint(1,100) / 100))
        pyautogui.mouseDown()

        offset_y += random.randint(9,19)
        pyautogui.moveTo(offset_x + int(x * random.randint(15,25) / 20),offset_y,duration=0.28)

        offset_y += random.randint(-9,0)
        pyautogui.moveTo(offset_x + int(x * random.randint(17,23) / 20),offset_y,duration=random.randint(20,31) / 100)

        # offset_y += random.randint(0,8)
        # pyautogui.moveTo(offset_x + int(x * random.randint(19,21) / 20),offset_y,duration=random.randint(20,40) / 100)
        #
        # offset_y += random.randint(-3,3)
        # pyautogui.moveTo(x + offset_x + random.randint(-3,3),offset_y,duration=0.5 + random.randint(-10,10) / 100)

        offset_y += random.randint(-2,2)
        pyautogui.moveTo(x + offset_x + random.randint(-0.5,0.5),offset_y,duration=0.5 + random.randint(-3,3) / 100)
        pyautogui.mouseUp()
        time.sleep(1)
        result = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[4]/div[2]/div').text
        if '不匹配' in result:
            print("账户名密码不匹配!", result)
            break
    except:
        print("异常!")
        break