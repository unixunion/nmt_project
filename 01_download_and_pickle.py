import sys
from lxml import html

from data import get_and_cache_page, urls, get_next_link


def spider(start_url):
    page = get_and_cache_page(start_url)
    sys.stdout.flush()
    next_url = get_next_link(page)
    if next_url:
        spider(next_url)
    else:
        print("\nspidering complete for url: {}".format(start_url))


if __name__ == "__main__":
    for url in urls:
        print("starting spider for url: {}".format(url))
        spider(url)
