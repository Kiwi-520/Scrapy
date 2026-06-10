import scrapy


class CromaSpiderSpider(scrapy.Spider):
    name = "croma_spider"
    allowed_domains = ["croma.com"]
    start_urls = ["https://www.croma.com/"]

    def parse(self, response):
        pass
