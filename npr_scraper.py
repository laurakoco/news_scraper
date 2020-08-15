
import json
import datetime
from scraper import *



def npr_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # election
    npr_election = npr(data)
    npr_election.url = 'https://www.npr.org/sections/elections/'
    npr_election.section = 'election'

    # national
    npr_national = npr(data)
    npr_national.url = 'https://www.npr.org/sections/national/'
    npr_national.section = 'us'

    # politics
    npr_politics = npr(data)
    npr_politics.url = 'https://www.npr.org/sections/politics/'
    npr_politics.section = 'politics'
    npr_politics.scan_limit = 10

    # health
    npr_health = npr(data)
    npr_health.url = 'https://www.npr.org/sections/health/'
    npr_health.section = 'health'

    # business
    npr_business = npr(data)
    npr_business.url = 'https://www.npr.org/sections/business/'
    npr_business.section = 'business'

    # tech
    npr_tech = npr(data)
    npr_tech.url = 'https://www.npr.org/sections/technology/'
    npr_tech.section = 'tech'

    # science
    npr_science = npr(data)
    npr_science.url = 'https://www.npr.org/sections/science/'
    npr_science.section = 'science'

    # npr_election.scrape()
    npr_national.scrape()
    npr_politics.scrape()
    npr_health.scrape()
    npr_business.scrape()
    npr_tech.scrape()
    npr_science.scrape()

    filepath = 'npr/npr-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

npr_run()