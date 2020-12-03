import requests
import lxml
import requests
from bs4 import BeautifulSoup
links = []
for x in range(0, 251, 25):      # 10页循环
    MainPage = "https://movie.douban.com/top250?start="+str(x)+'filter='
    # 来自Postman工具，用于得到request
    payload = {}
    headers = {
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
      'Cookie': 'city=0571; prov=cn0571; weather_city=zj_hz; region_ip=60.176.44.x; region_ver=1.2; adb_isBlock=0; ifengRotator_iis3_c=6; ifengWindowCookieName_0=1; userid=1599482322428_4gykmt8460'
    }
    strMainpage = requests.request("GET", MainPage, headers=headers, data=payload)
    Soup = BeautifulSoup(strMainpage.text, 'lxml')
    for i in range(1, 26):
        # 获取每部电影的主页
        Data = Soup.select('#content > div > div.article > ol > li:nth-child('+str(i)+') > div > div.info > div.hd > a')
        # 将得到的链接内容存到list列表中
        for item in Data:
            links.append(item.get('href'))
            print('导入链接成功')
print(links)       #输出电影所在的网址
for link in links:     #将电影演员表导入txt文件
    url = link
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        'Cookie': 'city=0571; prov=cn0571; weather_city=zj_hz; region_ip=60.176.44.x; region_ver=1.2; adb_isBlock=0; ifengRotator_iis3_c=6; ifengWindowCookieName_0=1; userid=1599482322428_4gykmt8460'
    }
    strurl = requests.request("GET", url, headers=headers, data=payload)
    Soup = BeautifulSoup(strurl.text, 'lxml')
    data = Soup.select('#info')
    for x in data:
        film = {
            'actor': x.get_text()
        }
        f = open('电影.txt', 'a', encoding = 'utf-8')      
        f.write(film['actor'])
        f.close()
        print('导入成功')