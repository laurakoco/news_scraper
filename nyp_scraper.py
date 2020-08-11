
import json
import datetime
from scraper import *

# class scraper:
#
#     def __init__(self):
#         self.section = 'n/a'
#         self.url = 'n/a'
#         self.article_heading_id = 'entry-heading'
#         self.content_id = 'entry-content entry-content-read-more'
#
#     def scrape(self):
#
#         date = datetime.datetime.now().strftime("%Y-%m-%d")
#
#         r1 = requests.get(self.url)
#
#         coverpage = r1.content
#
#         soup = BeautifulSoup(coverpage, 'html5lib')
#
#         coverpage_news = soup.find_all('h3', class_=self.article_heading_id)
#
#         number_of_articles = len(coverpage_news)
#
#         #base_url = 'https://nypost.com/'
#
#         id = 0
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             # get title
#             title = coverpage_news[n].find('a').get_text()
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             #link = base_url + link
#
#             print(title)
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
#                 'id': 'nyp' + str(id),
#                 'publisher': 'new york post',
#                 'label': 'right-center',
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
#
# ##

def nyp_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # business
    nyp_business = nyp(data)
    nyp_business.url = 'https://nypost.com/business/'
    nyp_business.section = 'business'

    # news
    # nyp_news = scraper(data)
    # nyp_news.url = 'https://nypost.com/news/'
    # nyp_news.section = 'news'

    # metro
    nyp_metro = nyp(data)
    nyp_metro.url = 'https://nypost.com/metro/'
    nyp_metro.section = 'metro'

    # tech
    nyp_tech = nyp(data)
    nyp_tech.url = 'https://nypost.com/tech/'
    nyp_tech.section = 'tech'

    nyp_business.scrape()
    # nyp_news.scrape()
    nyp_metro.scrape()
    nyp_tech.scrape()

    filepath = 'nyp/nyp-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nyp_run()