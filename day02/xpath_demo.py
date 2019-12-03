from lxml import etree

html="""
<div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-07-26</p>   
</div>
<div class="d1">
    <li id="link1">百度</li>
    <li id="link2">新浪</li>
    <li id="link3">网易</li>
    <p>hello world</p>
    <p>你好世界！</p>
</div>
"""
parse_html=etree.HTML(html)#将网页源代码转化成xpath对象
# data=parse_html.xpath('//div')#获取所有的div节点
#data=parse_html.xpath("//p")
#data=parse_html.xpath('//div/p')#获取div节点下的p节点
# data=parse_html.xpath('//div[@class="d1"]/p')#获取class为d1的div节点下的p节点
# data=parse_html.xpath('//div[@class="d1"]/p/text()')#获取class为d1的div节点下的p节点中的文本信息
#data=parse_html.xpath('//div[@class="d1"]/p[1]/text()')#获取class为d1的div节点下的第一个p节点中的文本信息
data=parse_html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
#获取class为movie-item-info的div节点下的p节点中的a节点的title属性
print(data)
