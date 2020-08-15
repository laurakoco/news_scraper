
import json
import datetime
from scraper import *

def fox_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    fox_us = fox(data)
    fox_us.url = 'https://www.foxnews.com/us'
    fox_us.section = 'us'
    fox_us.base_url_required = False

    # politics
    fox_politics = fox(data)
    fox_politics.url = 'https://www.foxnews.com/politics'
    fox_politics.section = 'politics'

    # business
    # fox_business = scraper(data)
    # fox_business.url = 'https://www.foxbusiness.com/'
    # fox_business.article_heading_id = 'title'
    # fox_business.content_id = 'article-body'

    fox_health = fox(data)
    fox_health.url = 'https://www.foxnews.com/health'
    fox_health.section = 'health'

    # science
    fox_science = fox(data)
    fox_science.url = 'https://www.foxnews.com/science'
    fox_science.section = 'science'

    # tech
    fox_tech = fox(data)
    fox_tech.url = 'https://www.foxnews.com/tech'
    fox_tech.section = 'tech'

    # fox_us.scrape()
    fox_politics.scrape()
    fox_health.scrape()
    fox_science.scrape()
    fox_tech.scrape()

    filepath = 'fox/fox-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

fox_run()