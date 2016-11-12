import scrapy
import json
from restaurant_crawler.items import RestaurantItem

class EaterSpider(scrapy.Spider):
    name = 'eatermaps'

    def parse(self, response):
        json_response = json.loads(response.body)
        for data in json_response:
            yield scrapy.Request(response.urljoin(data['permalink']), self.parse_map)

    def parse_map(self, response):
        item = RestaurantItem()
        for r in response.css('div.m-map__item-card'):
            item['name'] = r.css('h3::text').extract_first()
            item['description'] = r.css('p::text').extract_first()
            item['address'] = u','.join(r.css('div.m-map__item-address div.m-map__item-contact-segment::text').extract())
            item['source'] = 'Eater Maps'
            item['source_url'] = response.url
            item['source_title'] = response.css('title::text').extract_first()
            yield item

    start_urls = ['http://ny.eater.com/maps/search.json?community_id=460&q=*']
