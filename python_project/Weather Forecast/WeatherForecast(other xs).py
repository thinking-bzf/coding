# -*- encoding: utf-8 -*-
# here put the import lib
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib.pyplot import MultipleLocator
from sklearn.linear_model import LinearRegression
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
}


def initplot():
    plt.figure(figsize=(10, 10))
    plt.grid(True)
    # ax为两条坐标轴的实例


def get_YearUrl(city_url):
    MonthDir = {}
    city_content = requests.request("GET", city_url, headers=headers).text
    city_Soup = BeautifulSoup(city_content, 'lxml')
    years_box = city_Soup.find('div', class_='wdetail')
    StartYear = int(years_box.find('h2').text[:4])
    Year = StartYear
    All_years = years_box.find_all('div', class_='box pcity')
    for year in All_years:
        All_month = year.find_all('a')
        List = []
        for month in All_month:
            List.append('http://www.tianqihoubao.com/' + month.get('href'))
        MonthDir[Year] = List
        Year += 1
    EndYear = Year - 1
    return (MonthDir, StartYear, EndYear)


# 获取天气数据
def get_data(url):

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
        Tmax = T.split('/')[0].replace('℃','')
        Tmin = T.split('/')[1].replace('℃','')
        # 将三大信息加入到/list中
        Weathers.append([date, weather, Tmax, Tmin])
    return Weathers


def MonthAnalysis(source):
    AverageDir = {}
    for month in range(1, 13):
        SheetList = [k for k in source.keys() if (int(k[-2:]) == month)]
        # print(SheetList)
        AverageList = []
        for sheet in SheetList:
            DT = source[sheet]
            # DT['最高气温'] = DT['最高气温'].str.split('/', expand=True)[0]
            DT['最高气温'] = DT['最高气温'].map(lambda x: int(x))
            AverageList.append(DT['最高气温'].mean())
        AverageList = list(map(lambda x: float(format(x, '.3')), AverageList))
        AverageDir[month] = AverageList
        initplot()
        plt.plot(range(len(AverageList)), AverageList)
        # plt.show()
        model = LinearRegression()

        xTrain = np.array(range(len(AverageList)))[:, np.newaxis]
        yTrain = np.array(AverageList)
        hypothesis = model.fit(xTrain, yTrain)
        xNew = np.array([1, len(AverageList)])[:, np.newaxis]
        yNew = model.predict(xNew)
        # plt.plot(xNew, yNew, 'g--')
        # plt.show()
        print(model.predict([[len(AverageList) + 1]])[0])
        print(AverageList)
    return AverageDir


def TempEffect(source, maxtemp):
    EffectDir = {}
    for month in range(1, 13):
        SheetList = [k for k in source.keys() if (int(k[-2:]) == month)]
        MonthEffectDir = {}
        for sheet in SheetList:
            DT = source[sheet]
            Effect = []
            for item in DT['天气情况']:
                # Effect.append()
                MonthEffectDir['item'].append()


if __name__ == "__main__":
    # 获取杭州所有的年份的url
    if not os.path.exists(r"Weather Forecast\result.xlsx"):
        MonthDir, StartYear, EndYear = get_YearUrl(
            'http://www.tianqihoubao.com/lishi/hangzhou.html')
        # print(MonthDir)
        writer = pd.ExcelWriter('Weather Forecast/result.xlsx',
                                engine="xlsxwriter")
        for year in range(StartYear, EndYear + 1):
            for month in MonthDir[year]:
                monthdata = get_data(month)
                weather = pd.DataFrame(monthdata,
                                       columns=['日期', '天气情况', '最高气温', '最低气温'])
                weather.to_excel(writer, sheet_name=month[-11:-5], index=False)
                print(month[-11:-5] + ' OK!')
        writer.save()
    result = pd.read_excel(r'Weather Forecast\result.xlsx', None)
    # 得到每年每个月的最高气温平均值字典
    Monthdir = MonthAnalysis(result)
    TempEffectDir = {}
    # TempEffectDir = TempEffect(result, Monthdir)
