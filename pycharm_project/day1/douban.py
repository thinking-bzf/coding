# -*- encoding: utf-8 -*-
# here put the import lib
# -*- encoding: utf-8 -*-
# here put the import lib

import requests
import lxml
from bs4 import BeautifulSoup

links = []
for x in range(0, 251, 25):  # 10页循环
    MainPage = "https://movie.douban.com/top250?start=" + str(x)
    payload = {}  #来自Postman工具，用于得到request
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    strMainpage = requests.get(
        url=MainPage,
        headers=headers,
    )
    Soup = BeautifulSoup(strMainpage.text, 'lxml')
    for i in range(1, 26):
        Data = Soup.select(
            '#content > div > div.article > ol > li:nth-child(' + str(i) +
            ') > div > div.info > div.hd > a')
        for item in Data:
            links.append(item.get('href'))
            print('导入链接成功: %s' % item.get('href'))
print(links)  #输出电影所在的网址
for link in links:  #将电影演员表导入txt文件
    # url = link
    payload = {}
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    strurl = requests.get(url=link, headers=headers)
    # strurl = requests.get(links)
    strurl.raise_for_status()
    Soup = BeautifulSoup(strurl.text, 'lxml')
    Titledata = Soup.select('#content > h1 > span:nth-child(1)')
    Actordata = Soup.select('#info')
    film = {}
    for x in Titledata:
        film['title'] = x.get_text()
    for x in Actordata:
        film['actor'] = x.get_text()

    f = open('电影.txt', 'a', encoding='utf-8')
    f.write(film['title'])
    f.write(film['actor'])
    f.close()
    print('导入成功:%s' % film['title'])
