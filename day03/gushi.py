import requests
from bs4 import  BeautifulSoup
from day02.User_headers import L
import os
import random

class Gushi:

    def __init__(self):
        self.url="https://www.gushiwen.org/default_4.aspx"
        self.headers={"User-Agent":random.choice(L)}

    def get_soup(self):
        self.files="./古诗词"
        if not os.path.exists(self.files):
            os.mkdir(self.files)
        res=requests.get(self.url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        soup=BeautifulSoup(html,"lxml")
        self.get_data(soup)

    def get_data(self,soup):
        title=soup.select('div > p > a >b')#通过css选择查看标题内容
        comment=soup.find_all("div",class_="contson")#通过方法选择器查找内容
        self.save_data(title,comment)#调用保存信息的函数

    def save_data(self,title,comment):
        for i in range(len(title)):#获取标题和内容列表的索引
            name=title[i].text
            for j in name:
                if j=="/":
                    name=name.replace(j,"")
            filename=self.files+"//"+name+".txt"
            data=comment[i].text
            with open(filename,"w",encoding="utf-8") as f:
                f.write(name)
                for i in data:
                    f.write(i)
                    if i=="。":#如果写入的字符为。,添加换行
                        f.write("\n")
                print("数据存储成功")
gushi=Gushi()
gushi.get_soup()