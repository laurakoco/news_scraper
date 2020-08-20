
import json

import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 2 # wait 5 seconds between scraping articles

# date = datetime.datetime.now().strftime("%Y-%m-%d")
date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

class nymag_scraper:

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
            title = self.format_paragraph(title)

            # get link of article
            link = coverpage_news[n].find('a')['href']

            if self.base_url_required == True:
                link = self.base_url + link

            if self.publisher == 'nymag': # remove // from beginning of link
                link = link[2:-1]
                link = 'http://' + link

            print(self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            if 'article-content inset' in soup_article:
                self.content_id = 'article-content inset'
            if 'article-content inline' in soup_article:
                self.content_id = 'article-content inline'

            else:
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


# ny mag
class nymag(nymag_scraper):

    def __init__(self,data):

        super(nymag, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 20

        self.publisher = 'nymag'
        self.label = 'left'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'span'
        self.article_heading_id = 'main-article-content'
        self.article_element = 'div'
        self.content_id = 'article-content inset'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

def nymag_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    nymag_politics = nymag(data)
    nymag_politics.url = 'https://nymag.com/intelligencer/politics/'
    nymag_politics.section = 'politics'

    # business
    nymag_business = nymag(data)
    nymag_business.url = 'https://nymag.com/intelligencer/business/'
    nymag_business.section = 'business'

    # tech
    nymag_tech = nymag(data)
    nymag_tech.url = 'https://nymag.com/intelligencer/tech/'
    nymag_tech.section = 'tech'

    nymag_politics.scrape()
    nymag_business.scrape()
    nymag_tech.scrape()

    filepath = 'nymag/nymag-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nymag_run()
