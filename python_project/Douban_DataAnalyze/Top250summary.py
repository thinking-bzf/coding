# -*- encoding: utf-8 -*-
# here put the import lib

import requests
import lxml
from bs4 import BeautifulSoup
import re
import random
import time
import pandas as pd


# 250部电影的主页链接
def get_links():
    # 存放250部电影的主页链接
    links = []
    # 10页循环得到每一页的电影链接 发现每一页的网址区别主要在start=(x)不同 x是变量 每次累加25
    for x in range(0, 251, 25):
        # 电影列表的每一页链接构造
        MainPage = "https://movie.douban.com/top250?start=" + str(
            x) + '&filter='
        # payload 和 headers 来自Postman，主要用途伪造一个非机器人是的请求头，不会被直接拦截，不需要看懂
        payload = {}
        headers = {
            'Connection':
            'keep-alive',
            'Pragma':
            'no-cache',
            'Cache-Control':
            'no-cache',
            'Upgrade-Insecure-Requests':
            '1',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site':
            'same-origin',
            'Sec-Fetch-Mode':
            'navigate',
            'Sec-Fetch-User':
            '?1',
            'Sec-Fetch-Dest':
            'document',
            'Accept-Language':
            'zh-CN,zh;q=0.9,zh-TW;q=0.8',
            'Cookie':
            'll="108298"; bid=YIM8c0oC3z8; _vwo_uuid_v2=DA59572CC5515F0AF9A0B787F07363E96|800fa068f4ddbb1f28a7cf944dc33808; __yadk_uid=2TENzogWpAYdmfaBRwFXDDe8Vgb9iG8T; dbcl2="223067959:xIw7GTJifiw"; ck=Xfzi; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmv=30149280.22306; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599561500%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1259386353.1599489952.1599555333.1599561501.3; __utmb=30149280.0.10.1599561501; __utmz=30149280.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.319377288.1599489955.1599555342.1599561501.3; __utmb=223695111.0.10.1599561501; __utmz=223695111.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=c1a04398ac037345.1599446599.11.1599561677.1599556556.'
        }
        # get方式请求网页
        strMainpage = requests.get(url=MainPage, headers=headers,
                                   data=payload).text

        # 用BeautifulSoup方法将得到的网页转换成可解析的类型
        Soup = BeautifulSoup(strMainpage, 'lxml')
        # 1-25循环在该页的25条电影记录中寻找链接
        for i in range(1, 25):
            # 网页源代码得到网页链接a标签的选择器
            Data = Soup.select(
                '#content > div > div.article > ol > li:nth-child(' + str(i) +
                ') > div > div.info > div.hd > a')
            # 将得到的标签内容中的href属性值添加到links列表 由于Data得到的是一个元组，所以需要用for循环迭代
            for item in Data:
                links.append(item.get('href'))
                print('导入链接成功: %s' % item.get('href'))

        # 每次循环产生一个随机数 每次结束后让程序停1-3秒
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
    return links


# 输出电影所在的网址
# print(links)


# 依次打开links中的链接爬取内容 并将内容导入到txt中
def get_summary(links):
    f = open(r'Douban_DataAnalyze\电影简介.txt', 'w', encoding='utf-8')
    for link in links:
        # url = link
        payload = {}
        headers = {
            'Connection':
            'keep-alive',
            'Pragma':
            'no-cache',
            'Cache-Control':
            'no-cache',
            'Upgrade-Insecure-Requests':
            '1',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site':
            'same-origin',
            'Sec-Fetch-Mode':
            'navigate',
            'Sec-Fetch-User':
            '?1',
            'Sec-Fetch-Dest':
            'document',
            'Accept-Language':
            'zh-CN,zh;q=0.9,zh-TW;q=0.8',
            'Cookie':
            'll="108298"; bid=YIM8c0oC3z8; _vwo_uuid_v2=DA59572CC5515F0AF9A0B787F07363E96|800fa068f4ddbb1f28a7cf944dc33808; __yadk_uid=2TENzogWpAYdmfaBRwFXDDe8Vgb9iG8T; dbcl2="223067959:xIw7GTJifiw"; ck=Xfzi; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmv=30149280.22306; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599561500%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1259386353.1599489952.1599555333.1599561501.3; __utmb=30149280.0.10.1599561501; __utmz=30149280.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.319377288.1599489955.1599555342.1599561501.3; __utmb=223695111.0.10.1599561501; __utmz=223695111.1599561501.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=c1a04398ac037345.1599446599.11.1599561758.1599556556.'
        }
        strurl = requests.get(url=link, headers=headers, data=payload).text
        # 接下来的操作与之前的一样 ： 获得text 再从text中清洗内容传入到film字典中
        Soup = BeautifulSoup(strurl, 'lxml')
        # 获取标题和简介的标签
        Title_data = Soup.select('#content > h1 > span:nth-child(1)')
        Summary_data = Soup.select('#link-report > span:nth-child(1)')
        # 建立一个电影字典 映射存放标题和简介
        film = {}
        # 由于得到的是一个set对象 所以迭代获取其中的文本
        for x in Title_data:
            film['title'] = x.get_text()
        for x in Summary_data:
            # 将空格变成'' 并按'\n'分割形成列表
            film['Summary'] = x.get_text().replace(' ', '').split('\n')
        print('导入简介:%s' % film['title'])
        # 写入文件
        f.write(film['title'])
        f.write('\n-----------------\n')
        for x in film['Summary']:
            # 如果是''就不写入文件
            if x != '':
                f.write(x)
                f.write('\n')
        f.write(
            '\n---------------------------------------------------------\n')
        # 设置延迟
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
    f.close()


if __name__ == '__main__':
    # 得到所有的主页主页链接
    Movie_links = get_links()
    print('链接获取成功')
    get_summary(Movie_links)
    print('获取简介成功')