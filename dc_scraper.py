
import json
import datetime
from scraper import *

def dc_run():

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    dc_us = dc(data)
    dc_us.url = 'https://dailycaller.com/section/us/'
    dc_us.section = 'us'

    # politics
    dc_politics = dc(data)
    dc_politics.url = 'https://dailycaller.com/section/politics/'
    dc_politics.section = 'politics'
    dc_politics.scan_limit = 4

    # business
    dc_business = dc(data)
    dc_business.url = 'https://dailycaller.com/section/business/'
    dc_business.section = 'business'

    # news
    dc_news = dc(data)
    dc_news.url = 'https://dailycaller.com/section/business/'
    dc_news.section = 'news'
    dc_news.title_element = 'a'
    dc_news.article_heading_id = 'font-ruda font-black text-base mb-1'
    dc_news.article_element = 'div'

    dc_us.scrape()
    dc_politics.scrape()
    dc_business.scrape()
    dc_news.scrape()

    filepath = 'dc/dc-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

dc_run()