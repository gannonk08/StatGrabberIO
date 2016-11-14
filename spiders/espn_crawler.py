# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from items import *
import logging
import re


class EspnCrawlerSpider(CrawlSpider):

    name = 'espn_crawler'

    def __init__(self, *args, **kwargs):
      super(EspnCrawlerSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]

    allowed_domains = ['espn.com']

    custom_settings = {
        'ITEM_PIPELINES': {
            'pipelines.AddTablePipeline': 500,
            'export_pipelines.ExportJSON':400,

        }
    }

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    def parse(self, response):
        scores = response.xpath('//*[@id="linescore"]/tbody/tr/td/text()')

        i = 0

        homeIndex = 1
        homeItem = homeTeamItem()

        awayIndex = 1
        awayItem = awayTeamItem()

        requestItem = requestURLItem()
        requestItem['url'] = self.start_urls[0]

        sportTypeMatch = re.search(r"(?<=espn.com)(.*)(?=game[?])",self.start_urls[0])
        if sportTypeMatch:
            awayItem['sportType'] = sportTypeMatch.groups()[0].replace("/","")
            homeItem['sportType'] = sportTypeMatch.groups()[0].replace("/","")

        gameIdMatch = re.search(r"(?<=gameId=)(.*)",self.start_urls[0])
        if gameIdMatch:
            awayItem['gameId'] = gameIdMatch.groups()[0]
            homeItem['gameId'] = gameIdMatch.groups()[0]





        for score in scores:
            if i <= 5:
                if i == 0:
                    awayItem['awayTeam'] = score.extract()
                elif i == 5:
                    awayItem['final'] = score.extract()
                else:
                    awayItem['Q' + str(awayIndex)] = score.extract()
                    awayIndex = awayIndex + 1
            if i > 5:
                if i == 6:
                    homeItem['homeTeam'] = score.extract()
                elif i == 11:
                    homeItem['final'] = score.extract()
                else:
                    homeItem['Q' + str(homeIndex)] = score.extract()
                    homeIndex = homeIndex + 1
            i += 1

        yield awayItem
        yield homeItem
