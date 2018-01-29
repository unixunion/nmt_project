import pickle
from lxml import html, etree

from data import clean, urls, get_and_cache_page, get_next_link

from multiprocessing import Pool

def process(data, url=None):
    tree = html.fromstring(data)

    utterances = tree.xpath('//div[@id="noFear-comparison"]/table[@class="noFear"]/tr')

    for e in utterances:
        # for original lines
        speaker = e.xpath('td[@class="noFear-left"]/b/text()')

        if speaker:

            print("Speaker: {}".format(speaker))

            original_line = ""
            # for element in e.xpath('td[@class="noFear-left"]/div[@class="original-line"]/text()'):
            for element in e.xpath('td[@class="noFear-left"]/div[@class="original-line"]'):
                etree.strip_tags(element, 'a')
                original_line = original_line + ' ' + element.text_content()

            original_line = clean(original_line)
            print("Shakespeare: {}".format(original_line))

            modern_line = ""
            for element in e.xpath('td[@class="noFear-right"]/div[@class="modern-line"]'):
                etree.strip_elements(element, 'span', with_tail=False)
                etree.strip_tags(element, 'a')
                modern_line = modern_line + ' ' + element.text_content()

            modern_line = clean(modern_line)
            print("Modern: {}".format(modern_line))

            with open('utterances.pickle', 'a+b') as f:
                pickle.dump({"speaker": speaker, "shakespeare": original_line, "modern": modern_line, "url": url}, f)


def spider(start_url):
    if start_url:
        print("url: {}".format(start_url))
        page = get_and_cache_page(start_url)
        process(page, url=start_url)
        next_url = get_next_link(page)
        spider(next_url)


if __name__ == "__main__":

    pool = Pool(processes=8)
    r = pool.map_async(spider, urls)
    r.wait()
