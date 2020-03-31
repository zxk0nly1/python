#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :ciyun.py
@说明    :
@时间    :2020/03/31 12:22:41
@作者    :Russell Zhou
@版本    :1.0
'''

import numpy as np
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread

import warnings
warnings.filterwarnings("ignore")

# 读取数据
df = pd.read_excel("评论_汇总.xlsx")
df.head()
# 利用jieba进行分析操作
df["评论"] = df["评论"].apply(jieba.lcut)
df.head()
# 去除停用词操作
with open("stopword.txt","r",encoding="gbk") as f:
    stop = f.read()  # 返回的是一个字符串
    
stop = stop.split()  # 这里得到的是一个列表.split()会将空格，\n，\t进行切分，因此我们可以将这些加到停用词当中
stop = stop + [" ","\n","\t"]
df_after = df["评论"].apply(lambda x: [i for i in x if i not in stop])
df_after.head()
# 词频统计
all_words = []
for i in df_after:
    all_words.extend(i)

word_count = pd.Series(all_words).value_counts()
word_count[:10]
# 绘制词云图
# 1、读取背景图片
back_picture = imread(r"F:\\Python\\IDE\\python\\pachong\\malilian.png")
# 2、设置词云参数
wc = WordCloud(font_path="F:\Python\IDE\python\pachong\simhei.ttf",
               background_color="white",
               max_words=2000,
               mask=back_picture,
               max_font_size=200,
               random_state=42
              )
wc2 = wc.fit_words(word_count)
# 3、绘制词云图
plt.figure(figsize=(16,8))
plt.imshow(wc2)
plt.axis("off")
plt.show()
wc.to_file("wordcloud.png")