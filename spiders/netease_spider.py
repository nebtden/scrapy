import scrapy
from learing_scrapy.items import NetEaseItem


class NeteaseSpider(scrapy.Spider):
    name = "netease"
    allowed_domains = "news.163.com"

    start_urls = [
        "http://news.163.com/rank/",
        "http://news.163.com/shehui/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = NetEaseItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item
