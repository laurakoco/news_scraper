
import json
import datetime
from scraper import *


import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 2 # wait 5 seconds between scraping articles

date = datetime.datetime.now().strftime("%Y-%m-%d")

def msnbc_run():

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # us
    msnbc_us = msnbc(data)
    msnbc_us.url = 'https://www.nbcnews.com/us-news'
    msnbc_us.section = 'us'

    # politics
    msnbc_politics = msnbc(data)
    msnbc_politics.url = 'https://www.nbcnews.com/politics'
    msnbc_politics.section = 'politics'

    # business
    msnbc_business = msnbc(data)
    msnbc_business.url = 'https://www.nbcnews.com/business'
    msnbc_business.section = 'business'

    # science
    msnbc_science = msnbc(data)
    msnbc_science.url = 'https://www.nbcnews.com/science'
    msnbc_science.section = 'science'

    # tech
    msnbc_tech = msnbc(data)
    msnbc_tech.url = 'https://www.nbcnews.com/tech-media'
    msnbc_tech.section = 'tech'

    # health
    msnbc_health = msnbc(data)
    msnbc_health.url = 'https://www.nbcnews.com/health'
    msnbc_health.section = 'health'

    msnbc_us.scrape()
    msnbc_politics.scrape()
    msnbc_business.scrape()
    msnbc_science.scrape()
    msnbc_tech.scrape()
    msnbc_health.scrape()

    filepath = 'msnbc/msnbc-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

msnbc_run()
