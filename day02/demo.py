import requests

url="https://www.baidu.com/"#确定抓取网页的url
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
res=requests.get(url,headers=headers) #对网页发起请求并响应信息
res.encoding="utf-8"
html=res.text # 解析得到的响应内容
print(html)

