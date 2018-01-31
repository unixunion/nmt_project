import re


def clean(data: str):
    result = "{} ".format(data)
    result = result.replace('\xa0', ' ')
    result = result.replace('\u2003', ' ')
    result = re.sub('\[.*\]', ' ', result)
    result = re.sub('\(.*\)', ' ', result)
    result = re.sub('"', ' ', result)
    # result = re.sub("'", ' ', result)
    result = re.sub("\.", " ", result)
    result = re.sub("\n", " ", result)
    result = re.sub("\r", " ", result)
    result = re.sub(",", " ", result)
    result = re.sub("\?", " ", result)
    # result = re.sub("’", "", result)
    result = re.sub(";", " ", result)
    result = re.sub(":", " ", result)
    result = re.sub("!", " ", result)
    result = re.sub(":", " ", result)
    result = re.sub("-", " ", result)
    result = re.sub("—", " ", result)
    result = re.sub('”', " ", result)
    result = re.sub('“', " ", result)
    #result = re.sub(r'[\W_\s\'\`\]+', ' ', result)
    result = re.sub(' +', ' ', result)
    return result.lower()



with open("data_in/train.from", "rt") as f:
    with open("data_in/train.to", "rt") as t:
        line1 = f.read()
        line2 = t.read()

        with open("data_in/text", "at") as o:
            o.write(clean("{} {}".format(line1, line2)))
