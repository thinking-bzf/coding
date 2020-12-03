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
            "//div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/p/text()"
        )
        print(item)
