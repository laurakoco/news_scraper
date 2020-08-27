
import json
import datetime
from scraper import *

import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 0 # wait 5 seconds between scraping articles

# date = datetime.datetime.now().strftime("%Y-%m-%d")
date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

class usatoday_scraper:

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

        number_of_articles = len(coverpage_news)

        for n in np.arange(0, number_of_articles):

            if self.limit_scans == True:
                if n == self.scan_limit:
                    break

            # get title
            #title = coverpage_news[n].find(self.title_element).get_text().strip()

            a = coverpage_news[n].attrs
            if 'data-c-br' in a:
                title = coverpage_news[n]['data-c-br']
                title = self.format_paragraph(title)
            else:
                continue

            # get link of article
            link = coverpage_news[n]['href']

            if 'newsletter' in link:
                continue

            if self.base_url_required == True:
                link = self.base_url + link

            print(str(n) + ' ' + self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            body = soup_article.find_all(self.content_element, class_= self.content_id)

            if len(body) == 0:
                continue

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

## child class


# usa today
class usatoday(usatoday_scraper):

    def __init__(self, data):
        super(usatoday, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 15

        self.publisher = 'usatoday'
        self.label = 'left-center'
        self.base_url_required = True
        self.base_url = 'https://www.usatoday.com'

        self.title_element = 'a'
        self.article_heading_id = 'gnt_m_flm_a'
        self.article_element = 'a'
        self.content_id = 'gnt_ar_b'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

def usatoday_run():

    print('usa today')

    data = {}
    data['articles'] = []

    # news
    usatoday_news = usatoday(data)
    usatoday_news.url = 'https://www.usatoday.com/news/'
    usatoday_news.section = 'news'

    # tech
    usatoday_tech = usatoday(data)
    usatoday_tech.url = 'https://www.usatoday.com/tech/'
    usatoday_tech.section = 'tech'

    # health
    usatoday_health = usatoday(data)
    usatoday_health.url = 'https://www.usatoday.com/news/health/'
    usatoday_health.section = 'health'

    # business
    usatoday_business = usatoday(data)
    usatoday_business.url = 'https://www.usatoday.com/money/'
    usatoday_business.section = 'business'

    # politics
    usatoday_politics = usatoday(data)
    usatoday_politics.url = 'https://www.usatoday.com/news/politics/'
    usatoday_politics.section = 'politics'
    usatoday_politics.base_url_required = True

    # election
    usatoday_election = usatoday(data)
    usatoday_election.url = 'https://www.usatoday.com/elections/'
    usatoday_election.section = 'election'

    # us
    usatoday_us = usatoday(data)
    usatoday_us.url = 'https://www.usatoday.com/news/nation/'
    usatoday_us.section = 'us'

    usatoday_news.scrape()
    usatoday_tech.scrape()
    usatoday_health.scrape()
    usatoday_business.scrape()
    usatoday_politics.scrape()
    usatoday_election.scrape()
    usatoday_us.scrape()

    filepath = 'usatoday/usatoday-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

usatoday_run()
