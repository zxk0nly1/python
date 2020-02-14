import requests
from lxml import etree
from day02.User_headers import L
import random

class Mzitu:
    def __init__(self):
        self.url="https://www.mzitu.com/xinggan/"
        self.headers={"User-Agent":random.choice(L)}

    def get_response(self):
        response=requests.get(url=self.url,headers=self.headers)
        response.encoding="utf-8"
        html = etree.HTML(response.text)
        page_img_urls = []
        page_img_content = html.xpath('//div[@class="postlist"]//ul//li')
        for img_content in page_img_content:
            img_info = {}
            img_info['name'] = img_content.xpath('./a[1]/img/@alt')
            img_info['url'] = img_content.xpath('./a[1]/@href')
            print(img_info)





mzitu=Mzitu()
mzitu.get_response()