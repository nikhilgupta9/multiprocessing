from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def main():
    req = Request("http://jsoc.stanford.edu/data/aia/images/2021/12/25/131/")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    print(links)

if __name__ == "__main__":
    main()
