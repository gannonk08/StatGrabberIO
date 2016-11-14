import scrapy

from scrapy.item import Item, Field

class awayTeamItem(Item):
    gameId = Field()
    sportType = Field()
    awayTeam = Field()
    Q1 = Field()
    Q2 = Field()
    Q3 = Field()
    Q4 = Field()
    final = Field()


class homeTeamItem(Item):
    gameId = Field()
    sportType = Field()
    homeTeam = Field()
    Q1 = Field()
    Q2 = Field()
    Q3 = Field()
    Q4 = Field()
    final = Field()

class requestURLItem(Item):
    url = Field()
