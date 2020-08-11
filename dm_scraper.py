
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
#         number_of_articles = len(coverpage_news)
#
#         base_url = 'https://www.dailymail.co.uk'
#
#         id = 0
#
#         temp_dict = {}
#         temp_dict['article'] = []
#
#         for n in np.arange(0, number_of_articles):
#
#             if id == 20:
#                 break
#
#             # get title
#             title = coverpage_news[n].find('a').get_text().strip()
#
#             # get link of article
#             link = coverpage_news[n].find('a')['href']
#             if self.section == 'business' or self.section == 'science-tech':
#                 link = base_url + link
#
#             print(title)
#
#             # read content (it is divided in paragraphs)
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all('p', class_='mol-para-with-font')
#             #x = body[0].find_all('p')
#
#             # Unifying the paragraphs
#             list_paragraphs = []
#             for p in np.arange(0, len(body)):
#                 paragraph = body[p].get_text()
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             # news_contents.append(final_article)
#
#             temp_dict['article'].append({
#                 'id': 'dailymail' + str(id),
#                 'publisher': 'dailymail',
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

def dm_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # us 2020 election
    dm_election = dm(data)
    dm_election.url = 'https://www.dailymail.co.uk/news/2020-election/index.html'
    dm_election.section = 'election'

    # business
    dm_business = dm(data)
    dm_business.url = 'https://www.dailymail.co.uk/money/markets/index.html'
    dm_business.section = 'business'
    dm_business.base_url_required = True

    # science-tech
    dm_science = dm(data)
    dm_science.url = 'https://www.dailymail.co.uk/sciencetech/index.html'
    dm_science.section = 'science-tech'
    dm_science.base_url_required = True

    # home
    # dm_home = scraper()
    # dm_home.url = 'https://www.dailymail.co.uk/ushome/index.html'
    # dm_home.article_heading_id = 'linkro-darkred'
    # dm_home.content_id = 'articleBody'

    dm_election.scrape()
    dm_business.scrape()
    dm_science.scrape()

    filepath = 'dm/dm-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

dm_run()