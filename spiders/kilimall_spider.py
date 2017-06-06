import scrapy
from learing_scrapy.items import ArticleItem


class KilimallSpider(scrapy.Spider):
    name = "kilimall"
    allowed_domains = "http://www.kilimall.co.ke"
    start_urls = [
        "http://www.kilimall.co.ke/women-dresses/",
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #

    def parse(self, response):
        for sel in response.xpath('//h3[@class="goods-name"]/a'):
            item = ArticleItem()
            item['title'] = sel.xpath('text()').extract()
            item['url'] = sel.xpath('@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
# title = sel.xpath('a/text()').extract()
# link = sel.xpath('a/@href').extract()
# desc = sel.xpath('text()').extract()
# print(title, link, desc)
# for sel in response.xpath('//ul[@class="menu"]'):
#     item = KilimallItem()
#     item['title'] = sel.css('a/text()').extract()
#     item['link'] = sel.css('a/@href').extract()
#     item['desc'] = sel.css('text()').extract()
#     yield item
