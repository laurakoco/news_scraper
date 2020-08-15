
import json
import datetime
from scraper import *

def marketwatch_run():

    # date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

    data = {}
    data['articles'] = []

    # politics
    marketwatch_politics = marketwatch(data)
    marketwatch_politics.url = 'https://www.marketwatch.com/economy-politics?mod=side_nav'
    marketwatch_politics.section = 'politics'

    # election
    marketwatch_election = marketwatch(data)
    marketwatch_election.url = 'https://www.marketwatch.com/economy-politics/election-2020?mod=side_nav'
    marketwatch_election.section = 'politics'

    marketwatch_politics.scrape()
    marketwatch_election.scrape()

    filepath = 'marketwatch/marketwatch-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

marketwatch_run()
