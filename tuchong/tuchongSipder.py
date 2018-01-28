
import requests
from bs4 import BeautifulSoup

base_url='https://tuchong.com/explore/'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}

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

def get_page_num(page_sort_url):
    '''

    :param page_sort_url: 传入的是照片分类的url
    :return: 返回该类别的总页数
    '''
    html=requests.get(page_sort_url,headers=header).text
    soup=BeautifulSoup(html,'lxml')
    tag=soup.find('span',class_='tag-posts').string
    page_num=int(tag[:-3])//20+2
    # print(tag)
    # print(num)
    return page_num

def get_pic_list(page_num,page_sort_url):
    '''

    :param page_num:
    :param url:
    :return:
    '''
    try:
        for i in range(1,page_num):
            new_url=page_sort_url+'posts?page=%s&count=20&order=weekly' %i
            data=requests.get(new_url,headers=header).json()
            # print(data)
            count=len(data['postList'])
            # print(len(data['postList']))
            for j in range(count):
                photo_urls=data['postList'][j]['url']
                print(photo_urls)
            print('--------第{}页--------'.format(i))
            # print(len(data['postList']))
        # print(html)
        return photo_urls
    except:
        print('--------------空-------------------')

def main():
    url_lists=[]
    get_url_sort(url_lists,base_url)

    for url in url_lists:
        # 转换url格式
        page_num= get_page_num(url)
        pic_url=url.replace('tags','rest/tags')
        get_pic_list(page_num,pic_url)
        # 关闭break可以获取全类别的url
        break
# print(url_lists)
main()