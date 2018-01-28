
import requests
from bs4 import BeautifulSoup
import re

url='https://tuchong.com/explore/'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
# 获取照片类别的url列表

def get_url_sort(url_list,url):
    '''
    :param url_list: 获得照片分类写入url_list列表
    :param url: 传入url进行请求
    :return: 返回url_list列表
    '''
    respons=requests.get(url,headers=header)
    html=respons.text
    soup=BeautifulSoup(html,'lxml')
    li_tags=soup.find_all('li',class_='tag-square-base')
    # url_list=[]
    count=0
    for li in li_tags:
        # 第一种方法
        # sort_url=li.a['href']
        # 第二种方法
        sort_url=li.find('a')['href']
        sort_name=li.span.get_text()
        url_list.append(sort_url)
        count +=1
        # print('{} {}   {}'.format(count,sort_name,sort_url))
    # print(url_list)
    return url_list

def get_pic_list(url):
    # range为页数
    for i in range(1,5):
        part_url=url+'posts?page=%s&count=20&order=weekly' %i
        data=requests.get(part_url).json()
        print(data)
        count=len(data['postList'])
        print(len(data['postList']))
        for j in range(count):
            photo_urls=data['postList'][j]['url']
            print(photo_urls)
        # print(len(data['postList']))
    # print(html)

url_lists=[]
get_url_sort(url_lists,url)

for pic_url in url_lists:
    # 转换url格式
    pic=pic_url.replace('tags','rest/tags')
    get_pic_list(pic)
    break
# print(url_lists)