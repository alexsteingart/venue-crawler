
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19"

SPIDER_MODULES = ['restaurant_crawler.spiders']

ITEM_PIPELINES = {
    'restaurant_crawler.pipelines.MongoPipeline': 100,
}
