from bs4 import BeautifulSoup
import requests


def get_soup(url):
    """
    Get a BeautifulSoup object back from the a URL

    :param url: URL to scrape
    :return:
    """

    r = requests.get(url)

    if r.status_code == 404:
        return None

    data = r.text
    return BeautifulSoup(data, "lxml")

