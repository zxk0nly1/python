import requests
import json
from day02.User_headers import L
import random
import csv

class Douban:

    def __init__(self):
        self.url="https://movie.douban.com/j/chart/top_list?"
        self.headers={"User-Agent":random.choice(L)}
        self.files="./豆瓣"

    def get_json_data(self):
        with open("movie.csv","w",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["电影名称","演员信息","国家","上映时间","评分","排名","类型"])

        for i in range(0,81,20):
            params={
                "type":"13",
                "interval_id":"100:90",
                "action":"",
                "start":str(i),
                "limit":"20"
            }
            res=requests.get(self.url,headers=self.headers,params=params)
            res.encoding="utf-8"
            html=res.text
            json_data=json.loads(html)
            self.get_data(json_data)

    def get_data(self,json_data):
        for i in json_data:
            title=i["title"]    #电影名称
            actors=i["actors"]# 演员 list
            actors=",".join(actors)
            regions=i["regions"]#国家 list
            regions = ",".join(regions)
            release_date=i["release_date"]#上映时间
            score=i["score"]#评分
            rank=i["rank"]#排名
            types=i["types"]#类型     list
            types = ",".join(types)
            content=[title,actors,regions,release_date,score,rank,types]
            self.save_data(content)

    def save_data(self,content):
        with open("movie.csv","a",encoding="utf-8",newline="") as  f:
            writer=csv.writer(f)
            writer.writerow(content)
            print("数据存储成功")

douban=Douban()
douban.get_json_data()