import re

html="""
<div class="book-mid-info">
                    <h4><a href="//book.qidian.com/info/1004608738" target="_blank" data-eid="qd_B58" data-bid="1004608738">圣墟</a></h4>
                    <p class="author">
                        <img src="//qidian.gtimg.com/qd/images/ico/user.f22d3.png"><a class="name" href="//my.qidian.com/author/4362453" data-eid="qd_B59" target="_blank">辰东</a><em>|</em><a href="//www.qidian.com/xuanhuan" target="_blank" data-eid="qd_B60">玄幻</a><i>·</i><a class="go-sub-type" data-typeid="21" data-subtypeid="8" href="javascript:" data-eid="qd_B61">东方玄幻</a><em>|</em><span>连载</span>
                        
                    </p>
                    <p class="intro">
                        在破败中崛起，在寂灭中复苏。沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……
                    </p>
                    <p class="update"><span><style>@font-face { font-family: CjUTgyWy; src: url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.ttf') format('truetype'); } .CjUTgyWy { font-family: 'CjUTgyWy' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="CjUTgyWy"></span>万字</span>
                        
                    </p>
                </div>
"""
#
#  p=re.compile('<div class="book-mid-info">.*?data-bid.*?>(.*?)</a>.*?class="intro">(.*?)</p>',re.S)#使用非贪婪匹配不需要的字符
# data=re.findall(p,html)
# print(data)
import csv
L=["小明","20","男"]
L1=["小红","25","女"]
with open("data.csv","w",encoding="utf-8",newline="") as f: #newline为了防止出现空行
    writer=csv.writer(f)
    writer.writerow(L)
    writer.writerow(L1)
