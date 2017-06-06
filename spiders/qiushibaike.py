import scrapy


class Qiushibaike(scrapy.Spider):
    name = "qiushibaike"
    allowed_domains = "www.qiushibaike.com"
    start_urls = [
        "http://www.qiushibaike.com/history/",
        "http://www.qiushibaike.com/pic/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
