import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from anadolubank.items import Article


class AnadoluSpider(scrapy.Spider):
    name = 'anadolu'
    allowed_domains = ['anadolubank.com.tr']
    start_urls = ['https://www.anadolubank.com.tr/ab/tumDuyurular']

    def parse(self, response):
        links = response.xpath('//div[@class="row features"]//h4/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="row features"]//h4//text()').get()
        content = response.xpath('//div[@class="span9"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = " ".join(content[2:])

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
