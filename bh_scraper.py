
import json
import datetime
from scraper import *

def bh_run():

    print('boston herald')

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    bh_politics = bh(data)
    bh_politics.url = 'https://www.bostonherald.com/news/politics/'
    bh_politics.section = 'politics'

    # election
    bh_election = bh(data)
    bh_election.url = 'https://www.bostonherald.com/tag/2020-election/'
    bh_election.section = 'election'

    # us
    bh_us = bh(data)
    bh_us.url = 'https://www.bostonherald.com/news/national-news/'
    bh_us.section = 'us'

    # business
    bh_business = bh(data)
    bh_business.url = 'https://www.bostonherald.com/news/business/'
    bh_business.section = 'business'

    # health
    bh_health = bh(data)
    bh_health.url = 'https://www.bostonherald.com/news/health/'
    bh_health.section = 'health'

    # news
    bh_news = bh(data)
    bh_news.url = 'https://www.bostonherald.com/'
    bh_news.section = 'news'
    bh_news.article_element = 'h6'

    bh_politics.scrape()
    bh_election.scrape()
    bh_us.scrape()
    bh_business.scrape()
    bh_health.scrape()
    bh_news.scrape()

    filepath = 'bh/bh-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

bh_run()
