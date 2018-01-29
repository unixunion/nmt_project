import hashlib

import pickle
import re

import sys
from lxml import html

import requests

test_urls = ('http://nfs.sparknotes.com/antony-and-cleopatra/page_2.html',
        'http://nfs.sparknotes.com/asyoulikeit/page_2.html',
        'http://nfs.sparknotes.com/coriolanus/page_2.html')

urls = ('http://nfs.sparknotes.com/antony-and-cleopatra/page_2.html',
        'http://nfs.sparknotes.com/asyoulikeit/page_2.html',
        'http://nfs.sparknotes.com/coriolanus/page_2.html',
        'http://nfs.sparknotes.com/errors/page_2.html',
        'http://nfs.sparknotes.com/hamlet/page_2.html',
        'http://nfs.sparknotes.com/henry4pt1/page_3.html',
        'http://nfs.sparknotes.com/henry4pt2/page_269.html',
        'http://nfs.sparknotes.com/henryv/page_2.html',
        'http://nfs.sparknotes.com/juliuscaesar/page_2.html',
        'http://nfs.sparknotes.com/lear/page_2.html',
        'http://nfs.sparknotes.com/macbeth/page_2.html',
        'http://nfs.sparknotes.com/measure-for-measure/page_2.html',
        'http://nfs.sparknotes.com/merchant/page_2.html',
        'http://nfs.sparknotes.com/msnd/page_2.html',
        'http://nfs.sparknotes.com/muchado/page_2.html',
        'http://nfs.sparknotes.com/othello/page_2.html',
        'http://nfs.sparknotes.com/richardii/page_2.html',
        'http://nfs.sparknotes.com/richardiii/page_2.html',
        'http://nfs.sparknotes.com/romeojuliet/page_2.html',
        'http://nfs.sparknotes.com/shrew/page_2.html',
        'http://nfs.sparknotes.com/tempest/page_2.html',
        'http://nfs.sparknotes.com/twelfthnight/page_2.html',
        'http://nfs.sparknotes.com/twogentlemen/page_2.html',
        'http://nfs.sparknotes.com/winterstale/page_2.html')


def get_next_link(data):
    try:
        tree = html.fromstring(data)
        link = tree.xpath('//a[@class="right arrow-nav next text-color tooltip-link"]')[0]
        return link.attrib['href']
    except IndexError as e:
        return None



def encode(data):
    return "{}{}".format(data, "\n")


def get_and_cache_page(myurl):
    url_hash = hashlib.sha224(myurl.encode("utf-8")).hexdigest()

    try:
        with open("cache.pickle", 'rb') as f:
            while True:
                try:
                    cached_object = pickle.load(f)
                    if url_hash == cached_object['hash']:
                        # print("returning cached url: {}".format(myurl))
                        # sys.stdout.write('.')
                        return cached_object['page']
                except EOFError as e:
                    break
    except FileNotFoundError as b:
        print("no file: cache.pickle, creating it", b)
        pass

    # print("downloading: {}".format(myurl))
    # sys.stdout.write(':')
    page = requests.get(myurl)

    f = open('cache.pickle', 'a+b')
    pickle.dump({'hash': url_hash, 'page': page.content}, f)
    return page.content


def clean(data):
    str = "{}".format(data)
    str = str.replace('\t', ' ')
    str = str.replace('\n', ' ')
    str = str.replace('\r', ' ')
    str = re.sub(' +', ' ', str)
    return str


class Utterance:
    speaker = None
    shakespeare = None
    modern = None
    url = None

    def __init__(self, speaker, shakespeare, modern, url):
        self.speaker = speaker
        self.shakespeare = shakespeare
        self.modern = modern
        self.url = url

    def __repr__(self):
        return {"speaker": self.speaker, "shakespeare": self.shakespeare, "modern": self.modern, "url": self.url}

    def __str__(self):
        return str(self.__repr__())

    @staticmethod
    def build(data_dict : dict):
        return Utterance(data_dict['speaker'], data_dict['shakespeare'], data_dict['modern'], data_dict['url'])

