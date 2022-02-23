import scrapy

class ToScrapeXpath(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = ['http://quotes.toscrape.com/page/1','http://quotes.toscrape.com/page/2']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags':quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }
