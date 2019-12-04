import requests
from bs4 import  BeautifulSoup
from day02.User_headers import L
import os
import random
class Bilibili:
    def __init__(self):
        self.url="https://vc.bilibili.com/p/eden/rank#/?tab=%E5%BE%A1%E5%AE%85%E6%96%87%E5%8C%96&tag=%E5%B0%8F%E8%A7%86%E9%A2%91"
        self.headers={"User-Agent":random.choice(L)}

    def get_soup(self):
            self.files="./小视频"
            if not os.path.exists(self.files):
                os.mkdir(self.files)

    def save_data(self):
        pass


bilibili=Bilibili()
bilibili.get_soup()

