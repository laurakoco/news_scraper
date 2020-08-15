
import json
import datetime
from scraper import *

def dm_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us 2020 election
    dm_election = dm(data)
    dm_election.url = 'https://www.dailymail.co.uk/news/2020-election/index.html'
    dm_election.section = 'election'

    # business
    dm_business = dm(data)
    dm_business.url = 'https://www.dailymail.co.uk/money/markets/index.html'
    dm_business.section = 'business'
    dm_business.base_url_required = True

    # science-tech
    dm_science = dm(data)
    dm_science.url = 'https://www.dailymail.co.uk/sciencetech/index.html'
    dm_science.section = 'science-tech'
    dm_science.base_url_required = True

    # home
    # dm_home = scraper()
    # dm_home.url = 'https://www.dailymail.co.uk/ushome/index.html'
    # dm_home.article_heading_id = 'linkro-darkred'
    # dm_home.content_id = 'articleBody'

    # dm_election.scrape()
    dm_business.scrape()
    dm_science.scrape()

    filepath = 'dm/dm-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

dm_run()