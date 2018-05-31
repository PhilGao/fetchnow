import requests
import chardet
from requests import exceptions
from bs4 import BeautifulSoup
import time

# fetch homepage , get all the movies title /actor/rank/type/link , note the insert date time
# fetch the next pages , same as it

baseUrl = "http://www.dytt8.net/html/gndy/dyzz/"
headers = {
    'user-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}


def get_encoding(response):
    '''
    get encoding from response header ,content & detect the encoding , by using requests default function & property.

    :param response: response from https requests
    :return:encoding str
    '''
    encoding = requests.utils.get_encoding_from_headers(response.headers)
    if encoding == 'ISO-8859-1':
        encoding = requests.utils.get_encodings_from_content(response.text)
        if encoding == 'ISO-8859-1':
            encoding = response.apparent_encoding
    return "".join(encoding)


def get_raw_movie_data(url, rawdata):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = get_encoding(response)
        # print(response.encoding)
        # print(response.text)
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        results = soup.find('div', {"class": "co_content8"}).findNext('ul').findAllNext('table')
        for table in results:
            # print(table.findAll('tr'))
            row = table.findAll('tr')[-1].td.contents
            rawData.append(row)
        # get next link
        next_pageTag = soup.find('a', text="下一页")
        if next_pageTag:
            next_pagelink = next_pageTag.attrs['href']
        else:
            return rawData
        while next_pagelink:
            url = baseUrl + next_pagelink
            print(url)
            get_raw_movie_data(url, rawData)
            time.sleep(1)


    except (exceptions.RequestException) as e:
        response.close()
        print(e)

    return rawData


def parse_raw_data(list):
    return None


def insert_data():
    return None


rawData = []
indexUrl = baseUrl + 'index.html'
get_raw_movie_data(indexUrl, rawData)
print(rawData)
