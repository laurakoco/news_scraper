
# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd

import json
import datetime
from scraper import *

def cnn_run():

    data = {}
    data['articles'] = []

    #date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    cnn_us = cnn(data)
    cnn_us.url = 'https://www.cnn.com/us'
    cnn_us.section = 'us'

    # politics
    cnn_politics = cnn(data)
    cnn_politics.url = 'https://www.cnn.com/politics'
    cnn_politics.section = 'politics'

    # health
    cnn_health = cnn(data)
    cnn_health.url = 'https://www.cnn.com/health'
    cnn_health.section = 'health'

    # business
    cnn_business = cnn(data)
    cnn_business.url = ' https://www.cnn.com/business'
    cnn_business.section = 'business'
    cnn_business.limit_scans = True
    cnn_business.scan_limit = 5

    # # tech
    # cnn_tech = cnn(data)
    # cnn_tech.url = 'https://www.cnn.com/business/tech'
    # cnn_tech.section = 'business'

    cnn_us.scrape()
    # cnn_politics.scrape() politics won't scrape -- ??
    cnn_health.scrape()
    cnn_business.scrape()

    filepath = 'cnn/cnn-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

cnn_run()
