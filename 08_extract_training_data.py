import pickle
from data import encode, clean
import random

en_text = []
sh_text = []

count = 0
test = 0
dev = 0

with open("utterances-clean.pickle", "rb") as f:
    while True:
        try:
            u = pickle.load(f) # type: Utterance
            if random.random() > 0.1:
                if dev < 100:
                    with open("data_in/dev.from", "at") as d1:
                        d1.write(encode(clean(u.modern)))
                    with open("data_in/dev.to", "at") as d2:
                        d2.write(encode(clean(u.shakespeare)))
                    dev +=1
                elif test < 100:
                    with open("data_in/test.from", "at") as d1:
                        d1.write(encode(clean(u.modern)))
                    with open("data_in/test.to", "at") as d2:
                        d2.write(encode(clean(u.shakespeare)))
                    test +=1
                else:
                    with open("data_in/train.from", "at") as f2:
                        f2.write(encode(clean(u.modern)))
                    with open("data_in/train.to", "at") as f3:
                        f3.write(encode(clean(u.shakespeare)))
            else:
                with open("data_in/train.from", "at") as f2:
                    f2.write(encode(clean(u.modern)))
                with open("data_in/train.to", "at") as f3:
                    f3.write(encode(clean(u.shakespeare)))
        except Exception as e:
            print("error: ", e)
            break
