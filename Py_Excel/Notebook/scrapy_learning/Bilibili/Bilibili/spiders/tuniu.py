import scrapy
from lxml import etree

class PlaceItem(scrapy.Item):
    Program = scrapy.Field()

class TuniuSpider(scrapy.Spider):
    name = 'tuniu'
    allowed_domains = ['www.tuniu.com/guide/d-maerdaifu-3922']
    start_urls = ['http://https://www.tuniu.com/guide/d-maerdaifu-3922//']

    def parse(self, response):
        html = response.text
        html_obj = etree.HTML(html)
        item = PlaceItem()
        item["Program"] = html_obj.xpath(
            "//div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/a/text()"
        )
        print(item)
