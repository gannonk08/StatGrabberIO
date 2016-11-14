SPIDER_SETTINGS = [
    {
        'endpoint': 'dmoz',
        'location': 'spiders.DmozSpider',
        'spider': 'DmozSpider',
    }
]

DOWNLOAD_DELAY = 5

DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,}

RETRY_TIMES = 2
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
