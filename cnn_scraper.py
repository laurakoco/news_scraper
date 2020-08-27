
# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd

import json
import datetime
from scraper import *

class cnn_scraper:

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
            link = coverpage_news[n].find('a')['href']

            if self.base_url_required == True:
                link = self.base_url + link

            print(self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            body = soup_article.find_all(self.content_element, class_= 'zn-body__paragraph')

            if len(body) == 0:
                continue

            # x = body[0].find_all('div')

            # unify paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(body)):
                paragraph = body[p].get_text()
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


# cnn
class cnn(cnn_scraper):

    def __init__(self,data):

        super(cnn, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'cnn'
        self.label = 'left'
        self.base_url_required = True
        self.base_url = 'https://www.cnn.com'

        self.title_element = 'a'
        self.article_heading_id = 'cd__headline'
        self.article_element = 'h3'
        self.content_id = 'l-container'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'


def cnn_run():

    print('cnn')

    data = {}
    data['articles'] = []

    #date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    cnn_us = cnn(data)
    cnn_us.url = 'https://www.cnn.com/us'
    cnn_us.section = 'us'

    # politics
    cnn_politics = cnn(data)
    cnn_politics.url = 'https://www.cnn.com/politics'
    cnn_politics.section = 'politics'

    # health
    cnn_health = cnn(data)
    cnn_health.url = 'https://www.cnn.com/health'
    cnn_health.section = 'health'

    # business
    cnn_business = cnn(data)
    cnn_business.url = ' https://www.cnn.com/business'
    cnn_business.section = 'business'
    cnn_business.limit_scans = True
    cnn_business.scan_limit = 5

    # tech
    cnn_tech = cnn(data)
    cnn_tech.url = 'https://www.cnn.com/business/tech'
    cnn_tech.section = 'business'
    cnn_tech.scan_limit = 5

    # news
    cnn_news = cnn(data)
    cnn_news.url = 'https://www.cnn.com/'
    cnn_news.section = 'news'
    cnn_news.scan_limit = 5

    cnn_us.scrape()
    #cnn_health.scrape()
    #cnn_business.scrape()
    cnn_tech.scrape()
    cnn_news.scrape()

    filepath = 'cnn/cnn-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

cnn_run()
