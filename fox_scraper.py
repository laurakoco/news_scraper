
import json
import datetime
from scraper import *

# class scraper:
#
#     def __init__(self):
#         self.section = 'n/a'
#         self.url = 'n/a'
#         self.article_heading_id = 'title'
#         self.content_id = 'article-body'
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
#         coverpage_news = soup.find_all('h2', class_=self.article_heading_id)
#
#         number_of_articles = len(coverpage_news)
#
#         base_url = 'https://www.foxnews.com'
#
#         id = 0
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             # get title
#             title = coverpage_news[n].find('a').get_text().strip()
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
#             body = soup_article.find_all('div', class_=self.content_id)
#             x = body[0].find_all('p')
#
#             # Unifying the paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, len(x)):
#                 paragraph = x[p].get_text()
#                 paragraph = paragraph.strip('\n')
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             # news_contents.append(final_article)
#
#             temp_dict['article'].append({
#                 'id': 'fox' + str(id),
#                 'publisher': 'fox',
#                 'label': 'right',
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

def fox_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us
    fox_us = fox(data)
    fox_us.url = 'https://www.foxnews.com/us'
    fox_us.section = 'us'

    # politics
    fox_politics = fox(data)
    fox_politics.url = 'https://www.foxnews.com/politics'
    fox_politics.section = 'politics'

    # business
    # fox_business = scraper(data)
    # fox_business.url = 'https://www.foxbusiness.com/'
    # fox_business.article_heading_id = 'title'
    # fox_business.content_id = 'article-body'

    fox_health = fox(data)
    fox_health.url = 'https://www.foxnews.com/health'
    fox_health.section = 'health'

    # science
    fox_science = fox(data)
    fox_science.url = 'https://www.foxnews.com/science'
    fox_science.section = 'science'

    # tech
    fox_tech = fox(data)
    fox_tech.url = 'https://www.foxnews.com/tech'
    fox_tech.section = 'tech'

    fox_us.scrape()
    fox_politics.scrape()
    fox_health.scrape()
    fox_science.scrape()
    fox_tech.scrape()

    filepath = 'fox/fox-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

fox_run()