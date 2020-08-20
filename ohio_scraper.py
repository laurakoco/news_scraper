
import json
import datetime
from scraper import *

def ohio_run():

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    ohio_us = ohio(data)
    ohio_us.url = 'https://theohiostar.com/category/news/national/'
    ohio_us.section = 'us'

    # news
    ohio_news = ohio(data)
    ohio_news.url = 'https://theohiostar.com/category/news/'
    ohio_news.section = 'news'

    # politics
    ohio_politics = ohio(data)
    ohio_politics.url = 'https://theohiostar.com/category/politics/'
    ohio_politics.section = 'politics'

    ohio_us.scrape()
    ohio_news.scrape()
    ohio_politics.scrape()

    filepath = 'ohio/ohio-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

ohio_run()