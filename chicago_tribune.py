
# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd

import json
import datetime
from scraper import *

def chicago_run():

    print('chicago tribune')

    data = {}
    data['articles'] = []

    #date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    chicago_politics = chicago(data)
    chicago_politics.url = 'https://www.chicagotribune.com/politics/'
    chicago_politics.section = 'politics'

    # news
    chicago_news = chicago(data)
    chicago_news.url = 'https://www.chicagotribune.com/news/'
    chicago_news.section = 'news'

    # health
    chicago_health = chicago(data)
    chicago_health.url = 'https://www.chicagotribune.com/lifestyles/health/'
    chicago_health.section = 'health'

    # election
    chicago_election = chicago(data)
    chicago_election.url = 'https://www.chicagotribune.com/politics/elections/'
    chicago_election.section = 'election'

    # env
    chicago_env = chicago(data)
    chicago_env.url = 'https://www.chicagotribune.com/news/environment/'
    chicago_env.section = 'enviornment'

    # business
    chicago_business = chicago(data)
    chicago_business.url = 'https://www.chicagotribune.com/business/'
    chicago_business.section = 'business'

    chicago_politics.scrape()
    chicago_news.scrape()
    chicago_health.scrape()
    chicago_election.scrape()
    chicago_env.scrape()
    chicago_business.scrape()

    filepath = 'chicago/chicago-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

chicago_run()
