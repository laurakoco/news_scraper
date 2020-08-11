
import numpy as np
import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

delay = 5 # wait 5 seconds between scraping articles

date = datetime.datetime.now().strftime("%Y-%m-%d")

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

            # get link of article
            link = coverpage_news[n].find('a')['href']

            if self.base_url_required == True:
                link = self.base_url + link

            print(self.section+': '+title)

            # read content
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')

            if self.publisher == 'dm':
                body = soup_article.find_all(self.content_element, itemprop=self.content_id)
            else:
                body = soup_article.find_all(self.content_element, class_= self.content_id)
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

class ap(scraper):

  def __init__(self,data):

        super(ap, self).__init__()

        self.data = data

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

        super(ap, self).__init__()

        self.data = data

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

        super(ap, self).__init__()

        self.data = data

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

        super(ap, self).__init__()

        self.data = data

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

        super(ap, self).__init__()

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

# cnn
class cnn(scraper):

    def __init__(self,data):

        super(cnn, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

        self.publisher = 'cnn'
        self.label = 'left'
        self.base_url_required = True
        self.base_url = 'https://www.cnn.com'

        self.title_element = 'a'
        self.article_heading_id = 'cd__headline'
        self.article_element = 'h3'
        self.content_id = 'l-container'
        self.content_element = 'div'

        self.url = 'n/a'
        self.section = 'n/a'

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

class dm(scraper): # dailymail

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

class vox(scraper): # vox

    def __init__(self,data):

        super(vox, self).__init__()

        self.data = data

        self.limit_scans = True
        self.scan_limit = 10

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
        # self.scan_limit = 10

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




