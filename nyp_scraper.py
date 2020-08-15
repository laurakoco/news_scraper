
import json
import datetime
from scraper import *

def nyp_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # business
    nyp_business = nyp(data)
    nyp_business.url = 'https://nypost.com/business/'
    nyp_business.section = 'business'

    # news
    # nyp_news = scraper(data)
    # nyp_news.url = 'https://nypost.com/news/'
    # nyp_news.section = 'news'

    # metro
    nyp_metro = nyp(data)
    nyp_metro.url = 'https://nypost.com/metro/'
    nyp_metro.section = 'metro'

    # tech
    nyp_tech = nyp(data)
    nyp_tech.url = 'https://nypost.com/tech/'
    nyp_tech.section = 'tech'

    nyp_business.scrape()
    # nyp_news.scrape()
    nyp_metro.scrape()
    nyp_tech.scrape()

    filepath = 'nyp/nyp-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nyp_run()