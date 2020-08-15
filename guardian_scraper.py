

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

def guardian_run():

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    data = {}
    data['articles'] = []

    # politics
    guardian_politics = guardian(data)
    guardian_politics.url = 'https://www.theguardian.com/us-news/us-politics'
    guardian_politics.section = 'politics'

    # us
    guardian_us = guardian(data)
    guardian_us.url = 'https://www.theguardian.com/us-news'
    guardian_us.section = 'us'

    # business
    guardian_business = guardian(data)
    guardian_business.url = 'https://www.theguardian.com/us/business'
    guardian_business.section = 'business'

    # science
    guardian_science = guardian(data)
    guardian_science.url = 'https://www.theguardian.com/science'
    guardian_science.section = 'science'

    # tech
    guardian_tech = guardian(data)
    guardian_tech.url = 'https://www.theguardian.com/us/technology'
    guardian_tech.section = 'tech'

    # envionrment
    guardian_env = guardian(data)
    guardian_env.url = 'https://www.theguardian.com/us/environment'
    guardian_env.section = 'tech'

    guardian_politics.scrape()
    # guardian_us.scrape()
    # guardian_business.scrape()
    # guardian_science.scrape()
    # guardian_tech.scrape()
    # guardian_env.scrape()

    filepath = 'guardian/guardian-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

guardian_run()
