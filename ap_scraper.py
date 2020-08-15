

import json
import datetime
from scraper import *

def ap_run():

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # business
    ap_business = ap(data)
    ap_business.url = 'https://apnews.com/apf-business'
    ap_business.section = 'business'
    ap_business.article_heading_id = 'CardHeadline headline-0-2-106'

    # us news
    ap_us = ap(data)
    ap_us.url = 'https://apnews.com/apf-usnews'
    ap_us.section = 'us'
    ap_us.article_heading_id = 'CardHeadline headline-0-2-101'

    # tech
    ap_tech = ap(data)
    ap_tech.url = 'https://apnews.com/apf-technology'
    ap_tech.section = 'tech'
    ap_tech.article_heading_id = 'CardHeadline headline-0-2-106'

    # science
    ap_science = ap(data)
    ap_science.url = 'https://apnews.com/apf-science'
    ap_science.section = 'science'
    ap_science.article_heading_id = 'CardHeadline headline-0-2-101'

    # health
    ap_health = ap(data)
    ap_health.url = 'https://apnews.com/apf-science'
    ap_health.section = 'health'
    ap_health.article_heading_id = 'CardHeadline headline-0-2-101'

    ap_business.scrape()
    ap_us.scrape()
    ap_tech.scrape()
    ap_science.scrape()
    ap_health.scrape()

    filepath = 'ap/ap-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

ap_run()
