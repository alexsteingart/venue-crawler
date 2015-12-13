import scrapy
from restaurant_crawler.items import RestaurantItem

class EaterSpider(scrapy.Spider):
    name = 'eatermaps'

    def parse(self, response):
        item = RestaurantItem()
        for r in response.css('div.m-map__item-card'):
            item['name'] = r.css('h3::text').extract_first()
            item['description'] = r.css('p::text').extract_first()
            item['address'] = u','.join(r.css('div.m-map__item-address div.m-map__item-contact-segment::text').extract())
            item['source'] = 'Eater Maps'
            item['source_url'] = response.url
            item['source_title'] = response.css('title::text').extract_first()
            yield item


    start_urls = [
     "http://ny.eater.com/maps/cheap-eats-nyc-mapped",
     "http://ny.eater.com/maps/the-hottest-restaurants-in-queens-right-now-may-2015",
     "http://ny.eater.com/maps/best-new-new-york-restaurants-heatmap",
     "http://ny.eater.com/maps/new-york-christmas-eve-restaurant",
     "http://ny.eater.com/maps/thanksgiving-specials-nyc",
     "http://ny.eater.com/maps/thanksgiving-restaurant-nyc",
     "http://ny.eater.com/maps/best-new-bakery-nyc",
     "http://ny.eater.com/maps/old-diners-best-new-york",
     "http://ny.eater.com/maps/the-best-places-to-drink-negra-modela",
     "http://ny.eater.com/maps/best-new-brunch-nyc-restaurants",
     "http://ny.eater.com/maps/10-restaurants-where-you-can-go-off-menu-in-nyc",
     "http://ny.eater.com/maps/williamsburg-greenpoint-restaurants-near-mofad-lab",
     "http://ny.eater.com/maps/best-martini-nyc",
     "http://ny.eater.com/maps/burgers-and-cocktails-a-match-made-in-heaven",
     "http://ny.eater.com/maps/sponsored-somms-sliders-new-york-city-s-best-burgers-paired-with-napa",
     "http://ny.eater.com/maps/new-york-city-best-cocktail-bars",
     "http://ny.eater.com/maps/best-new-york-restaurants-38",
     "http://ny.eater.com/maps/best-beer-bars-nyc",
     "http://ny.eater.com/maps/michelin-new-york-restaurants-2016",
     "http://ny.eater.com/maps/best-chicken-wings-nyc",
     "http://ny.eater.com/maps/natural-wine-bar-nyc",
     "http://ny.eater.com/maps/best-new-cocktail-bars-new-york-city-heatmap",
     "http://ny.eater.com/maps/free-wifi-coffee-shops-ny-east-village",
     "http://ny.eater.com/maps/wine-deals-nyc",
     "http://ny.eater.com/maps/best-late-night-restaurants-new-york-weeknight",
     "http://ny.eater.com/maps/best-new-ice-cream-shops-new-york-city",
     "http://ny.eater.com/maps/pizza-heat-map",
     "http://ny.eater.com/maps/best-cafe-coffee-shop-new-york-city-brooklyn-queens",
     "http://ny.eater.com/maps/best-cheap-eats-nyc-the-contest-eater",
     "http://ny.eater.com/maps/12-superior-steakhouse-side-dishes",
     "http://ny.eater.com/maps/cheap-snacks-nyc-vanessas-grays-papaya-lam-zhou",
     "http://ny.eater.com/maps/nyc-cheap-eats-best",
     "http://ny.eater.com/maps/10-sensational-steaks-to-eat-in-new-york-city",
     "http://ny.eater.com/maps/east-end-new-restaurants-2014",
     "http://ny.eater.com/maps/best-breakfast-NYC-Balthazar-egg-santina",
     "http://ny.eater.com/maps/best-beer-bars-new-york-city",
     "http://ny.eater.com/maps/best-hot-dogs-new-york-classic",
     "http://ny.eater.com/maps/new-york-city-best-barbecue-brooklyn-queens",
     "http://ny.eater.com/maps/hot-dogs-burgers-fried-clams-best-connecticut",
     "http://ny.eater.com/maps/ted-allens-picks-for-excellent-dining-in-new-york-city",
     "http://ny.eater.com/maps/wedding-nyc-restaurant-wedding-reception",
     "http://ny.eater.com/maps/best-karaoke-bars-new-york-city",
     "http://ny.eater.com/maps/sponsored-ny-negroni-week",
     "http://ny.eater.com/maps/best-new-nyc-outdoor-dining-restaurants-heatmap",
     "http://ny.eater.com/maps/best-new-burgers-new-york-city",
     "http://ny.eater.com/maps/best-outdoor-bar-beer-gardens-new-york-city",
     "http://ny.eater.com/maps/best-frozen-cocktails-bars-nyc-brooklyn",
     "http://ny.eater.com/maps/hannah-harts-go-to-new-york-city-restaurants",
     "http://ny.eater.com/maps/new-york-city-best-burgers-restaurants-burger-week",
     "http://ny.eater.com/maps/25-burgers-that-prove-that-midtown-doesnt-suck",
     "http://ny.eater.com/maps/12-terrific-restaurants-for-watching-the-snow-fall-in-nyc",
     "http://ny.eater.com/maps/jon-potters-guide-to-brooklyn",
     "http://ny.eater.com/maps/pappy-van-winkle-nyc-bar-restaurant",
     "http://ny.eater.com/maps/full-english-breakfast-fry-up-restaurants-new-york-city",
     "http://ny.eater.com/maps/where-to-eat-in-flushings-chinatown",
     "http://ny.eater.com/maps/sponsored-its-freezing-dont-go-outside-order-from-seamless",
     "http://ny.eater.com/maps/sea-urchin-where-to-eat-uni-new-york-city",
     "http://ny.eater.com/maps/spiciest-dishes-new-york-city",
     "http://ny.eater.com/maps/25-iconic-new-york-dishes",
     "http://ny.eater.com/maps/super-bowl-party-food-where-to-eat-new-york-city",
     "http://ny.eater.com/maps/classic-restaurants",
     "http://ny.eater.com/maps/the-hottest-restaurants-in-manhattan-right-now-january-2015",
     "http://ny.eater.com/maps/new-york-city-new-years-eve-restaurants-betony-cherche-midi-dirty-french",
     "http://ny.eater.com/maps/best-christmas-eve-dinners-in-new-york-city-2014",
     "http://ny.eater.com/maps/where-to-eat-on-christmas-day-in-new-york-city-4",
     "http://ny.eater.com/maps/pork-ribs-nyc",
     "http://ny.eater.com/maps/new-york-city-Thanksgiving-dinner-restaurant-best",
     "http://ny.eater.com/maps/the-unexpected-cuisines-that-pair-perfectly-with-negra-modelo"
    ]
