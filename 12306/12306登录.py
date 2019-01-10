import requests
from urllib.parse import urlencode
from selenium import webdriver
import time
import re
from Day01.YDM import *
from fake_useragent import UserAgent


# https://kyfw.12306.cn/otn/login/init 登陆网址
# 匹配图片的xpath ： //img[@class="touclick-image"]/@src
# https://kyfw.12306.cn/otn/view/index.html 个人中心

# 检查是否有票的xpath ：tr[@class="bgc"]|//tr[@class="bgc xh-highlight"]
class Spider:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.ua = UserAgent()
        self.pattern = re.compile(r'.*?touclick-image" alt="" src="(.*?)".*?')
        self.img = {'1': '35,40', '2': '104,36', '3': '180,42', '4': '250,44', '5': '40,115', '6': '100,122',
                    '7': '180,114', '8': '250,124'}
        self.begin = input("起始站:")
        self.end = input("终止站:")
        self.datetime = input("出发日期(2019-02-06):")

    def login(self):
        self.driver.get('https://kyfw.12306.cn/otn/login/init')
        # 网速慢，等待加载完毕
        time.sleep(0.5)
        html = self.driver.page_source
        # 获取到验证码图片的url
        image_Link = self.pattern.findall(html)[0]
        image = requests.get(image_Link).content
        with open('yzm.jpg', 'wb') as f:
            f.write(image)
            print("验证码获取成功")
        cid, result = yundama.decode(filename, codetype, timeout)
        print(cid,result)
        self.Mycenter(result)
        # 个人中心

    def Mycenter(self, result):
        # 坐标 : coordinate
        # 将得到验证码字符串拆开得出图片坐标，拼接到参数上访问个人中心
        img_coordinate = ''
        for i in result:
            img_coordinate += self.img[i] + "|"
        #'图片坐标1|图片坐标2'
        # coordinate :坐标
        print("正在拼接验证码坐标...")
        coordinate = img_coordinate[:-1]
        data = {
            'answer':coordinate,
            'login_site':'E',
            'rand':'sjrand',
        }
        url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={},&ts={},&date={}&flag=N,N,Y'.format(self.begin,self.end,self.datetime)
        req = requests.get(url,headers={'User-Agent':self.ua.ie},data=data)
        req.encoding = 'utf-8'
        html = req.text
        print(html)
    def main(self):
        self.login()


if __name__ == '__main__':
    spider = Spider()
    spider.main()
