import requests
from lxml import etree
from day02.User_headers import L
import random
import os

class Cunjin:
    def __init__(self):
        self.url="http://www.gdcjxy.com/index.html"
        self.headers={"User-Agent":random.choice(L)}

    def get_html(self,url):#源代码
        res=requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        parse_html=etree.HTML(html)
        return parse_html

    def get_t_link(self):#站内链接的函数并拼接成完整链接
        self.files="./寸金学院"
        if not os.path.exists(self.files):  #检测当前目录下是否存在同名文件夹
            os.mkdir(self.files)
        parse_html=self.get_html(self.url)
        t_url=parse_html.xpath('//a[@class="p"]/@href')
        for link in t_url:
            url="http://www.gdcjxy.com"+link
            self.get_pic_url(url)#调用获取图片链接的函数

    def get_pic_url(self,url):  #获取所有图片的链接函数
        parse_html=self.get_html(url)
        pic_url=parse_html.xpath('//span[@style="font-size:18px;"]/img/@src')
        for link in pic_url:
            pic_link="http://www.gdcjxy.com"+link
            filename=self.files+"//"+pic_link[-15:]#以图片连接的后15位作为图片名称
            self.save_pic(pic_link,filename)#保存图片函数

    def save_pic(self,pic_link,filename):#图片下载到本地的函数
        res=requests.get(pic_link,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        with open(filename,"wb") as f:
            f.write(html)
            print(filename,"下载成功")


cunjin=Cunjin()
cunjin.get_t_link()
