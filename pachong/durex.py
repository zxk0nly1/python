#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :durex.py
@说明    :
@时间    :2020/03/31 11:02:53
@作者    :Russell Zhou
@版本    :1.0
'''
import re
import requests
import pandas as pd
import time

# def get_durex_detail():
#     true_url="https://rate.tmall.com/list_detail_rate.htm?itemId=43751299764&spuId=864684242&sellerId=2380958892&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvkpvUvbpvUvCkvvvvvjiPn25OAj3nRszU1jthPmPWsj3Pn2cp0jl8nLdU6jn8RphvCvvvphmtvpvIvvCvpvvv9k%2BvvhbsvvmClvvvBGwvvvUwvvCj1Qvvv99vvhNjvvvmmUyCvvOCvhE2gWmivpvUvvCCWb9Jsp9EvpCWvvX6aCzhe4TK5kx%2Ftj7r%2Bu0Oakrl%2BboJVii1Bd2XrqpAhjCbFO7t%2B3vXwyFEDLuTRLa9C7zZdiTAdcZIdU9T%2BLpBfvc6sEu4V1O07phCvvOv9hCvvvvPvpvhvv2MMTwCvvpvvhHh&needFold=0&_ksTS=1585623573863_436&callback=jsonp437"
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#         'referer':'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.311b7e7cuc95GC&id=43751299764&skuId=4493124079453&areaId=441500&user_id=2380958892&cat_id=2&is_b=1&rn=e1c7c29478d0087e577ae6e4b87f7f9c',
#         'cookie':'cna=PSjpFn9Y9QYCAXFSh7m122gu; dnk=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; uc1=tag=8&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=UoTUP2R%2BsyMUfA%3D%3D&cookie21=VFC%2FuZ9ainBZ&existShop=false&lng=zh_CN&pas=0&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; uc3=nk2=saDJsmcPKOiAog%3D%3D&id2=UUGlR2tb4Ida8g%3D%3D&vt3=F8dBxdAQyZNSUOGlN4I%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; lid=%E4%B8%80%E7%AC%91%E5%A5%88%E4%BD%9548; uc4=nk4=0%40s8WJlii5cdimkDu8kq%2FLPWwQiS6I&id4=0%40U2OSUL6T9i8KRo7uEK3%2Fd4YxgKWm; _l_g_=Ug%3D%3D; unb=2979609909; lgc=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; cookie1=Bqbjhc3wgxOsTx1MpyEKIts%2FU7JRDGtkpl4NzH6gN%2Fo%3D; login=true; cookie17=UUGlR2tb4Ida8g%3D%3D; cookie2=15b44d9d3fdbfc3e4e51405dbfec93eb; _nk_=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; sgcookie=ERBfOBpqb%2B0nyVBDfn59N; t=3b4a9ead2be424a7f2683c0fca79c069; sg=89a; csg=f86791e3; _tb_token_=f5f5b3f75eb74; enc=OzBu5H4lO3AjAQeoaC%2FWkjIvQ%2FDH2Vksac7xhIqnJ6zAO0E4ci5aUqf6KUj6w%2F%2Fd2MBwQfu%2BGUISJc0aA9tnTA%3D%3D; l=dBNpONd7Qc8Y3yhNBOCwourza77OSIRAguPzaNbMi_5CL686cJbOosuABFJ6VjWfT3YB4cjscS29-etkmSqhOP5P97Rw_xDc.; isg=BPX1pnpuxzZRwyNzzQaF0H4VBHGvcqmEJaSD6HcasWy5ThVAP8K5VAPImBL4DsE8'
#     }
#     data=requests.get(true_url,headers=headers).text
#     #get_rate_content(data)
#     #print(data)

# def get_rate_content(data):
#     result=re.findall('rateContent":"(.*?)"fromMall"',data)
#     # print(result)
#     #save_rate_content(result)

#  def save_rate_content():
#      data_list=[]
#      first="https://rate.tmall.com/list_detail_rate.htm?itemId=43751299764&spuId=864684242&sellerId=2380958892&order=3&currentPage="
#      last="&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvkpvUvbpvUvCkvvvvvjiPn25OAj3nRszU1jthPmPWsj3Pn2cp0jl8nLdU6jn8RphvCvvvphmtvpvIvvCvpvvv9k%2BvvhbsvvmClvvvBGwvvvUwvvCj1Qvvv99vvhNjvvvmmUyCvvOCvhE2gWmivpvUvvCCWb9Jsp9EvpCWvvX6aCzhe4TK5kx%2Ftj7r%2Bu0Oakrl%2BboJVii1Bd2XrqpAhjCbFO7t%2B3vXwyFEDLuTRLa9C7zZdiTAdcZIdU9T%2BLpBfvc6sEu4V1O07phCvvOv9hCvvvvPvpvhvv2MMTwCvvpvvhHh&needFold=0&_ksTS=1585623573863_436&callback=jsonp437"
#      for i in range(1,300,1):
#          print("正在爬取第"+str(i)+"页")
#          url=first+str(i)+last
#          headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#         'referer':'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.311b7e7cuc95GC&id=43751299764&skuId=4493124079453&areaId=441500&user_id=2380958892&cat_id=2&is_b=1&rn=e1c7c29478d0087e577ae6e4b87f7f9c',
#         'cookie':'cna=PSjpFn9Y9QYCAXFSh7m122gu; dnk=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; uc1=tag=8&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=UoTUP2R%2BsyMUfA%3D%3D&cookie21=VFC%2FuZ9ainBZ&existShop=false&lng=zh_CN&pas=0&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; uc3=nk2=saDJsmcPKOiAog%3D%3D&id2=UUGlR2tb4Ida8g%3D%3D&vt3=F8dBxdAQyZNSUOGlN4I%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; lid=%E4%B8%80%E7%AC%91%E5%A5%88%E4%BD%9548; uc4=nk4=0%40s8WJlii5cdimkDu8kq%2FLPWwQiS6I&id4=0%40U2OSUL6T9i8KRo7uEK3%2Fd4YxgKWm; _l_g_=Ug%3D%3D; unb=2979609909; lgc=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; cookie1=Bqbjhc3wgxOsTx1MpyEKIts%2FU7JRDGtkpl4NzH6gN%2Fo%3D; login=true; cookie17=UUGlR2tb4Ida8g%3D%3D; cookie2=15b44d9d3fdbfc3e4e51405dbfec93eb; _nk_=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; sgcookie=ERBfOBpqb%2B0nyVBDfn59N; t=3b4a9ead2be424a7f2683c0fca79c069; sg=89a; csg=f86791e3; _tb_token_=f5f5b3f75eb74; enc=OzBu5H4lO3AjAQeoaC%2FWkjIvQ%2FDH2Vksac7xhIqnJ6zAO0E4ci5aUqf6KUj6w%2F%2Fd2MBwQfu%2BGUISJc0aA9tnTA%3D%3D; l=dBNpONd7Qc8Y3yhNBOCwourza77OSIRAguPzaNbMi_5CL686cJbOosuABFJ6VjWfT3YB4cjscS29-etkmSqhOP5P97Rw_xDc.; isg=BPX1pnpuxzZRwyNzzQaF0H4VBHGvcqmEJaSD6HcasWy5ThVAP8K5VAPImBL4DsE8'
#         }
#          try:
#              data=requests.get(url,headers=headers).text
#              time.sleep(10)
#              result=re.findall('rateContent":"(.*?)"fromMall"',data)
#              data_list.extend(result)
#         except:
#             print("本页爬取失败")
#     df=pd.DataFrame()
#     df["评论"]=data_list
#     df.to_excel("评论_汇总.xlsx")

# if __name__=='__main__':
#     #get_durex_detail()
#     save_rate_content()




data_list = []
first="https://rate.tmall.com/list_detail_rate.htm?itemId=43751299764&spuId=864684242&sellerId=2380958892&order=3&currentPage="
last="&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvkpvUvbpvUvCkvvvvvjiPn25OAj3nRszU1jthPmPWsj3Pn2cp0jl8nLdU6jn8RphvCvvvphmtvpvIvvCvpvvv9k%2BvvhbsvvmClvvvBGwvvvUwvvCj1Qvvv99vvhNjvvvmmUyCvvOCvhE2gWmivpvUvvCCWb9Jsp9EvpCWvvX6aCzhe4TK5kx%2Ftj7r%2Bu0Oakrl%2BboJVii1Bd2XrqpAhjCbFO7t%2B3vXwyFEDLuTRLa9C7zZdiTAdcZIdU9T%2BLpBfvc6sEu4V1O07phCvvOv9hCvvvvPvpvhvv2MMTwCvvpvvhHh&needFold=0&_ksTS=1585623573863_436&callback=jsonp437"

for i in range(1,300,1):
         print("正在爬取第"+str(i)+"页")
         url=first+str(i)+last
         headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'referer':'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.311b7e7cuc95GC&id=43751299764&skuId=4493124079453&areaId=441500&user_id=2380958892&cat_id=2&is_b=1&rn=e1c7c29478d0087e577ae6e4b87f7f9c',
        'cookie':'cna=PSjpFn9Y9QYCAXFSh7m122gu; dnk=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; uc1=tag=8&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie14=UoTUP2R%2BsyMUfA%3D%3D&cookie21=VFC%2FuZ9ainBZ&existShop=false&lng=zh_CN&pas=0&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; uc3=nk2=saDJsmcPKOiAog%3D%3D&id2=UUGlR2tb4Ida8g%3D%3D&vt3=F8dBxdAQyZNSUOGlN4I%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; lid=%E4%B8%80%E7%AC%91%E5%A5%88%E4%BD%9548; uc4=nk4=0%40s8WJlii5cdimkDu8kq%2FLPWwQiS6I&id4=0%40U2OSUL6T9i8KRo7uEK3%2Fd4YxgKWm; _l_g_=Ug%3D%3D; unb=2979609909; lgc=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; cookie1=Bqbjhc3wgxOsTx1MpyEKIts%2FU7JRDGtkpl4NzH6gN%2Fo%3D; login=true; cookie17=UUGlR2tb4Ida8g%3D%3D; cookie2=15b44d9d3fdbfc3e4e51405dbfec93eb; _nk_=%5Cu4E00%5Cu7B11%5Cu5948%5Cu4F5548; sgcookie=ERBfOBpqb%2B0nyVBDfn59N; t=3b4a9ead2be424a7f2683c0fca79c069; sg=89a; csg=f86791e3; _tb_token_=f5f5b3f75eb74; enc=OzBu5H4lO3AjAQeoaC%2FWkjIvQ%2FDH2Vksac7xhIqnJ6zAO0E4ci5aUqf6KUj6w%2F%2Fd2MBwQfu%2BGUISJc0aA9tnTA%3D%3D; l=dBNpONd7Qc8Y3yhNBOCwourza77OSIRAguPzaNbMi_5CL686cJbOosuABFJ6VjWfT3YB4cjscS29-etkmSqhOP5P97Rw_xDc.; isg=BPX1pnpuxzZRwyNzzQaF0H4VBHGvcqmEJaSD6HcasWy5ThVAP8K5VAPImBL4DsE8'
        }
         try:
             data=requests.get(url,headers=headers).text
             time.sleep(10)
             result=re.findall('rateContent":"(.*?)"fromMall"',data)
             data_list.extend(result)
         except:
            print("本页爬取失败")


df=pd.DataFrame()
df["评论"]=data_list
df.to_excel("评论_汇总.xlsx")