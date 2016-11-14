from flask import Flask, request, jsonify
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from spiders.espn_crawler import EspnCrawlerSpider
from items import awayTeamItem
from items import homeTeamItem
from items import requestURLItem

from export_pipelines import *


import os
from flask import Flask, render_template, url_for, json


app = Flask(__name__)

spiders = ['espn_crawler']

@app.route('/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        content = request.get_json(silent=True)
        if content['spider'] in spiders:
            configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
            runner = CrawlerRunner()
            d = runner.crawl(EspnCrawlerSpider, start_url=content['url'])
            d.addBoth(lambda _: reactor.stop())
            reactor.run()

            SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
            json_url = os.path.join(SITE_ROOT, "exports/json/", "espn_crawler.json")
            data = json.load(open(json_url))


            return jsonify(data)
        return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
