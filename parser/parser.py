import requests
from bs4 import BeautifulSoup

URL = 'https://riac34.ru/news/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
           'accept': '*/*'}
HOST = 'https://riac34.ru'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-xl-8 col-lg-8 col-md-8 col-sm-12')

    articles = []
    for item in items:
        link_to_text = HOST + item.find('a', class_='caption').get('href')

        article_html = get_html(link_to_text).text
        soup_text = BeautifulSoup(article_html, 'html.parser')
        text = soup_text.find('div', class_='full-text').get_text()

        articles.append({
            'title': item.find('a', class_='caption').get_text(),
            'link': HOST + item.find('a', class_='caption').get('href'),
            'date': item.find('div', class_='new-attr').find('span', class_='date').get_text(),
            'desc': item.find('div', class_='desc').get_text(strip=True),
            'tag': item.find('div', class_='new-attr').find('a', class_='cat').get_text(),
            'text': text
        })
    return articles


def parse(pages_count):
    html = get_html(URL)
    news = []
    if html.status_code == 200:
        for page in range(1, pages_count + 1):
            print(f'Парсим страницу {page} из {pages_count}...')
            html = get_html(URL, params={'PAGEN_1': page})
            news.extend(get_content(html.text))
        print(f'Получено {len(news)} новостей')
    else:
        print('ERROR!')
    return news


