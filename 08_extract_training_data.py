import pickle
import re

from data import encode, clean_and_split, match
from data import clean

import random

en_text = []
sh_text = []

count = 0
test = 0
dev = 0



def split_and_write(file1, data1, file2, data2):
    with open(file1, "at") as f1:
        with open(file2, "at") as f2:
            z = match(data1, data2)
            if z > 0.05:
                d1_count, d1_cleaned = clean_and_split(data1)
                d2_count, d2_cleaned = clean_and_split(data2)
                if (d1_count == d2_count):
                    f1.write(encode(d1_cleaned))
                    f2.write(encode(d2_cleaned))
                else:
                    f1.write(encode(clean(data1)))
                    f2.write(encode(clean(data2)))
            else:
                print("'{}' unlike '{}'\n".format(data1, data2))
                f1.write(encode(clean(data1)))
                f2.write(encode(clean(data2)))


with open("utterances-clean.pickle", "rb") as f:
    while True:
        try:
            u = pickle.load(f)  # type: Utterance
            if random.random() > 0.1:
                if dev < 1000:

                    split_and_write("data_in/dev.from", u.modern, "data_in/dev.to", u.shakespeare)

                    # with open("data_in/dev.from", "at") as d1:
                    #     with open("data_in/dev.to", "at") as d2:
                    #         d1_count, d1_cleaned = clean_and_split(u.modern)
                    #         d2_count, d2_cleaned = clean_and_split(u.shakespeare)
                    #         if (d1_count == d2_count):
                    #             d1.write(encode(d1_cleaned))
                    #             d2.write(encode(d2_cleaned))
                    #         else:
                    #             d1.write(encode(clean(u.modern)))
                    #             d2.write(encode(clean(u.shakespeare)))
                    dev += 1
                if test < 1000:

                    split_and_write("data_in/test.from", u.modern, "data_in/test.to", u.shakespeare)

                    # with open("data_in/test.from", "at") as d1:
                    #     d1.write(encode(clean(u.modern)))
                    # with open("data_in/test.to", "at") as d2:
                    #     d2.write(encode(clean(u.shakespeare)))
                    test += 1
                else:
                    split_and_write("data_in/train.from", u.modern, "data_in/train.to", u.shakespeare)
                    # with open("data_in/train.from", "at") as f2:
                    #     f2.write(encode(clean(u.modern)))
                    # with open("data_in/train.to", "at") as f3:
                    #     f3.write(encode(clean(u.shakespeare)))
            else:
                split_and_write("data_in/train.from", u.modern, "data_in/train.to", u.shakespeare)
                # with open("data_in/train.from", "at") as f2:
                #     f2.write(encode(clean(u.modern)))
                # with open("data_in/train.to", "at") as f3:
                #     f3.write(encode(clean(u.shakespeare)))
        except Exception as e:
            print("error: ", e)
            break
