import scrapy
from restaurant_crawler.items import RestaurantItem

class NYMagSpider(scrapy.Spider):
    name = 'nymag'
    start_urls = ['http://nymag.com/srch?t=restaurant&N=265+336&No=0&Ns=nyml_sort_name%7C0']

    def parse(self, response):
        for url in response.css('dl.result a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_review)

        for url in response.css('li.next > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse)

    def parse_review(self, response):
        item = RestaurantItem()
        if len(response.css('div.summary-address')):
            item['name'] = response.css('h1::text')[3].extract()
            item['description'] = response.css('meta[name=nyml_suggested_text]::attr(content)').extract_first()
            item['address'] = response.css('meta[name=nyml_address]::attr(content)').extract_first() + ', ' + response.css('meta[name=nyml_address_city]::attr(content)').extract_first() + ', ' + response.css('meta[name=nyml_address_state]::attr(content)').extract_first() + ', ' + response.css('meta[name=nyml_address_zip]::attr(content)').extract_first()
            item['source'] = 'NYMag Critic\'s Picks'
            item['source_url'] = response.url
            yield item
