import scrapy

class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
    address = scrapy.Field()
