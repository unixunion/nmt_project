import re

from data import super_clean

with open("data_in/train.from", "rt") as f:
    with open("data_in/train.to", "rt") as t:
        line1 = f.read()
        line2 = t.read()

        with open("data_in/text", "at") as o:
            o.write(super_clean("{} {}".format(line1, line2)))
