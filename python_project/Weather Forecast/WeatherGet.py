# -*- encoding: utf-8 -*-
# here put the import lib
import requests
from bs4 import BeautifulSoup
import pandas as pd


# 获取天气数据
def get_data():
    url = "http://www.tianqihoubao.com/lishi/hangzhou/month/201812.html"
    Weathers = []
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    }
    # get方式请求网页 获取源码文本
    strpage = requests.request("GET", url, headers=headers).text
    # 将源码解析 缩小范围 用'lxml'加快解析速度
    Soup = BeautifulSoup(strpage, 'lxml')
    # 寻找所有tr表格元素
    All_tr = Soup.find_all('tr')
    # 在获取的tr元素中查找相对应的信息元素
    for x in All_tr[1:]:
        # 拆分字符串，形成数组
        List = x.text.split()
        # 日期
        date = ''.join(List[0])
        # 天气情况
        weather = ''.join(List[1:3])
        # 气温
        T = ''.join(List[3:6])
        # 将三大信息加入到/list中
        Weathers.append([date, weather, T])
    return Weathers



if __name__ == '__main__':
    result = get_data()
    # 构造DataFrame数据类型
    weather = pd.DataFrame(result, columns=['日期', '天气情况', '气温'])
    # 将DataFrame数据类型输出到表格
    weather.to_excel('Weather Forecast/201812杭州天气情况.xlsx', index=False)