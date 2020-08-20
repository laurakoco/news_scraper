
import json
import datetime
from scraper import *

def reuters_run():

    print('reuters')

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

    # politics
    reuters_politics = reuters(data)
    reuters_politics.url = 'https://www.reuters.com/politics'
    reuters_politics.section = 'politics'

    # business
    reuters_business = reuters(data)
    reuters_business.url = 'https://www.reuters.com/finance'
    reuters_business.section = 'business'

    # us news
    reuters_us = reuters(data)
    reuters_us.url = 'https://www.reuters.com/news/us'
    reuters_us.section = 'us'

    # tech
    reuters_tech = reuters(data)
    reuters_tech.url = 'https://www.reuters.com/news/technology'
    reuters_tech.section = 'tech'

    # news
    reuters_news = reuters(data)
    reuters_news.url = 'https://www.reuters.com/'
    reuters_news.section = 'news'

    reuters_politics.scrape()
    reuters_business.scrape()
    reuters_us.scrape()
    reuters_tech.scrape()
    # reuters_news.scrape()

    filepath = 'reuters/reuters-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

reuters_run()