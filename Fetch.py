import requests
import chardet
from requests import exceptions

# fetch homepage , get all the movies title /actor/rank/type/link , note the insert date time
# fetch the next pages , same as it

baseUrl = "http://www.dytt8.net/html/gndy/dyzz/index.html"
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


def get_movies(url):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = get_encoding(response)
        # print(response.encoding)
        print(response.text)
    except (exceptions.RequestException) as e:
        response.close()

        print(e)
    else:
        response.close()

    return None


def insert_data():
    return None


get_movies(baseUrl)
