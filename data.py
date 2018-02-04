import hashlib

import pickle
import re

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
        'http://nfs.sparknotes.com/winterstale/page_2.html',
        'http://nfs.sparknotes.com/sonnets/sonnet_1.html')


def get_next_link(data):
    try:
        tree = html.fromstring(data)
        link = tree.xpath('//a[@class="right arrow-nav next text-color tooltip-link"]')[0]
        return link.attrib['href']
    except IndexError as e:
        return None


def encode(myd):
    return "{}{}".format(myd, "\n")


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
    str = str.replace(",", " , ")
    str = str.replace(".", " . ")
    str = str.replace('"', ' ')
    str = str.replace("'", ' ')
    str = re.sub(' +', ' ', str)
    return str.strip()


def match(d1, d2):
    d1_vocab = {}
    d2_vocab = {}
    total_vocab = []
    common_vocab = []
    uncommon_vocab = []

    d1_tokens = re.split(" ", d1)
    d2_tokens = re.split(" ", d2)

    # o = len(d1_tokens)-len(d2_tokens)
    # if o < -20:
    #     print("{}:{}-{} '{}'\n vs '{}'".format(o, len(d1), len(d2), d1, d2))

    for w in d1_tokens:
        d1_vocab[w] = w
        if not w in total_vocab:
            total_vocab.append(w)
    for w in d2_tokens:
        d2_vocab[w] = w
        if not w in total_vocab:
            total_vocab.append(w)

    for w in d1_vocab:
        if w in d2_vocab:
            common_vocab.append(w)
        else:
            uncommon_vocab.append(w)


    for w in d2_vocab:
        if w in d1_vocab:
            if not w in common_vocab:
                common_vocab.append(w)
        else:
            uncommon_vocab.append(w)

    if len(common_vocab) > 0:
        return len(common_vocab)/len(total_vocab)
    else:
        return 0


def clean_and_split(data):
    s = clean(data)
    lines = re.split("\.\s", s)
    response = ""
    count = 0
    for line in lines:
        if count == 0:
            response = line
        else:
            response = response + "\n" + line
        count += 1
    return count, response


def super_clean(data):
    result = "{} ".format(data)
    result = result.replace('\xa0', ' ')
    result = result.replace('\u2003', ' ')
    result = re.sub('\[.*\]', ' ', result)
    result = re.sub('\(.*\)', ' ', result)
    result = re.sub('"', ' ', result)
    result = re.sub("\.", " . ", result)
    result = re.sub("\n", " ", result)
    result = re.sub("\r", " ", result)
    result = re.sub(",", " , ", result)
    result = re.sub("\?", " ", result)
    result = re.sub(";", " ", result)
    result = re.sub(":", " ", result)
    result = re.sub("!", " ", result)
    result = re.sub(":", " ", result)
    result = re.sub("-", " ", result)
    result = re.sub("—", " ", result)
    result = re.sub('”', " ", result)
    result = re.sub('“', " ", result)
    result = re.sub('"', ' ', result)
    result = re.sub("'", ' ', result)
    result = re.sub(' +', ' ', result)
    return result.lower()


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
    def build(data_dict: dict):
        return Utterance(data_dict['speaker'], data_dict['shakespeare'], data_dict['modern'], data_dict['url'])
