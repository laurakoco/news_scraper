
import json
import datetime
from scraper import *

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
#         coverpage_news = soup.find_all('h2', class_=self.article_heading_id)
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
#         base_url = 'https://www.nytimes.com'
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
#             if title == 'Here\'s What Extreme Heat Looks Like: Profoundly Unequal':
#                 continue
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             link = base_url + link
#
#             print(self.section + ': ' + title)
#
#             # read content (it is divided in paragraphs)
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all('p', class_= self.content_id)
#
#             a = body[0]
#             x = len(body)
#             # x = body[0].find_all('p')
#
#             # unify paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, x):
#                 paragraph = body[p].get_text()
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             # news_contents.append(final_article)
#
#             temp_dict['article'].append({
#                 'id': 'nyt' + str(id),
#                 'publisher': 'new york times',
#                 'label': 'left-center',
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

def nyt_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    #             if self.section == 'business' or self.section == 'science-tech':
    #                 link = base_url + link


    # us
    nyt_us = nyt(data)
    nyt_us.url = 'https://www.nytimes.com/section/us'
    nyt_us.article_heading_id = 'css-1hdf4fa eb5pyrn3'
    nyt_us.section = 'us'

    # politics
    nyt_politics = nyt(data)
    nyt_politics.url = 'https://www.nytimes.com/section/politics'
    nyt_politics.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_politics.section = 'politics'

    # # climate
    # nyt_climate = scraper()
    # nyt_climate.url = 'https://www.nytimes.com/section/climate'
    # nyt_climate.article_heading_id = 'css-l2vidh e4e4i5l1'
    # nyt_climate.section = 'climate'

    # 2020 election
    nyt_election = nyt(data)
    nyt_election.url = 'https://www.nytimes.com/section/technology'
    nyt_election.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_election.section = 'election'

    # tech
    nyt_tech = nyt(data)
    nyt_tech.url = 'https://www.nytimes.com/section/technology'
    nyt_tech.article_heading_id = 'css-1hdf4fa e1xdw5352'
    nyt_tech.section = 'tech'
    nyt_us.base_url_required = True

    # business
    nyt_business = nyt(data)
    nyt_business.url = 'https://www.nytimes.com/section/business'
    nyt_business.article_heading_id = 'css-l2vidh e4e4i5l1'
    nyt_business.section = 'business'
    nyt_us.base_url_required = True

    # science
    nyt_science = nyt(data)
    nyt_science.url = 'https://www.nytimes.com/section/science'
    nyt_science.article_heading_id = 'css-1hdf4fa e1xdw5352'
    nyt_science.section = 'science'

    # health
    nyt_health = nyt(data)
    nyt_health.url = 'https://www.nytimes.com/section/health'
    nyt_health.article_heading_id = 'css-1j0585e e1xdw5352'
    nyt_health.section = 'health'

    nyt_us.scrape()
    nyt_politics.scrape()
    # nyt_election.scrape()
    # nyt_business.scrape()
    # nyt_tech.scrape()
    # nyt_science.scrape()
    # nyt_health.scrape()

    filepath = 'nyt/nyt-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

nyt_run()
