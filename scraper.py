
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 0 # wait 5 seconds between scraping articles

# date = datetime.datetime.now().strftime("%Y-%m-%d")
date = datetime.datetime.now().strftime("%Y-%m-%d-%I%p")

class scraper:

    def __init__(self):

        self.limit_scans = False
        self.scan_limit = 0

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
            title = self.format_paragraph(title)

            # get link of article
            link = coverpage_news[n].find('a')['href']

            if self.base_url_required == True:
                link = self.base_url + link

            if self.publisher == 'nymag': # remove // from beginning of link
                link = link[2:-1]
                link = 'http://' + link

            print(str(n) + ' ' + self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            # weird unique things
            if self.publisher == 'dm':
                body = soup_article.find_all(self.content_element, itemprop=self.content_id)

            if self.publisher == 'nymag':
                if 'article-content inset' in soup_article:
                    self.content_id = 'article-content inset'
                if 'article-content inline' in soup_article:
                    self.content_id = 'article-content inline'

            else:
                body = soup_article.find_all(self.content_element, class_= self.content_id)
            if len(body) == 0:
                continue

            if self.publisher == 'refinery29':
                x = body
            else:
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

## child class

# associated press
class ap(scraper):

  def __init__(self,data):

        super(ap, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 15

        self.publisher = 'ap'
        self.label = 'center'
        self.base_url_required = True
        self.base_url = 'https://apnews.com'
        self.article_element = 'div'
        self.content_id = 'Article'
        self.content_element = 'div'
        self.title_element = 'h1'

        self.url = 'n/a'
        self.section = 'n/a'
        self.article_heading_id = 'n/a'

# npr
class npr(scraper):

    def __init__(self,data):

        super(npr, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 15

        self.publisher = 'npr'
        self.label = 'left-center'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'title'
        self.article_element = 'h2'
        self.content_id = 'storytext'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# fox news
class fox(scraper):

    def __init__(self,data):

        super(fox, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 15

        self.publisher = 'fox'
        self.label = 'right'
        self.base_url_required = True
        self.base_url = 'https://www.foxnews.com'

        self.title_element = 'a'
        self.article_heading_id = 'title'
        self.article_element = 'h2'
        self.content_id = 'article-body'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# reuters
class reuters(scraper):

    def __init__(self,data):

        super(reuters, self).__init__()

        self.data = data

        self.limit_scans = False
        self.scan_limit = 15

        self.publisher = 'reuters'
        self.label = 'center'
        self.base_url_required = True
        self.base_url = 'https://www.reuters.com/article'

        self.title_element = 'h3'
        self.article_heading_id = 'story-content'
        self.article_element = 'div'
        self.content_id = 'StandardArticleBody_body'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# new york post
class nyp(scraper):

    def __init__(self,data):

        super(nyp, self).__init__()

        self.data = data

        self.publisher = 'nyp'
        self.label = 'right-center'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'entry-heading'
        self.article_element = 'h3'
        self.content_id = 'entry-content entry-content-read-more'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# new york times
class nyt(scraper):

    def __init__(self,data):

        super(nyt, self).__init__()

        self.data = data

        self.publisher = 'nyt'
        self.label = 'left-center'
        self.base_url_required = True
        self.base_url = 'https://www.nytimes.com'

        self.title_element = 'a'
        self.article_heading_id = 'n/a'
        self.article_element = 'h2'
        # self.content_id = 'css-158dogj evys1bk0'
        self.content_id = 'css-53u6y8'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# dailymail
class dm(scraper):

    def __init__(self,data):

        super(dm, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'dm'
        self.label = 'right'
        self.base_url_required = False
        self.base_url = 'https://www.dailymail.co.uk'

        self.title_element = 'a'
        self.article_heading_id = 'linkro-darkred'
        self.article_element = 'h2'
        self.content_id = 'articleBody'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# vox
class vox(scraper):

    def __init__(self,data):

        super(vox, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 15

        self.publisher = 'vox'
        self.label = 'left'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'c-entry-box--compact__title' # 'c-entry-box-base__headline'
        self.article_element = 'h2' # h3
        self.content_id = 'c-entry-content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# boston herald
class bh(scraper): # news week

    def __init__(self,data):

        super(bh, self).__init__()

        self.data = data

        # self.limit_scans = True
        # self.scan_limit = 20

        self.publisher = 'bh'
        self.label = 'right-center'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'entry-title'
        self.article_element = 'h4'
        self.content_id = 'body-copy'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'


# christian post
class cp(scraper):

    def __init__(self,data):

        super(cp, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'cp'
        self.label = 'right'
        self.base_url_required = True
        self.base_url = 'https://www.christianpost.com'

        self.title_element = 'a'
        self.article_heading_id = 'h2'
        self.article_element = 'h3'
        self.content_id = 'full-article'
        self.content_element = 'article'

        self.url = 'n/a'
        self.section = 'n/a'

# washington post
class washpost(scraper):

    def __init__(self,data):

        super(washpost, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 5

        self.publisher = 'washpost'
        self.label = 'left-center'
        self.base_url_required = False
        self.base_url = 'https://www.washingtonpost.com'

        self.title_element = 'a'
        self.article_heading_id = ''
        self.article_element = 'h2'
        self.content_id = 'remainder-content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# guardian
class guardian(scraper):

    def __init__(self,data):

        super(guardian, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'guardian'
        self.label = 'left'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'fc-item__title'
        self.article_element = 'h3'
        self.content_id = 'content__article-body from-content-api js-article__body'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# # intercept
# class intercept(scraper):
#
#     def __init__(self,data):
#
#         super(intercept, self).__init__()
#
#         self.data = data
#
#         self.limit_scans = True
#         self.scan_limit = 10
#
#         self.publisher = 'intercept'
#         self.label = 'left-center'
#         self.base_url_required = False
#         self.base_url = 'n/a'
#
#         self.title_element = 'a'
#         self.article_heading_id = 'fc-item__title'
#         self.article_element = 'h3'
#         self.content_id = 'content__article-body from-content-api js-article__body'
#         self.content_element = 'div'
#
#         self.url = 'n/a'
#         self.section = 'n/a'

# msnbc
class msnbc(scraper):

    def __init__(self,data):

        super(msnbc, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'msnbc'
        self.label = 'left'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'span'
        self.article_heading_id = 'tease-card__headline tease-card__title relative'
        self.article_element = 'h2'
        self.content_id = 'article-body__content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# marketwatch
class marketwatch(scraper):

    def __init__(self,data):

        super(marketwatch, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'marketwatch'
        self.label = 'right-center'
        self.base_url_required = False
        self.base_url = 'n/a'

        self.title_element = 'a'
        self.article_heading_id = 'article__headline'
        self.article_element = 'h3'
        self.content_id = 'column column--full article__content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# daily caller
class dc(scraper):

    def __init__(self, data):
        super(dc, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'dc'
        self.label = 'right'
        self.base_url_required = True
        self.base_url = 'https://dailycaller.com'

        self.title_element = 'a'
        self.article_heading_id = 'text-black mb-4 leading-tight text-2xl'
        self.article_element = 'h2'
        self.content_id = 'article-content mb-2 pb-2 tracking-tight'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'


# ohio star
class ohio(scraper):

    def __init__(self, data):
        super(ohio, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'ohio'
        self.label = 'right'
        self.base_url_required = False
        self.base_url = 'https://theohiostar.com'

        self.title_element = 'a'
        self.article_heading_id = 'entry-title'
        self.article_element = 'h2'
        self.content_id = 'entry-content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# chicago tribune
class chicago(scraper):

    def __init__(self, data):
        super(chicago, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'chicago'
        self.label = 'right-center'
        self.base_url_required = True
        self.base_url = 'https://www.chicagotribune.com'

        self.title_element = 'a'
        self.article_heading_id = 'r-mb h5-mb h5'
        self.article_element = 'h2'
        self.content_id = 'clln clln-crd oflw cs__ctn__border-bottom'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# people
class people(scraper):

    def __init__(self, data):
        super(people, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'people'
        self.label = 'left'
        self.base_url_required = False
        self.base_url = ''

        self.title_element = 'h3'
        self.article_heading_id = 'category-page-item-content'
        self.article_element = 'div'
        self.content_id = 'paragraph'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

# tennessee
class tennessee(scraper):

    def __init__(self, data):
        super(tennessee, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'tennessee'
        self.label = 'right'
        self.base_url_required = False
        self.base_url = ''

        self.title_element = 'a'
        self.article_heading_id = 'entry-title'
        self.article_element = 'h2'
        self.content_id = 'entry-content'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'
