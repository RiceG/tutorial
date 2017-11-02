import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dotamax.com/ladder/",
        "http://www.dotamax.com/ladder/se_asia/"
    ]

    def parse(self, response):
        for sel in response.xpath('/html'):
            item = DmozItem()
            item['title'] = sel.xpath('//title').extract()
            #item['link'] = sel.xpath('a/@href').extract()
            #item['desc'] = sel.xpath('text()').extract()
            yield item