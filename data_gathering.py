from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os
from tqdm import tqdm
import wget

def findImages(webPage : str) -> list:
    """
    This function takes a webpage as an input and returns all the links present on that page into a list
    :param webPage:
    :return: a list of all the link texts
    """
    req = Request(webPage)
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    return links

def main():
    WEBPAGE = "http://jsoc.stanford.edu/data/aia/images/2021/12/25/131/"
    OUTURL = 'data/input'
    IMAGE_EXTENSION = '.jp2'
    #Saving all the link texts into one list
    links = findImages(WEBPAGE)
    #Filtering all the texts which do not comtain the suffix .jp2
    images = []
    for link in links:
        if link.endswith(IMAGE_EXTENSION):
            images.append(link)
    #Creating folders for image downloading
    if not os.path.exists(OUTURL):
        os.makedirs(OUTURL)
    #Downloading first 100 images into a folder
    for img in tqdm(images[0:100]):
        imgURL = WEBPAGE + img
        destination = os.getcwd() + '/' + OUTURL
        wget.download(imgURL, out=destination)

if __name__ == "__main__":
    main()

