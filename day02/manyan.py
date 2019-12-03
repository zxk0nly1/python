import re
import requests
from day02.User_headers import L
import random
import csv

class Maoyan:
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset=?"
        self.headers = {"User-Agent": random.choice(L)}

    def change_page(self): #进行翻页函数
        with open("maoyan.csv","a",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["电影名称","电影主演","上映时间"])
        for page in range(1,10):
            offset=(page-1)*10
            params={
                "offset":offset
            }
            self.get_html(params)#调用获取网页源代码的函数

    def get_html(self,params):     # 获取网页源代码函数
        res=requests.get(self.url,headers=self.headers,params=params)
        res.encoding="utf-8"
        html=res.text
        self.get_data(html) #调用解析数据的函数


    def get_data(self,html):     # 解析网页的数据函数
            p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
            data = re.findall(p, html)
            self.save_data(data) # 调用保存数据的函数


    def save_data(self,data):        # 保存数据的函数
        for i in data:
            title=i[0] #获取电影名称
            star=i[1].strip()# 获取电影主演        strip()代表去掉字符串两边的空白字符以及换行符
            time=i[2].strip()# 获取电影上映时间
            content=[title,star,time] #创建写入csv文件
            with open("maoyan.csv","a",encoding="utf-8",newline="") as f:
                writer = csv.writer(f)
                writer.writerow(content)
                print("数据写入成功")


maoyan=Maoyan()#类的实例化

maoyan.change_page()