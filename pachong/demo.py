import requests
from lxml import etree
import json
from time import sleep


def get_response(url):
    response=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"})
    return  response

def parse_html(response):
    html=etree.HTML(response.text)
    page_img_urls=[]
    page_img_content=html.xpath('//div[@class="postlist"]//ul//li')
    for img_content in page_img_content:
        img_info={}
        img_info['name']=img_content.xpath('./a[1]/img/@alt')
        img_info['url']=img_content.xpath('./a[1]/@href')
        page_img_urls.append(img_info)
    print(page_img_urls)
    return page_img_urls


def get_next_page_url(response):
    html=etree.HTML(response.text)
    next_page_url=html.xpath('//a[text()="下一页»"]/@href')
    if len(next_page_url)>0:
        return next_page_url[0]
    else:
        return None

def save_to_file(filename,data):
    data=json.dumps(data)
    filename=filename+'.json'
    with open(filename,'w') as f:
        print('正在保存{}'.format(filename))
        f.write(data)
    print('保存完成')




def run():
    '''
    1.获取首页response 内容
    2. 解析内容套图名称及url地址
    3. 循环获取下一页的response内容
    '''
    index_urls=['https://www.mzitu.com/xinggan/','https://www.mzitu.com/japan/','https://www.mzitu.com/taiwan/','https://www.mzitu.com/mm/']
    index_url='https://www.mzitu.com/xinggan/'
    all_img_info=[]
    response=get_response(index_url)
    parse_html(response)
    next_page_url=get_next_page_url(response)
    while next_page_url:
        sleep(2)
        print(next_page_url)
        response = get_response(next_page_url)
        all_img_info.extend(parse_html(response))
        next_page_url = get_next_page_url(response)
    print('爬取完成，共%d条数据'%len(all_img_info))
    save_to_file(filename='meizi',data=all_img_info)


if __name__ == '__main__':
    run()