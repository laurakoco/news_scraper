
import json
import datetime
from scraper import *

def vox_run():

    print('vox')

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

    # politics
    vox_politics = vox(data)
    vox_politics.url = 'https://www.vox.com/policy-and-politics'
    vox_politics.section = 'politics'

    # science-health
    vox_science = vox(data)
    vox_science.url = 'https://www.vox.com/science-and-health'
    vox_science.section = 'science-health'

    # business
    vox_business = vox(data)
    vox_business.url = 'https://www.vox.com/business-and-finance'
    vox_business.section = 'business'

    # technology
    vox_tech = vox(data)
    vox_tech.url = 'https://www.vox.com/technology'
    vox_tech.section = 'tech'

    # enviornment
    vox_env = vox(data)
    vox_env.url = 'https://www.vox.com/energy-and-environment'
    vox_env.section = 'enviornment'

    # enviornment
    vox_news = vox(data)
    vox_news.url = 'https://www.vox.com'
    vox_news.section = 'news'

    vox_politics.scrape()
    vox_science.scrape()
    vox_business.scrape()
    vox_tech.scrape()
    vox_env.scrape()
    vox_news.scrape()

    filepath = 'vox/vox-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

vox_run()
