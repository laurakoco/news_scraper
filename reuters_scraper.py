
import json
import datetime
from scraper import *

# class scraper:
#
#     def __init__(self):
#         self.section = 'n/a'
#         self.url = 'n/a'
#         self.article_heading_id = 'story-content'
#         self.content_id = 'StandardArticleBody_body'
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
#         coverpage_news = soup.find_all('div', class_=self.article_heading_id)
#
#         # a = coverpage_news[0].get_text()
#         # b = coverpage_news[0]
#
#         # scraping the first 2 articles
#         number_of_articles = len(coverpage_news)
#
#         # empty lists for content, links and titles
#         # news_contents = []
#         # list_links = []
#         # list_titles = []
#
#         base_url = 'https://www.reuters.com/article'
#
#         id = 0
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             # get title
#             title = coverpage_news[n].find('h3').get_text().strip()
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             link = base_url + link
#
#             print(self.section+': '+title)
#
#             # read content (it is divided in paragraphs)
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all('div', class_= self.content_id)
#             x = body[0].find_all('p')
#
#             # unify paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, len(x)):
#                 paragraph = x[p].get_text()
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             # news_contents.append(final_article)
#
#             temp_dict['article'].append({
#                 'id': 'reuters' + str(id),
#                 'publisher': 'reuters',
#                 'label': 'center',
#                 'title': title,
#                 'link': link,
#                 'section': self.section,
#                 'date': date,
#                 'body': final_article
#             })
#
#             id = id + 1
#
#         return temp_dict

def reuters_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # politics
    reuters_politics = reuters(data)
    reuters_politics.url = 'https://www.reuters.com/politics'
    reuters_politics.section = 'politics'

    # business
    reuters_business = reuters(data)
    reuters_business.url = 'https://www.reuters.com/finance'
    reuters_business.section = 'business'

    # us news
    reuters_us = reuters(data)
    reuters_us.url = 'https://www.reuters.com/news/us'
    reuters_us.section = 'us'

    # tech
    reuters_tech = reuters(data)
    reuters_tech.url = 'https://www.reuters.com/news/technology'
    reuters_tech.section = 'tech'

    reuters_politics.scrape()
    reuters_business.scrape()
    reuters_us.scrape()
    reuters_tech.scrape()

    filepath = 'reuters/reuters-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

reuters_run()