#import scrapy
#from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
#from sample_project.items import CraigslistSampleItem


#class MySpider(BaseSpider):
#    name = "hello"
#    allowed_domains = ["hellosantateresa.com"]
#    start_urls = [
#        "http://hellosantateresa.com/property_type/all/"
#        ]

#    def parse(self, response):
#        hxs = HtmlPathSelector(response)
#        
        #titles = hxs.select("//p")
        #items = []
        #for titles in titles:
            #item = CraigslistSampleItem()
            #item ["title"] = titles.select("a/text()").extract()
            #item ["link"] = titles.select("a/@href").extract()
            #item.append(item)



import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
