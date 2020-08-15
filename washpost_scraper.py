
import json
import datetime
from scraper import *

def washpost_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    washpost_politics = washpost(data)
    washpost_politics.url = 'https://www.washingtonpost.com/politics/?itid=nb_hp_politics'
    washpost_politics.section = 'politics'
    washpost_politics.article_heading_id = ''
    washpost_politics.article_element = 'h2'

    # business
    washpost_business = washpost(data)
    washpost_business.url = 'https://www.washingtonpost.com/business/?itid=nb_front_business'
    washpost_business.section = 'business'
    washpost_business.article_heading_id = 'headline xx-small normal-style text-align-inherit'
    washpost_business.article_element = 'h2'

    # election
    washpost_election = washpost(data)
    washpost_election.url = 'https://www.washingtonpost.com/elections/?tid=nb_elections&itid=nb_elections'
    washpost_election.section = 'election'
    washpost_election.article_heading_id = 'headline x-small normal-style text-align-inherit'
    washpost_election.article_element = 'div'

    # tech
    washpost_tech = washpost(data)
    washpost_tech.url = 'https://www.washingtonpost.com/business/technology/?itid=nb_front_technology'
    washpost_tech.section = 'tech'
    washpost_tech.article_heading_id = ''
    washpost_tech.article_element = 'h2'

    # science
    washpost_science = washpost(data)
    washpost_science.url = 'https://www.washingtonpost.com/business/technology/?itid=nb_front_technology'
    washpost_science.section = 'science'
    washpost_science.article_heading_id = ''
    washpost_science.article_element = 'h2'

    # health
    washpost_health = washpost(data)
    washpost_health.url = 'https://www.washingtonpost.com/health/?itid=nb_front_health'
    washpost_health.section = 'health'
    washpost_health.article_heading_id = ''
    washpost_health.article_element = 'h2'

    # climate and enviornment
    washpost_env = washpost(data)
    washpost_env.url = 'https://www.washingtonpost.com/climate-environment/?itid=nb_front_climate-environment'
    washpost_env.section = 'enviornment'
    washpost_env.article_heading_id = ''
    washpost_env.article_element = 'h2'

    washpost_politics.scrape()
    washpost_business.scrape()

    # washpost_election.scrape()

    washpost_tech.scrape()
    washpost_science.scrape()

    #washpost_health.scrape()

    # washpost_env.scrape()

    filepath = 'washpost/washpost-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

washpost_run()
