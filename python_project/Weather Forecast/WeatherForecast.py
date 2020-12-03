# -*- encoding: utf-8 -*-
# here put the import lib
import requests
from bs4 import BeautifulSoup
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import MultipleLocator
from sklearn.linear_model import LinearRegression


# 获取天气数据
def get_data():
    url = "http://www.tianqihoubao.com/lishi/hangzhou/month/202008.html"
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


def initplot():
    plt.figure(figsize=(15, 7))
    plt.grid(True)
    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(1)
    # ax为两条坐标轴的实例
    ax = plt.gca()
    # 把x轴的主刻度设置为1的倍数
    ax.xaxis.set_major_locator(x_major_locator)
    #把y轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)


def SingleVariableTemplot(DF):
    data = DF
    data['最高气温'] = data['气温'].str.split('/', expand=True)[0]
    data['最高气温'] = data['最高气温'].map(lambda x: int(x.replace('℃', '')))
    data['最低气温'] = data['气温'].str.split('/', expand=True)[1]
    data['最低气温'] = data['最低气温'].map(lambda x: int(x.replace('℃', '')))
    data['日期'] = data['日期'].map(lambda x: int(x.replace('2020年08月', '')[:-1]))
    initplot()
    plt.yticks(np.arange(30, 40))
    plt.xticks(np.arange(1, 24))
    plt.title("单变量线形回归预测天气-杭州08月")

    plt.plot(data['日期'], data['最高气温'], 'k.')
    # plt.plot(data['日期'], data['最低气温'], 'k.')
    for a, b in zip(data['日期'], data['最高气温']):
        plt.text(a, b, b, ha="center", va="bottom", fontsize=12)
        # plt.text(a, c, c, ha="center", va="bottom", fontsize=12)
    # 将日期转为矩阵
    xTrain = np.array(data['日期'])[:, np.newaxis]
    # 为方便理解，也转换成列向量
    yTrain = np.array(data['最高气温'])
    xtest = np.array([3, 6, 9, 12, 15, 18])[:, np.newaxis]
    ytest = np.array([36, 35, 35, 38, 38, 38])
    # 创建模型对象
    model = LinearRegression()
    # 根据训练数据拟合出直线(以得到假设函数)

    hypothesis = model.fit(xTrain, yTrain)
    # 截距
    print("直线截距=", hypothesis.intercept_)
    # 斜率
    print("直线斜率=", hypothesis.coef_)

    # 测试组的预测值
    hpyTest = model.predict(xtest)
    # 计算测试组的残差
    ssResTest = sum((ytest - hpyTest)** 2)
    print(f"训练组的残差为{model._residues}")
    print(f"测试组的残差为{ssResTest}")
    # 预测2020年8月20日的最高气温
    print("单变量线性回归预测:2020年8月21日的最高气温：", model.predict([[21]])[0])
    for i in [21, 22, 23]:
        plt.text(i,
                 model.predict([[i]])[0],
                 model.predict([[i]])[0],
                 ha="center",
                 va="bottom",
                 fontsize=10)
    # 也可以批量预测多个日期的气温，注意要以列向量形式表达（有余数据集量少，故间隔时间长气温可能有较大差异）
    # 此处仅利用模型表示，不代表真实值（假设要预测21号、22号、23号的天气）
    xNew = np.array([
        1,
        23,
    ])[:, np.newaxis]
    yNew = model.predict(xNew)

    plt.plot(xNew, yNew, 'g--')
    plt.savefig(r'Weather Forecast\img\WeatherForecast.jpg')
    plt.show()


if __name__ == '__main__':

    #解决中文乱码问题
    plt.rcParams["font.sans-serif"] = "SimHei"
    #解决负号无法正常显示的问题
    plt.rcParams['axes.unicode_minus'] = False
    if not os.path.exists(r"Weather Forecast\202008杭州上中旬天气情况.xlsx"):
        result = get_data()
        # 构造DataFrame数据类型
        weather = pd.DataFrame(result, columns=['日期', '天气情况', '气温'])
        # 将DataFrame数据类型输出到表格
        weather.to_excel('Weather Forecast/202008杭州上中旬天气情况.xlsx', index=False)
    weather_frame = pd.read_excel('Weather Forecast/202008杭州上中旬天气情况.xlsx')
    img_path = 'Weather Forecast/img'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    print("单变量线性回归")
    SingleVariableTemplot(weather_frame)