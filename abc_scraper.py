
import json
import datetime
from scraper import *

import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 2 # wait 5 seconds between scraping articles

date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

class abc_scraper:

    def __init__(self):

        self.limit_scans = False
        self.scan_limit = 0
        self.link_element = 'a'

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
            #link = coverpage_news[n]['href']

            if self.section == 'news':
                link = coverpage_news[n].find('a')['href']
            else:
                link = coverpage_news[n]['href']

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

# abc
class abc(abc_scraper):

    def __init__(self,data):

        super(abc, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'bbc'
        self.label = 'left-center'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'div'
        self.article_heading_id = 'AnchorLink News__Item external flex flex-row'
        self.article_element = 'a'
        self.content_id = 'Article__Column Article__Column--main'
        self.content_element = 'section'

        self.url = 'n/a'
        self.section = 'n/a'

def abc_run():

    print('abc')

    data = {}
    data['articles'] = []

    #date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    abc_politics = abc(data)
    abc_politics.url = 'https://abcnews.go.com/Politics'
    abc_politics.section = 'politics'
    abc_politics.article_heading_id = 'AnchorLink News__Item external flex flex-row'
    abc_politics.article_element = 'a'
    abc_politics.content_id = 'Article__Column Article__Column--main'
    abc_politics.content_element = 'section'

    # tech - hard
    # abc_tech = abc(data)
    # abc_tech.url = 'https://abcnews.go.com/Technology'
    # abc_tech.section = 'tech'
    # abc_tech.article_heading_id = 'AnchorLink'
    # abc_tech.article_element = 'a'
    # abc_tech.title_element = 'a'
    # abc_tech.content_id = 'Article__Content story'
    # abc_tech.content_element = 'article'

    # health
    abc_health = abc(data)
    abc_health.url = 'https://abcnews.go.com/Health'
    abc_health.section = 'health'
    abc_health.article_heading_id = 'AnchorLink News__Item external flex flex-row'
    abc_health.article_element = 'a'
    abc_health.content_id = 'Article__Column Article__Column--main'
    abc_health.content_element = 'section'

    # business
    abc_business = abc(data)
    abc_business.url = 'https://abcnews.go.com/Business'
    abc_business.section = 'business'
    abc_business.article_heading_id = 'AnchorLink News__Item external flex flex-row'
    abc_business.article_element = 'a'
    abc_business.content_id = 'Article__Column Article__Column--main'
    abc_business.content_element = 'section'

    # us
    abc_us = abc(data)
    abc_us.url = 'https://abcnews.go.com/US'
    abc_us.section = 'us'
    abc_us.article_heading_id = 'AnchorLink News__Item external flex flex-row'
    abc_us.article_element = 'a'
    abc_us.content_id = 'Article__Column Article__Column--main'
    abc_us.content_element = 'section'

    # new
    abc_news = abc(data)
    abc_news.url = 'https://abcnews.go.com/'
    abc_news.section = 'news'
    abc_news.article_heading_id = 'headlines-li-div'
    abc_news.article_element = 'div'
    abc_news.title_element = 'a'
    abc_news.content_id = 'Article__Column Article__Column--main'
    abc_news.content_element = 'section'

    abc_politics.scrape()
    abc_health.scrape()
    abc_business.scrape()
    abc_us.scrape()
    abc_news.scrape()

    filepath = 'abc/abc-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

abc_run()
