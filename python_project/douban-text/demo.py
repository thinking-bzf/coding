'''
  function:爬取豆瓣top250的电影信息，并写入Excel文件
  env:python3.6.5
  author:jxc
'''
import time

import requests
import re
from openpyxl import workbook  # 写入Excel表所用
from bs4 import BeautifulSoup as bs


class Top250:
	def __init__(self):
		#起始地址
		self.start_url = 'https://movie.douban.com/top250'
		#请求头，浏览器模拟
		self.headers = {
			'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
		}
		#爬取页数
		self.page_num = 10
		# self.proxy={'http':'http://101.4.136.34:81'}

	'''url拼接'''

	def get_page_url(self):
		n = 0  #第一页开始,下标0
		while n < self.page_num:
			yield self.start_url + '?start={}&filter='.format(n * 25)
			n += 1

	'''获取页面源码'''

	def getHtml(self):
		gu = self.get_page_url()  #url生成器
		for url in gu:
			html = requests.get(url, headers=self.headers).text
			yield html

	'''电影数据提取'''

	def getData(self):
		gh = self.getHtml()  # html源码生成器
		for html in gh:  # html:网页源码
			soup = bs(html, 'lxml')
			for info in soup.find_all('div', class_='info'):
				c_name = info.find('span',
								   class_='title').text.strip()  # 得到电影中文名
				message = info.select(
					'div.bd p')[0].text.strip()  #得到导演、主演、年份、地区信息
				yat = re.search('[0-9]+.*\/?',
								message).group().split('/')  #得到年份、地区、类型信息列表
				year, area, type = yat[0], yat[1], yat[2]  #得到年份、地区、类型
				da = re.search('导演.+\s',
							   message).group().strip() + '...'  #得到导演、主演混合信息
				director = re.findall('导演:(.+?)\s', da)[0].strip()  #得到导演信息
				#得到主演信息,不存在时发生异常，进行异常处理
				try:
					mainActors = re.findall('主演:(.+?)[.,]+', da)[0].strip()
				except IndexError:
					mainActors = '暂无主演信息'
				mark_info = info.find('div', class_='star')  #得到评分、评价人数混合信息
				score = mark_info.find('span',
									   class_='rating_num').text.strip()  #得到评分
				count = re.search(
					'[0-9]+',
					mark_info.select('span')[3].text).group()  #得到评价人数
				#得到简介,捕捉不存在时的异常
				try:
					quote = info.select('p.quote span')[0].text.strip()
				except IndexError:
					quote = '该影片暂时无简介'
				yield [
					c_name, year, area, type, director, mainActors, score,
					count, quote
				]

	'''保存到excel文件
	:param file_name:文件名
	'''

	def saveToExcel(self, file_name):
		wb = workbook.Workbook()  # 创建Excel对象
		ws = wb.active  # 获取当前正在操作的表对象
		ws.append(['电影名', '年份', '地区', '剧情类型', '导演', '主演', '评分', '评论人数', '简介'])
		gd = self.getData()  #数据生成器
		for data in gd:
			ws.append(data)
		wb.save(file_name)


if __name__ == '__main__':
	start = time.time()
	top = Top250()
	try:
		top.saveToExcel('top250.xlsx')
		print('抓取成功,用时%4.2f' % (time.time() - start) + '秒')
	except Exception as e:
		print('抓取失败,原因:%s' % e)
