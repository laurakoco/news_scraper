

import json
import datetime

import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 2 # wait 5 seconds between scraping articles

date = datetime.datetime.now().strftime("%Y-%m-%d")

class scraper:

    def __init__(self):

        self.limit_scans = False
        self.scan_limit = 0

    def format_paragraph(self,paragraph):

        " ".join(paragraph.split())
        paragraph = paragraph.strip('\n')
        paragraph = paragraph.strip('\t')
        paragraph = paragraph.replace('\n', '')
        paragraph = paragraph.replace('\t', '')
        paragraph = re.sub(' +',' ', paragraph)

        return paragraph

    def scrape(self):

        r1 = requests.get(self.url)
        coverpage = r1.content

        soup = BeautifulSoup(coverpage, 'html5lib')

        coverpage_news = soup.find_all(self.article_element, class_=self.article_heading_id)

        if self.section == 'election': # remove weird non-articles
            coverpage_news = coverpage_news[2:-1]

        number_of_articles = len(coverpage_news)

        for n in np.arange(0, number_of_articles):

            if self.limit_scans == True:
                if n == self.scan_limit:
                    break

            # get title
            title = coverpage_news[n].find(self.title_element).get_text().strip()

            # get link of article
            link = coverpage_news[n].find('a')['href']

            if self.base_url_required == True:
                link = self.base_url + link

            print(self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            body = soup_article.find_all(self.content_element, class_= self.content_id)
            x = body[0].find_all('p')

            # unify paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(x)):
                paragraph = x[p].get_text()
                paragraph = self.format_paragraph(paragraph)
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)

            num_keys = len(self.data['articles'])

            self.data['articles'].append({
                'id': self.publisher + str(num_keys),
                'publisher': self.publisher,
                'label': self.label,
                'title': title,
                'link': link,
                'section': self.section,
                'date': date,
                'body': final_article
            })

            time.sleep(delay)

        return self.data

# politico
class politico(scraper):

    def __init__(self,data):

        super(politico, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'politico'
        self.label = 'center'
        self.base_url_required = False
        self.base_url = 'https://www.politico.com/'

        self.title_element = 'a'
        self.article_heading_id = ''
        self.article_element = 'h1'
        self.content_id = 'story-text'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

def politico_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # election
    politico_election = politico(data)
    politico_election.url = 'https://www.politico.com/news/2020-elections'
    politico_election.section = 'election'

    # tech
    politico_tech = politico(data)
    politico_tech.url = 'https://www.politico.com/technology'
    politico_tech.section = 'tech'
    politico_tech.article_heading_id = ''
    politico_tech.article_element = 'h3'
    politico_tech.limit_scans = True
    politico_tech.scan_limit = 8

    # health
    politico_health = politico(data)
    politico_health.url = 'https://www.politico.com/ehealth'
    politico_health.section = 'health'
    politico_health.article_heading_id = ''
    politico_health.article_element = 'h3'
    politico_health.limit_scans = True
    politico_health.scan_limit = 3

    # business
    politico_business = politico(data)
    politico_business.url = 'https://www.politico.com/financeh'
    politico_business.section = 'business'
    politico_business.article_heading_id = ''
    politico_business.article_element = 'h3'
    politico_business.limit_scans = True
    politico_business.scan_limit = 8

    # enviornment
    politico_env = politico(data)
    politico_env.url = 'https://www.politico.com/financeh'
    politico_env.section = 'enviornment'
    politico_env.article_heading_id = ''
    politico_env.article_element = 'h3'
    politico_env.limit_scans = True
    politico_env.scan_limit = 8

    politico_election.scrape()
    politico_tech.scrape()
    politico_health.scrape()
    politico_business.scrape()
    politico_env.scrape()


    filepath = 'politico/politico-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

politico_run()
