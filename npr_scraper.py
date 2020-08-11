
import json
import datetime
from scraper import *

# class scraper:
#
#     def __init__(self):
#         self.section = 'n/a'
#         self.url = 'n/a'
#         self.article_heading_id = 'title'
#         self.article_element = 'h2'
#         self.content_id = 'storytext'
#         self.content_element = 'div'
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
#         coverpage_news = soup.find_all(self.article_element, class_=self.article_heading_id)
#
#         number_of_articles = len(coverpage_news)
#
#         #base_url = 'https://www.npr.org'
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
#             #link = base_url + link
#
#             print(self.section+': '+title)
#
#             # read content
#             article = requests.get(link)
#             article_content = article.content
#             soup_article = BeautifulSoup(article_content, 'html5lib')
#             body = soup_article.find_all(self.content_element, class_=self.content_id)
#             x = body[0].find_all('p')
#
#             # unify the paragraph
#             list_paragraphs = []
#             for p in np.arange(0, len(x)):
#                 paragraph = x[p].get_text()
#                 " ".join(paragraph.split())
#                 paragraph = paragraph.strip('\n')
#                 paragraph = paragraph.strip('\t')
#                 paragraph = paragraph.replace('\n', '')
#                 paragraph = paragraph.replace('\t', '')
#                 paragraph = re.sub(' +',' ', paragraph)
#                 list_paragraphs.append(paragraph)
#                 final_article = " ".join(list_paragraphs)
#
#             num_keys = len(data['articles'])
#
#             data['articles'].append({
#                 'id': 'npr' + str(num_keys-1),
#                 'publisher': 'npr',
#                 'label': 'left-center',
#                 'title': title,
#                 'section': self.section,
#                 'link': link,
#                 'date': date,
#                 'body': final_article
#             })
#
#         return temp_dict

def npr_run():

    data = {}
    data['articles'] = []

    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # election
    npr_election = npr(data)
    npr_election.url = 'https://www.npr.org/sections/elections/'
    npr_election.section = 'election'

    # national
    npr_national = npr(data)
    npr_national.url = 'https://www.npr.org/sections/national/'
    npr_national.section = 'us'

    # politics
    npr_politics = npr(data)
    npr_politics.url = 'https://www.npr.org/sections/politics/'
    npr_politics.section = 'politics'

    # health
    npr_health = npr(data)
    npr_health.url = 'https://www.npr.org/sections/health/'
    npr_health.section = 'health'

    # business
    npr_business = npr(data)
    npr_business.url = 'https://www.npr.org/sections/business/'
    npr_business.section = 'business'

    # tech
    npr_tech = npr(data)
    npr_tech.url = 'https://www.npr.org/sections/technology/'
    npr_tech.section = 'tech'

    # science
    npr_science = npr(data)
    npr_science.url = 'https://www.npr.org/sections/science/'
    npr_science.section = 'science'

    npr_election.scrape()
    npr_national.scrape()
    npr_politics.scrape()
    npr_health.scrape()
    npr_business.scrape()
    npr_tech.scrape()
    npr_science.scrape()

    filepath = 'npr/npr-'+date+'.json'
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

npr_run()