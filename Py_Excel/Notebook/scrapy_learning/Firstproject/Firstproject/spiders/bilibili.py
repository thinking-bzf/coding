import scrapy
from lxml import etree


class ProgramItem(scrapy.Item):
    Program = scrapy.Field()
    # author = scrapy.Field()


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com/']
    start_urls = ['http://www.bilibili.com//']

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        item = ProgramItem()
        item["Program"] = html_obj.xpath(
            "//div[@id='app']/div[@class='international-home']/div[@class='first-screen b-wrap']/div[@id='reportFirst2']/div[@class='extension']/div[@class='ext-box']/div[@class='video-card-common ex-card-common']"
        )
        print(item)

