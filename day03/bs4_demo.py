from bs4 import BeautifulSoup

html="""
<div class="threadlist_title">
    <a class="d1">新浪</a>
    
    <a rel="noreferrer" href="/p/5548033527" title="【吧规】图片精简版" target="_blank" class="j_th_tit ">【吧规】图片精简版</a>
</div>
<div class="d1">
    <ul id="link">
        <li>百度</li>
        <li>京东</li>
        <li>淘宝</li>
    </ul>
</div>
"""
soup=BeautifulSoup(html,"lxml")
#data=soup.a
#data=soup.div
# data=soup.a.attrs["class"]    #获取节点属性
# data=soup.a["class"]

#data=soup.div.a["class"]    #嵌套选择
#data=soup.find_all(name="div")  #查找所有节点为div的节点信息
#data=soup.find_all(attrs={"id":"link"})
#data=soup.find_all(id="link")
#data=soup.find_all(class_="d1")#查找class为d1的信息
#data=soup.find_all("div",class_="d1")#查找class为d1的信息
data=soup.select('div > ul > li') #层级选择
#data=soup.select('div.threadlist_title')#通过选择器属性定位节点信息
#print(data)
for i in data:#获取节点的信息
    print(i.text)
    print(i.string)