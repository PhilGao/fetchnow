from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

pages = set()
baseUrl = 'https://en.wikipedia.org'


def getLink(urlPath):
    try:
        response = urlopen(baseUrl + urlPath)
    except (HTTPError, URLError) as e:
        return None
    bsobject = BeautifulSoup(response, "lxml")
    for link in bsobject.find_all('a', href=re.compile('^(/wiki/)*(?!Wikipedia).*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getLink(newpage)


getLink("/wiki/wow")

print("********************************")
print(pages)
