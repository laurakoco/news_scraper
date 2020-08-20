

import json
import datetime
from scraper import *

def guardian_run():

    print('guardian')

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # politics
    guardian_politics = guardian(data)
    guardian_politics.url = 'https://www.theguardian.com/us-news/us-politics'
    guardian_politics.section = 'politics'

    # us
    guardian_us = guardian(data)
    guardian_us.url = 'https://www.theguardian.com/us-news'
    guardian_us.section = 'us'

    # business
    guardian_business = guardian(data)
    guardian_business.url = 'https://www.theguardian.com/us/business'
    guardian_business.section = 'business'

    # science
    guardian_science = guardian(data)
    guardian_science.url = 'https://www.theguardian.com/science'
    guardian_science.section = 'science'

    # tech
    guardian_tech = guardian(data)
    guardian_tech.url = 'https://www.theguardian.com/us/technology'
    guardian_tech.section = 'tech'

    # envionrment
    guardian_env = guardian(data)
    guardian_env.url = 'https://www.theguardian.com/us/environment'
    guardian_env.section = 'tech'

    # news
    guardian_news = guardian(data)
    guardian_news.url = 'https://www.theguardian.com/'
    guardian_news.section = 'news'
    guardian_news.scan_limit = 25

    guardian_politics.scrape()
    guardian_us.scrape()
    guardian_business.scrape()
    guardian_science.scrape()
    guardian_tech.scrape()
    guardian_env.scrape()
    guardian_news.scrape()

    filepath = 'guardian/guardian-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

guardian_run()
