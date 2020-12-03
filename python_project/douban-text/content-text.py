# -*- encoding: utf-8 -*-
# here put the import lib
import requests
import lxml
from bs4 import BeautifulSoup

# 以下完成将250部电影的名称 导演 编剧 主演 类型 制片国家/地区 上映时间 语言 时长 又名 记录到txt文件中 后期将导入excel文件中
# 实例
# 肖申克的救赎 The Shawshank Redemption
# 导演: 弗兰克·德拉邦特
# 编剧: 弗兰克·德拉邦特 / 斯蒂芬·金
# 主演: 蒂姆·罗宾斯 / 摩根·弗里曼 / 鲍勃·冈顿 / 威廉姆·赛德勒 / 克兰西·布朗 / 吉尔·贝罗斯 / 马克·罗斯顿 / 詹姆斯·惠特摩 / 杰弗里·德曼 / 拉里·布兰登伯格 / 尼尔·吉恩托利 / 布赖恩·利比 / 大卫·普罗瓦尔 / 约瑟夫·劳格诺 / 祖德·塞克利拉 / 保罗·麦克兰尼 / 芮妮·布莱恩 / 阿方索·弗里曼 / V·J·福斯特 / 弗兰克·梅德拉诺 / 马克·迈尔斯 / 尼尔·萨默斯 / 耐德·巴拉米 / 布赖恩·戴拉特 / 唐·麦克马纳斯
# 类型: 剧情 / 犯罪
# 制片国家/地区: 美国
# 语言: 英语
# 上映日期: 1994-09-10(多伦多电影节) / 1994-10-14(美国)
# 片长: 142分钟
# 又名: 月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎

# 存放250部电影的主页链接
links = []
# 10页循环得到每一页的电影链接
for x in range(0, 25, 25):
    # 电影列表的每一页链接构造
    MainPage = "https://movie.douban.com/top250?start=" + str(x) + '&filter='
    # payload 和 headers 来自Postman，用于请求网页链接
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
    strMainpage = requests.get(url=MainPage, headers=headers, data=payload)
    # 用BeautifulSoup方法将得到的网页转换成可解析的类型
    Soup = BeautifulSoup(strMainpage.text, 'lxml')
    # 在每一页的电影列表得到电影的主页
    for i in range(1, 26):
        # 在网页源代码处复制需要得到的标签
        Data = Soup.select(
            '#content > div > div.article > ol > li:nth-child(' + str(i) +
            ') > div > div.info > div.hd > a')
        # 将得到的标签内容中的href属性值传给links列表
        for item in Data:
            links.append(item.get('href'))
            print('导入链接成功: %s' % item.get('href'))

# 输出电影所在的网址
# print(links)
f = open('txt1.txt', 'w', encoding='utf-8')
# 依次打开links中的链接爬取内容 并将内容导入到txt中
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
    strurl = requests.get(url=link, headers=headers, data=payload)

    # 接下来的操作与之前的一样 ： 获得text 再从text中清洗内容传入到film字典中
    Soup = BeautifulSoup(strurl.text, 'lxml')
    Titledata = Soup.select('#content > h1 > span:nth-child(1)')
    hotComment = Soup.select('#hot-comments')
    ShortComments = hotComment[0].find_all('div', class_='comment-item')
    film = {}
    for x in Titledata:
        film['title'] = x.get_text()
    for item in ShortComments:
        film['ShortComment'] = []
        film['ShortComment'].append(item.find('span', class_='short').text)
        # f.write(ShortComment)
    # for x in hotComment:
    #     film['hotcommments'] = x.get_text()
    #
    f.write(film['title'])
    f.write('\n')
    for x in film['ShortComment']:
        f.write(x)
        f.write('\n')
    f.write('------------------------------------------------------------\n')
    print('导入成功:%s' % film['title'])
f.close()
