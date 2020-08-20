
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

date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

class sun_scraper:

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
            title = coverpage_news[n].find(self.title_element).get_text().strip()

            # get link of article
            link = coverpage_news[n]['href']

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

class sun(sun_scraper):

    def __init__(self,data):

        super(sun, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'sun'
        self.label = 'right'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'h2'
        self.article_heading_id = 'text-anchor-wrap'
        self.article_element = 'a'
        self.content_id = 'article__content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

def sun_run():

    print('the sun')

    data = {}
    data['articles'] = []

    # date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    sun_us = sun(data)
    sun_us.url = 'https://www.the-sun.com/news/us-news/'
    sun_us.section = 'us'

    # health
    sun_health = sun(data)
    sun_health.url = 'https://www.the-sun.com/lifestyle/health/'
    sun_health.section = 'health'

    # tech
    sun_tech = sun(data)
    sun_tech.url = 'https://www.the-sun.com/lifestyle/tech/'
    sun_tech.section = 'tech'

    # news
    sun_news = sun(data)
    sun_news.url = 'https://www.the-sun.com/news/'
    sun_news.section = 'news'

    sun_us.scrape()
    sun_health.scrape()
    sun_tech.scrape()
    sun_news.scrape()

    filepath = 'sun/sun-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

sun_run()
