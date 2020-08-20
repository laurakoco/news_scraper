
import json
import datetime
from scraper import *

def people_run():

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # news
    people_news = people(data)
    people_news.url = 'https://people.com/tag/news/'
    people_news.section = 'news'

    # politics
    people_politics = people(data)
    people_politics.url = 'https://people.com/politics/'
    people_politics.section = 'politics'

    # health
    people_health = people(data)
    people_health.url = 'https://people.com/health/'
    people_health.section = 'health'

    # tech
    people_tech = people(data)
    people_tech.url = 'https://people.com/tech/'
    people_tech.section = 'tech'

    people_news.scrape()
    people_politics.scrape()
    people_health.scrape()
    people_tech.scrape()

    filepath = 'people/people-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

people_run()