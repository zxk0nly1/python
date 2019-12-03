import requests
from day02.User_headers import L
import random
url="https://www.qidian.com/all?"
headers={"User-Agent":random.choice(L)}     #请求头从文件中随机抽取
for page in range(1,5):
    params={
        "page":str(page)
    }
    res=requests.get(url,headers=headers,params=params)
    res.encoding="utf-8"
    html=res.text
    filename="第"+str(page)+"页.html"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
        print(filename,"下载成功")


