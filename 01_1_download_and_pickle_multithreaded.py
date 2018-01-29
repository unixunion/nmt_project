from multiprocessing import Pool
import os

from data import get_and_cache_page, urls, get_next_link


def spider(start_url):
    print("{} spider: {}".format(os.getpid(), start_url))
    page = get_and_cache_page(start_url)
    next_url = get_next_link(page)
    if next_url:
        spider(next_url)
    else:
        print("{}: spidering complete for url: {}".format(os.getpid(), start_url))


if __name__ == "__main__":
    pool = Pool(processes=8)
    r = pool.map_async(spider, urls)
    r.wait()
