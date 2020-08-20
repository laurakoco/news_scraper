
import json
import datetime
from scraper import *
import os

def cp_run():

    print('christian post')

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # politics
    cp_politics = cp(data)
    cp_politics.url = 'https://www.christianpost.com/category/politics'
    cp_politics.section = 'politics'

    # us
    cp_us = cp(data)
    cp_us.url = 'https://www.christianpost.com/category/us'
    cp_us.section = 'us'

    # business
    cp_business = cp(data)
    cp_business.url = 'https://www.christianpost.com/business'
    cp_business.section = 'business'

    # news
    cp_news = cp(data)
    cp_news.url = 'https://www.christianpost.com/'
    cp_news.section = 'news'

    cp_politics.scrape()
    cp_us.scrape()
    cp_business.scrape()
    cp_news.scrape()

    filepath = 'cp/cp-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

cp_run()
