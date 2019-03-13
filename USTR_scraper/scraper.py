import re
import time
from dateutil.parser import parse
from .parser import parse_page
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


def yield_latest_allnews(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = parse(begin_date)
    end_page = 72
    n_news = 0
    outdate = False

    for year in (2019, 2018):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all= []
        url = base_url.format(year)
        soup = get_soup(url)
        sub_links = soup.find('ul', class_= 'listing')
        for link in sub_links.find_all("a"):
            if 'href' in link.attrs:
                 links_all += ['https://ustr.gov' + link.attrs['href']]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = news_json['time']
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)
