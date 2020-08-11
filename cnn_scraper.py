
# import requests
# from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd

import json
import datetime
from scraper import *
#
# class scraper:
#
#     def __init__(self):
#         self.section = 'n/a'
#         self.url = 'n/a'
#         self.article_heading_id = 'n/a'
#         self.content_id = 'n/a'
#
#     def scrape(self):
#
#         date = datetime.datetime.now().strftime("%Y-%m-%d")
#
#         r1 = requests.get(self.url)
#         coverpage = r1.content
#
#         soup = BeautifulSoup(coverpage, 'html5lib')
#
#         coverpage_news = soup.find_all('h3', class_=self.article_heading_id)
#
#         number_of_articles = len(coverpage_news)
#
#         # empty lists for content, links and titles
#         # news_contents = []
#         # list_links = []
#         # list_titles = []
#
#         base_url = 'https://www.cnn.com'
#
#         id = 0
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             if id == 10: # don't scrape more than 10
#                 break
#
#             # get title
#             title = coverpage_news[n].find('a').get_text()
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             link = base_url + link
#
#             print(title)
#
#             # read content (it is divided in paragraphs)
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all('div', class_= self.content_id)
#             #x = body[0].find_all('div')
#
#             # unify paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, len(body)):
#                 paragraph = body[p].get_text()
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             # news_contents.append(final_article)
#
#             temp_dict['article'].append({
#                 'id': 'cnn' + str(id),
#                 'publisher': 'cnn',
#                 'label': 'left',
#                 'title': title,
#                 'section': self.section,
#                 'link': link,
#                 'date': date,
#                 'body': final_article
#             })
#
#             id = id + 1
#
#         return temp_dict

##

def cnn_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

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

    # # tech
    # cnn_tech = cnn(data)
    # cnn_tech.url = 'https://www.cnn.com/business/tech'
    # cnn_tech.section = 'business'

    cnn_us.scrape()
    # cnn_politics.scrape() politics won't scrape -- ??
    cnn_health.scrape()
    cnn_business.scrape()

    filepath = 'cnn/cnn-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

cnn_run()
