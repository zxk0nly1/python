import requests
import json
from day02.User_headers import L
import random
import time
from hashlib import md5

class Youdao:

    def __init__(self):
        self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers={"User-Agent":random.choice(L),
                      "Cookie":"OUTFOX_SEARCH_USER_ID=540471167@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1608093058.2426364; _ntes_nnid=ada25bd2a551d9fb3ba1eabd078d186d,1570727177026; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcZVq5uoEgq3b4Iufv7w; ___rl__test__cookies=1575539083073",
                      "Referer":"http://fanyi.youdao.com/"}

    def get_json(self):
        word=input("请输入需要翻译的单词：")
        ts=str(int(time.time() * 10000)) # 获取时间戳
        salt=ts+str(random.randint(0, 9))  # 生成0-9随机整数
        data="fanyideskweb" + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(data.encode())
        sign = s.hexdigest()
        data={
            "i":word,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dist",
            "client":"fanyideskweb",
            "salt":salt,
            "sign":sign,
            "ts":ts,
            "bv":"bc250de095a39eeec212da07435b6924",
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTlME"
        }
        res=requests.post(self.url,headers=self.headers,data=data)
        res.encoding="utf-8"
        html=res.text
        json_data=json.loads(html)
        self.get_data(json_data)

    def get_data(self,json_data):
        data=json_data["translateResult"][0][0]["tgt"]
        print("翻译的结果为：",data)

youdao=Youdao()
youdao.get_json()
