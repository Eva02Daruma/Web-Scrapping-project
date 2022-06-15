from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ImdbCrawler(CrawlSpider):
    name = 'zmart'
    allowed_domains = ['www.zmart.cl']
    start_urls = ['https://www.zmart.cl/Scripts/default.asp']
    rules = (Rule(LinkExtractor()),)
