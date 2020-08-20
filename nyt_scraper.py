
import json
import datetime
from scraper import *

def nyt_run():

    print('new york times')

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    nyt_us = nyt(data)
    nyt_us.url = 'https://www.nytimes.com/section/us'
    nyt_us.article_heading_id = 'css-1hdf4fa eb5pyrn3'
    nyt_us.section = 'us'

    # politics
    nyt_politics = nyt(data)
    nyt_politics.url = 'https://www.nytimes.com/section/politics'
    nyt_politics.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_politics.section = 'politics'

    # # climate
    # nyt_climate = scraper()
    # nyt_climate.url = 'https://www.nytimes.com/section/climate'
    # nyt_climate.article_heading_id = 'css-l2vidh e4e4i5l1'
    # nyt_climate.section = 'climate'

    # 2020 election
    nyt_election = nyt(data)
    nyt_election.url = 'https://www.nytimes.com/section/technology'
    nyt_election.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_election.section = 'election'

    # tech
    nyt_tech = nyt(data)
    nyt_tech.url = 'https://www.nytimes.com/section/technology'
    nyt_tech.article_heading_id = 'css-1hdf4fa e1xdw5352'
    nyt_tech.section = 'tech'
    nyt_us.base_url_required = True

    # business
    nyt_business = nyt(data)
    nyt_business.url = 'https://www.nytimes.com/section/business'
    nyt_business.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_business.section = 'business'
    nyt_us.base_url_required = True

    # science
    nyt_science = nyt(data)
    nyt_science.url = 'https://www.nytimes.com/section/science'
    nyt_science.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_science.section = 'science'

    # health
    nyt_health = nyt(data)
    nyt_health.url = 'https://www.nytimes.com/section/health'
    nyt_health.article_heading_id = 'css-171kk9w e4e4i5l1'
    nyt_health.section = 'health'

    # news
    nyt_news = nyt(data)
    nyt_news.url = 'https://www.nytimes.com/'
    nyt_news.article_heading_id = 'css-1rvhhh9 e1whdksc1'
    nyt_news.section = 'news'

    nyt_us.scrape()
    nyt_politics.scrape()
    nyt_election.scrape()
    nyt_business.scrape()
    nyt_tech.scrape()
    nyt_science.scrape()
    nyt_health.scrape()
    #nyt_news.scrape()

    filepath = 'nyt/nyt-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nyt_run()
