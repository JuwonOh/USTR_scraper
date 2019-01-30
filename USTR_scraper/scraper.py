import re
import time
from .utils import get_soup

def get_latest_allnews(last_date, sleep=1.0):
    """
    Artuments
    ---------
    last_date : Date
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns = [re.compile('https://www.state.gov/[\w]+')]
base_url = 'https://ustr.gov/about-us/policy-offices/press-office/press-releases/{}'

def get_allnews_urls(begin_year=2018, end_year=2019, verbose=True):
    """
    Arguments
    ---------
    begin_year : int
        Default is 2018
    end_year : int
        Default is 2019
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for year in (begin_year, end_year):
        url = base_url.format(year)
        soup = get_soup(url)
        sub_links = soup.find('ul', class_= 'listing')
        for link in sub_links.find_all("a"):
            if 'href' in link.attrs:
                 links_all += [link.attrs['href']]
        if verbose:
            print('get briefing statement urls {} / {}'.format(begin_year, end_year))

    links_all = ['https://ustr.gov' + i for i in links_all]

    return links_all
