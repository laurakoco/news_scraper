

import json
import datetime
from scraper import *

def nymag_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    nymag_politics = nymag(data)
    nymag_politics.url = 'https://nymag.com/intelligencer/politics/'
    nymag_politics.section = 'politics'

    # business
    nymag_business = nymag(data)
    nymag_business.url = 'https://nymag.com/intelligencer/business/'
    nymag_business.section = 'business'

    # tech
    nymag_tech = nymag(data)
    nymag_tech.url = 'https://nymag.com/intelligencer/tech/'
    nymag_tech.section = 'tech'

    nymag_politics.scrape()
    nymag_business.scrape()
    nymag_tech.scrape()

    filepath = 'nymag/nymag-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nymag_run()
