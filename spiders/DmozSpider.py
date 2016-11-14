import scrapy
from items import *

class DmozSpider(scrapy.Spider):

    name = 'dmoz'

    custom_settings = {
        'ITEM_PIPELINES': {
            'pipelines.AddTablePipeline': 500,
            'export_pipelines.ExportJSON':400,
            # 'screenshot_pipelines.ScreenshotPipeline':300,

        }
    }

    def __init__(self, *args, **kwargs):
      super(DmozSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]

    allowed_domains = ['dmoz.org']
    start_urls = []

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
