# -*- encoding: utf-8 -*-
# here put the import lib
import requests
import lxml
from bs4 import BeautifulSoup
import re
import random
import time
import pandas as pd

"""
改程序实现将250部电影的details存储到excel文件中 以便之后的数据分析
实现翻页 不实现主页跳转
"""

def get_details():
    # 存储每部影片的细节信息
    movie_details = []
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
        # 在获取解析好BeautifulSoup类Soup中寻找class='grid_view'的'ol'标签 25条记录的details都写在该标签下
        ol_tag = Soup.find('ol', class_='grid_view')
        # 在找到的'ol'标签中寻找所有的li标签 共会得到25条
        details = ol_tag.find_all('li')
        # li标签迭代 即每条记录中寻找各类信息
        for detail in details:
            # 电影排名 存放在em标签中 获取其text属性
            movie_rank = detail.find('em').text
            # 电影标题 存放在class='title' 的span标签 获取其text属性
            movie_title = '《' + detail.find('span', class_='title').text + '》'
            # 电影别名 与title同理 存放在class='other'的span标签中
            movie_other = '《' + detail.find(
                'span', class_='other').text.split('\xa0')[-1].strip() + '》'
            # 电影评论数 运用正则表达式 寻找 xxx人评价的字段 将他变成字符串 用切片的方法取倒数第三个字以前的内容
            movie_CommentNum = detail.find(
                text=re.compile(r'\d+人评价')).string[:-3]
            # 电影评分 寻找class='rating_num'的span标签 获取其text属性
            movie_score = detail.find('span', class_='rating_num').text
            # 查看页面结构 会发现上映时间等信息都存在p标签中 所以先获取p标签的所有内容
            movie_P = detail.find('p').text
            # 用split方法根据回车分割成两个字符串
            movie_P1 = movie_P.split('\n')[1]
            movie_P2 = movie_P.split('\n')[2]
            # 电影导演 P1中用split 根据'\xa0'分割 取第一个元素 strip方法去除空格 再获取其前第4个字符以后的字符即导演
            movie_director = movie_P1.split('\xa0')[0].strip()[4:]
            # 电影上映时间 P2中用split 根据'\xa0'分割 取第一个元素 strip方法去除空格 再获取其前4个字符即上映时间
            movie_year = movie_P2.split('\xa0')[0].strip()[:4]
            # 制片国家 P2中用split 根据'\xa0'分割 取第二个元素
            movie_country = movie_P2.split('\xa0')[2]
            # 电影类型 P2中用split 根据'\xa0'分割 取最后一个元素
            movie_type = movie_P2.split('\xa0')[-1].strip()
            # 将必要的属性加入到details的列表中
            movie_details.append([
                movie_rank,
                movie_title,
                movie_other,
                movie_CommentNum,
                movie_score,
                movie_year,
                movie_director,
                movie_country,
                movie_type,
            ])
            print([
                movie_rank,
                movie_title,
                movie_other,
                movie_CommentNum,
                movie_score,
                movie_year,
                movie_director,
                movie_country,
                movie_type,
            ])
        # 每次循环产生一个随机数 每次结束后让程序停1-3秒
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
    return movie_details


if __name__ == '__main__':
    Movie_details = get_details()
    # 用得到的details用pandas构造DataFrame对象 columns表示每一列的字段
    movie_frame = pd.DataFrame(
        Movie_details,
        columns=['排名', '标题', '又名', '评论数', '评分', '上映时间', '导演', '制片国家', '电影类型'])
    # 将整理好的DataFrame对象导出成excel表格
    movie_frame.to_excel('Douban_DataAnalyze/top250.xlsx',index=False)
    print('导出成功')
