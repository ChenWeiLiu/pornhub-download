import urllib2
import requests
from requests.exceptions import RequestException
import json
from json import JSONDecoder
from bs4 import BeautifulSoup
import re

headers = {
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'

}

urls = []

def get_page_index():
    url = 'https://www.pornhub.com/playlist/20033522'
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print('index failed')
        return None


def parse_page_index(html):
    soup = BeautifulSoup(html,'html.parser')
    for a in soup.select('.videos .img'):
        if len(a.select('.img')):
            print(a.select('.img')[0]['href'])
            urls.append(a.select('.img')[0]['href'])
    return urls

def main_a():
    html = get_page_index()
    parse_page_index(html)


if __name__ == '__main__':
    main_a()


