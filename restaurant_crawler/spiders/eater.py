import scrapy
from restaurant_crawler.items import RestaurantItem

class EaterSpider(scrapy.Spider):
    name = 'eater'
    start_urls = ['http://ny.eater.com/reviews']

    def parse(self, response):
        for url in response.css('a[data-analytics-link="review"]::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_review)

        for url in response.css('span.m-pagination__next > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse)

    def parse_review(self, response):
        item = RestaurantItem()
        if len(response.css('h1::text')) > 1:
            item['name'] = response.css('h1::text')[1].extract()
            item['description'] = u"{}. {}".format(response.css('h1::text').extract_first(), response.css('h2::text').extract_first())
            item['date'] = response.css('span.p-byline__time::text').extract_first()
            item['address'] = response.css('div.m-review-scratch__contact-group p::text').extract_first()
            yield item
