import requests
from bs4 import BeautifulSoup

def get_links():
    url = 'http://stackoverflow.com/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a',{'class': 'question-hyperlink'}):
        href = 'http://stackoverflow.com' + link.get('href')
        title = link.string
        print(href)
        print(title)

get_links();