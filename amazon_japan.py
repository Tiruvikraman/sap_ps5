import scrapy
from scrapy.crawler import CrawlerProcess
import time


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.co']
    start_urls = ['https://www.amazon.co.jp/s?k=iphone+15+pro']

    def parse(self, response):
        time.sleep(2)
        price = response.css('span.a-price-whole::text').get()
        yield {
            'price': price.strip() if price else None
        }

# Create a CrawlerProcess instance
process = CrawlerProcess()

# Start the crawling process by passing the spider object
process.crawl(AmazonSpider)

# This will start the crawling process and won't stop until the spider has finished or encountered an error
process.start()
process.stop()
