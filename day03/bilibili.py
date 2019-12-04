import requests
import json
import os
from day02.User_headers import L
import random
import string

class Bilibili:
    def __init__(self):
        self.url="https://api.vc.bilibili.com/board/v1/ranking/top?"
        self.headers={"User-Agent":random.choice(L)}
        self.all_chars=string.whitespace+string.punctuation #设置一个变量绑定所有的空白字符以及特殊字符
        self.files="./B站视频"


    def get_json(self): #对网页发起请求并获取json信息的函数
        if not os.path.exists(self.files):
            os.mkdir(self.files)
        for i in range(1,82,10):
            params={
                "page_size":"10",
                "next_offset":str(i),
                "tag":"小视频",
                "type":"tag_general_week",
                "platform":"pc"
            }
            res=requests.get(self.url,headers=self.headers,params=params)
            res.encoding="utf-8"
            html=res.text
            json_data=json.loads(html)#获取的json数据转换成为python数据类型
            self.get_video_url(json_data)#获取视频链接的函数

    def get_video_url(self,json_data):#解析json数据获取视频下载链接的函数
        for i in json_data["data"]["items"]:
            video_url=i["item"]["video_playurl"]#获取视频地址
            name=i["item"]["description"]#获取视频名称
            if len(name)>15:
                name=name[-15:]
            for j in name:
                if j in self.all_chars:#如果标题存在特殊字符，就替换为空字符
                    name=name.replace(j,"")
            filename=self.files+"//"+name+".mp4"
            self.save_video(video_url,filename)#调用保存本地的函数

    def save_video(self,video_url,filename):#保存视频到本地的函数
        res=requests.get(video_url,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        with open(filename,"wb") as f:
            f.write(html)
            print(filename,"下载成功")

bilibili=Bilibili()
bilibili.get_json()