

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
#         self.article_element = 'div'
#         self.content_id = 'Article'
#         self.content_element = 'div'
#         self.title_element = 'h1'
#
#     def scrape(self):
#
#         r1 = requests.get(self.url)
#         coverpage = r1.content
#
#         soup = BeautifulSoup(coverpage, 'html5lib')
#
#         coverpage_news = soup.find_all(self.article_element, class_=self.article_heading_id)
#
#         number_of_articles = len(coverpage_news)
#
#         base_url = 'https://apnews.com'
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             # get title
#             title = coverpage_news[n].find(self.title_element).get_text().strip()
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             link = base_url + link
#
#             print(self.section+': '+title)
#
#             # read content
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all(self.content_element, class_= self.content_id)
#             x = body[0].find_all('p')
#
#             # unify paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, len(x)):
#                 paragraph = x[p].get_text()
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             num_keys = len(data['articles'])
#             id = 'ap' + str(num_keys)
#
#             data.append({
#                 #'id': 'ap' + str(num_keys),
#                 'publisher': 'ap',
#                 'label': 'center',
#                 'title': title,
#                 'link': link,
#                 'section': self.section,
#                 'date': date,
#                 'body': final_article
#             })

def ap_run():

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # business
    ap_business = ap(data)
    ap_business.url = 'https://apnews.com/apf-business'
    ap_business.section = 'business'
    ap_business.article_heading_id = 'CardHeadline headline-0-2-106'

    # us news
    ap_us = ap(data)
    ap_us.url = 'https://apnews.com/apf-usnews'
    ap_us.section = 'us'
    ap_us.article_heading_id = 'CardHeadline headline-0-2-101'

    # tech
    ap_tech = ap(data)
    ap_tech.url = 'https://apnews.com/apf-technology'
    ap_tech.section = 'tech'
    ap_tech.article_heading_id = 'CardHeadline headline-0-2-106'

    # science
    ap_science = ap(data)
    ap_science.url = 'https://apnews.com/apf-science'
    ap_science.section = 'science'
    ap_science.article_heading_id = 'CardHeadline headline-0-2-101'

    # health
    ap_health = ap(data)
    ap_health.url = 'https://apnews.com/apf-science'
    ap_health.section = 'health'
    ap_health.article_heading_id = 'CardHeadline headline-0-2-101'

    data = ap_business.scrape()
    # data = ap_us.scrape()
    # data = ap_tech.scrape()
    # data = ap_science.scrape()
    # data = ap_health.scrape()

    filepath = 'ap/ap-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

ap_run()
