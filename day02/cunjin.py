import requests
from lxml import etree
from day02.User_headers import L
import random


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
            print(pic_link)

    def save_pic(self):#图片下载到本地的函数
        pass


cunjin=Cunjin()
cunjin.get_t_link()
